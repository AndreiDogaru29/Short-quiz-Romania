print("Welcome to the quiz")
answer = input("Are you ready? yes or no? ")
points = 0


def give_points(points):
    points = points + 1
    return points



if answer.lower() == "yes":

    answer = input("First question: What is the capital of Romania? ")
    if answer.lower() == "bucharest":
        print("Good answer")
        points = give_points(points)

    else:
        print("Wrong answer")

    answer = input("Second question: What is the highest mountain in Romania? ")
    if answer.lower() == "moldoveanu":
        print("Good answer")
        points = give_points(points)

    else:
        print("Wrong answer")

    answer = input("Third question: Name of the sea in Romania? ")
    if answer.lower() == "black sea":
        print("Good answer")
        points = give_points(points)

    else:
        print("Wrong answer")

    answer = input("In what year did Romania become part of the EU? ")
    if answer.lower() == "2007":
        print("Good answer")
        points = give_points(points)

    else:
        print("Wrong answer")

print("Thank you for playing this game. I hope you  had fun. You answered" , points, "questions correctly")
mark = points * 25
print("The score: ", mark)