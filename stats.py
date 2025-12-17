def word_count(book_string):
    '''
    Docstring for word_count
    
    Takes a string version of a book and returns the number of total words in the book.

    :param book_string: must be a valid string, ideally from a book.
    '''
    # Split the book string into a manageable list of the words. Then count the number of words using len().

    word_list = book_string.split()
    num_words = len(word_list)
    return f"Found {num_words} total words"


def character_count(book_string):
    '''
    Docstring for character_count
    
    Takes a string version of a book and returns the number of times each character is present in the book.

    :param book_string: must be a valid string, ideally from a book.
    '''
    # Create a summary dictionary to hold all of the characters and associated counts in.

    summary = {}
    # For every character in the string, make sure it is lowercase, then check to see if it's in the summary.

    for char in book_string:
        if char.lower() not in summary:
            summary[char.lower()] = 1
        else:
            summary[char.lower()] += 1

    return summary


def sort_on(items):
    '''
    Docstring for sort_on
    
    A function that takes a dictionary and returns the value of the "num" key.

    :param items: a valid dictionary
    '''
    return items["num"]


def sorted_dictionary(dictionary):
    '''
    Docstring for sorted_dictionary
    
    Takes a dictionary of characters and their counts and returns a sorted list of dictionaries.
    Each dictionary should have two key-value pairs: one for the character itself and one for that character's count.
    (e.g. {"char": "b", "num": 4868})

    :param dictionary: A valid dictionary of characters and their counts.
    '''
    # Create an empty list variable.

    summary = []
    # For each character in the dictionary argument, append a list element dictionary of that character and its associated count.

    for char in dictionary:
        summary.append({"char": char, "num": dictionary[char]})
    # Sort the list in reverse order based on the "num" key (from greatest to least)

    summary.sort(reverse=True, key=sort_on)
    return summary