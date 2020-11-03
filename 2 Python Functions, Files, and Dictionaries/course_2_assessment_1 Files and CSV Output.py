# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.
text = open("travel_plans.txt", "r")
num = 0
num = len(text.read())

# We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.
num_words = 0
with open("emotion_words.txt", "r") as text:
    for line in text:
        print (line.strip())
        num_words = num_words + len(line.split(" "))

# Assign to the variable num_lines the number of lines in the file school_prompt.txt.
with open("school_prompt.txt", "r") as text:
    num_lines = len(text.readlines())

# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
with open("school_prompt.txt", "r") as text:
    beginning_chars = text.read()[:30]

# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
three = []
with open ("school_prompt.txt", "r") as text:
    for line in text.readlines():
        three.append(line.split(" ")[2])

# Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
emotions = []
with open("emotion_words.txt", "r") as text:
    for line in text.readlines():
        emotions.append(line.split()[0])

# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
first_chars = ""
with open ("travel_plans.txt", "r") as text:
    first_chars = text.read()[:33]

# Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
p_words = []

with open("school_prompt.txt", "r") as text:
    #for x in text.read().split():
     #   if "p" in x:
       #     p_words.append (x)

    p_words = [word for word in text.read().split() if 'p' in word]
    print(p_words)
