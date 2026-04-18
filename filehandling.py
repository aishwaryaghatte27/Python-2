@@ -0,0 +1,25 @@
# Step 1: Write to file

file = open("myfile.txt", "w")

file.write("Hello Students")

file.close()

# Step 2: Append to file

file = open("myfile.txt", "a")

file.write("\nWelcome to Python")

file.close()

#Step 3: Read from file

file = open("myfile.txt", "r")

data = file.read()

print(data)

file.close()  
