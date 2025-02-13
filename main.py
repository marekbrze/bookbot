def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(count_words(file_contents))
        counted_symbols = count_symbols(file_contents)
        filtered_letters = filter_letters(counted_symbols)
        converted_dicts = convert_dict_to_list(filtered_letters)
        sorted_list_dicts = sort_counted_symbols(converted_dicts)
        counted_words = count_words(file_contents)
        print_report(counted_words, sorted_list_dicts)


def count_words(text):
    words = text.split()
    return len(words)


def count_symbols(text):
    counted_symbols = {}
    lowered_string = text.lower()
    for symbol in lowered_string:
        if symbol in counted_symbols:
            counted_symbols[symbol] += 1
        else:
            counted_symbols[symbol] = 1
    return counted_symbols


def filter_letters(symbols_dict):
    filtered_dict = {}
    for symbol in symbols_dict:
        if symbol.isalpha():
            filtered_dict[symbol] = symbols_dict[symbol]
    return filtered_dict


def convert_dict_to_list(dict):
    symbols_list = []
    for letter in dict:
        item = {}
        item["letter"] = letter
        item["count"] = dict[letter]
        symbols_list.append(item)
    return symbols_list


def sort_on(dict):
    return dict["count"]


def sort_counted_symbols(symbols_list):
    symbols_list.sort(reverse=True, key=sort_on)
    return symbols_list


def print_report(counted_words, sorted_symbols):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{counted_words} words found in the document\n")
    for letter in sorted_symbols:
        print(f"The '{letter['letter']}' was found {letter['count']} times")
    print("--- End report ---")


main()
