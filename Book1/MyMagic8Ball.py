# MyMagic8Ball
import random
# write answers
ans1="definately!"
ans2="No way, Jose!"
ans3="I'm not sure. Ask me again."
ans4="Fear of the unknown is what imprisons us."
ans5="It would be madness to do that!"
ans6="Bad question! Ask me a different one."
ans7="Makes no difference to me,do or don't - whatever."
ans8="Yes."

print("Welcome to MyMagic8Ball\n\n")

name=input("What is your name?\n")
print("Hello",name)
# get the users question
question = input("Please, ask me for advice then press ENTER to shake me.\n")

print("shaking...\n"*4)
# use the randint() function to select the correct answer
choice=random.randint(1, 8)
if choice==1:
    answer=ans1
elif choice==2:
    answer=ans2
elif choice==3:
    answer=ans3
elif choice==4:
    answer=ans4
elif choice==5:
    answer=ans5
elif choice==6:
    answer=ans6
elif choice==7:
    answer=ans7
else:
    answer=ans8

# print the answer to the screen
print(answer)

print("\n\nThanks for playing",name)
input("\nPress the RETURN key to finish.")
