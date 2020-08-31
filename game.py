import random
l=["Snake","Water","Gun"]
s="Snake"
w="Water"
g="Gun"
n=input("Enter your name - ")
i=1
j=k=0
while (i<=10):
    a=random.choice(l)
    b=input("Enter your choice Snake/Water/Gun : ")
    if (a==s and b==s) or (a==w and b==w) or (a==g and b==g):
        print("Computer - ",a)
        print(n," - ",b)
        print("It's a tie")
    elif (a==s and b==w) or (a==w and b==g) or (a==g and b==s):
        print("Computer - ",a)
        print(n," - ",b)
        print("Computer won!!")
        j+=1
    else:
        print("Computer - ",a)
        print(n," - ",b)
        print("You won!!")
        k+=1
    i+=1
print("Game over!!")
if j>k:
    print("Score:\n Computer vs ",n," : ",j," - ",k)
    print("You lost!!")
elif j<k:
    print("Score:\n Computer vs ",n," : ",j," - ",k)
    print("You won!!")
else:
    print("Score:\n computer vs ",n," : ",j," - ",k)
    print("Tie!!")

