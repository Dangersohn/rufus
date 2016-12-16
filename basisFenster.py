from curses import wrapper
import curses
import os
import sys,time,random


def main(stdscr):
    # Clear screen
    stdscr.clear()
    screen = curses.initscr()
    screen.border(0)

    #Inof über die Felder auslesen
    ymax, xmax = screen.getmaxyx()
    ylow, xlow = screen.getbegyx()
    # legt ein neuens Feld an (height, width, begin_y, begin_x)
    box1 = curses.newwin(int(ymax *0.3) ,xmax - 4,int(ymax - ymax * 0.31  ),xlow + 2)
    box2 = curses.newwin(int(ymax *0.6) ,xmax - 4,int(ylow + 2),xlow + 2)

#Läd die Boxen das Erste mal das sie angzeigt wereden
    box1.box()
    box2.box()
    screen.refresh()
    # Läd die Box beu
    box1.refresh()
    box2.refresh()

    x = 1
    y = 1

    file = open("choice1.1.txt", "r")
    text = file.read()
    for letter in text:
        if( xmax -5  == x):
            y = y + 1
            x = 1
        else:
            box1.addch(y, x,letter)
            box1.refresh()
            box1.border(0)
            box1.refresh()
            x = x + 1
            time.sleep(0.008)
    file.close()


    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
