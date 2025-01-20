# Moholo Lerato

from anagramsearch import frequencyLetter
from anagramsearch import areAnagrams

def find_anagram_sets(word_len, filename):
    try:
        with open('EnglishWords.txt', 'r') as file:
            words = [line.strip() for line in file if line.strip().isalpha() and len(line.strip()) == word_len]

        anagram_sets = {}

        for word in words:
            key = ''.join(sorted(word.lower()))
            anagram_sets.setdefault(key, []).append(word)

        anagram_sets = [sorted(group) for group in anagram_sets.values() if len(group) > 1]
        anagram_sets.sort()

        with open(filename, 'w') as output_file:
            if not anagram_sets:
                output_file.write("No anagram sets found.\n")
            else:
                for group in anagram_sets:
                    output_file.write(str(group) + '\n')

        print(f"Writing results to '{filename}'...")

    except FileNotFoundError:
        print("Sorry, could not find file 'EnglishWords.txt'.")

def main():
    print("***** Anagram Set Search *****")
    word_len = int(input("Enter word length:\n"))
    print("Searching...")
    filename = input("Enter file name: ")

    find_anagram_sets(word_len, filename)

if __name__ == "__main__":
    main()