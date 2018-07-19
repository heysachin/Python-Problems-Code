#<-------- Part 1 Fundamentals --------->

#              Basics



# Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" 
# Output :
# Twinkle, twinkle, little star,
#     How I wonder what you are! 
#         Up above the world so high,
#         Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
#     How I wonder what you are
# ----------------------------------------------------
# Hints
# Using \n (newline) and \t (tab) to format the string
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!") 





# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)



# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)




#              Condition & Loop



# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1 
# j = 0,1, n-1.
# Input
# Input number of rows: 3                                                                                       
# Input number of columns: 4  
# Output
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
 
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col
print(multi_list)



# Write a Python program to check a triangle is valid or not
def triangle_check(l1,l2,l3):
    if (l1>l2+l3) or (l2>l1+l3) or (l3>l1+l2):
        print('No, the lengths wont form a triangle')
    elif (l1==l2+l3) or (l2==l1+l3) or (l3==l1+l2):
        print('yes, it can form a degenerated triangle')
    else:
        print('Yes, a triangle can be formed out of it')
length1 = int(input('enter side 1\n'))
length2 = int(input('enter side 2\n'))
length3 = int(input('enter side 3\n'))
triangle_check(length1,length2,length3)



# Write a Python program to construct the following pattern, using a nested loop number.
# 1                                                                                                             
# 22                                                                                                            
# 333                                                                                                           
# 4444                                                                                                          
# 55555                                                                                                         
# 666666                                                                                                        
# 7777777                                                                                                       
# 88888888                                                                                                      
# 999999999
for i in range(10):
    print(str(i) * i)



#  Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')



# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6 
# Digits 2
s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)




# Count the number of even and odd numbers from a series of numbers
# Input 
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4                                                                                    
# Number of odd numbers : 5
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
        count_even+=1
        else:
        count_odd+=1
                
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)





# Write a Python program to get the Fibonacci series between 0 to 50
x,y=0,1
while y<50:
    print(y)
    x,y = y,x+y


#  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
nl=[]
for x in range(1500, 2700):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))



# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
import random
number = random.randint(1,9)
guess = 0
count = 0
while guess != number and guess != "exit":
    guess = input("What's your guess?")
    
    if guess == "exit":
        break
    
    guess = int(guess)
    count += 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it!")
        print("And it only took you",count,"tries!")




# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# Input
# W3r@100a
# Output
# Valid password
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Not a Valid Password")
 




# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x == y == z:
 print("Equilateral triangle")
elif x != y != z:
 print("Scalene triangle")
else:
 print("isosceles triangle") 
    

# Write a Python program to check whether an alphabet is a vowel or consonant
l = input("Input a letter of the alphabet: ")
if l in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a vowel." % l)
elif l == 'y':
    print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
    print("%s is a consonant." % l) 






#              List





# Convert a list of characters into a string
# Input ['a', 'b', 'c', 'd']
# Output abcd
s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)




# Write a Python program to check whether a list contains a sublist.
# Input
# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))
# Output
 
def is_Sublist(l, s):
    sub_set = False
    if s == []:
        sub_set = True
    elif s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = False
 
    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i+n] == s[n]):
                    n += 1
                
                if n == len(s):
                    sub_set = True
 
    return sub_set
 
a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))



# Write a Python program to find common items from two lists.
# input
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# output
# {'Green', 'White'}
color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print(set(color1) & set(color2))



# Write a Python program to get the difference between the two lists
# Input 
# list1 = [1, 2, 3, 4]
# list2 = [1, 2]
# Output
# [3,4]
list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(list(set(list1) - set(list2)))




# Write a Python program to get the smallest number from a list.
# max_num_in_list([1, 2, -8, 0])
# return 2
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))




# Write a Python program to get the frequency of the elements in a list.
# input
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# outout
# {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)




#  Write a Python program to generate all permutations of a list in Python
# Input [1,2,3]
# Output [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
import itertools
print(list(itertools.permutations([1,2,3])))




# Write a Python program to remove duplicates from a list.
# Input a = [10,20,30,20,10,50,60,40,80,50,40]
# Output [10, 20, 30, 50, 60, 40, 80]
a = [10,20,30,20,10,50,60,40,80,50,40]
dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(uniq_items)




# Write a Python program to find the second smallest number in a list.
# input
# second_smallest([1, 2, -8, -2, 0])
# output
# -2
def second_smallest(numbers):
    a1, a2 = float('inf'), float('inf')
    for x in numbers:
        if x <= a1:
            a1, a2 = x, a1
        elif x < a2:
            a2 = x
    return a2
print(second_smallest([1, 2, -8, -2, 0]))




# Write a Python program to sum all the items in a list
# Example sum_list([1,2,-8])
# Return -5
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))




#              String



# Write a Python program to create a Caesar encryption
 
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
# The method is named after Julius Caesar, who used it in his private correspondence.
 
# plaintext:  defend the east wall of the castle
# ciphertext: efgfoe uif fbtu xbmm pg uif dbtumf
 
