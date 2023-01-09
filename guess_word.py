# GuessWord

import random

words = ["cat", "rat", "dog", "sheep", "elephant", "bat", "house", "hospital", "fox"]
hidden = words[random.randint(0,len(words)-1)]
shown = list('_'*len(hidden))

found = False

while not found:

    l = False
    char = False
    while not char:

        guess = input("Pick a letter: ")

        if len(guess) == 1:
            char = True
        else:
            print("You can only guess one letter at a time")
        

    for i in range(0, len(hidden)):
        if hidden[i] == guess.lower():
            shown[i] = hidden[i]
            print(''.join(shown))
            l = True
            
    if not l:
        print("Didn't work.", ''.join(shown))
            
    if hidden == ''.join(shown):
        break
    
print("Congrats! Your word is: " + ''.join(shown))
            
            
