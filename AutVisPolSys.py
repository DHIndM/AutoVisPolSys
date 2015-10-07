# -*- coding: utf-8 -*-
"""
# ################################################################################################
# ################################################################################################
# ################################################################################################
# 
#  #    #    #    # #    #     #     ###     #          ####     ###    #     #    ####    #####
#   #    #   #   #       #     #   #     #   #          #   #   #   #   #     #   #    #   #
#    #   #   #     #     #     #   #######   #          ####    #   #   #     #   #        ###
#     # #    #       #   #     #   #     #   #          #       #   #   #     #   #    #   #
#      #     #    # #      ###     #     #   ######     #        ###    ####  #    ####    #####
# 
# ################################################################################################
# ################################################################################################
# ################################################################################################

"""

# Import all files and moduls
from time import gmtime, strftime
from Tkinter import *

#import recognition
#import recording

numberOfCams = 4


from Tkinter import Tk, Text, BOTH, W, N, E, S
from ttk import Frame, Button, Label, Style


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Windows")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        
        lbl = Label(self, text="Windows")
        lbl.grid(sticky=W, pady=4, padx=5)
        
        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=4, 
            padx=5, sticky=E+W+S+N)
        
        abtn = Button(self, text="Activate")
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="Close")
        cbtn.grid(row=2, column=3, pady=4)
        
        hbtn = Button(self, text="Help")
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="OK")
        obtn.grid(row=5, column=3)

# ################################################################################################
def main():
	""" Main method of everything """
	#print "\t Starting ... in time: ", strftime("%a, %d %b %Y %X", gmtime()), "\n"

	#print "\t Running ... in time: ", strftime("%a, %d %b %Y %X", gmtime()), "\n"

	#print "\t Recording ... in time: ", strftime("%Y-%m-%d %H:%M:%S", gmtime()), "\n"

	#print "\t Ending ... in time: ", strftime("%Y-%m-%d %H:%M:%S", gmtime()), "\n"


	# create the root window
	root = Tk()

	# modify the window
	root.title("Auto visual police system")
	root.geometry("1000x800")

	

	Button(root, text="Ukončit celý system", command=root.destroy).pack()

	for cam in xrange(numberOfCams):
		Button(root, text="Kamera číslo: "+str(cam), command=root.destroy).pack(padx=5, pady=10, fill=X, side="left")

	# Start the window's event-loop
	root.mainloop()


# ################################################################################################
if __name__ == '__main__':
	#print (__doc__)
	main()





