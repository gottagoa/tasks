# N students take K apples and distribute them evenly among themselves. The remaining(indivisible part) 
# remains in the basket. How many apples will each student get ? How many apples will remain in the basket? 
# A program receives N students and K apples from a user.
# It has to print out two answers. How many will each student and how many apples will 
# be left in the basket.

students = int(input('Enter the number of students: '))
apples = int(input('Enter the number of apples: '))

apple_students = apples // students 
basket = apples % students

print(f'Each student will have: {apple_students} apples')
if basket == 0:
    print('There are no apples left in the basket')
else:
    print(f'There are {basket} apples left in the basket')
