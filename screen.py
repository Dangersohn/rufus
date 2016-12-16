from curses import wrapper
import curses
import os
import sys,time,random


def main(stdscr):
    # Clear screen
    stdscr.clear()
    screen = curses.initscr()
    screen.border(0)

    screenmax = screen.getmaxyx()
    # Mach eine neue box (height, width, begin_y, begin_x)
    box1 = curses.newwin(19,screenmax[1] -2 ,40,2)
    box1.box()
    # Läd die Box beu
    box1.refresh()
    screen.refresh()
    stdscr.refresh()
   
## Öffnet das File und printet es an die richitg stelle
    x = 1
    y = 1

    file = open("choice1.1.txt", "r")
    text = file.read()
    for letter in text:
        if( screenmax[1] -1  == x):
            y = y + 1
            x = 1
        else:
            screen.addch(y, x,letter)
            screen.refresh()
            screen.border(0)
            box1.refresh()
            x = x + 1
            time.sleep(0.008)
    file.close()


    stdscr.getkey()

wrapper(main)


