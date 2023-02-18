import random

dice1 = random.randrange(1, 6 ,1)
dice2 = random.randrange(1, 6 ,1)
sumdice = dice1 + dice2

print('The sum is ', dice1, '+', dice2, '=', sumdice)

if sumdice == 7 or sumdice == 11:
    print('you won')
elif sumdice == 2 or sumdice == 3 or sumdice ==12:
    print('you lost')
elif (sumdice >= 4 and sumdice <= 6) or (sumdice >= 8 and sumdice <= 10):
    goal = sumdice 
    print("your new goal is ", goal)


while True:
    dice1 = random.randrange(1, 6 ,1)
    dice2 = random.randrange(1, 6 ,1)
    sumdice = dice1 + dice2
    print("The sum is ", dice1, "+", dice2, "=", sumdice ) 
    if sumdice == 7:
        print("you lost")
        break
    elif sumdice == goal:
        print("you won")
        break

