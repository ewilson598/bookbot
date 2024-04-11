def main():
    import string
    alphabet = string.ascii_lowercase

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = text.split()
    print(len(wordcount))

    character_counts = {}

    for char in text.lower():
          if char in alphabet:
                if char in character_counts:
                      character_counts[char] += 1
                else:
                      character_counts[char] = 1
    print (character_counts)

    list_of_tuples = list(character_counts.items())
    sorted_list_of_tuples = sorted(list_of_tuples, key=lambda x: x[1], reverse=True)
    for char, count in sorted_list_of_tuples:
          print(f"The '{char}' character was found {count} times")

def get_book_text(path):
    with open(path) as f:
              return f.read()
      
main()