import random

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/
'''                   
print(logo)

symbol = [
'''
        ------
	|   | 
	|    
	|  
	|    
	|  
	| 
	--------- 
''',
'''
        ------
	|   | 
	|   O 
	|  
	|    
	|  
	| 
	--------- 
''',
'''
        ------
	|   | 
	|   O 
	|   |
	|   |
	|   
	| 
	--------- 
''',
'''
        ------
	|   | 
	|   O 
	|  /|
	|   |  
	|  
	| 
	--------- 
''',
'''
        ------
	|   | 
	|   O 
	|  /|\\
	|   | 
	|  
	| 
	--------- 
''',
'''
        ------
	|   | 
	|   O 
	|  /|\\
	|   | 
	|  /
	| 
	--------- 
''',
'''
        ------
	|   | 
	|   O 
	|  /|\\
	|   | 
	|  / \\
	| 
	--------- 
'''
]

wordlist = ["adventure", "horizon", "discovery", "serenity", "galaxy", "kindness", "vibrant", "harmony", "courage", "eclipse","melody", "illusion", "waterfall", "phoenix", "solitude","whisper", "mystery", "enchantment", "twilight", "fortune"]
chosenword = random.choice(wordlist)
chosenword = list(chosenword)

placeholder = "_" * len(chosenword)
placeholder = list(placeholder)
print(" ".join(placeholder))

lives=0
guessed_letters = []

while not(placeholder==chosenword):
     guessedletter = input("Guess a Letter:\n").lower()
     if guessedletter in guessed_letters:
        print(f"You've already guessed '{guessedletter}'. Try a different letter.")
        continue
     guessed_letters.append(guessedletter)
     if guessedletter in chosenword:
       for i in range(len(chosenword)):
               if chosenword[i] == guessedletter:
                    placeholder[i] = guessedletter
     else:
       lives = lives + 1
     if lives == 6:
               print(symbol[lives])
               print("You lose")
               print("The word was:", "".join(chosenword))
               break
     print(symbol[lives])
     print(" ".join(placeholder))
if placeholder==chosenword:
     print("Congratulations! You've guessed the word:", "".join(chosenword))
        
        
