import random
name = input("what is your name?")
print("good luck",name)
words=['criket','football','computer','science'
       ,'success','genius']
word=random.choice(words)

print("guess the characters:")
guesses = ''
turns=10

while turns >0 :
    failed = 0

    for char in word:
        if char in guesses:
            print(char,end=" ")

        else:
            print("_")
            failed -=1


    if failed ==0:
        print("you win !")
        print("the word is:",word)
        break

    print()
    guess =  input("guess a character")

    guesses+=guess

    if guess not in word:

        turns-=1

        print("wrong!")

        print("you have ",turns,"more guesses")

        if turns==0:
            print("you lose !")
