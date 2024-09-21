'''
Unit 1
Session 2
Problem Set Version 2
Group 28 - Abigail Huang, Gianelli Lagos, Sierra Obi
'''

print('\n----------------------------------------\n')
print('Problem 1\n')
'''
Write a function convertTemp() that takes in celsius as a parameter, which denotes the temperature in celsius. The variable is a non-negative floating point number rounded to two decimal places. In the function, convert celsius into Kelvin and Fahrenheit and return the list ans, in which ans = [kelvin, fahrenheit]
'''
def convertTemp(celsius):
    kelvin = celsius + 273.15
    farenheit = (celsius * 1.80) + 32.00
    conversions = [kelvin,farenheit] # [1,1]

    # conversions = [] # [1,1]
    # conversions.append(kelvin) # conversions[0]
    # conversions.append(farenheit) # conversion[1]

    return conversions

temps = convertTemp(23.00)
print(temps)

print('\n----------------------------------------\n')
print('Problem 2\n')
'''
Write a function average() that takes in a list of integers scores as a parameter and returns the average score.
'''
def average(scores):
    total = 0
    for score in scores:
        total += score
    avg = total/len(scores)
    return avg
scores = [84,73,92,95,88]
print(average(scores))


print('\n----------------------------------------\n')
print('Problem 3\n')
'''
Write a function increment_values() that takes in a list of integers lst as a parameter and returns a new list containing each element incremented by 1.
'''
def increment_values(lst):
    # new_lst = [1]*len(lst)
    new_lst = []
    for elem in lst:
        new_lst.append(elem+1)
    return new_lst

lst = [3,5,8,2]
new_lst = increment_values(lst)
print(new_lst)

print('\n----------------------------------------\n')
print('Problem 4\n')
'''
Plan - do a linear scan of the list, checking if each element is equal to the target number
'''
def check_num(lst, num):
    for elem in lst:
        if elem == num:
            return True
    return False

lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
print(flag1)
flag2 = check_num(lst,4)
print(flag2)