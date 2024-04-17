def main():
    book_path = 'books/frankenstein.txt'
    text = get_text(book_path)
    num_words = count_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_list)

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(string):
    words = string.split()
    return len(words)

def get_chars_dict(string):
    chars = {}

    lowered_string = string.lower()

    for char in lowered_string:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        if char.isalpha():
            sorted_list.append({"name": char, "num": chars_dict[char]})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]

def print_report(book_name, num_words, char_list):
    print(f'--- Begin report of {book_name} ---')
    print(f'{num_words} words found in the document')
    print()
    for dict in char_list:
        print(f"The '{dict["name"]}' was found {dict["num"]} times")
    print('--- End report ---')
    

main()