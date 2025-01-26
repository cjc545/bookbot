freq = {}

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n")

    for item in chars_sorted_list:
        if not item["Char"].isalpha():
            continue
        print(f"The '{item['Char']}' character was found {item['Num']} times")

    print("\n--- End report ---")

    
def get_book_text(path):
    with open(path) as f:
        return f.read()
        

def get_num_words(book):
    words = book.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"Char": ch, "Num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["Num"]



if __name__ == '__main__':
    main()