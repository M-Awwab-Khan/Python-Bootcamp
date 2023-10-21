import turtle as t

tim = t.Turtle()

num_sides = [i for i in range(3, 11)]


for side in num_sides:
	angle = 360 / side
	for _ in range(side):
		tim.forward(100)
		tim.right(angle)

