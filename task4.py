# create a function that accepts 2 arguments: 1 - word, 2 - number (integer)
# If number matches or exceeds the word length, the program returns the entered word without changes
# But if the entered number is less than the word length, the program outputs the part of the 
# word starting 
# from the beginning up to the index corresponding to 
# the number + add ... to the end# func("Hello", 1)

# --> H...

# func("Hello", 4)
# --> Hell...

# func("Hello", 5)
# --> Hello

def func(word, number):
    if number >= len(word):
        return word
    else:
        return word[:number] + "..."

print(func("Hello", 1))
# Output: H...

print(func("Hello", 4))
# Output: Hell...

print(func("Hello", 5))
# Output: Hello