from stats import count_words, get_num_char

def get_book_text(filepath):
    file_contents  = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
   
def main():
    ans = str(count_words((get_book_text("books/frankenstein.txt")))) + " words found in the document"
    print(ans)
    char_dict = get_num_char(get_book_text("books/frankenstein.txt"))
    print(char_dict)
main()