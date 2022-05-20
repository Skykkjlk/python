from turtle import *
color = ['orange','red','yellow','blue','green']
for x in range(360):
    pencolor(color[x % 5])
    width(x/5 +1)
    forward(x)
    left(35)