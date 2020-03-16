import sys
import os
from pathlib import Path

import PIL
from PIL import Image
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


class Root(Tk, Image):
    def __init__(self):
        super(Root, self).__init__()
        self.title("tkinter Dialog")
        self.minsize(640, 400)
        self.labelFrame = ttk.LabelFrame(self, text="Select input location")
        self.labelFrame2 = ttk.LabelFrame(self, text="Select output location")
        self.labelFrame3 = ttk.LabelFrame(self, text="Convert")
        self.labelFrame3.grid(column=0, row=9, padx=20, pady=20)
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)
        self.labelFrame2.grid(column=0, row=5, padx=20, pady=20)
        self.sizes = [16, 24, 32, 48, 256]
        self.button1()
        self.button2()
        self.Convert()

    def png_to_ico(self):
        if self.sizes is None:
            self.sizes = [16, 32, 48]
        icon_sizes = [(x, x) for x in self.sizes]
        PIL.Image.open(self.sourcefile).save(self.targetfile, icon_sizes=icon_sizes)

    def Convert(self):
        self.Convert = ttk.Button(self.labelFrame3, text="Convert", command=self.png_to_ico())
        self.Convert.grid(column=1, row=1)

    def button1(self):
        self.button1 = ttk.Button(self.labelFrame, text="Select a file", command=self.fileDialog1())
        self.button1.grid(column=1, row=1)

    def button2(self):
        self.button2 = ttk.Button(self.labelFrame2, text="select the output directory for file",
                                  command=self.fileDialog2())
        self.button2.grid(column=1, row=5)

    def fileDialog1(self):
        self.sourcefile = filedialog.askopenfilename(initialdir="/", title="select a file")
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.sourcefile)

    def fileDialog2(self):
        self.targetfile = filedialog.asksaveasfilename(initialdir="/", title="select the output directory for file")
        self.label = ttk.Label(self.labelFrame2, text="")
        self.label.grid(column=1, row=6)
        self.label.configure(text=self.targetfile)


if __name__ == '__main__':
    root = Root()
    root.mainloop()

