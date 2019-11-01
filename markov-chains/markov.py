"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)

    entire_text = file.read()

    return entire_text.replace('\n', ' ')


def make_chains(text_string):
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

    for i in range(len(words) - 2):
        pair = (words[i], words[i + 1])
        
        if pair not in chains:
            chains[pair] = [words[i + 2]]
        else:
            chains[pair].append(words[i + 2])

        i += 1

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    key_pair = choice(list(chains.keys()))
    words.append(key_pair[0])
    words.append(key_pair[1])

    while True:
        if key_pair in chains:
            new_random = choice(chains.get(key_pair))
            new_key = (key_pair[1], new_random)
            words.append(new_random)
            key_pair = new_key
        else:
            break

    return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
