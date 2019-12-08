# Problem Set 2, hangman.py
# Name: Taras Pyndykivskiy
# Collaborators: 
# Time spent: ~12hrs
# D:\Taras Pyndykivskiy\kpi\programming\python\hangman_project
# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
   
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
   
    return all([True if(i in letters_guessed) else False for i in secret_word])	

def get_guessed_word(secret_word, letters_guessed):

	return "".join(list(map((lambda a: a if a in letters_guessed else "_ "), secret_word)))

def get_available_letters(letters_guessed):

	return "".join(list(map(lambda a: a+" " if (a not in letters_guessed) else "", list(string.ascii_lowercase))))
    
def hangman(secret_word, wordlist):
	CRED='\033[91m'
	CYELLOW='\033[93m'
	CEND='\033[0m'
	CCYAN='\033[36m'
	CGREEN='\033[32m'
	CORANGE='\033[33m'
	CBLUE='\033[94m' 
	CLIGHTGREEN='\033[92m'
	CPURPLE='\033[94m'
	print("\n\nWelcome to the game Hangman!")
	score=0
	print("\nI am thinking of a word that is " +str(len(secret_word)) + " letters long.")

	warnings_counter=3
	guesses_counter=6
	user_symbols=list()
	print(CORANGE + "You have " + str(warnings_counter) + " warnings left." + CEND)
	
	while((is_word_guessed(secret_word, user_symbols)==False) and (guesses_counter>0)):

		print(CORANGE + "You have " + str(guesses_counter) + " guesses left." + CEND)
		print(CYELLOW + "Available letters : "+ CEND + CRED + get_available_letters(user_symbols) + CEND)

		entered_character=input("Please guess a letter : ").lower()


		if(len(entered_character)!=1 or (entered_character.isalpha()==False) or (entered_character in user_symbols)) :
			warnings_counter-=1
			print("Oops " + define_error(entered_character, user_symbols) + " You now have " + str(warnings_counter) + " warnings. " + get_guessed_word(secret_word, user_symbols))
			print("-"*60)
			if(warnings_counter<1):
				guesses_counter-=1
				warnings_counter=3
			continue
		
		user_symbols.append(entered_character)
		
		
		if(entered_character in secret_word):
			print(CLIGHTGREEN + "Good guess : " + get_guessed_word(secret_word, user_symbols) + CEND)

		else:
			print(CORANGE + "Oops! That letter is not in my word : " + get_guessed_word(secret_word, user_symbols) + CEND)
			guesses_counter-=2 if entered_character in ('a', 'o', 'e', 'i', 'u') else 1

			
		print("-"*60)

		if(warnings_counter<1):
			guesses_counter-=1
			warnings_counter=3

	if(is_word_guessed(secret_word, user_symbols)==True):
		score+=(guesses_counter)*unique_letters(secret_word)
		print(CGREEN + "\nCongratulations, you won! Your total score for this game is: " + str(score))	
	
	else:

		print(CLIGHTGREEN + "\nUnfortunately, you haven't guessed the secret word, cause you are out of tries." + CEND)
		print(CYELLOW + "\nThe secret word was : " + CEND + CORANGE + secret_word + CEND)
		
	return score

def match_with_gaps(my_word, other_word):
	my_word = my_word.replace("_", "")

	if(len(my_word)!=len(other_word)):
		return False

	my_word_gaps=my_word
	my_word=my_word.replace(" ", "")

	dict_my_word=dict()
	dict_other_word=dict()

	if(set(my_word).issubset(set(other_word))):

		for symbol in set(my_word):
			dict_my_word[symbol]=my_word.count(symbol)
			dict_other_word[symbol]=other_word.count(symbol)

		return all([False if dict_my_word[symbol]!=dict_other_word[symbol] else True for symbol in my_word]) and all([True if((my_word_gaps[i]==other_word[i]) and (my_word_gaps[i]!=" ") or (my_word_gaps[i]==" ")) else False for i in range(len(my_word_gaps))])
				
	else: return False

def define_error(text, user_symbols):
	if(len(text)!=1):
		return "You have to enter one character!"
	elif(text.isalpha()==False):
		return "It's not a valid character!"
	elif(text in user_symbols):
		return "You've already guessed that letter."

