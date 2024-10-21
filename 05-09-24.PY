#program to  add a key to a dictionar
my_dict={"a":1,"b":4}
my_dict["c"]=3
print(my_dict)

#Program to check weather the given value is present in the dictionary or not
my_dict={"name":"SAI","age":20}
value=20
if value in my_dict.values():
    print(" given value is present in  dictionary")
else:
    print(" given value is not present in  dictionary")

#Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
square_dict = {}
for i in range(1, 16):
    square_dict[i] = i**2
print(square_dict)

#program to create a dictionary from the string
s = 'hello world'
d = {}
for char in s:
    if char != ' ':
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
print(d)

#program to combine two dictionaries by adding values of common keys 
dict_1={"a":1,"b":2,"c":3}
dict_2={"a":4,"b":5,"c":6}
for key in dict_1 and dict_2:
    dict_1[key]=dict_1[key]+dict_2[key]
print(dict_1)

#program to merge two python dictionaries
dict_1={"name":'sai',"age":20}
dict_2={"city":"delhi","job":"sde"}
dict_1.update(dict_2)
print(dict_1)

# program to sort dictionary by keys or values
my_dict = {'c': 8, 'b': 6, 'a': 1, 'd': 2}
sorted_by_keys = sorted(my_dict.items())
print(dict(sorted_by_keys))
