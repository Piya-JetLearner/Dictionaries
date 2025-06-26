print("hello")
my_dictionary={}
# my_dictionary["orange"]="an orange fruit"
# print(my_dictionary)
# my_dictionary["sweet or sour"]="orange fruit"
# print(my_dictionary)
# print(my_dictionary["orange"])
# #del my_dictionary["orange"]
# for item in my_dictionary:
#     print(item,my_dictionary[item])
print("\nWelcome to my online dictiopnary! ")
print("1. Add/update a word")
print("2. Retrieve a word's definition")
print("3. Delete a word")
print("4. View all the words")
print("5.Exit")
user=int(input("enter what number you want to do: "))
if user==1:
    word=input("What word do you want to use?")
    meaning=input("What is the meaning of this word?")
    my_dictionary[word]=meaning
elif user==2:
    word=input("enter a word you want to learn:")
    print(my_dictionary[word])