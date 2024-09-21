'''
Unit 1 - Problem Set Version 2
'''
# Problem 1
print('\n----------------------------------------\n')
print('Problem 1\n')
'''
Write a function greet_user() that takes in a string name as a parameter and prints "Hello <name>".
'''

def greet_user(name):
    print("Hello " + name)

greet_user("Michael")

# Problem 2
print('\n----------------------------------------\n')
print('Problem 2\n')
'''
Write a function difference() that returns the difference between two integers a and b (b should be subtracted from a).
'''

def difference(a, b):
    return abs(a-b)
diff = difference(3,8)
print(diff)

# Problem 3
print('\n----------------------------------------\n')
print('Problem 3\n')
'''
Given an integer list nums of length n, create a function concatenate_list() that creates and returns a list ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums lists.
'''

def concatenate_list(nums):
    length = len(nums)
    new_list = [-1]*length*2
    new_list[:length] = nums
    new_list[length:] = nums
    return new_list

list1 = [1,2,3,4]
concat_list = concatenate_list(list1)
print(concat_list)

# Problem 4
print('\n----------------------------------------\n')
print('Problem 4\n')
'''
Write a function sleep_assessment() that takes in an integer parameter hours indicating the number of hours the user slept.
If hours is less than 8, print "Oof, go back to bed!".
If hours is greater than or equal to 8 and less than or equal to 10, print "You got a good night's rest!".
If hours is greater than 10, print "You're a sleep prodigy!".
'''
def sleep_assessment(hours):
    if hours > 10:
        print("You're a sleep prodigy!")
    elif hours >= 8 and hours <= 10:
        print("You got a good night's rest!")
    else:
        print("Oof, go back to bed!")

# Unit Tests
sleep_assessment(10)
sleep_assessment(4)
sleep_assessment(12)
sleep_assessment(9)

# Problem 5
print('\n----------------------------------------\n')
print('Problem 5\n')
'''
Write a function calculate_tip() that takes in a float bill and a string service_quality as parameters.
If service_quality is "poor", the function should return 10% of the bill value.
If service_quality is "average", the function should return 15% of the bill value.
If service_quality is "excellent", the function should return 20% of the bill value.
If service_quality is any other value, the function should return None.
'''
def calculate_tip(bill, service_quality):
    match service_quality:
        case "average":
            return bill * 0.15
        case "excellent":
            return bill * 0.2
        case "poor":
            return bill * 0.1
        case _:
            return None

# Unit Tests
tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)
tip4 = calculate_tip(44.53, "random")
print(tip4)

# Problem 6
print('\n----------------------------------------\n')
print('Problem 6\n')
'''
Write a function rock_paper_scissors() that determines the winner of a game of Rock, Paper, Scissors. The function accepts two strings as parameters: player1 and player2. Each parameter can have a value of "rock", "paper", or "scissors".

Print either "Player 1 wins!" or "Player 2 wins!" according to the following rules:
Rock wins against scissors.
Scissors wins against paper.
Paper wins against rock.

If both player1 and player2 have the same value, print "It's a tie!".
'''
def rock_paper_scissors(player1, player2):
    valid_play = {"scissors", "rock", "paper"}
    if player1 not in valid_play or player2 not in valid_play:
        print("Invalid play")
        return    
    if player1 == player2:
        print("It's a tie!")
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        print("Player 1 wins!")
    else: 
        print("Player 2 wins!")

# Tests
rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")
rock_paper_scissors("paperd", "rockt")

# Problem 7
print('\n----------------------------------------\n')
print('Problem 7\n')


# Problem 8
print('\n----------------------------------------\n')
print('Problem 8\n')


# Problem 9
print('\n----------------------------------------\n')
print('Problem 9\n')


# Problem 10
print('\n----------------------------------------\n')
print('Problem 10\n')


# Problem 11
print('\n----------------------------------------\n')
print('Problem 1\n')


# Problem 11
print('\n----------------------------------------\n')
print('Problem 1\n')


# Problem 12
print('\n----------------------------------------\n')
print('Problem 1\n')



# Problem 13
print('\n----------------------------------------\n')
print('Problem 13\n')


# Problem 14
print('\n----------------------------------------\n')
print('Problem 14\n')


# Problem 15
print('\n----------------------------------------\n')
print('Problem 15\n')