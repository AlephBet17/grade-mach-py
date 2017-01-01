print("How many questions were on the assignment?")
que = int(input("> "))
print("")
print("How many questions did the student get right?")
rite = int(input(">"))


def grade():
    print("Would you like to weigh the grade? Y/N")
    weight = str(input("> "))
    if weight == "Y":
        print("How much would you weigh? Use percentages w/o the % sign.")
        lbs = int(input("> "))
        new_lbs = lbs / 100
        gr = rite / que * 100
        new_gr = gr * new_lbs
        print("Your student has a " + str(new_gr) + ".")
    else:
        gr = rite / que * 100
        print("Your student has a " + str(gr) + ".")
grade()
input(" ")
