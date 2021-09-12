myfile = open('text.txt', 'w') # Open File

# Get File Info
# print(f"My FIle is {myfile.name}")
# print(f"Closed: {myfile.closed}")
# print(f"Mode: {myfile.mode}")

myfile.write("p = 10")
myfile.write("n/ I Love Pythone and Javascript")
myfile.close()

# Append to File
myfile = open('text.txt', 'a')
myfile.write("n/\ I Love Python")
myfile.close()

myfile = open('text.txt', 'r+')
text = myfile.read()
print(text)