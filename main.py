import random
import json
with open("guess_word/Include/words.json", "r") as words_file:
    words = json.load(words_file)
    word_selected = str(random.choice(words))
    word_selected_copy = word_selected
    try:
        Run = random.randrange(1, (int(len(word_selected_copy)/ 2)))
    except:
        Run = 1
    while Run > 0:
        word = random.choice(word_selected)
        word_selected = word_selected.replace(word, "_")
        Run -= 1
    false_characters = []
    while True:
        print(word_selected)
        if word_selected == word_selected_copy:
            print("You win")
            print(f'Wrong words : {false_characters}')
            break
        input_character = input("Enter the character : ")
        input_character = input_character.lower()
        if len(input_character) < 2:
            word_selected_list = list(word_selected)
            if input_character in word_selected_copy:
                if word_selected_copy.count(input_character) == 1:
                    index = word_selected_copy.index(input_character)
                    word_selected_list[index] = input_character
                else:
                    for i, i_2 in enumerate(word_selected_copy):
                        if i_2 == input_character:
                            word_selected_list[i] = i_2
                result = ""
                for i in word_selected_list:
                    result += i
                word_selected = result
                print(f'This {input_character} word is correct\n')
            else:
                print("This character does not exist in the word\n")
                false_characters.append(input_character)
        else:
            print("Enter only one character\n")