# How to get Extract Color from any pic
# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors =[]
# for color in colors:
#     #rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(249, 248, 248), (231, 235, 241), (234, 242, 240), (246, 241, 245), (1, 9, 29), (121, 96, 42),
            (238, 211, 72), (77, 34, 23), (221, 80, 59), (225, 117, 100), (92, 1, 21), (178, 140, 171),
            (151, 92, 116), (35, 90, 26), (8, 154, 73), (204, 64, 92), (220, 178, 219), (167, 129, 76),
            (1, 63, 146), (4, 220, 218), (3, 80, 30), (80, 135, 178), (78, 115, 146), (131, 156, 178),
            (122, 186, 167), (122, 11, 32), (10, 216, 222), (137, 221, 208), (245, 202, 7), (229, 174, 166)]
tim.setheading(219)
tim.forward(400)
tim.setheading(0)
number_of_dots = 110
for dot_count in range(1, number_of_dots + 1 ):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