def caesar_encrypt(realText, step):
    outText = []
    cryptText = []
    
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
    for eachLetter in realText:
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)
            crypting = (index + step) % 26
            cryptText.append(crypting)
            newLetter = uppercase[crypting]
            outText.append(newLetter)
        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)
            crypting = (index + step) % 26
            cryptText.append(crypting)
            newLetter = lowercase[crypting]
            outText.append(newLetter)
    return outText
 
code = caesar_encrypt('defend the east wall of the castle', 1)
print()
print(code)
print()
 




#  Write a Python program to change a given string to a new string where the first and last chars have been exchanged
def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
    
print(change_sring('abcd'))
print(change_sring('12345'))


# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google'
# Expected Result : {'g': 2, 'o': 2, 'l': 1, 'e': 1}
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google'))





# Write a Python function to create the HTML string with tags around the word(s).
# Sample function and result : 
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
 
def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)
 
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))


# Write a Python function that takes a list of words and returns the length of the longest one
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]
print(find_longest_word(["PHP", "Exercises", "Backend"]))





# Write a Python program to remove the nth index character from a nonempty string
def remove_char(str, n):
      first_part = str[:n] 
      last_pasrt = str[n+1:]
      return first_part + last_pasrt
    
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))




# 'The quick brown fox jumps over the lazy dog.'
# input : "The quick brown fox jumps over the lazy dog."
# output : "dog. lazy the over jumps fox brown quick The "
def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
    
print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
print(reverse_string_words("Python Exercises."))




# Write a Python program to calculate the length of a string.
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('hello world'))




# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)
items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))


#  Write a Python program to count the occurrences of each word in a given sentence
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print( word_count('the quick brown fox jumps over the lazy dog.'))





#              Dictionary



# Check if a given key already exists in a dictionary
# input
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# is_key_present(5)
# is_key_present(9)
# output
# Key is present in the dictionary                                                                              
# Key is not present in the dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)




# Write a Python script to concatenate following dictionaries to create a new one
# Input
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Output
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
 
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)




# Write a Python program to iterate over dictionaries using for loops.
d = {'x': 10, 'y': 20, 'z': 30} 
for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value)


# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary :  {0: 0, 1: 2, 2: 1, 3: 4, 4: 3}                                                         
# Dictionary in ascending order by value :  [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)]                            
# Dictionary in descending order by value :  [(4, 3), (3, 4), (2, 1), (1, 2), (0, 0)]
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value : ',sorted_d)



# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)




#              File


# Sum all the items in a dictionary
# Input {'data1':100,'data2':-54,'data3':247}
# Output 293
my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))



# Write a Python program to read first n lines of a file.
# Use test.txt file
def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
                        
file_read_from_head('test.txt',2)



# Write a python program to find the longest words in a file
# Using text.txt file in same folder
def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print(longest_word('test.txt'))




# Write a Python program to read a random line from a file.
# Using test.txt
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('test.txt'))



#              Class




# Write a Python program to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
# These brackets must be close in the correct order, 
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{‌{‌{" are invalid.
class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0
print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))




# Write a Python class named Circle constructed by a radius and two methods which
# will compute the area and the perimeter of a circle.
class Circle():
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14
NewCircle = Circle(8)
print(NewCircle.area())
print(NewCircle.perimeter())


# Write a Python class to convert a roman numeral to an integer
# Sample input
# 'MMMCMLXXXVI'
# 'MMMM'
# 'C'
# Sample output
# 3986                                                                                                          
# 4000                                                                                                          
# 100
class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val
print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('MMMM'))
print(py_solution().roman_to_int('C'))



# Write a Python program to convert an integer to a roman numeral.
class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
print(py_solution().int_to_Roman(1))
print(py_solution().int_to_Roman(4000))



# Write a Python class which has two methods get_String and print_String. 
# get_String accept a string from the user and print_String print the string in upper case.
class IOString():
    def __init__(self):
        self.str1 = ""
    def get_String(self):
        self.str1 = input()
    def print_String(self):
        print(self.str1.upper())
str1 = IOString()
str1.get_String()
str1.print_String()




# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w
    def rectangle_area(self):
        return self.length*self.width
newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())




# Write a Python class to reverse a string word by word.
# Input "hello world"
# Output "world hello"
class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))
print(py_solution().reverse_words('hello world'))




# Write a Python program to find the three elements that sum to zero from a set (array) of n real numbers.
# Input
# [-25, -10, -7, -3, 2, 4, 8, 10]
# Output
# [[-10, 2, 8], [-7, -3, 10]]
class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result
print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))
 





#              Math



# Write a Python program to convert a binary number to decimal number.
 
 
b_num = list(input("Input a binary number: "))
value = 0
 
for i in range(len(b_num)):
    digit = b_num.pop()
    if digit == '1':
        value = value + pow(2, i)
print("The decimal value of the number is", value)





# Write a Python program to flip a coin 1000 times and count heads and tails.
import random
import itertools
results = {
    'heads': 0,
    'tails': 0,
}
sides = list(results.keys())
for i in range(10000):
    results[random.choice(sides)] += 1
print('Heads:', results['heads'])
print('Tails:', results['tails'])




