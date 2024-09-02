#count occurence in a string
name=input("RAM")
count=0
for i in name:
    count=count+1
    print(count)

#to check if two strings are anagram
element1=input("string1 is:")
element2=input("string2 is:")
if sorted(element1)==sorted(element2):
    print("strings are anagram:")
else:
    print("strings are not anagram:")

#to check string is palindrome or not
a=input("enter string:")
b=a[::-1]
if(a==b):
    print("palindrome")
else:
    print("not a palindrome")

#to replace string space with given character using replace()method
input_string=input("enter string:")
replace_char=input("enter character")
new_string=input_string.replace("",replace_char)
print(new_string)

#to convert lower case char to upper case of string
name=input("enter name:")
print(name.upper())

#to convert lowercase vowel to uppercase in string
name=input("enter name:")
vowels="aeiou"
new_str=""
for given_name in name:
    if given_name in vowels:
        new_str+=given_name.upper()
    else:
        new_str+=given_name
print(new_str)

#to separate characters in a given string
input_string=input("enter string:")
for char in input_string:
    print(char)

#to remove blank space from string
name = input("Enter your name:")
given_name = name.replace(" ", "")
print(given_name)

#to concatenate two strings using join() method
var1=input("enter1:")
var2=input("enter2:")
var3=(var1+""+var2)
print(var3)

#to concatenate two strings without using join() method
var1=input("enter1:")
var2=input("enter2:")
var3=(var1+""+var2)
print(var3)

#to remove repeated character from string
element = input("Enter your element: ")
output = ""
for char in element:
    if char not in output:
        output =output+ char
print(output)

# to check given character is vowel or consonant
char = input("Enter any char: ")
if char in 'AEIOUaeiou':
    print("Given char is a vowel.")
elif char.isalpha():
    print("Given char is a consonant.")
else:
    print("Invalid input, Please enter a valid one.")

#to check given character is digit or not
element = input("Enter your number: ")
if element.isdigit():
    print("It's a valid input")
else:
    print("Not a vaild input")

#to delete vowels in a given string
string = input("enter your string:")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""
for char in string:
    if char not in vowels:
        result = result + char
print(result)

#to count the Occurrence Of Vowels & Consonants in a String.
string = input("enter your string:")
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

vowel_count = 0
consonant_count = 0

for char in string:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1

print("The number of vowels =", vowel_count)
print("The number of consonants =", consonant_count)

# to print the highest frequency character in a String
string = input("Enter string: ")
max_count = 0
max_char = ''
for i in string:
    count = string.count(i)
    if count > max_count:
        max_count = count
        max_char = i
    elif count == max_count:
        continue
print("The highest frequency character :", max_char)

#to Replace First Occurrence Of Vowel With ‘-‘ in String
def replace_vowel(string):
    vowels = "AEIOUaeiou"
    for i in range(len(string)):
        if string[i] in vowels:
            string = string[:i] + '-' + string[i+1:]
            break
    return string

string = input("please enter a string: ")
print("Original String:", string)
print("Modified String:", replace_vowel(string)) 

# to count alphabets, digits and special characters
string = input("enter your string : ")
alphabets = digits = special = 0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
        
print("Total Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)

# to check given character is digit or not using isdigit() method
element = input("enter your number: ")
if element.isdigit():
    print("its a valid input")
else:
    print("its not a vaild input")


#to calculate sum of integers in string
int_string = input("enter a string: ")
sum_of_integers = 0
for char in int_string:
    if char.isdigit():
        sum_of_integers += int(char)
print(sum_of_integers)

#to print all non repeating character in string
string = input("enter a string:")
output= ""
for char in string:
    if char not in output:
        output += char
print(output)

#to copy one string to another string
original = input("enter name: ")
copy = original[:]
print(copy)

# to check given character is vowel or consonant
string = input("enter string: ")

vowels_list = "aeiouAEIOU"
consonants_list = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

vowels = ""
consonants = ""

for char in string:
    if char in vowels_list:
        vowels += char
    elif char in consonants_list:
        consonants += char
        
print("the vowels in string are:", vowels)
print("the consonants in  string are:", consonants)

#to check given character is digit or not
element = input("enter your number: ")
if element.isdigit():
    print("its a valid input")
else:
    print("its not a vaild input")