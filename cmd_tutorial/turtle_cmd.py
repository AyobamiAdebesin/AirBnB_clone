#!/usr/bin/env python3
"""This module contains a command line program using turtle"""

import sys, cmd
from turtle import *


class TurtleShell(cmd.Cmd):
    """A turtle shell class"""
    intro = "Welcome to the turtle shell. Type help or ? to list commands.\n"
    prompt = '(turtle)'
    file = None

    def do_forward(self, arg):
        forward(*parse(arg))
    def do_right(self, arg):
        right(*parse(arg))
    def do_left(self, arg):
        left(*parse(arg))
    def do_goto(self, arg):
        goto(*parse(arg))
    def do_home(self, arg):
        home()
    def do_circle(self, arg):
        circle(*parse(arg))
    def do_position(self, arg):
        print('Current position is %d %d\n' % position())
    def do_heading(self, arg):
        print('Current heading is %d\n' % (heading(),))
    def do_color(self, arg):
        color(arg.lower())
    def do_undo(self, arg):
        'Undo (repeatedly) the last turtle action(s):  UNDO'
    def do_reset(self, arg):
        reset()
    def do_bye(self, arg):
        print('Thank you for using Turtle')
        bye()
        return True
    
    def do_record(self, arg):
        'Save future commands to filename:  RECORD rose.cmd'
        self.file = open(arg, 'w')
    def do_playback(self, arg):
        'Playback commands from a file:  PLAYBACK rose.cmd'
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())
    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line
    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    TurtleShell().cmdloop()

    
