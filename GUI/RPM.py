#!/usr/bin/env python

from Tkinter import *

class RPM(Frame):
    
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.bgColor = "black"
        self.fgColor = "white"
        self.label = Label(self, text="RPM: ----", font = ('times', 38), bg = self.bgColor, fg = self.fgColor)
        self.label.pack()
        self.config(bg = self.bgColor)
        
    def setRPM(self, rpm):
		self.label.config(text="RPM: " + str(rpm))

    def reset(self):
        self.label.config(text="RPM: ----")
	

#######################################################################################
################################ If running as main ###################################
#######################################################################################
	
if __name__ =='__main__':
	root = Tk()
	RPM().pack()
	root.mainloop()