#  Write a Python program to generate a series of unique random numbers
import random
choices = list(range(100))
random.shuffle(choices)
print(choices.pop())
while choices:
    print(choices.pop())



    
# Write a Python function to round up a number to specified digits.
import math
def roundup(a, digits=0):
    n = 10**-digits
    return round(math.ceil(a / n) * n, digits)
x = 123.01247
print("Original  Number: ",x)
print(roundup(x, 0))
print(roundup(x, 1))
print(roundup(x, 2))
print(roundup(x, 3))





# Write a Python program to calculate the standard deviation of the following data.
# Input
# Sample Data:  [4, 2, 5, 8, 6]                                                                                 
# Output
# Standard Deviation :  2.23606797749979
import math
import sys
def sd_calc(data):
    n = len(data)
    if n <= 1:
        return 0.0
    mean, sd = avg_calc(data), 0.0
    # calculate stan. dev.
    for el in data:
        sd += (float(el) - mean)**2
    sd = math.sqrt(sd / float(n-1))
    return sd
def avg_calc(ls):
    n, mean = len(ls), 0.0
    if n <= 1:
        return ls[0]
    # calculate average
    for el in ls:
        mean = mean + float(el)
    mean = mean / float(n)
    return mean
data = [4, 2, 5, 8, 6]
print("Sample Data: ",data)
print("Standard Deviation : ",sd_calc(data))
 

#              Datetime


#  Write a Python program to convert Year/Month/Day to Day of Year in Python
import datetime
today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
print(day_of_year)



#  Write a Python program to get the current time in Python.
import datetime
print(datetime.datetime.now().time())



# Write a Python script to display the various Date Time formats.
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week
import time
import datetime
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))



# Write a Python program to get current time in milliseconds in Python
import time
milli_sec = int(round(time.time() * 1000))
print(milli_sec)



#  Write a Python program to subtract five days from current date
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)




#              Regex



# Write a Python program to find all five characters long word in a string.
# Input
# 'The quick brown fox jumps over the lazy dog.'
# Output
# ['quick', 'brown', 'jumps']
import re
text = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r"\b\w{5}\b", text))


# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
# Input
# "ABCDEFabcdef123450"
# "*&%@#!}{"
# Output
# True                                                                                                          
# False
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)
print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))



# Write a Python program to find the occurrence and position of the substrings within a string.
# 
# Input
# text = 'Python exercises, PHP exercises, C# exercises'
# pattern = 'exercises'
# 
# Output
# Found "exercises" at 7:16                                                                                     
# Found "exercises" at 22:31                                                                                    
# Found "exercises" at 36:45
import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))


# Write a Python program to remove everything except alphanumeric characters from a string.
# Input
# '**//Python Exercises// - 12. '
# Output
# PythonExercises12
import re
text1 = '**//Python Exercises// - 12. '
pattern = re.compile('[\W_]+')
print(pattern.sub('', text1))


# Write a Python program to remove the parenthesis area in a string.
# 
# Input
# ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
# 
# Output
# example                                                                                                       
# w3resource                                                                                                    
# github                                                                                                        
# stackoverflow
import re
items = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for item in items:
    print(re.sub(r" ?\([^)]+\)", "", item))



# Remove all whitespaces from a string
# 
# Input
# ' Python    Exercises '
# Output
# PythonExercises
import re
text1 = ' Python    Exercises '
print("Original string:",text1)
print("Without extra spaces:",re.sub(r'\s+', '',text1))



# Write a Python program to remove leading zeros from an IP address.
# Input
# "216.08.094.196"
# Output
# 216.8.94.196
import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)


#<-------- Part 2 Algorithms --------->

#              Array


str = "abcdbdba"

def longest_substring(str):
    max_length=0

    for i,c in enumerate(str):
        start=i
        sub_str=[]
        while start<len(str) and str[start] not in sub_str:
            sub_str.append(str[start])
            start=start+1
        print(sub_str)

        if max_length<len(sub_str):
            max_length=len(sub_str)

    return max_length

print (longest_substring(str))




"""
Given a collection of intervals which are already sorted by start number, merge all overlapping intervals.
For example,
Given [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]],
return [[1, 10], [11, 18], [19, 22]]
"""
org_intervals = [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]]
i = 0
while i < len(org_intervals)-1:
#     print(org_intervals[i])
    if org_intervals[i+1][0] < org_intervals[i][1]:
        org_intervals[i][1]=org_intervals[i+1][1]
        del org_intervals[i+1]
        i = i - 1
    i = i + 1
print(org_intervals)


"""
Given a collection of intervals which are already sorted by start number, merge all overlapping intervals.
For example,
Given [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]],
return [[1, 10], [11, 18], [19, 22]]
"""
org_intervals = [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]]
i = 0
while i < len(org_intervals)-1:
    print(org_intervals)
    if org_intervals[i+1][0] < org_intervals[i][1]:
        print("{} < {}".format(org_intervals[i+1][0], org_intervals[i][1]))
        org_intervals[i][1]=org_intervals[i+1][1]
        print(org_intervals)
        del org_intervals[i+1]
        i = i - 1
    i = i + 1
print(org_intervals)
























