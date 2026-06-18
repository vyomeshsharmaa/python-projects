# conditionals.py — making decisions in Python

# Basic if/else
age = 18

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# if/elif/else
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Conditionals with user input
password = input("Enter password: ")

if password == "python123":
    print("Access granted")
else:
    print("Access denied")

# Nested conditional
is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("Welcome, Admin")
    else:
        print("Welcome, User")
else:
    print("Please log in first")
