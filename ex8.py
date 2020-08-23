#created a variable named formatter which will format all data that it is apphended to
formatter = "{} {} {} {}"

#
print(formatter.format(1, 2, 3, 4))
#
print(formatter.format("one", "two", "three", "four"))
#The varible will format the following and remove all of the commas
print(formatter.format(True, False, False, True))
#the fomatter variable will print out the variable four times
print(formatter.format(formatter, formatter, formatter, formatter))
#The data is formatted and aligned to the same line and remove all of the commas again
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
