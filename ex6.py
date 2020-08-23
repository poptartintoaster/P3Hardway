types_of_people = 10
x = f"There are {types_of_people} types_of_people."

binary = "binary"
do_not = "Don't"
y = f"Those who know {binary} and those who {do_not}."

#The following is meant to add the variables within existing statement
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

#The following is the start and a conversation and a reponse
hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

#the following is meant to apphend variable e after w
w = "This is the left side of..."
e = "a string with a right side"

print(w + e)
