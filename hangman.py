# Problem Set 2, hangman.py
# Name: Taras Pyndykivskiy
# Collaborators: Time, food, cup of tea.
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
import re

pattern=re.compile(r"[a-zA-Z]{1}|\*")
WORDLIST_FILENAME = "words.txt"

def character_validator(pattern, prompt, user_symbols):
	CEND='\033[0m'
	CRED='\033[91m'
	data=validator(pattern, "Enter the symbol you think is in the secret word : ")
	while (data in user_symbols) :
		print(CRED + "\nYou have already entered such character!" + CEND)	
		data=validator(pattern, "Enter the symbol you think is in the secret word : ")

	return data

def validator(pattern, prompt):
	
	CEND='\033[0m'
	CCYAN='\033[36m'
	CRED='\033[91m'
	text=input(CCYAN + prompt + CEND)
	while (not bool(pattern.match(text))) or len(text)!=1:
		print(CRED + "\nYou have to enter one character!" + CEND)
		text=input(CCYAN + prompt + CEND)

	return text.lower()

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
   
    result=True
    for symbol in secret_word:
    	if(symbol in letters_guessed):
    		result=True
    	else:
	    	result=False
	    	break

    return result	



def get_guessed_word(secret_word, letters_guessed):

	word_being_guessed=[None]*len(secret_word)

	for symbol in letters_guessed:
		if symbol in secret_word:
			for i in range(len(secret_word)):
				if(symbol==secret_word[i]):
					word_being_guessed[i]=symbol	
		
	formated_word=str()
	not_formated=""

	for element in word_being_guessed:
		if(element!=None):
			not_formated+=element
			formated_word+=element
		else:
			not_formated+=' '
			formated_word+="_"
		formated_word+=" "
	
	return formated_word, not_formated

def get_available_letters(letters_guessed):

	available_letters=list(string.ascii_lowercase)
	for element in letters_guessed:
		available_letters.remove(element)

	final_result=""
	for element in available_letters:
		final_result+=element
		final_result+=" "

	return final_result[0:len(final_result)-1]
    
def info(secret_word, user_symbols):
	CRED='\033[91m'
	CYELLOW='\033[93m'
	CEND='\033[0m'
	print(CRED + get_guessed_word(secret_word, user_symbols)[0] + CEND)
	print("\n")
	print(CYELLOW + "-----------------------------------------------" + CEND)
"""
def hangman(secret_word):
	
	print("\nWelcome to the game Hangman!")
	score=0
	print("\nI am thinking of a word that is " +str(len(secret_word)) + " letters long.")

	guesses_counter=6
	user_symbols=list()

	while((guesses_counter>0) and (secret_word != get_guessed_word(secret_word, user_symbols)[1])) :

		print("\nYou have " + str(guesses_counter) + " tries.")
		print("It's possible to use such characters : " + get_available_letters(user_symbols))
		entered_character=input("Enter the symbol you think is in the secret word : ")
		while((len(entered_character)!=1) or (entered_character.isalpha()==False) or (entered_character in user_symbols)):
			if (entered_character in user_symbols):
				print("\nYou have already entered such character!")	
			else:
				print("\nYou have to enter a character!")
			entered_character=input("Enter the symbol you think is in the secret word : ")

		if(entered_character=="*"):
			print(show_possible_matches(get_guessed_word(secret_word, user_symbols)[1], wordlist))
			continue
		if(entered_character!="*"):
			user_symbols.append(entered_character)
		if(entered_character in secret_word):
			print("\nYou guessed a correct character !")
			print("Secret word does contain such character : " + entered_character)

		else:
			print("Secret word doesn't contain such character : " + entered_character)
			guesses_counter-=1
			print(get_guessed_word(secret_word, user_symbols)[0])
			
			print("-----------------------------------------------")
			continue

			
		print(get_guessed_word(secret_word, user_symbols)[0])
		
		print("-----------------------------------------------")

	if(secret_word == get_guessed_word(secret_word, user_symbols)[1]):
		print("\nCongratulations! You have guessed the secret word. It was : " + secret_word )	
		print("It took " + str (6-guesses_counter) + " tries to to guess the word.")
		score+=(guesses_counter)*len(secret_word)
		print("Your score is : " + str(score))
	else:
		print("\nUnfortunately, you haven't guessed the secret word, cause you are out of tries."+
		"\nThe secret word was : " + secret_word )
		score+=0
		print("Your score is : " + str(score))
"""

def match_with_gaps(my_word, other_word):
	result=False
	if(len(my_word)!=len(other_word)):
		return False

	for i in range(len(my_word)):
		if((my_word[i]!=" ") and (my_word[i]==other_word[i])):
			result=True
		elif((my_word[i]!=" ") and (my_word[i]!=other_word[i])):
			result=False
			break
		else:
			result=True
	return result

def show_possible_matches(my_word, wordlist):
	appropriate_words=[]
	for element in wordlist:
		if(match_with_gaps(my_word, element)==True):
			appropriate_words.append(element)
	return appropriate_words
 


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

	guesses_counter=6
	user_symbols=list()

	while((is_word_guessed(secret_word, user_symbols)==False) and (guesses_counter>0)):

		print(CORANGE + "\nYou have " + str(guesses_counter) + " more tries." + CEND)
		print(CYELLOW + "It's possible to use such characters : "+ CEND + CRED + get_available_letters(user_symbols) + CEND)

		entered_character=character_validator(pattern, "Enter the symbol you think is in the secret word : ", user_symbols)

		if(entered_character=='*'):
			print(CPURPLE + "\nThere some words that correspond to the charactes you've guessed : " + CEND)
			print(CPURPLE + str(show_possible_matches(get_guessed_word(secret_word, user_symbols)[1], wordlist)) + CEND)
			
			print("\n")
			print(CYELLOW + "-----------------------------------------------" + CEND)

			continue

		user_symbols.append(entered_character)

		if(entered_character in secret_word):
			print(CGREEN + "\nYou guessed a correct character !" + CEND)
			print(CLIGHTGREEN + "Secret word does contain such character : " + entered_character + CEND)

		else:
			print(CORANGE + "Secret word doesn't contain such character : " + entered_character + CEND)
			guesses_counter-=1
#			info(secret_word, user_symbols)
#			continue

		info(secret_word, user_symbols)

	if(is_word_guessed(secret_word, user_symbols)==True):
		print(CGREEN + "\nCongratulations! You have guessed the secret word. It was : "+ CEND + CORANGE + secret_word + CEND)	
		print(CYELLOW + "It took " + str (6-guesses_counter) + " tries to to guess the word." + CEND)
		score+=(guesses_counter)*len(secret_word)
		print(CBLUE + "Your score in this game is : " + str(score) + CEND)

	else:
		print(CLIGHTGREEN + "\nUnfortunately, you haven't guessed the secret word, cause you are out of tries." + CEND)
		print(CYELLOW + "\nThe secret word was : " + CEND + CORANGE + secret_word + CEND)
		score+=0
		print(CBLUE + "Your score in this game is : " + str(score) + CEND)
  
	return score



if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

#############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines.
     
	number_games=0
	points=0
	cont=''
	while(cont==''):
		secret_word=choose_word(wordlist)
		points+=hangman_with_hints(secret_word, wordlist)
		number_games+=1
		cont=str(input("\nIf you want to continue, press Enter button or anything else to leave : "))

	print("\nYou scored " + str(points) + " points in " + str(number_games) + " games")
