import os
import glob
import tkinter as tk
from tkinter import filedialog
from fnmatch import fnmatch

root = tk.Tk()
root.withdraw()

#prompt user for directory and set path as root search folder
user_path = filedialog.askdirectory()
start_search_path = user_path
print ('Du hast ', user_path, ' als Hauptordner gewählt.')

#add file filter into directory
#prompt user for filefilter
#Beispiel nur jpg:
file_filter = '*.jpg'
#file_filter = input('Dateifilter eingeben (z.B. *.jpg):')
print ('Du hast ', file_filter, ' eingegeben.')
input('Press any key to continue')
for path, subdirs, files in os.walk(start_search_path):
    for name in files:
        if fnmatch(name, file_filter):
            print (os.path.join(path, name))

