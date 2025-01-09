import curses 
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr("Hello!")
    stdscr.refresh()
    stdscr.getkey()
    
wrapper(main)
    
