# counts words in the provided text, prints number of words
def count_words(text):
    words = text.split()

    #print(len(words))
    return len(words)

# text is string, lowercase all chars, returns number of times each letter appears
def count_characters(text):

    # setup dictionary to store counts
    char_counts = {}

    for char in text:
        if char.lower() in char_counts:
            char_counts[char.lower()] += 1
        else:
            char_counts[char.lower()] = 1

    return char_counts

# sorts dicts by number key
def sort_dicts(dict):
    sorted_dict = dict.items()
    sorted_dict = sorted(sorted_dict, key=lambda x: x[1], reverse=True)
    
    return sorted_dict

# formats report for printing
def format_report(file):

    # get word count
    word_count = count_words(file)

    # get char count
    char_count = count_characters(file)

    # sort char count
    sorted_char_count = sort_dicts(char_count)

    # print report
    print(f"Report for book: Frankenstein")
    print(f"Number of words: {word_count}")
    for char in sorted_char_count:
        if char[0].isalpha():
            print(f"The {char[0]} character appears {char[1]} times")


with open("books/frankenstein.txt") as file:
    file_contents = file.read()

    # print(file_contents)
    format_report(file_contents)