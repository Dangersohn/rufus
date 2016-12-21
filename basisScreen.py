from curses import wrapper
import curses
import os
import sys,time,random


# Gibt eine Datei in eine Fenster aus 
def boxOutput(datei,fenster):
    x = 1
    y = 1
    file = open(datei, "r")
    text = file.read()
    for letter in text:
        if( xmax -5  == x):
            y = y + 1
            x = 1
        else:
            fenster.addch(y, x,letter)
            fenster.refresh()
            fenster.border(0)
            fenster.refresh()
            x = x + 1
            time.sleep(0.008)
    file.close()



def main(stdscr):
    def rufusAnzeige():
        rufusPanel.addstr(1, 1, "Rufus")
        rufusPanel.refresh()
# Clear screen
    stdscr.clear()
    screen = curses.initscr()
    screen.border(0)

#Info über die Felder auslesen
    global ymax
    global xmax
    global ylow
    global xlow
    ymax, xmax = screen.getmaxyx()
    ylow, xlow = screen.getbegyx()
    
# legt ein neuens Feld an (height, width, begin_y, begin_x)
    box1 = curses.newwin(int(ymax *0.3) ,xmax - 4,int(ymax - ymax * 0.31  ),xlow + 2)
    box2 = curses.newwin(int(ymax *0.6) ,xmax - 30 ,int(ylow + 2),xlow + 2)
    rufusPanel = curses.newwin(int(ymax *0.2) ,xlow + 26,int(ylow + 2),xmax - 28)
    inventa = curses.newwin(int(ymax *0.4) ,xlow + 26,int(ymax *0.2+2),xmax - 28)

##Läd die Boxen das Erste mal das sie angzeigt wereden#######
    box1.box()
    box2.box()
    rufusPanel.box()
    inventa.box()
    screen.refresh()
    box2.refresh()
    box1.refresh()
    rufusPanel.refresh()
    inventa.refresh()
######################################################
    rufusAnzeige()
    boxOutput("text.txt",box1)

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
