#!/usr/bin/env python
import sys
from Starters import *
from Tkinter import *
from PIL import Image, ImageTk
import RiotConsts as Consts


CHNAME = Consts.CHNAME
app = Tk()
champion_list = []
adress = 'champions/'
#app.geometry("600x400")
app.title("F2P Champion Pool")

#---------------------------------------------
#Labels
#lab1 = Label(text = "KURWA", fg = "white", bg = "black")
#lab2 = Label(text = "NAPIERDALAJ", fg = "yellow", bg = "blue")
#lab1.pack()
#lab2.pack()
#lab1.place(x=300,y=200)
#lab1.grid(row=0, column=0, sticky=W)
#lab2.grid(row=1, column=0, sticky=E)
#--------------------------------------------

#--------------------------------------------
def hello():
	championListStart(champion_list) 	
	F2PIDchampionPool(champion_list,champsID)	
	SearchChampByID(CHNAME,champsID,l)
	image0 = Image.open("champions/"+Consts.ICONS[champsID[0]])
	photo0 = ImageTk.PhotoImage(image0)
	imageLabel0 = Label(image=photo0)
	imageLabel0.image = photo0
	imageLabel0.grid(row=0, column=0)
	ch0L = Label(app, text=l[0]).grid(row=1, column=0)
	image1 = Image.open("champions/"+Consts.ICONS[champsID[1]])
	photo1 = ImageTk.PhotoImage(image1)
	imageLabel1 = Label(image=photo1)
	imageLabel1.image = photo1
	imageLabel1.grid(row=0, column=2)
	ch1L = Label(app, text=l[1]).grid(row=1, column=2)
	image2 = Image.open("champions/"+Consts.ICONS[champsID[2]])
	photo2 = ImageTk.PhotoImage(image2)
	imageLabel2 = Label(image=photo2)
	imageLabel2.image = photo2
	imageLabel2.grid(row=0, column=3)
	ch2L = Label(app, text=l[2]).grid(row=1, column=3)
	image3 = Image.open("champions/"+Consts.ICONS[champsID[3]])
	photo3 = ImageTk.PhotoImage(image3)
	imageLabel3 = Label(image=photo3)
	imageLabel3.image = photo3
	imageLabel3.grid(row=0, column=4)
	ch3L = Label(app, text=l[3]).grid(row=1, column=4)
	image4 = Image.open("champions/"+Consts.ICONS[champsID[4]])
	photo4 = ImageTk.PhotoImage(image4)
	imageLabel4 = Label(image=photo4)
	imageLabel4.image = photo4
	imageLabel4.grid(row=0, column=5)
	ch4L = Label(app, text=l[4]).grid(row=1, column=5)
	image5 = Image.open("champions/"+Consts.ICONS[champsID[5]])
	photo5 = ImageTk.PhotoImage(image5)
	imageLabel5 = Label(image=photo5)
	imageLabel5.image = photo5
	imageLabel5.grid(row=0, column=6)
	ch5L = Label(app, text=l[5]).grid(row=1, column=6)
	image6 = Image.open("champions/"+Consts.ICONS[champsID[6]])
	photo6 = ImageTk.PhotoImage(image6)
	imageLabel6 = Label(image=photo6)
	imageLabel6.image = photo6
	imageLabel6.grid(row=0, column=7)
	ch6L = Label(app, text=l[6]).grid(row=1, column=7)
	image7 = Image.open("champions/"+Consts.ICONS[champsID[7]])
	photo7 = ImageTk.PhotoImage(image7)
	imageLabel7 = Label(image=photo7)
	imageLabel7.image = photo7
	imageLabel7.grid(row=0, column=8)
	ch7L = Label(app, text=l[7]).grid(row=1, column=8)
	image8 = Image.open("champions/"+Consts.ICONS[champsID[8]])
	photo8 = ImageTk.PhotoImage(image8)
	imageLabel8 = Label(image=photo8)
	imageLabel8.image = photo8
	imageLabel8.grid(row=0, column=9)
	ch8L = Label(app, text=l[8]).grid(row=1, column=9)
	image9 = Image.open("champions/"+Consts.ICONS[champsID[9]])
	photo9 = ImageTk.PhotoImage(image9)
	imageLabel9 = Label(image=photo9)
	imageLabel9.image = photo9
	imageLabel9.grid(row=0, column=10)
	ch9L = Label(app, text=l[9]).grid(row=1, column=10)

#---------------------------------------------

startButton = Button(app, text="START", command=hello)
startButton.pack()




#---------------------------------------------
app.mainloop()