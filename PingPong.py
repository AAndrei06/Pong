import turtle
import time
import tkinter

# Screen

error = False
stop_game = True

try:

	wn=turtle.Screen()
	wn.bgcolor("#44B12F")
	wn.setup(width=800,height=600)
	wn.title("Ping Pong")
	wn.tracer(0)
	try:
		img = tkinter.Image("photo", file="pong.png")
		turtle._Screen._root.iconphoto(True, img)
	except:
		if error == False:
			error = True
		else:
			error = False

	try:
		wn.bgpic("sp.gif")
	except:
		error = True

	# Pen

	pen=turtle.Turtle()
	pen.color("black")
	pen.penup()
	pen.hideturtle()
	pen.setposition(-320,260)

	# Pen 2

	pen2=turtle.Turtle()
	pen2.color("black")
	pen2.penup()
	pen2.hideturtle()
	pen2.setposition(20,260)

	# Pen 3

	pen3=turtle.Turtle()
	pen3.color("blue")
	pen3.penup()
	pen3.hideturtle()
	pen3.setheading(90)
	pen3.setposition(0,0)

	# Pen 4

	pen4=turtle.Turtle()
	pen4.color("white")
	pen4.penup()
	pen4.hideturtle()
	pen4.setheading(90)
	pen4.setposition(-399,-292)
	pen4.showturtle()
	pen4.pendown()
	pen4.width(5)

	# Pen 5

	pen5=turtle.Turtle()
	pen5.color("Black")
	pen5.penup()
	pen5.hideturtle()
	pen5.setposition(0,0)
	pen5.write("Player 1: 'W' and 'S'|Player 2: 'Up Arrow Key' and 'Down Arrow Key' \n                                        PRESS 'P' To Pause",align="center",font=("Arial Black",16))
	time.sleep(6)
	pen5.clear()

	# Border

	for line in range(2):
		pen4.forward(590)
		pen4.right(90)
		pen4.forward(800)
		pen4.right(90)
	pen4.hideturtle()



	# Padlle A

	padlle_a=turtle.Turtle()
	padlle_a.color("DarkBlue")
	padlle_a.shape("square")
	padlle_a.shapesize(5,1)
	padlle_a.penup()
	padlle_a.goto(-360,0)

	# Padlle B

	padlle_b=turtle.Turtle()
	padlle_b.color("DarkOrange")
	padlle_b.shape("square")
	padlle_b.shapesize(5,1)
	padlle_b.penup()
	padlle_b.goto(360,0)

	# Ball

	ball=turtle.Turtle()
	ball.color("red")
	ball.shape("circle")
	ball.shapesize(1.5,1.5)
	ball.penup()
	ball.speed(0)
	ball.goto(0,0)

	# Variables ***************************************************************

	ball_speed=1.4
	ball_dx=ball_speed
	ball_dy=ball_speed
	score_a=0
	score_b=0
	is_paused=False

	# Functions

	def up_a():
		y=padlle_a.ycor()
		y+=50
		padlle_a.sety(y)

	def down_a():
		y=padlle_a.ycor()
		y-=50
		padlle_a.sety(y)

	def up_b():
		y=padlle_b.ycor()
		y+=50
		padlle_b.sety(y)

	def down_b():
		y=padlle_b.ycor()
		y-=50
		padlle_b.sety(y)

	def pause():
		global is_paused
		if is_paused == False:
			is_paused=True
		else:
			is_paused=False


	# Keyboard

	turtle.listen()
	turtle.onkey(up_a,"w")
	turtle.onkey(down_a,"s")
	turtle.onkey(up_b,"Up")
	turtle.onkey(down_b,"Down")
	turtle.onkey(pause,"p")

	# Main Game Loop

	while True:
		
		wn.update()

		
		if is_paused==False:
			x=ball.xcor()
			y=ball.ycor()
			x+=ball_dx
			y+=ball_dy
			ball.setx(x)
			ball.sety(y)

			if ball.ycor() > 290:
				ball_dy*=-1

			if ball.ycor() < -290:
				ball_dy*=-1

			if padlle_a.ycor() > 250:
				padlle_a.sety(240)

			if padlle_a.ycor() < -250:
				padlle_a.sety(-240)


			if padlle_b.ycor() > 250:
				padlle_b.sety(240)

			if padlle_b.ycor() < -250:
				padlle_b.sety(-240)

			# Padlle and ball collision

			if (ball.xcor() < -342) and (ball.ycor() < padlle_a.ycor() + 55) and (ball.ycor() > padlle_a.ycor() - 55):
				ball_dx*=-1

			if (ball.xcor() > 342) and (ball.ycor() < padlle_b.ycor() + 55) and (ball.ycor() > padlle_b.ycor() - 55):
				ball_dx*=-1

			# Score

			if ball.xcor() > 425:
				ball.hideturtle()
				ball.setposition(0,0)
				ball.showturtle()
				score_a+=1
				ball_dx*=-1
				pen.clear()
				pen.write("Player 1 score: {}/5".format(score_a),font=("Arial Black",22))

			if ball.xcor() < -425:
				ball.hideturtle()
				ball.setposition(0,0)
				ball.showturtle()
				ball_dx*=-1
				score_b+=1
				pen2.clear()
				pen2.write("Player 2 score: {}/5".format(score_b),font=("Arial Black",22))

			# Final

			if score_a == 5:
				pen3.write("Player 1 Won",align="center",font=("Arial Black",38))
				break
		
			if score_b == 5:
				pen3.write("Player 2 Won",align="center",font=("Arial Black",38))
				break
		elif is_paused==True:
			x=ball.xcor()
			y=ball.ycor()
			ball.setposition(x,y)



	wn.mainloop()

except:
	stop_game = True


