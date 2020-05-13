import json
import random
import urllib.request
 
def get_random_word():                                     #Function to obtain random words
  url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
  words = json.loads(url.read())
  random_word = random.choice(words)
  return random_word.upper()


def game(word):                                            #Game Funtion
  trials = 6                                               #User has atmost 6 attempts to guess the word
  blanks = "_" * len(word)                                 #Initializing blanks as its length is equal to length of word
  guessed = False                                          #Initializing guessed as default
  guessed_letters = []                                     #Intitializing an empty list to store guessed letters in order to reduce repetitions 
 
  print("\nLet's begin") 
  print(visual(trials))
  print(" ".join(blanks))                                  #To print "_" with spaces

  while guessed == False and trials > 0:                   #Loop will run until user hasn't guessed and trials left
    guess = input("\nEnter a letter : ").upper()

    if len(guess) == 1 and guess.isalpha():                #input should be a single charecter and an alphabet

      if guess in guessed_letters:
        print("\nYou've guessed this letter, try again!")

      elif guess in word:
        for i in range(0,len(word)):
          if(word[i] == guess):
            blanks = blanks[:i] + guess + blanks[i+1:]     #Used splicing to replace letters as strings are immutable
        print(" ".join(blanks))
        guessed_letters.append(guess)

      else:
        trials -= 1
        guessed_letters.append(guess)
        print(visual(trials))
        print(" ".join(blanks))
  
    else:
      print("\nInvalid input!")    

    if blanks.find("_") == -1 :                            #User wins if she fills all the blanks 
      guessed = True
      print("\nYou've Won!")                               


  if guessed == False:                                     #User looses if she makes more than 6 mistakes
    print("\nYou all suck!\nAll Hail Jake")    
    print("\nThe word was ",word)


def visual(trials):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[trials]


consent = input("Do you want to play (Yes/No) : " ).upper()
while consent == "YES":
  word = get_random_word()
  game(word)
  consent = input("\nDo you want to play again(Yes/No) : ").upper()


#Author Hritik Valluvar
