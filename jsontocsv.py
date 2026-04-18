anged
+48
-0
lines changed
Search within code
 
‎filehandling.py‎
+25
Lines changed: 25 additions & 0 deletions
Original file line number	Diff line number	Diff line change
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
‎jsontocsv.py‎
+23
Lines changed: 23 additions & 0 deletions
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,23 @@
import json
import csv
# Step 1: Open and read JSON file
json_file = open("students.json", "r")
data = json.load(json_file)
json_file.close()
# Step 2: Open CSV file for writing
csv_file = open("students.csv", "w", newline="")
# Step 3: Get headers from JSON keys
headers = data[0].keys()
writer = csv.DictWriter(csv_file, fieldnames=headers)
# Step 4: Write header and rows
writer.writeheader()
writer.writerows(data)
# Step 5: Close CSV file
csv_file.close()
print("Conversion completed! Check students.csv file.")
