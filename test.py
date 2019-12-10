
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


	 
print(match_with_gaps("te_ t", "tact")) #False
print(match_with_gaps("a_ _ le", "banana")) #False
print(match_with_gaps("a_ _ le", "apple")) #True
print(match_with_gaps("a_ ple", "apple")) #False
print("\n")
print(match_with_gaps('ap le', 'apple')) #False
print(match_with_gaps('a ple', 'apple')) #False
print(match_with_gaps('a  le', 'apple')) #True
print("\n")

print(match_with_gaps('a_ _ l_ ', 'apple')) #True
print(match_with_gaps('visi_ _ ', 'vision'))
