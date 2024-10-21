# create a empty tuple on python
empty_tuple = ()
print(type(empty_tuple))  
print(empty_tuple)  


#program to unpack a tuple into several variables 
my_tuple = ("SAI", 20, "DELHI")
name, age, city = my_tuple
print("Name:", name)
print("Age:", age)
print("City:", city)

#program to add an item to the tuple
my_tuple = ("SAI", 20, "DELHI")
my_list = list(my_tuple)
my_list.append("CHENNAI")
my_tuple = tuple(my_list)
print(my_tuple)

#proram to convert tuple into a string 
my_tuple = ("I'm", "sai")
my_string = ' '.join(my_tuple)
print(my_string)

# program to find most frequent element in tuple
words = (1, 2, 8, 1, 2, 109)
count = 0
index = words[0]
for i in words:
    curr_freq =words.count(i)
    if(curr_freq > count):
        count = curr_freq
        index = i
print("Maximum element frequency tuple : " + str(index))
