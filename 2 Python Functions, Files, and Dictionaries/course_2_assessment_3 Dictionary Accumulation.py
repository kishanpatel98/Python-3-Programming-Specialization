# The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable credits. Do not hardcode this – use dictionary accumulation!
Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}

credits = 0
for key, val in Junior.items():
    credits = credits + val

# Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.
str1 = "peter piper picked a peck of pickled peppers"
freq = {}

for x in str1:
    freq[x] = freq.get(x, 0) + 1

# Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.
s1 = "hello"
counts = {}

for x in s1:
    counts[x] = counts.get(x, 0) + 1

# Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}

for x in str1.split(" "):
    freq_words[x] = freq_words.get(x, 0) + 1

# Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

wrd_d = {}

for x in sent.split(" "):
    wrd_d[x] = wrd_d.get(x, 0) + 1

# Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.
sally = "sally sells sea shells by the sea shore"

characters = {}

for x in sally:
    characters[x] = characters.get(x, 0) + 1

best_char = ""
current = 0

best_char = sorted(characters.items(), key = lambda frequency: frequency[1])[-1][0]


#for key, value in characters.items():
#    if value > current:
#        current = value
#        best_char = key


# Sort those dictionary keys (tuples) by value.
#
# characters.items() are the items in your dictionary as (key, value) tuples.
#
# sorted(dictionary.items(), key=function) will sort those tuples, but we'll want a key function to tell sorted how to sort them.
#
# We define a lambda function to sort by item[1]. The lambda function accepts a (key, value) tuple and returns (key, value)[1], which is the value. That way sorted() will know to sort by the second item in the tuple.
#
# Select the last tuple [-1]. Select the key.[0]


# Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.
sally = "sally sells sea shells by the sea shore and by the road"
characters = {}

for x in sally:
    characters[x] = characters.get(x, 0) + 1

worst_char = sorted(characters.items(), key = lambda key: key[1])[0][0]

# Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.
string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts = {}

for x in string1.lower():
    letter_counts[x] = letter_counts.get(x, 0) + 1

# Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = {}

for x in p.lower():
    low_d[x] = low_d.get(x, 0) + 1