def show_possible_matches(my_word):
	my_word=my_word.replace("_", "")
	appropriate_words=""
	appropriate_words=" ".join([word for word in wordlist if(match_with_gaps(my_word, word)==True)])
	if(appropriate_words):
		print (appropriate_words)
	else: print ("No matches found!")

 
def unique_letters(secret_word):
	return len(set(secret_word))

def hangman_with_hints(secret_word, wordlist):
	CRED='\033[91m'
	CYELLOW='\033[93m'
	CEND='\033[0m'
	CCYAN='\033[36m'
	CGREEN='\033[32m'
	CORANGE='\033[33m'
	CBLUE='\033[94m' 
	CLIGHTGREEN='\033[92m'
	CPURPLE='\033[94m'
	print("\n\nWelcome to the game Hangman!")
	score=0
	print("\nI am thinking of a word that is " +str(len(secret_word)) + " letters long.")
	hint_activated=False
	warnings_counter=3
	guesses_counter=6
	user_symbols=list()
	print(CORANGE + "You have " + str(warnings_counter) + " warnings left." + CEND)
	
	while((is_word_guessed(secret_word, user_symbols)==False) and (guesses_counter>0)):

		print(CORANGE + "You have " + str(guesses_counter) + " guesses left." + CEND)
		print(CYELLOW + "Available letters : "+ CEND + CRED + get_available_letters(user_symbols) + CEND)

		entered_character=input("Please guess a letter : ").lower()


		if(len(entered_character)!=1 or (entered_character.isalpha()==False and entered_character!="*") or (entered_character in user_symbols)) :
			warnings_counter-=1
			print("Oops " + define_error(entered_character, user_symbols) + " You now have " + str(warnings_counter) + " warnings. " + get_guessed_word(secret_word, user_symbols))
			print("-"*60)
			if(warnings_counter<1):
				guesses_counter-=1
				warnings_counter=3
			continue
		
		user_symbols.append(entered_character)
		
		
		if(entered_character in secret_word):
			print(CLIGHTGREEN + "Good guess : " + get_guessed_word(secret_word, user_symbols) + CEND)

		else:
			if(entered_character!="*"):
				print(CORANGE + "Oops! That letter is not in my word : " + get_guessed_word(secret_word, user_symbols) + CEND)

			guesses_counter-=2 if entered_character in ('a', 'o', 'e', 'i', 'u') else 1

			
		if(entered_character=='*'):
			hint_activated=True
			print(CPURPLE + "Possible word matches are: " + CEND)
			show_possible_matches(get_guessed_word(secret_word, user_symbols).replace("_",""))
			user_symbols.remove(entered_character)

		print("-"*60)

		if(warnings_counter<1):
			guesses_counter-=1
			warnings_counter=3

	if(is_word_guessed(secret_word, user_symbols)==True) and hint_activated==False:
		score+=(guesses_counter)*unique_letters(secret_word)
		print(CGREEN + "\nCongratulations, you won! Your total score for this game is: " + str(score))	
		
	elif(hint_activated==True and guesses_counter>0):
		print("You've used a hint!")

	else:

		print(CLIGHTGREEN + "\nUnfortunately, you haven't guessed the secret word, cause you are out of tries." + CEND)
		if(hint_activated):
			print("You've used a hint, but that didn't help!")
		print(CYELLOW + "\nThe secret word was : " + CEND + CORANGE + secret_word + CEND)
		
	return score

def play_hints():
	number_games=0
	points=0
	cont=''
	while(cont==''):
		secret_word=choose_word(wordlist)
		points+=hangman_with_hints(secret_word, wordlist)
		number_games+=1
		cont=str(input("\nIf you want to continue, press Enter button or anything else to leave : "))

	print("\nYou scored " + str(points) + " points in " + str(number_games) + " games")

def play_without_hints():
	number_games=0
	points=0
	cont=''
	while(cont==''):
		secret_word=choose_word(wordlist)
		points+=hangman(secret_word, wordlist)
		number_games+=1
		cont=str(input("\nIf you want to continue, press Enter button or anything else to leave : "))

	print("\nYou scored " + str(points) + " points in " + str(number_games) + " games")

if __name__ == "__main__":
   
	choice=input("If you want to play with hints - press Enter button, any other key otherwise: ")
	if(choice==""):
		play_hints()
	else:
		play_without_hints()	