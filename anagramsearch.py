# 17/10/2024
# Lerato Moholo

print("***** Anagram Finder *****")


Lexicon = "EnglishWords.txt"
try:
    with open(Lexicon, "r") as English_Words:
        input_word = input("Enter a word:\n").lower()
        word_list = [word.strip().lower() for word in English_Words.readlines()]
        sortedinput_word = ''.join(sorted(input_word))
        anagrams_list = []
        
        for word_in_list in word_list:
            if ''.join(sorted(word_in_list)) == sortedinput_word and word_in_list != input_word:
                anagrams_list.append(word_in_list)

        
        if anagrams_list:
            print(sorted(anagrams_list))
        else:
            print(f"Sorry, anagrams of '{input_word}' could not be found.")            
except FileNotFoundError:
    print(f"Sorry, could not find file '{Lexicon}'.")