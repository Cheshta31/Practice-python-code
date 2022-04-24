print("Rock Scissor Paper Game")
print("Plz enter rock,paper and scissor in small letters")
user_1=input("User 1-Choose between rock,paper and scissor")
user_2=input("User 2-Choose between rock,paper and scissor")
if user_1==user_2:
    print("Both are same,play again")
elif user_1=="rock" and user_2=="paper":
    print("User 1 wins")
elif user_1=="rock" and user_2=="scissor":
    print("User 1 wins")
elif user_1=="paper" and user_2=="rock":
    print("User 2 wins")
elif user_1=="paper" and user_2=="scissor":
    print("User 2 wins")
elif user_1=="scissor" and user_2=="paper":
    print("User 1 wins")
elif user_1=="scissor" and user_2=="rock":
    print("User 2 wins")
else:
    print("Invalid Choice")

