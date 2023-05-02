from random import randint

def monty_hall():    
    
    car = randint(0, 2)  # car
    choice1 = randint(0, 2)  # 1st choice
    
    open_door = car  # for while works   
    while open_door == car or open_door == choice1:  # open_door isn't car/choice1
        open_door = randint(0, 2)

    choice2 = choice1  # for while works
    while choice2 == choice1 or choice2 == open_door:  # open_door isn't car/choice1
        choice2 = randint(0, 2)

    return car == choice1, car == choice2  # return true/false


hits1 = hits2 = 0  # sum of 1st/ 2nd hits
total = 10000
for i in range(total):
    hit1, hit2 = monty_hall()  # hit1 from choice1  # hit2 from choice2
    if hit1:
        hits1 += 1
    elif hit2:
        hits2 += 1
        
print(f"#  Monty Hall Simulation Results\n")
print(f"1st choices: {hits1}/{total} = {round(hits1 / total, 2)}%")
print(f"2nd choices: {hits2}/{total} = {round(hits2 / total, 2)}%")