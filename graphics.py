from image import Window, Point, Line
import tkinter as tk




CENTER_X = 100
CENTER_Y = 100
RADIUS = 50

X1 = CENTER_X - RADIUS
Y1 = CENTER_Y - RADIUS
X2 = CENTER_X + RADIUS 
Y2 = CENTER_Y + RADIUS  

canvas.create_oval(X1, Y1, X2, Y2, fill="red", outline="black", width=25)




