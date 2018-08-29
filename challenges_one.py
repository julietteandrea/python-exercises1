
def has_unique_chars(word):
    """Does word contain unique set of characters?
	
	>>> has_unique_chars("Monday")
	True

	>>> has_unique_chars("Moonday")
	False

	>>> has_unique_chars("")
	True

    """
    #alternative 1
    # chars = {}

    # for char in word:
    # 	chars[char] = chars.get(char, 0) +1

    # for v in chars.values():
    # 	if v > 1:
    # 		return False
    # return True

    #alternative 2
    unique_lst = []

    for char in word:
    	if char not in unique_lst:
    		unique_lst.append(char)
    	else:
    		return False
    return True


def does_string_contain_letter(letter, string):
	"""Determine whether a given letter is in a string.

	for  example::

		>>> does_string_contain_letter("a", "apple")
		True
		>>> does_string_contain_letter("t", "florida")
		False
	"""
	
	#iterate over string, and check if the letter is in the string. If it it
	#return True if not, return False

	for char in string:
		if letter == char:
			return True
		else:
			return False

def duplicate_letters(string1, string2):
	"""Determine whether there are duplicate letters in a string.

	for example::

		>>> duplicate_letters("hello", "world")
		True
		>>> duplicate_letters("ship", "car")
		False
	"""
	
	for char in string1:
		if char in string2:
			return True
	return False


def duplicate_letters_2(string1, string2):
	"""Return a list of duplicate letters between two strings.
	If a letter appears more than once, the list should only contain the letter
	once.

	for example::

		>>> duplicate_letters_2("banana", "grape")
		['a']
		>>> duplicate_letters_2("raspberry", "cherry")
		['e', 'r', 'y']
		>>> duplicate_letters_2("red", "book")
		[]

	"""
	#iterate over string1 and string2
	#if char in string1 in string2
	#add to an empty set
	#return the set
	#if no duplicates return empty list

	duplicate_letters = set()

	for char in string1:
		if char in string2:
			duplicate_letters.add(char)

	if duplicate_letters:
		return list(sorted(duplicate_letters))
	return []
	

def is_palindrome(word):
	"""Return True/False if this word is a palindrome.

	for example::

		>>> is_palindrome("a")
		True

		>>> is_palindrome("noon")
		True

		>>> is_palindrome("porcupine")
		False

		>>> is_palindrome("racecar")
		True

	"""
	#create two counters
	#iterate over word if more than 1(return True if not)
	#if first char matches the last char
	#move first char count +1 and last char count to -1
	#return True when iteration ends
	#if chars don't match, return false

	start = 0
	end = -1

	if len(word) < 2 :
		return True

	for index in word:
		if word[start] == word[end]:
			start += 1
			end -= 1
		else:
			return False
	return True


def is_num_prime(input):
	"""return true if number is prime, otherwise return false.

	for example::
		>>> is_num_prime(3)
		True

		>>> is_num_prime(2)
		True

		>>> is_num_prime(8)
		False

	"""
	if input == 1 or input == 2:
		return True

	div_num = 2

	while div_num < input:
		if input % div_num == 0:
			return False
		div_num += 1

	return True


def pig_latin(phrase):
	"""Turn a phrase into pig latin.

	There will be no uppercase letters or punctuation in the phrase.
	if first letter is a constant, place it in the back and add "ay"
	if first letter is a vowel, add "yay" to the end

		>>> pig_latin('hello awesome programmer')
		'ellohay awesomeyay rogrammerpay'
	"""
	
	phrase = phrase.split(" ")
	vowels = "aeiou"
	new_list = []

	for word in phrase:
		if word[0] in vowels:
			new_list.append(word + "yay")
		else:
			new_list.append(word[1:] + word[0] + "ay")

	return " ".join(new_list)

def is_anagram_of_palindrome(word):
	"""Is the word an anagram of a palindrome?

	>>> is_anagram_of_palindrome("a")
	True

	>>> is_anagram_of_palindrome("ab")
	False

	>>> is_anagram_of_palindrome("aab")
	True

	>>> is_anagram_of_palindrome("arceace")
	True

	>>> is_anagram_of_palindrome("arceaceb")
	False
	
	"""
	pass	
		

