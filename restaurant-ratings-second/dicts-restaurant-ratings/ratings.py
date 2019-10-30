"""Restaurant rating lister."""

import random

def restaurant_rater(filename):
    
    #create empty dictionary
    restaurant_ratings = {}
    #open file with restaurant lists
    file = open(filename)
    #loop though restaurant lists
    for line in file:
        line = line.rstrip()
        restaurants_info = line.split(":")
        restaurant_name = restaurants_info[0]
        rating = restaurants_info[1]

        #add to the dictionary
        restaurant_ratings[restaurant_name] = rating
    return restaurant_ratings
    

def add_new_restaurant():
    """user can add new restaurant and rating"""

    new_restaurant_name = input("What is the cool new restaurant you went to?")
    # take restaurant rating
    new_rating = input("What is your rating of this restaurant.")
    # store new rating in restaurante_ratings

    restaurant_ratings[new_restaurant_name] = new_rating

    return restaurant_ratings

def show_restaurant_ratings(restaurant_ratings):
    """set up a function for user to view ratings"""
    # create new list of key-value tuples and sort list (asc), then unpacks the
    # name and rating for easy printing
    for restaurant, rating in sorted(restaurant_ratings.items()):
        print(restaurant + " is rated at " + rating + ".")


def random_rest_update(restaurant_ratings):
    """selects a random restaurant and prompts user to update the rating"""

    rest_list = []
    for restaurant in restaurant_ratings:
        rest_list.append(restaurant)
    rand_restaurant = random.choice(rest_list)
    print(rand_restaurant)
    # select a random restaurant from the list of restaurants in the dictionary

    rating = restaurant_ratings[rand_restaurant]
    new_rating = input(f"""Your restaurant is {rand_restaurant}. {rand_restaurant} 
has a rating of {rating}. What do you want to change the rating to? > """)
    
    restaurant_ratings[rand_restaurant] = new_rating

    return restaurant_ratings


def restaurant_updater(restaurant_ratings):
    """User selects a specific restaurant and updates the score"""

    rest_to_update = input("What restaurant would you like to update? > ")
    current_rating = restaurant_ratings.get(rest_to_update, 0)

    new_rating = input(f"""{rest_to_update} has a rating of {current_rating}. 
        What do you want to change the rating to? > """)
        
    restaurant_ratings[rest_to_update] = new_rating

    return restaurant_ratings

restaurant_ratings = restaurant_rater('scores.txt')

while True:
    """take user input to determine if viewing, rating, or quitting"""
    choice = input("""What would you like to do? [V]iew restaurants, [A]dd 
restaurant, [R]andom restaurant, [U]pdate restaurant, or [Q]uit? > """)
    if choice == "Q":
        break
    elif choice == "V":
        show_restaurant_ratings(restaurant_ratings)
    elif choice == "A":
        add_new_restaurant()
    elif choice == "R":
        random_rest_update(restaurant_ratings)
    elif choice == "U":
        restaurant_updater(restaurant_ratings)
    else:
        print("Please enter a correct value.")