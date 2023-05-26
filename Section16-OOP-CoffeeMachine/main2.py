from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
# Dot notation is reserved for class objects
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()