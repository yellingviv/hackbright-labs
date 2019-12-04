"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file = open(file_path)
    entire_text = file.read()
    return entire_text.replace('\n', ' ')


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split()
    for i in range(len(words) - n):
        key = tuple(words[i:i + n])
        if key not in chains:
            chains[key] = [words[i + n]]
        else:
            chains[key].append(words[i + n])
    return chains


def make_text(chains):
    """Return text from chains."""
    words = []
    key_block = choice(list(chains.keys()))
    
    # check if first letter of block is capitalized
    while key_block[0][0].isupper() is False:
        key_block = choice(list(chains.keys()))

    # add the key block words to the list of words
    for key in key_block:
        words.append(key)

    while True:
        # check if the key block is a valid key in the chain dictionary
        if key_block in chains:
            new_key = list(key_block[1:])
            new_random = choice(chains.get(key_block))
            new_key.append(new_random)
            words.append(new_random)
            key_block = tuple(new_key) 
        else:
            # if the key is not in the dictionary, check if it's punctuated
            # if it isn't, generate new key till punctuated to end on punctuation
            while key_block[-1][-1].isalnum():
                key_block = choice(list(chains.keys()))
            for key in key_block:
                words.append(key)
            break

    return " ".join(words)


input_path = sys.argv[1]
ngram = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, ngram)

# Produce random text
random_text = make_text(chains)

print(random_text)
