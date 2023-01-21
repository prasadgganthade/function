# 1. Write a Python function to find the Max of three numbers.
def max_of_two(x,y):
    if x > y:
        return x
    return y
def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z))
print(max_of_three(3,6,-5))
print(max_of_three(10,5,2))
print(max_of_three(5,15,25))
# 2 Write a Python function to sum all the numbers in a list.
def sum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total
numbers = [8,2,3,0,7]
number2 = [10,25,65,3]
print(sum(numbers))
print(sum(number2))
# 3. Write a Python function to multiply all the numbers in a list.
def multiply(list1):
    mul = 1
    for i in list1:
        mul = mul * i
    return mul
list1 = [8,2,3,-1,7]
list2 = [10,5,2]
print(multiply(list1))
print(multiply(list2))
# 4. Write a Python program to reverse a string.
def reverse(name):
    return name[::-1]
name = '1234abcd'
name1 = '5678pqrs'
print(reverse(name))
print(reverse(name1))
# method 2
def reverse_string(str1):
    new_str = ''
    index = len(str1)
    while index > 0:
        new_str += str1[index - 1]
        index = index - 1
    return new_str
str1 = '1234abcd'
str11 = '5678pqrs'
print(reverse_string(str1))
print(reverse_string(str11))
# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input('Enter the number : '))
print(factorial(n))

"""
# 6. Write a Python function to check whether a number falls in a given range.
def test_range(num, start_num,end_num = 0):
    return start_num <= num <= end_num if end_num >= start_num else end_num <= num <= start_num
print(test_range(5, 2, 7))
print(test_range(5, 7))
print(test_range(1, 3, 6))
print(test_range(6, 5))
# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def string_test(s):
    d = {'upper_case': 0, 'lower_case': 0}
    for i in s:
        if i.isupper():
            d['upper_case'] += 1
        elif i.islower():
            d['lower_case'] += 1
        else:
            pass
    print('Original sting is',s)
    print('No of uppercase letters are :',d['upper_case'])
    print('No of lowercase letters are :',d['lower_case'])
str1 = 'The Qwick Brown Fox Jumps Over Lady'
str2 = 'hello world'
str3 = 'HIGH POWER'
string_test(str1)
string_test(str2)
string_test(str3)
#8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(list1):
    x = []
    for i in list1:
        if i not in x:
            x.append(i)
    return x
list1 = [1,2,3,3,3,3,4,4,5]
list2 = [1,1,2,2,]
print(unique_list(list1))
print(unique_list(list2))
# method 2
def uni_list(list1):
    x = list(set(list1))
    print(x)
uni_list(list1)
uni_list(list2)
# 9. Write a Python function that takes a number as a parameter and check the number is prime or not.
"""
def check_prime(number):
    if (number == 1):
        return False
    elif number == 2:
        return True
    else:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
number = int(input('Enter the number : '))
print(check_prime(number))
"""
# 10. Write a Python program to print the even numbers from a given list.
def even_num(list1):
    even = []
    for i in list1:
        if i % 2 == 0:
            even.append(i)
    return even
list1 = [1,2,3,4,5,6,7,8,9]
print(even_num(list1))
# 11. Write a Python function to check whether a number is perfect or not.
def perfect_number(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return sum == n
print(perfect_number(28))
print(perfect_number(100))
print(perfect_number(6))
#12. Write a Python function that checks whether a passed string is palindrome or not.
# method 1
def ispalindrome(s):
    return s == s[::-1]
s = 'malayalam'
ans = ispalindrome(s)
if ans == True:
    print('Yes')
else:
    print('No')
# method2
def is_palindrome(s):
    for i in range(0,int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
ans = is_palindrome(s)
if ans == True:
    print('The string is palindrome')
else:
    print('The string is not palindrome')
# method 3
def palindrome_(s):
    rev = ''.join(reversed(s))
    if s == rev:
        return True
    return False
ans = palindrome_(s)
if ans:
    print('Palindrome is yes')
else:
    print('Palindrome is no')
#13. Write a Python function that prints out the first n rows of Pascal's triangle
def pascal_triangle(n):
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            print(" ",end='')
        c = 1
        for j in range(1, i+1):
            print(' ',c,sep='',end='')
            c = c * (i-j) // j
        print()
n = 5
pascal_triangle(n)
#14. Write a Python function to check whether a string is a pangram or not.
import string
alphabet = set(string.ascii_lowercase)
def ispangram(string):
    return set(string.lower()) >= alphabet
str1 = 'The quick brown fox jumps over the lazy dog'
p = ispangram(str1)
if p == True:
    print('Yes it is pangram')
else:
    print('No its not pangram')
# 15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
"""
print("Enter words seperated by hyphens : ")
list1 = [word for word in input().split("-")]
list1.sort()
print('-'.join(list1))
"""
# 16. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
def square_number(x,y):
    list1 = []
    for i in range(x,y+1):
        list1.append(i**2)
    print(list1)
square_number(1,30)


