# There is a function we are providing in for you in this problem called square. It takes one integer and returns the square of that integer value. Write code to assign a variable called xyz the value 5*5 (five squared). Use the square function, rather than just multiplying with *.
xyz = square(5)

# Write code to assign the number of characters in the string rv to a variable num_chars.
rv = """Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    'Tis some visitor, I muttered, tapping at my chamber door;
    Only this and nothing more."""

# Write your code here!
num_chars = len(rv)

# data-19-1: The code below initializes two variables, z and y. We want to assign the total number of characters in z and in y to the variable a. Which of the following solutions, if any, would be considered hard coding?
#
# z = "hello world"
# y = "welcome!"
# A. a = len("hello worldwelcome!")
# B. a = 11 + 8
# C. a = len(z) + len(y)
# D. a = len("hello world") + len("welcome!")
# E. none of the above are hardcoding.
#
# ✔️Correct.
# A. Though we are using the len function here, we are hardcoding what len should return the length of. We are not referencing z or y.
# B. This is hardcoding, we are writing in the value without referencing z or y.
# D. Though we are using the len function here, we are hardcoding what len should return the length of each time we call len. We are not referencing z or y.
