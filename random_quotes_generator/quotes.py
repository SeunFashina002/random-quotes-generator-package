import random

file_path = "random_quotes_generator\quotes.txt"

def get_random_quote(file_path):
    with open(file_path, 'r') as file:
        new_quotes = file.readlines()
        return random.choice(new_quotes)




