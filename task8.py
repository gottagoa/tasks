"""
Write a function that takes a person's full name, weight, and height as arguments. 
Let the function return these same data in the form of a dictionary.
Create a decorator that calculates the Body Mass Index (BMI) coefficient and 
provides a verdict. For example:

Name: Bob, Height: 175 cm, Weight: 68 kg ----> Bob has a BMI of 22.2 - normal weight.
Name: Joe, Height: 180 cm, Weight: 55 kg ----> Joe has a BMI of 17.0 - underweight.
Name: Finn, Height: 160 cm, Weight: 80 kg ----> Finn has a BMI of 31.2 - overweight.
"""

def decorate(func):
    def wrapper(name, height, weight):
        result = func(name, height, weight)
        imt = round(float((weight / ((height / 100) ** 2))), 1)
        if imt < 16:
            verdict = 'severe underweight'
        elif 16 < imt < 18.5:
            verdict = 'underweight'
        elif 18.5 <= imt < 25:
            verdict = 'normal weight'
        elif 25 <= imt < 30:
            verdict = 'overweight'
        elif 30 <= imt < 35:
            verdict = 'obesity class 1'
        elif 35 <= imt < 40:
            verdict = 'obesity class 2'
        else:
            verdict = 'obesity class 3'
        
        return f"""
        name: {name}, height: {height}, weight: {weight} ----> {name} has an IMT of {imt} - {verdict}.
        """
    return wrapper

@decorate
def get_user_parameters(name, height, weight):
    answer = {'name': name, "height": height, 'weight': weight}
    return answer

print(get_user_parameters('Joe', 185, 70))
