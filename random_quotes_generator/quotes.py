import random

FILE_PATH = "random_quotes_generator\quotes.txt"

def get_random_quotes():
    with open(FILE_PATH, 'r') as file:
        new_quotes = file.readlines()
        return random.choice(new_quotes)

print(get_random_quotes())