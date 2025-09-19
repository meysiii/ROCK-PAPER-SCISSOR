import random
choices=["rock","paper","scissors"]
user=input("Enter: ").lower()
comp=random.choice(choices)
print("Computer:",comp)
if user==comp: print("Tie!")
elif (user=="rock" and comp=="scissors") or \
     (user=="paper" and comp=="rock") or \
     (user=="scissors" and comp=="paper"):
    print("You win! 🎉")
else: print("You lose ❌")
