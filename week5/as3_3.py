# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the
# score is between 0.0 and 1.0, print a grade using the following table: Score Grade >= 0.9 A >= 0.8 B >= 0.7 C >=
# 0.6 D < 0.6 F If the user enters a value out of range, print a suitable error message and exit. For the test,
# enter a score of 0.85.

score = input("Enter Score: ")
sf = 0.0
try:
    sf = float(score)
except ValueError:
    print("enter numeric input")
    quit()


def computegrade(stringgrade):
    if (stringgrade > 1.0) | (stringgrade < 0):
        print("score out of bounds")
        quit()
    else:
        if stringgrade >= 0.8:
            if stringgrade >= 0.9:
                return "A"
            else:
                return "B"
        elif stringgrade >= 0.7:
            return "C"
        elif stringgrade >= 0.6:
            return "D"
        else:
            return "F"


print(computegrade(sf))
