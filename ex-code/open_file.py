
myfile = open("sample.txt") # using the file object 'myfile' and 'open' - open is a pyhton function
content = myfile.read() # stored in content as a string
myfile.close() # close the file object if you're done with it
print(content)
