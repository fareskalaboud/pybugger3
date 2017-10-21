# myaixterm.py: custom color mappings for the aixterm 256-color palette.
# Copyright (c) cxw 2015

import itertools
import csv
import os

_DEF_COLOR_FN= 'myaixterm-db.txt'

aix_colors={}

def get_all_colors():
    return aix_colors

def aix_fg(color):
    """ Returns a string that will set the foreground to _color_, which can
        be a color number (0..255) or a name in aix_colors. """
    if isinstance(color,str):
        colornum=aix_colors[color]
    else:
        colornum=color
    return '\033[38;5;%dm'%colornum

def aix_bg(color):
    """ Returns a string that will set the background to _color_, which can
        be a color number (0..255) or a name in aix_colors. """
    if isinstance(color,str):
        colornum=aix_colors[color]
    else:
        colornum=color
    return '\033[48;5;%dm'%colornum

def aix_normal():
    """ Returns a string that will set the foreground and background
        to their default colors. """
    return '\033[0m'

def aix_init(fn=_DEF_COLOR_FN):
    with open(os.path.join(os.path.dirname(__file__), fn)) as fd:
        reallines=itertools.filterfalse(lambda r: r.startswith('#'), fd)
        for row in csv.DictReader(reallines,
                                    fieldnames=['r','g','b','n'],
                                    restkey='names'):
            for name in row['names']:
                aix_colors[name]=int(row['n'])
            #end foreach name
        #end foreach row
    #end with
# end aix_init
