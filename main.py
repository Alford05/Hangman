from image import Window, Point, Line, Circle
import sys

def main():
    screen_x = 1000
    screen_y = 1000

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)


    def draw_line(canvas, x1, y1, x2, y2, color="black"):
        line = Line(Point(x1, y1), Point(x2, y2))
        canvas.draw_line(line, color)

    draw_line(win, 100, 950, 950, 950, color="red")

    draw_line(win, 100, 930, 950, 930, color="red")

    draw_line(win, 200, 930, 200, 100, color="red")

    draw_line(win, 250, 930, 250, 100, color="red")

    draw_line(win, 200, 100, 550, 100, color="red")

    draw_line(win, 450, 100, 450, 190, color="red") 


    canvas = win.get_canvas()
    my_circle = Circle(center_x=450, center_y=265, radius=75)
    my_circle.draw(canvas=canvas, fill_color="white")
    

 #   print("Can you save hom?")
 #   is_solvable = maze.solve()
 #   if not is_solvable:
 #       print("You Lose!")
 #   else:
 #       print("You win! Great work!")

    win.wait_for_close()


main()