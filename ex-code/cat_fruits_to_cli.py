content_file = open("fruits.txt")
fruits =  content_file.read()
content_file.close()

# print(fruits)

# FOR LOOP
# first convert content into lists

fruits_list = fruits.splitlines()

for each_fruit in fruits_list:
    print(each_fruit + " is a fruit")

# Keys:values in a dictionary {}

my_object = {"Guava":"green", "Oranges":5, "Pomme":"is french for apple"}
for gangsta_ting in my_object:
    print(gangsta_ting) # prints values

for gangsta_ting in my_object.keys():
    print(gangsta_ting) # prints values

for gangsta_ting in my_object.values():
    print(gangsta_ting) # prints values
