import random

def roll_dices():
    return [random.randit(1,6),random.randit(1,6)]
random_number1 = 0
random_number2 = 0
   
while random_number1 !=1 and random_number2 !=1 :
    results = roll_dices()
    random_number1 = results[0]
    random_number2 = results[1]
    random_sum = random_number1 + random_number2
    print(f"Wylosowałeś: {random_number1} i {random_number2}")
    print(f"Twój wynik: {random_sum}")

"""
def roll_dices():
    random_number1 = random.randint(1,6)
    random_number2 = random.randint(1,6)
    results = []
    results.append(random_number1)
    results.append(random_number2)
    return results
"""