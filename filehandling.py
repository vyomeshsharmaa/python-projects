# Writing to a file
with open("notes.txt", "w") as file:
    file.write("Stage 4 Concept 5: File Handling\n")
    file.write("Started learning today.\n")

# Reading the entire file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

# Appending to a file without erasing what's there
with open("notes.txt", "a") as file:
    file.write("Adding one more line.\n")

# Reading all lines into a list
with open("notes.txt", "r") as file:
    lines = file.readlines()
    print(lines)