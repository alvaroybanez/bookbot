def word_count(book_text):
    words = book_text.split()
    return f'{len(words)}'

def letter_count(book_text):
    book_text = book_text.lower()
    letter_count = {}
    for letter in book_text:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

# A function that takes a dictionary and returns the value of the "num" key in descending order with newlines
def sorted_letter_count(letter_count):
    sorted_items = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
    result = ""
    for letter, count in sorted_items:
        result += f"{letter}: {count}\n"
    return result
