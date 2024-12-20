import turtle

screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('light steel blue')


t_ground = turtle.Turtle()
t_ground.penup()
t_ground.pencolor('snow1')
t_ground.fillcolor('snow1')
t_ground.speed(0)
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()

t_tree = turtle.Turtle()
t_tree.hideturtle()
t_tree.speed(0)
t_tree.pensize(20)
t_tree.pencolor('brown')
t_tree.setheading(90)
t_tree.penup()
t_tree.goto(-90,-200)
t_tree.pendown()
t_tree.forward(50)
t_tree.pensize(15)
t_tree.penup()
t_tree.goto(-150,-150)
t_tree.setheading(0)
t_tree.pendown()
t_tree.pencolor('darkolivegreen')
t_tree.fillcolor("darkolivegreen")
t_tree.begin_fill()
t_tree.goto(-25,-150)
t_tree.goto(-100,200)
t_tree.goto(-150,-150)
t_tree.end_fill()

t_ornament = turtle.Turtle()
t_ornament.hideturtle()
t_ornament.speed(0)
t_ornament.pensize(1)
t_ornament.penup()
t_ornament.fillcolor("blue")
t_ornament.goto(-100,-100)
t_ornament.pendown()
t_ornament.begin_fill()
t_ornament.circle(10)
t_ornament.end_fill()
t_ornament.penup()
t_ornament.fillcolor("red")
t_ornament.goto(-100,100)
t_ornament.pendown()
t_ornament.begin_fill()
t_ornament.circle(10)
t_ornament.end_fill()
t_ornament.penup()
t_ornament.fillcolor("purple")
t_ornament.goto(-100,0)
t_ornament.pendown()
t_ornament.begin_fill()
t_ornament.circle(10)
t_ornament.end_fill()
t_ornament.penup()
t_ornament.fillcolor("orange")
t_ornament.goto(-75,50)
t_ornament.pendown()
t_ornament.begin_fill()
t_ornament.circle(10)
t_ornament.end_fill()
t_ornament.penup()
t_ornament.fillcolor("yellow")
t_ornament.goto(-75,-50)
t_ornament.pendown()
t_ornament.begin_fill()
t_ornament.circle(10)
t_ornament.end_fill()

t_present = turtle.Turtle()
t_present.hideturtle()
t_present.speed(0)
t_present.penup()
t_present.goto(-65,-250)
t_present.pendown()
t_present.fillcolor("red")
t_present.begin_fill()
t_present.forward(50)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.end_fill()
t_present.penup()
t_present.goto(-40,-250)
t_present.pendown()
t_present.fillcolor("green")
t_present.begin_fill()
t_present.forward(5)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.forward(5)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.end_fill()
t_present.penup()
t_present.goto(-65,-225)
t_present.pendown()
t_present.fillcolor("green")
t_present.begin_fill()
t_present.forward(50)
t_present.left(90)
t_present.forward(5)
t_present.left(90)
t_present.forward(50)
t_present.left(90)
t_present.forward(5)
t_present.left(90)
t_present.end_fill()

