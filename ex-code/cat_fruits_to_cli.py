content_file = open("fruits.txt")
fruits =  content_file.read()
content_file.close()

# print(fruits)

# FOR LOOP
# first convert content into lists

fruits_list = fruits.splitlines()

for each_fruit in fruits_list:
    print(each_fruit + " is a fruit")
