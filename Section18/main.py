import turtle as t
import heroes
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

# def draw(sides = 3):
#   for _ in range(7):
#     angle = float(360 / sides)
#     tim.color(random.choice(colors))
#     for _ in range(int(sides)):
#       tim.forward(100)
#       tim.right(angle)
#     sides += 1
    
# draw()


def random_pattern(count = 200):
  directions = [0, 90, 180, 270]
  tim.pensize(15)
  for _ in range(count):
    tim.color(random_color())
    tim.forward(25)
    tim.setheading(random.choice(directions))
    
random_pattern(10000)

# def spiral(gap = 5):
#   circle = int(360 / gap)
#   for _ in range(circle):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(tim.heading() + gap)
    
# spiral()