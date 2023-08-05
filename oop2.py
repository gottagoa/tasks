'''
Alphabet Class

Create a class called Alphabet.
Create a __init__() method inside it, within which two dynamic properties will be defined: 
1) lang - language, and 
2) letters - a list of letters. Initial values of the properties are taken from the method's input parameters.
Create a method called print_letters() that will print the alphabet letters to the console.
Create a method called letters_num() that will return the count of letters in the alphabet.

EngAlphabet Class

Create a class called EngAlphabet by inheriting from the Alphabet class.
Create a __init__() method inside it, which will call the parent __init__() method.
It will receive language designation (e.g., 'En') and a string consisting of all alphabet 
letters as its parameters.
super().init("En", "string with all English letters")
Add a property called letters_num, which will store the count of letters in the alphabet.
Create a method called is_en_letter() that will take a letter as a parameter and determine if 
the letter belongs to the English alphabet.
Override the letters_num() method - in the current class, it should return the value of the 
letters_num property.

Create a method called example() that will return an example of text in the English language.
Tests:

Create an object of the EngAlphabet class.
Print the alphabet letters for this object.
Display the count of letters in the alphabet.
Check if the letter 'F' belongs to the English alphabet.
Check if the letter 'Щ' belongs to the English alphabet.
Display an example of text in the English language.
'''

class Alphabet():
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_letters(self):
        print(f'Alphabet letters in the English language: {self.letters}')

    def letters_num(self):
        print(f'Number of letters in the English alphabet: {len(self.letters)}')


class EngAlphabet(Alphabet):

    def __init__(self):
        super().__init__('En', 'ABCDEFGHIGKLMNOPQRSTUVWXYZ')
        self.num_of_letters = len(self.letters)

    def letters_num(self):
        return self.num_of_letters

    def is_en_letter(self, letter):
        letter = letter.upper()
        if letter in self.letters:
            print(f'{letter} is a letter of the English alphabet')
        else:
            print(f'"{letter}" is not a letter of the English alphabet')

    def example(self):
        return "Life is good!"


word = EngAlphabet()
word.print_letters()
print(word.letters_num())
print(word.is_en_letter('л'))
print(word.example())
