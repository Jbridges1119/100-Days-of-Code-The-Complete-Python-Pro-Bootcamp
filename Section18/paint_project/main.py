###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
import random

rgb_colors = []
colors = colorgram.extract('Section18\paint_project\image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g , b)
    rgb_colors.append(new_color)

print(rgb_colors)

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
tim.hideturtle()


def painting():
  tim.setheading(225)
  tim.penup()
  tim.forward(300)
  tim.setheading(0)
  for count in range(1, 101):
    tim.pendown()
    tim.dot(20, random.choice(rgb_colors))
    tim.penup()
    tim.forward(50)
    
    if count % 10 == 0:
      tim.setheading(90)
      tim.forward(50)
      tim.setheading(180)
      tim.forward(500)
      tim.setheading(0)
  
  
  screen = t.Screen()
  screen.exitonclick()
  

painting()