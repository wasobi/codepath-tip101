'''
Unit 1 - Problem Set Version 1
Team Members: Ashley Tamdjo, Usman Rashid
'''
print('\n----------------------------------------\n')
print('Problem 1\n')
# Problem 1: Hello World!
def hello_world():
	print("Hello world!")
hello_world() # Output: Hello World!

print('\n----------------------------------------\n')
print('Problem 2\n')
# Problem 2: Today's Mood
def todays_mood():
	mood = "🤗🤠🥲😁😝"
	print(mood)
todays_mood() # Output: Today's mood: 🤗🤠🥲😁😝

print('\n----------------------------------------\n')
print('Problem 3\n')
# Problem 3: Lunch Menu
def print_menu(menu):
	print("Lunch today is: " + menu)
print_menu("🍕") # output: Lunch today is: 🍕

print('\n----------------------------------------\n')
print('Problem 4\n')
# Problem 4: Sum of Two Integers
def sum(a, b):
	return a + b
sum_of_integers = sum(13,27)
print(2*sum_of_integers)

print('\n----------------------------------------\n')
print('Problem 5\n')
# Problem 5: Product of Two Integers
def product(x,y):
	return x * y
print(product(22,7))

print('\n----------------------------------------\n')
print('Problem 6\n')
# Problem 6: Classify Age
'''
Write a function classify_age() that takes an integer age as a parameter and returns "child" if the age is less than 18, and returns "adult" otherwise.
'''
def classify_age (age):
	if age < 18:
		return "child"
	else:
		return "adult"
output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)

print('\n----------------------------------------\n')
print('Problem 7\n')
# Problem 7: What Time Is It?
'''
Let's put what we learned in Problems 1-4 all together! Write a function named what_time_is_it() that takes an integer hour as a parameter.
If hour is 2, the function should return "taco time 🌮".
If hour is 12, the function should return "peanut butter jelly time 🥪”.
Otherwise, the function should return "nap time 😴".
'''
def what_time_is_it(hour):
	if hour == 2:
		return 'taco time 🌮'
	elif hour == 12:
		return 'peanut butter jelly time 🥪'
	else:
		return 'nap time 😴'

time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)

print('\n----------------------------------------\n')
print('Problem 8\n')
# Problem 8: Blackjack
'''
In the game Blackjack, players try to draw a hand of cards that totals as close to 21 as possible. Players "bust" if their cards total more than 21. Players say "Hit me!" if they want the dealer to give them another card.

Write a function called blackjack() that takes an integer score as a parameter.
If score equals 21, print "Blackjack!".
If score is greater than 21, print "Bust!".
If score is greater than or equal to 17 and less than 21, print "Nice hand!".
If score is less than 17, print "Hit me!".
'''
def blackjack(score):
	if score == 21:
		print("Blackjack!")
	elif score > 21:
		print("Bust!")
	elif score >= 17 and score < 21:
		print("Nice hand!")
	else:
		print("Hit me!")
	return

blackjack(24)
blackjack(19)
blackjack(21)
blackjack(10)

print('\n----------------------------------------\n')
print('Problem 9\n')
# Problem 9
'''
Write a function get_first() that takes in a list as a parameter and returns the first item in the list. Return None if the list is empty.
'''

def get_first(array):
	if array is None or len(array) < 1:
		return None
	else:
		return array[0]

print(get_first([3,1,6,7,5]))
print(get_first([]))

print('\n----------------------------------------\n')
print('Problem 10\n')
# Problem 10
'''
Write a function get_last() that takes in a list as a parameter and returns the last item in the list. Return None if the list is empty.
'''
def get_last(array):
	if array is None or len(array) < 1:
		return None
	else:
		return array[len(array)-1]

print(get_first([3,1,6,7,5]))
print(get_first([]))

print('\n----------------------------------------\n')
print('Problem 11\n')
# Problem 11
'''
Write a function counter() that uses the range function to print numbers between 1 and a given stop value (inclusive).
'''
def counter(stop):
	for i in range(1,stop+1):
		print(i)
counter(7)
counter(10)

print('\n----------------------------------------\n')
print('Problem 12\n')
# Problem 12: Sum of 1 to 10
'''
Write a function sum_ten() that returns the sum of numbers from 1 to 10.
'''
def sum_ten():
	total = 0
	for i in range(1,11):
		total += i
	return total
print(sum_ten())

print('\n----------------------------------------\n')
print('Problem 13\n')
# Problem 13: Total Sum
'''
Write a function sum_positive_range() that returns the sum of numbers from 1 to a given stop value (inclusive).
'''
def sum_positive_range(stop):
	total_sum = 0
	for i in range(1,stop+1):
		total_sum += i
	return total_sum
sum = sum_positive_range(6)
print(sum)

print('\n----------------------------------------\n')
print('Problem 14\n')
# Problem 14: Total Sum in Range
'''
Write a function sum_range() that returns the sum of numbers from a given start value to a given stop value (inclusive).
'''
def sum_range(start, stop):
	total = 0
	for i in range(start,stop+1):
		total += i
	return total
total = sum_range(3, 9)
print(total)

print('\n----------------------------------------\n')
print('Problem 15\n')
# Problem 15
'''
Write a function print_negatives() that takes a list of integers lst and prints all negative numbers in the list.
'''
def print_negatives(lst):
	is_negative = False

	for i in range(len(lst)):
		if lst[i] < 0:
			print(lst[i])
			is_negative = True
	if is_negative == False:
		print("None")

print_negatives([1,2,3,4,5])
print_negatives([3,-2,2,1,-5])