import turtle

def draw_square(square_shape):
    for i in range (1,5):
        square_shape.forward(100)
        square_shape.right(90)

    # Or else the loop below will also work just as for
    # while (side_count<square_count):
    #     brad.forward(100)
    #     brad.right(90)
    #     side_count =  side_count+1


def draw_shapes():

    turtle.Turtle()
    window = turtle.Screen()
    window.bgcolor("white")
    brad = turtle.Turtle()

    rotations=0
    circlerotations=360

    # while (rotations<circlerotations):
    #     draw_square(brad)
    #     brad.right(1)
    #     brad.speed(20)
    #     rotations=rotations+1

    for i in range (1,360):
        draw_square(brad)
        brad.right(1)
        brad.speed(20)
        # rotations=rotations+1

    #Drawing of a circle
    # angie = turtle.Turtle()
    # angie.circle(300)
    # angie.speed(1)
    # angie.color("white")

    window.exitonclick()
draw_shapes()
