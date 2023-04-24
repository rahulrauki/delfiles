import os
import random
import string


dictionary = ["rahul", "age", 'happy', 'rauki', 'crazy', 'cool', 'good', 'nice', 'vendetta']
# Define a function to generate a random filename
def random_filename():
    letters = string.ascii_lowercase
    return ''.join(random.choice(dictionary) + random.choice(letters) for i in range(1))

# Define a directory path to create the files in
directory = os.path.abspath('./sample')

# Create 30 files with random names in the directory
for i in range(30):
    filename = random_filename()
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as file:
        file.write('This is a test file.')
