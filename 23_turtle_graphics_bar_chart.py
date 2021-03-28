""" Design a Python script using the Turtle graphics library to construct a turtle bar chart representing the grades obtained by N students read from a file categorizing them into distinction, first class, second class, third class and failed. """
import turtle
import pandas as pd
file = r"C:\Python36\rakesh\marks.xlsx"
data = pd.read_excel(file,usecols = "D")
list1 = data.values.tolist()
details = []
for i in list1:
    for j in i:
        details.append(j)
max_marks = details.count(max(details))
min_marks = details.count(min(details))
max_marks = details.count(max(details))
average_marks = sum(details)/len(details)
def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()                
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                  



xs = [min_marks, max_marks, len(details),average_marks]  
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()             
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           
tess.color("blue")
tess.fillcolor("red")
tess.pensize(1)
tess1 = turtle.Turtle()
tess1.color("white")
tess2 = turtle.Turtle()
tess2.color("white")
tess3= turtle.Turtle()
tess3.color("white")
tess4= turtle.Turtle()
tess4.color("white")
tess5= turtle.Turtle()
tess5.color("yellow")

for a in xs:
    drawBar(tess, a)

tess1.setposition(0,-200)
tess1.write("MINIMUM\nMARKS", font = ("Arial","10","normal"))
tess2.hideturtle()           
tess2.penup()                
tess2.goto(40, -150)
tess2.showturtle()
tess2.pendown()
tess2.write("MAXIMUM\nMARKS", font = ("Arial","10","normal"))
tess2.goto(40,0)
tess2.right(90)
tess2.forward(50)
tess3.hideturtle()           
tess3.penup()                
tess3.goto(80, -100)
tess3.showturtle()
tess3.pendown()
tess3.write("WRITTEN\nMEMBERS", font = ("Arial","10","normal"))
tess3.goto(80,0)
tess3.right(90)
tess3.forward(100)
tess4.hideturtle()           
tess4.penup()                
tess4.goto(120, -50)
tess4.showturtle()
tess4.pendown()
tess4.write("AVERAGE\nMARKS", font = ("Arial","10","normal"))
tess4.goto(120,0)
tess4.right(90)
tess4.forward(50)
tess5.setposition(-350,200)
tess5.write("GRAPH OF EXAM MARKS", font=("Arial","20","normal"))
wn.exitonclick()
