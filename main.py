def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    num_letters = count_letters(book_text)
    # print(num_words)
    # print(num_letters)

    # niceley formatted
    print("f{num_words} words found in the document\n")
    for d in chars_dict_to_sorted_list(num_letters):
        print(f"The '{d["char"]}' was found {d["count"]} times")

def chars_dict_to_sorted_list(char_dict):
    """transform a character count dictionary
    returns a list of dicts [{"char": key, "count": val}]
    """
    def sort_on(d):
        return d["char"]
    
    ls = [{"char": k, "count": v} for k, v in char_dict.items() if k.isalpha()]
    ls.sort(key=sort_on) 
    
    return ls

def count_letters(book_text):
    letter_count = {}

    for letter in book_text:
        lowered_letter = letter.lower()

        if lowered_letter not in letter_count:
            letter_count[lowered_letter] = 1
        else:
            letter_count[lowered_letter] += 1

    return letter_count

def count_words(book_text):
    num_words = len(book_text.split())
    return num_words

def get_book_text(file_path):
    with open (file_path) as f:
        file_contents = f.read()
    return file_contents

if __name__ == "__main__":
    main()