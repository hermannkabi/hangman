from tkinter import *
import time
import random
import sys

def play():

    def newGame():
        root.destroy()
        play()

        
        
    
    global guesses
    rt = Tk()
    root = Canvas(rt)
    root.pack()
    rt.title("Poomine")
    rt.geometry("500x300")


    guesses = 0
    maxGuesses = 8
    words = ["kirves", "plaaster", "politseiülem", "korravalvur"]
    word = random.choice(words)
    wordList = list(word)
    uiList = list(len(word)*"_")
    uiList[0] = wordList[0]
    for pos in range(len(wordList)):
        if uiList[0] == wordList[pos]:
            uiList[pos] = wordList[pos]

    chancesVar = IntVar()
    chancesVar.set("10")
    var = IntVar()
    var.set(uiList)
    retry_button = Button(root)
    guessVar = StringVar()







    def checkUserChoice():
        global guesses
        if guesses >= maxGuesses:
            retry_l = Label(root,text="Kahjuks said Teie käigud otsa")
            retry_l.pack()
            retry_button = Button(root,text="Mängi uuesti", command=newGame())
            retry_button.pack()
            b.pack_forget()
            userEntry.pack_forget()
        else:
            guesses += 1
            guessVar.set(str(maxGuesses-guesses) + " katset veel")
            character = userEntry.get()
            for pos in range(len(wordList)):
                if wordList[pos] == character:
                    uiList[pos] = character
            var.set(uiList)
            if wordList==uiList:
                Label(root,text="Palju õnne, arvasite ära").pack()
                b.pack_forget()
                userEntry.pack_forget()
                retry_button = Button(root,text="Mängi uuesti", command=newGame())
                retry_button.pack()
            
        
        

    l1 = Label(root,textvariable=guessVar)
    l1.pack()

    l2 = Label(root,text="Tere tulemast poomisesse.\nPead {} korraga suvalise sõna ära arvama.\nKas oled valmis?".format(chancesVar.get()), justify = "center")
    l2.pack()

    l3 = Label(root,textvariable=var, font=("Times New Roman", 25))
    l3.pack()

    userEntry = Entry(root,width=1)
    userEntry.pack(pady=35)

    b = Button(root,text="Paku", command=checkUserChoice)
    b.pack()
play()
