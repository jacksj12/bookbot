from stats import count_words, get_num_char, sort_dict
import sys

def get_book_text(filepath):
    file_contents  = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def report(filename):
    text =get_book_text(filename)
    count = count_words(text)
    char_dict = get_num_char(text)
    ans = f"============ BOOKBOT ============\nAnalyzing book found at {filename}...\n----------- Word Count ----------\nFound {count} total words\n--------- Character Count -------\n"
    for word in char_dict:
        if word.isalpha():
            ans += word + ": " + str(char_dict[word]) + "\n"
    return ans + "============= END ==============="

def main():
    #ans = str(count_words((get_book_text("books/frankenstein.txt")))) + " words found in the document"
    #print(ans)
    #char_dict = get_num_char(get_book_text("books/frankenstein.txt"))
    #print(report("books/frankenstein.txt"))
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print(report(sys.argv[1]))
main()