t_snowman = turtle.Turtle()
t_snowman.hideturtle()
t_snowman.speed(0)
t_snowman.penup()
t_snowman.goto(100,-250)
t_snowman.pendown()
t_snowman.fillcolor("white")
t_snowman.begin_fill()
t_snowman.circle(50)
t_snowman.end_fill()
t_snowman.penup()
t_snowman.goto(100,-150)
t_snowman.pendown()
t_snowman.fillcolor("white")
t_snowman.begin_fill()
t_snowman.circle(40)
t_snowman.end_fill()
t_snowman.penup()
t_snowman.goto(100,-70)
t_snowman.pendown()
t_snowman.fillcolor("white")
t_snowman.begin_fill()
t_snowman.circle(30)
t_snowman.end_fill()
t_snowman.penup()
t_snowman.goto(100,-45)
t_snowman.pendown()
t_snowman.pencolor('orange')
t_snowman.pensize(4)
t_snowman.forward(25)
t_snowman.penup()
t_snowman.goto(90,-35)
t_snowman.pendown()
t_snowman.pencolor('black')
t_snowman.pensize(1)
t_snowman.fillcolor("black")
t_snowman.begin_fill()
t_snowman.circle(5)
t_snowman.end_fill()
t_snowman.penup()
t_snowman.goto(110,-35)
t_snowman.pendown()
t_snowman.fillcolor("black")
t_snowman.begin_fill()
t_snowman.circle(5)
t_snowman.end_fill()
t_snowman.penup()
t_snowman.goto(100,-110)
t_snowman.pendown()
t_snowman.fillcolor("black")
t_snowman.begin_fill()
t_snowman.circle(5)
t_snowman.end_fill()
t_snowman.penup()
t_snowman.goto(100,-125)
t_snowman.pendown()
t_snowman.fillcolor("black")
t_snowman.begin_fill()
t_snowman.circle(5)
t_snowman.end_fill()
t_snowman.penup()
t_snowman.goto(100,-200)
t_snowman.pendown()
t_snowman.fillcolor("black")
t_snowman.begin_fill()
t_snowman.circle(5)
t_snowman.end_fill()
t_snowman.penup()
t_snowman.goto(100,-175)
t_snowman.pendown()
t_snowman.fillcolor("black")
t_snowman.begin_fill()
t_snowman.circle(5)
t_snowman.end_fill()
t_snowman.penup()
t_snowman.goto(100,-225)
t_snowman.pendown()
t_snowman.fillcolor("black")
t_snowman.begin_fill()
t_snowman.circle(5)
t_snowman.end_fill()
t_snowman.penup()
t_snowman.goto(90,-60)
t_snowman.pendown()
t_snowman.fillcolor("black")
t_snowman.begin_fill()
t_snowman.circle(4)
t_snowman.end_fill()
t_snowman.penup()
t_snowman.goto(100,-65)
t_snowman.pendown()
t_snowman.fillcolor("black")
t_snowman.begin_fill()
t_snowman.circle(4)
t_snowman.end_fill()
t_snowman.penup()
t_snowman.goto(110,-60)
t_snowman.pendown()
t_snowman.fillcolor("black")
t_snowman.begin_fill()
t_snowman.circle(4)
t_snowman.end_fill()



chim = turtle.Turtle()
chim.hideturtle()
chim.penup()
chim.goto(-300,-75)
chim.fillcolor("tan")
chim.begin_fill()
chim.forward(25)
chim.left(90)
chim.forward(50)
chim.left(90)
chim.forward(25)
chim.left(90)
chim.forward(50)
chim.left(90)
chim.end_fill()
chim.penup()
chim.goto(-310,10)
chim.pendown()
chim.setheading(270)
chim.fillcolor("gray40")
chim.begin_fill()
chim.circle(25,180)
chim.forward(50)
chim.left(90)
chim.forward(25)
chim.goto(-310,10)
chim.end_fill()


t_house = turtle.Turtle()
t_house.hideturtle()
t_house.speed(0)
t_house.penup()
t_house.goto(-350,-200)
t_house.pendown()
t_house.fillcolor("saddlebrown")
t_house.begin_fill()
t_house.forward(100)
t_house.left(90)
t_house.forward(100)
t_house.left(90)
t_house.forward(100)
t_house.left(90)
t_house.forward(100)
t_house.left(90)
t_house.end_fill()
t_house.penup()
t_house.goto(-325,-200)
t_house.pendown()
t_house.fillcolor("firebrick4")
t_house.begin_fill()
t_house.forward(50)
t_house.left(90)
t_house.forward(75)
t_house.left(90)
t_house.forward(50)
t_house.left(90)
t_house.forward(75)
t_house.left(90)
t_house.end_fill()
t_house.penup()
t_house.goto(-350,-100)
t_house.pendown()
t_house.fillcolor("burlywood")
t_house.begin_fill()
t_house.goto(-300,-50)
t_house.goto(-250,-100)
t_house.goto(-350,-100)
t_house.end_fill()
t_house.pensize(4)
t_house.pencolor('green')
t_house.forward(100)
t_house.pencolor("blue")
t_house.setheading(270)
t_house.penup()
t_house.goto(-340,-100)
t_house.pendown()
t_house.forward(10)
t_house.pencolor("red")
t_house.penup()
t_house.goto(-320,-100)
t_house.pendown()
t_house.forward(10)
t_house.pencolor("pink")
t_house.penup()
t_house.goto(-300,-100)
t_house.pendown()
t_house.forward(10)
t_house.pencolor("purple")
t_house.penup()
t_house.goto(-280,-100)
t_house.pendown()
t_house.forward(10)
t_house.pencolor("orange")
t_house.penup()
t_house.goto(-260,-100)
t_house.pendown()
t_house.forward(10)

