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
   
    return all([i in letters_guessed for i in secret_word])	

def get_guessed_word(secret_word, letters_guessed):

	return "".join(list(map((lambda a: a if a in letters_guessed else "_ "), secret_word)))

def get_available_letters(letters_guessed):

	return "".join(list(map(lambda a: a+" " if (a not in letters_guessed) else "", list(string.ascii_lowercase))))
    
def hangman(secret_word, wordlist):

	print("\n\nWelcome to the game Hangman!")
	score=0
	print("\nI am thinking of a word that is " +str(len(secret_word)) + " letters long.")

	warnings_counter=3
	guesses_counter=6
	user_symbols=list()
	print("You have " + str(warnings_counter) + " warnings left.")
	
	while(not is_word_guessed(secret_word, user_symbols) and (guesses_counter>0)):

		print("You have " + str(guesses_counter) + " guesses left.")
		print("Available letters : " + get_available_letters(user_symbols))

		entered_character=input("Please guess a letter : ").lower()


		if(len(entered_character)!=1 or (entered_character.isalpha()==False) or (entered_character in user_symbols)) :
			if(warnings_counter<1):
				guesses_counter-=1
											
			else:
				warnings_counter-=1
			print("Oops " + define_error(entered_character, user_symbols) + " You now have " + str(warnings_counter) + " warnings. " + get_guessed_word(secret_word, user_symbols))
			print("-"*60)
			continue

		else:
			user_symbols.append(entered_character)
		
		
		if(entered_character in secret_word):
			print("Good guess : " + get_guessed_word(secret_word, user_symbols))

		else:
			print("Oops! That letter is not in my word : " + get_guessed_word(secret_word, user_symbols))
			guesses_counter-=2 if entered_character in ('a', 'o', 'e', 'i', 'u') else 1

			
		print("-"*60)
	
	if(is_word_guessed(secret_word, user_symbols)==True):
		score+=(guesses_counter)*unique_letters(secret_word)
		print("\nCongratulations, you won! Your total score for this game is: " + str(score))	
	
	else:

		print("\nUnfortunately, you haven't guessed the secret word, cause you are out of tries.")
		print("\nThe secret word was : " + secret_word)
		
	return score

def match_with_gaps(my_word, other_word):
	my_word = my_word.replace("_", "")

	if(len(my_word)!=len(other_word)):
		return False
	
	#character_corresponds=all([(my_word[i]==other_word[i]) or not my_word[i].isalpha() for i in range(len(my_word))])
	#complete_fill_of_letter=all([(not my_word[i].isalpha() and other_word[i] not in my_word) or my_word[i].isalpha() for i in range(len(my_word))])

	#we can get rid of "not my_word[i].isalpha()" although it doesn't seem so obvious to me:

	#complete_fill_of_letter=all([other_word[i] not in my_word or my_word[i].isalpha() for i in range(len(my_word))])

	#return character_corresponds and complete_fill_of_letter
	

	#or might be placed in one line:

	return all([((my_word[i]==other_word[i]) or not my_word[i].isalpha()) and (other_word[i] not in my_word or my_word[i].isalpha()) for i in range(len(my_word))])

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
	appropriate_words=" ".join([word for word in wordlist if(match_with_gaps(my_word, word))])
	if(appropriate_words):
		print (appropriate_words)
	else: print ("No matches found!")

 
def unique_letters(secret_word):
	return len(set(secret_word))

def hangman_with_hints(secret_word, wordlist):
	
	print("\n\nWelcome to the game Hangman!")
	score=0
	print("\nI am thinking of a word that is " +str(len(secret_word)) + " letters long.")
	hint_activated=False
	warnings_counter=3
	guesses_counter=6
	user_symbols=list()
	print("You have " + str(warnings_counter) + " warnings left.")
	
	while(not is_word_guessed(secret_word, user_symbols) and (guesses_counter>0)):

		print("You have " + str(guesses_counter) + " guesses left.")
		print("Available letters : " + get_available_letters(user_symbols))

		entered_character=input("Please guess a letter : ").lower()


		if(len(entered_character)!=1 or (not (entered_character.isalpha()) and (entered_character!="*")) or (entered_character in user_symbols)) :
			if(warnings_counter<1):
				guesses_counter-=1
												
			else:
				warnings_counter-=1

			print("Oops " + define_error(entered_character, user_symbols) + " You now have " + str(warnings_counter) + " warnings. " + get_guessed_word(secret_word, user_symbols))
			print("-"*60)
			continue

		else:
			user_symbols.append(entered_character)
		
		
		if(entered_character in secret_word):
			print("Good guess : " + get_guessed_word(secret_word, user_symbols))

		else:
			if(entered_character!="*"):
				print("Oops! That letter is not in my word : " + get_guessed_word(secret_word, user_symbols))

			guesses_counter-=2 if entered_character in ('a', 'o', 'e', 'i', 'u') else 1

			
		if(entered_character=='*'):
			hint_activated=True
			print("Possible word matches are: ")
			show_possible_matches(get_guessed_word(secret_word, user_symbols))
			user_symbols.remove(entered_character)

		print("-"*60)


	if(is_word_guessed(secret_word, user_symbols)==True) and hint_activated==False:
		score+=(guesses_counter)*unique_letters(secret_word)
		print("\nCongratulations, you won! Your total score for this game is: " + str(score))	
		
	elif(hint_activated==True and guesses_counter>0):
		print("You've used a hint!")

	else:

		print("\nUnfortunately, you haven't guessed the secret word, cause you are out of tries.")
		if(hint_activated):
			print("You've used a hint, but that didn't help!")
		print("\nThe secret word was : " + secret_word)
		
	return score

def play_with_hints():
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
   
	choice=input("If you want to play without hints - press Enter button, any other key otherwise: ")
	if(choice==""):
		play_without_hints()	
	else:
		play_with_hints()