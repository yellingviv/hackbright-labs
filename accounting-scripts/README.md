We return to Ubermelon! In this exercise, we are looking to improve how information about the melons is stored.

We currently have many dictionaries with information about melons, with numerical keys that are associated with string, integer, and boolean values. However, this requires knowing the numerical key for a given melon and then looking into multiple different dictionaries to find the associated information. Our task is to refactor this structure to make the data more easily accessible, and open up capacity for adding new information in the future.

I refactored the `melons.py` document, where the dictionaries were stored, to create one dictionary of all melon data. It contains each melon name as a key, and then each melon has a dictionary as its value, with keys such as price, weight, seedless, etc. This way you can query directly into one dictionary and just dig into one specific key and it's value to find the information you are looking for.

In addition, as demonstrated by the keys with `None` value, it is possible to add additional keys and values to the sub-dictionary for each melon. This is a data structure that gives Ubermelon room to grow and scale!
