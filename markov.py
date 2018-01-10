"""Generate Markov text from text files."""
from random import choice
from sys import argv


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    with open(file_path) as file_string:
        return file_string.read()


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each ngram (except the last) will be a key in chains:

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
    for i, word in enumerate(words[:-n]):
        # create a tuple of the ngram of that word and the next word in the string
            ngram = tuple(words[i:i + n])
            # if that tuple is not in the dict
            # LOOK INTO: set default
            if ngram not in chains:
                # add as a key in the dict with an empty list as the value
                chains[ngram] = []
            # append the word following the ngram to the list that is the value for that ngram
            chains[ngram].append(words[i + n])

    return chains


def make_text(chains, n):
    """Return text from chains."""

    words = []

    # your code goes here
    # find a random key
    ngram = choice(chains.keys())

    # if the randomly selected key doesn't start with a capital letter
    # keep picking new random keys until we find one that does
    while ngram[0].istitle() is False:
        ngram = choice(chains.keys())

    # add to words list
    words.extend(ngram)

    while ngram in chains:
        # attach the last value of the key to a value
        random_value = choice(chains[ngram])
        # add random value to words
        words.append(random_value)
        # assign that to a new key
        ngram = tuple(words[-n:])
        # repeat until finished

    for i, word in enumerate(words[::-1]):
        if word[-1] in '!.?"':
            end_index = i

    print end_index
    return " ".join(words[:end_index])


input_path1 = argv[1]
#input_path2 = argv[2]
#input_path3 = argv[3]
n = int(argv[-1])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path1)
# + open_and_read_file(input_path2)
# + open_and_read_file(input_path3)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n)

print random_text
