import random
k=0
answer = random.randint(1, 100)
while k<1:
    guess = int(input('guess='))
    print('Your guess is', guess)
    if guess == answer :
        print('Good guess')
        k=k+1
    elif guess < answer:
        print('Too low')
    else:
        print('Too high')