import turtle


def draw_tree(branch_length, pen):
	"""Draw one branch and recursively grow two smaller branches."""
	if branch_length < 8:
		return

	pen.forward(branch_length)

	pen.left(30)
	draw_tree(branch_length * 0.7, pen)

	pen.right(60)
	draw_tree(branch_length * 0.7, pen)

	pen.left(30)
	pen.backward(branch_length)


screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.bgcolor("midnight blue")
screen.title("Recursive Turtle Tree")

pen = turtle.Turtle()
pen.speed(0)
pen.color("forest green")
pen.pensize(2)
pen.left(90)
pen.penup()
pen.goto(0, -300)
pen.pendown()

draw_tree(140, pen)

pen.hideturtle()
screen.mainloop()