t_snowflake = turtle.Turtle()
t_snowflake.hideturtle()
t_snowflake.pencolor("white")
t_snowflake.pensize(5)
t_snowflake.penup()
t_snowflake.goto(100,250)
t_snowflake.pendown()
t_snowflake.forward(50)
t_snowflake.penup()
t_snowflake.goto(100,250)
t_snowflake.pendown()
t_snowflake.setheading(90)
t_snowflake.forward(50)
t_snowflake.penup()
t_snowflake.goto(100,250)
t_snowflake.pendown()
t_snowflake.setheading(270)
t_snowflake.forward(50)
t_snowflake.penup()
t_snowflake.goto(100,250)
t_snowflake.pendown()
t_snowflake.setheading(180)
t_snowflake.forward(50)
t_snowflake.penup()
t_snowflake.goto(100,250)
t_snowflake.pendown()
t_snowflake.setheading(45)
t_snowflake.forward(50)
t_snowflake.penup()
t_snowflake.goto(100,250)
t_snowflake.pendown()
t_snowflake.setheading(135)
t_snowflake.forward(50)
t_snowflake.penup()
t_snowflake.goto(100,250)
t_snowflake.pendown()
t_snowflake.setheading(225)
t_snowflake.forward(50)
t_snowflake.penup()
t_snowflake.goto(100,250)
t_snowflake.pendown()
t_snowflake.setheading(315)
t_snowflake.forward(50)

cndycn = turtle.Turtle()
cndycn.hideturtle()
cndycn.pensize(5)
cndycn.pencolor('red')
cndycn.penup()
cndycn.goto(-250,-300)
cndycn.pendown()
cndycn.setheading(90)
cndycn.forward(50)
cndycn.right(90)
cndycn.forward(10)
cndycn.right(90)
cndycn.forward(10)
cndycn.penup()
cndycn.goto(-350,-300)
cndycn.pendown()
cndycn.setheading(90)
cndycn.forward(50)
cndycn.right(90)
cndycn.forward(10)
cndycn.right(90)
cndycn.forward(10)
cndycn.penup()
cndycn.goto(-350,-250)
cndycn.pendown()
cndycn.setheading(90)
cndycn.forward(50)
cndycn.right(90)
cndycn.forward(10)
cndycn.right(90)
cndycn.forward(10)
cndycn.penup()
cndycn.goto(-250,-250)
cndycn.pendown()
cndycn.setheading(90)
cndycn.forward(50)
cndycn.right(90)
cndycn.forward(10)
cndycn.right(90)
cndycn.forward(10)
cndycn.penup()
cndycn.goto(-350,-350)
cndycn.pendown()
cndycn.setheading(90)
cndycn.forward(50)
cndycn.right(90)
cndycn.forward(10)
cndycn.right(90)
cndycn.forward(10)
cndycn.penup()
cndycn.goto(-250,-350)
cndycn.pendown()
cndycn.setheading(90)
cndycn.forward(50)
cndycn.right(90)
cndycn.forward(10)
cndycn.right(90)
cndycn.forward(10)


t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-100,300)
t.pendown()
t.write("Merry Christmas", font=("Arial", 24, "bold"), align="center")

turtle.done()
