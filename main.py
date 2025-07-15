from stats import countWords,count_each_character
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def sort_on_count(arr):
    return arr["count"]

def main():
    arguments = sys.argv
    if len(arguments)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookPath = arguments[1]
    content = get_book_text(bookPath)
    number_of_words = countWords(content)
    character_frequency_dict = count_each_character(content)
    char_freq_arr = []
    for item in character_frequency_dict:
        char_freq_arr.append({'name':item,'count':character_frequency_dict[item]})

    char_freq_arr.sort(reverse=True , key=sort_on_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookPath}...")
    print("----------- Word Count ----------")
    print(f"'Found {number_of_words} total words'")
    print("--------- Character Count -------")

    for i in range(0,len(char_freq_arr)):
        if char_freq_arr[i]['name'].isalpha():
            print(f"{char_freq_arr[i]['name']}: {char_freq_arr[i]['count']}")


    print("============= END ===============")

main()
