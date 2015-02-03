# My Magic 8 Ball
import random

# put answers in a tuple
answers = (
	"Definately!",
	"No way, Jose!",
	"I'm not sure. Ask me again.",
	"Fear of the unknown is what imprisons us.",
	"It would be madness to do that!",
	"Stupid question! Ask me a different one.",
	"Makes no difference to me, do or don't - whatever.",
	"Yes."
	)

# get the players name
name = input("What is your name?\n")
print("Hello", name)
# get the users question
question = input("Please, ask me for advice then press enter to shake me.\n")

print("Shaking...\n" * 4)

# use the randint() function to select the correct answer
choice = random.randint(0, 7)

# print the answer to the screen
print(answers[choice])

# exit nicely
input("\n\nPress the RETURN key to finish.")
