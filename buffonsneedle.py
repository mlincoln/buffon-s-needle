import random
import math
import cTurtle

def buffoon(width,length,needles):
#set our drawing
	T=cTurtle.Turtle()
#frame our drawing with a little bit of an edge so we can determine whether a pin is crossing the line
	T.setWorldCoordinates(0-(width/10),0-(width/10),width*1.1,width*1.1)
	T.up()
#draw lines to indicate the floorboards
	T.goto(width,0-(width/10))
	T.down()
	T.goto(width,width*1.1)
	T.up()
	T.goto(0,width*1.1)
	T.down()
	T.goto(0,0-(width/10))
#set acc variable for pins that fall on the lines
	onLine=0
#drop the needles
	for i in range(0,needles):
#pick a random point for one end of the needle
		x1=random.random()
		y1=random.random()
#pick a random angle
		angle=360*random.random()
#convert degrees to radians
		angle=math.radians(angle)
#use geometry to find the other endpoint of the needle based on one endpoint and angle
		x2=x1+(length*math.cos(angle))
		y2=y1+(length*math.sin(angle))
#determine whether the needle is intersecting a line
		if (x1>x2 and x1>0 and x2<0) or (x1<x2 and x1<0 and x2>0) or (x1>x2 and x1>1 and x2<1) or (x1<x2 and x1<1 and x2>1):
#if it is, draw it in red
			T.up()
			T.color("red")
			T.goto(x1,y1)
			T.down()
			T.goto(x2,y2)
			T.up()
#and count it
			onLine=onLine+1
		else:
#if it isnt, on the line draw it in black
			T.up()
			T.color("black")
			T.goto(x1,y1)
			T.down()
			T.goto(x2,y2)
			T.up()
#return the formula for buffon's needle to estimate pi
	return (2*needles*length)/(onLine*width)
