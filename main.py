def num_words(text):  
    words = text.split()
    print(f"{len(words)} words found in the document \n")
    dict = num_characters(words)
    return dict

def num_characters(words):
    char_dict = {}
    for word in words:
        for letter in word: 
            letter = letter.lower()
            if letter in char_dict:
                char_dict[letter] += 1
            else: 
                char_dict[letter] = 1

    return char_dict   

def main():
    with open("books/frankenstein.txt") as f: 
        book_text = f.read() 
        print("--- Begin report of frankenstein.txt ---") 
        characters_dict = num_words(book_text)
        characters_list = list(characters_dict.items())
        characters_list.sort(key = lambda x: x[1], reverse = True)
        for character in characters_list:
            if character[0].isalpha():
                print(f"The {character[0]} character was found {character[1]} times")
        print("--- End report ---")


if __name__ == "__main__":
    main()