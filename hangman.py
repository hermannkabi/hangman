import random
import sys
from hangman_utils import HangmanUtils


utils = HangmanUtils()

guesses = 0
allowed_guesses = 8
words = utils.words
word = random.choice(words)
uiList = list(len(word)*"_")
wordList = list(word)
uiList[0] = wordList[0]
for position in range(len(wordList)):
    if wordList[position] == wordList[0]:
        #See tähendab, et oli veel kohti, kus seda tähte kasutati
        uiList[position] = wordList[position]


print("Tere tulemast poomisesse, kus pead ära arvama sõna.\nKui arvad, et tead sõna, kirjuta 'tean'.\nJa sinu sõna on: ")

print(" ".join(uiList))
print()
while guesses < allowed_guesses:
    get_user_choice = input("Pakun tähte... ")
    if get_user_choice.lower() == "tean":
        print("Tore, et sa sõna tead (või vähemalt arvad nii)")
        user_thinks_word = input("Mis see sõna siis on? ")
        
        if user_thinks_word == "".join(wordList):
            print("Teadsidki")
            print("Palju õnne. Sul läks võitmiseks {} katset".format(guesses))
            sys.exit()
        else:
            print("Ega ikka ei teadnud küll!")
            if len(user_thinks_word) != len("".join(wordList)):
                print("Pealegi, see sõna pole isegi sama pikk. Hale!")
            guesses += 1
    elif (len(get_user_choice) > 1 and utils.is_input_int(get_user_choice)==True) or len(get_user_choice) > 1 or utils.is_input_int(get_user_choice)==True:
        print("Ole hea ja paku tähte. Ma tean, et sa tahad mu programmi hävitada")
    elif get_user_choice == "":
        print("Kirjuta ikka midagi")
    else:
        matches = 0
        guesses += 1
        for position in range(len(wordList)):
            if get_user_choice==wordList[position]:
                #print("Match at {}".format(position))
                matches += 1
                uiList[position] = wordList[position]
        if matches == 0:
            print("Kui kahju, ei läinud täppi")
            
        else:

            print("Jess, sa said {} kohas tähe õigesti. Tubli".format(matches))

        print("Jäänud veel {} katset".format(allowed_guesses-guesses))            
        print()
        print(" ".join(uiList))
        print()
        if wordList == uiList:
            print("Mäng sai läbi. Sa arvasid sõna {} korraga ära".format(guesses))
            sys.exit()

print("Katsed saidki otsa. Kahju!")
print("Muide, sõna oli {}".format(word))
sys.exit()


