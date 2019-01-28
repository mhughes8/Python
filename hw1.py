#Program:HomeWork 1
# Aurthor: [Montel Hughes]
# Date: 1/27/2019
# Purpose- The purpose of this program is to practice basic fuction such as in conversion,and slicing. 
# 1. Convert the following variable to a float and print() the result.
var_one = 100
var_one = float(var_one)
print(var_one)
# 2a. Convert the following variable to hexadecimal and print the result.
var_two_a = 296
var_two_a= hex(var_two_a)
print(var_two_a)
# 2b. Convert the following variable to an integer and print the result
var_two_b = '0xef'
var_two_b= int(var_two_b,0)
print(var_two_b)
# 3. Convert the following variables to an integer and print the result.

var_three_a = 5.969
var_three_a= int(var_three_a)
var_three_b = 3.00101
var_three_b= int(var_three_b)
print(var_three_a)
print(var_three_b)
# 4. Using a slice operation, print only the fourth word in the following string (no spaces).

var_four = 'this is only kind of a test'
var_four = var_four[12:17]
print (var_four)
# 5. Using a slice operation, print every other character in the following 
# string starting with the first character.

var_five = 'abcdefghijklmnopqrstuvwxyz'
var_five= var_five[::2]
print (var_five)

# 6. Create a tuple of five elements of different data types, assign it to a 
# variable and print the tuple.
car_tup = ('hondi',1,'ford',2,'chevy',3,'toyota',4,)
print(car_tup)
# 7. Use a built-in string method to *replace* all of the z characters 
# with a string of 5 in the following variable and pring the result.

var_seven = 'fizz buzz'
var_seven= var_seven.replace('z','5')
print(var_seven)
# 8. Convert the following variable to a tuple and print the new tuple.

var_eight = 'something nothing kind of sort of maybe'
var_eight=tuple(var_eight)
print(var_eight)
# 9. *Sort* the list in descending order and print the sorted list.

var_list = [539, 213, 111, 904, 545, 676, 1829, 18]
var_list.sort(reverse=True)
print(var_list)
# 10. Print a list of the keys from the following dictionary using a
# a built in dictionary method.

var_dict = {'ax':100, 'zy':200, 'ff': 300, 'de':400, 'po': 500}
print (var_dict.keys)