import sys
from stats import word_count, character_count, sorted_dictionary

def get_book_text(filepath):
    '''
    Docstring for get_book_text
    
    Takes a filepath as input and returns the contents of the file as a string.

    :param filepath: must be a valid filepath
    '''
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def create_header(title, segment, length):
    '''
    Docstring for create_header
    
    Creates a header of a given length with the title centered in between the desired segment characters.

    :param title: A valid string of a desired title.
    :param segment: Ideally one character in a string.
    :param length: An integer of the desired length of the header.
    '''
    length_of_title = len(title)
    repeats = (length - length_of_title) // 2

    result = (segment * repeats) + " " + title + " " + (segment * repeats)
    return result
    
    
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    # Create the main header with BOOKBOT 

    print(create_header("BOOKBOT", "=", 32))
    # Print the description with the desired book path

    print(f"Analyzing book found at {book_path}...")
    # Create a secondary header with Word Count

    print(create_header("Word Count", "-", 32))
    # Print the word count for the book

    print(word_count(get_book_text(book_path)))
    # Create a secondary header with Character Count

    print(create_header("Character Count", "-", 32))
    # Capture the character's and their associated counts

    list_of_sorted_characters = sorted_dictionary(character_count(get_book_text(book_path)))
    # print only alphabetical characters

    for _ in list_of_sorted_characters:
        if _["char"].isalpha():
            print(f"{_["char"]}: {_["num"]}")
        else:
            continue
    # Create a final header with END

    print(create_header("END", "=", 32))
    
main()