def count_recursively(lst):
	"""Return number of items in a list, using recursion.

	>>> count_recursively([])
	0

	>>> count_recursively([1, 2, 3])
	3
	
	"""
	if not lst:
		return 0

	return 1 + count_recursively(lst[1:])

def is_pangram(sentence):
	"""Given a string, return True if it is a pangram, False otherwise.
	
	>>> is_pangram("The quick brown fox jumps over the lazy dog!")
	True

	>>> is_pangram("I like cats, but not mice")
	False
	
	"""
	alphabet_lst = set()

	sentence = sentence.split(" ")

	for word in sentence:
		for char in word:
			char = char.lower()
			if char.isalpha(): #or in "abcdefghijklmnopqrstuvwxyz":
				alphabet_lst.add(char)
	
	if len(alphabet_lst) == 26:
		return True 
	return False

def print_digits(num):
	"""Given int, print digits in reverse order, starting with the ones place.

	>>> print_digits(1)
	1
	>>> print_digits(314)
	4
	1
	3
	>>> print_digits(12)
	2
	1
	
	"""
	pass

def print_recursively(lst):
	"""Print items in the list, using recursion.

	>>> print_recursively([1, 2, 3, 4])
	1
	2
	3
	4
	
	""" 
	if lst == []:
		return
	ele = lst[0]
	print(ele)

	print_recursively(lst[1:])


def deduped(items):
	"""Return new list from items with duplicates removed.

	>>> deduped([1, 1, 1])
	[1]
	>>> deduped([1, 2, 1, 1, 3])
	[1, 2, 3]
	>>> deduped([1, 2, 3])
	[1, 2, 3]

	This should return a new list, not mutate the existing list:

	>>> a = [1, 2, 3]
	>>> b = deduped(a)
	>>> a == b
	True

	>>> a is b
	False

	"""
	new_list = set()

	for i in items:
		new_list.add(i)

	return list(new_list)




def sum_list(nums):
	"""Using recursion, return the sum of numbers in a list.
	
	For example::

	>>> sum_list([5, 5])
	10

	>>> sum_list([-5, 10, 4])
	9

	>>> sum_list([20])
	20

	The sum of an empty list is zero::

	>>> sum_list([])
	0
	
	"""
	if nums == []:
		return 0

	#print("index 0 = {}".format(nums[0]))

	return nums[0] + sum_list(nums[1:])

def has_balanced_brackets(phrase):
	"""Does a given string have balanced pairs of brackets?

	Given a string as input, return True or False depending on whether the
	string contains balanced (), {}, [], and/or <>.
	
	>>> has_balanced_brackets("<ok>")
	True

	>>> has_balanced_brackets("<[ok]>")
	True

	>>> has_balanced_brackets("<[{(yay)}]>")
	True

	>>> has_balanced_brackets("(Oops!){")
	False

	>>> has_balanced_brackets("{[[This has too many open square brackets.]}")
	False
	
	>>> has_balanced_brackets("(This has {too many} ) closers. )")
	False

	>>> has_balanced_brackets("No brackets here!")
	True
	
	"""
	counter = 0

	phrase = phrase.replace(" ", "")

	
	for char in phrase:
		if char in "([{<":
			counter += 1
			if char in ")]}>":
				counter -=1

	if counter == 0:
		return True
	return False


""""  Tree class and tree node class.  """

class Node():
	"""Node in a tree."""

	def __init__(self, data, children=None):
		self.data = data
		self.children = children or []

	def __repr__(self):
		"""reader-friendly representation of a Node object."""
		return "<Node {data}>".format(data=self.data)

class Tree():
	"""Tree."""

	def __init__(self, root):
		self.root = root

	def __repr___(self):
		"""reader-friendly representation of a tree class"""
		return "<Tree root={root}>".format(root=self.root)

	def get_nodes(self,data):
		"""Return a list of nodes with the given data.

		for example::

			>>> b1 = Node("B")
			>>> b2 = Node("B")
			>>> e = Node("E")
			>>> c = Node("C", [ b1, e])
			>>> a = Node("A", [b2, c])
			>>> tree = Tree(a)
			>>> result = tree.get_nodes("B")
			>>> result == [b2, b1]
			True
			>>> tree.get_nodes("L")
			[]
		"""
		pass


if __name__ == "__main__":
	import doctest

	print()
	result = doctest.testmod()
	if not result.failed:
		print("ALL TEST PASSED. GOOD WORK!")
	print()