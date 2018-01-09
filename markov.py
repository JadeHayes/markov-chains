"""Generate Markov text from text files."""
from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as file_string:
        return file_string.read()


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

    # loop through each word in the text string
    for i, word in enumerate(words[:-2]):
        # create a tuple of the bigram of that word and the next word in the string
            bigram = (word, words[i + 1])
            # if that tuple is not in the dict
            # LOOK INTO: set default
            if bigram not in chains:
                # add as a key in the dict
                # and the word following the bigram as a value for that key
                chains[bigram] = [words[i + 2]]
            # else add the word following the bigram as an additional value for the tuple
            else:
                chains[bigram].append(words[i + 2])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    # find a random key
    bigram = choice(chains.keys())
    # add to words list
    words.extend(bigram)
    while bigram in chains:
        # attach the last value of the key to a value
        random_value = choice(chains[bigram])
        # add random value to words
        words.append(random_value)
        # assign that to a new key
        bigram = (bigram[1], random_value)
        # repeat until finished

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
