from tkinter import *
from tkinter import messagebox
import random

words=['Mango','Television','Grapes','run','potato','kohinoor','building','Mind','Faizan',
       'Intelligent','philosophy','digest','railway','sikkim','Capslock','Syria','Restaurant','Giraffe',
       'pen','index','love','Dictionary','December','January','Alphabet','nice','Killer','Python','object',
       'speed','icon','project','shahrukh','preity','khan']

sliderwords = ''
count = 0

def labelSlider():
    global count,sliderwords
    text='Welcome To Typing Speed Game'
    if(count>=len(text)):
        count=0
        sliderwords=''
    sliderwords+=text[count]
    count+=1
    fontlabel.config(text=sliderwords)
    fontlabel.after(250,labelSlider)

def game_timer():
    global timeleft,i
    if timeleft<11:
        timelabelcount.config(fg='red')
    if timeleft>0:
        timeleft-=1
        timelabelcount.config(text=timeleft)
        timelabelcount.after(1000, game_timer)
    else:
        wordEntry.config(state=DISABLED)
        result=score-miss
        gameplay_detaillabel.config(text=f'Correct Words= {score} \nWrong Words= {miss}\nFinal Score= {result}')
        if result<=15:
            poorLabel.config(image=poorpic)
            poor1Label.config(image=poorpic)


        elif result>15:
            poorLabel.config(image=goodpic)
            poor1Label.config(image=goodpic)

        elif result>=30:
            poorLabel.config(image=propic)
            poor1Label.config(image=propic)


        res=messagebox.askyesno("Speed Game",'Do You Want To Play Again?')
        if res:
            score=0
            timeleft=60
            miss=0
            i=0
            timelabelcount.config(fg='black')
            wordEntry.config(state=NORMAL)
            poorLabel.place_forget()
            poor1Label.place_forget()
            timelabelcount.config(text=timeleft)
            scorelabelcount.config(text=i)
            wordlabel.config(text=words[0])
            gameplay_detaillabel.config(text='Type Word And Hit Enter')

        else:
            root.destroy()



score=0
miss=0
i=0
def play_game(event):


    global timeleft,score,miss,i
    i += 1
    scorelabelcount.config(text=i)
    if timeleft==60:
        game_timer()
    gameplay_detaillabel.config(text='')
    if wordEntry.get()==wordlabel['text']:

        score+=1

    else:
        miss+=1

    random.shuffle(words)
    wordlabel.config(text=words[0])
    wordEntry.delete(0,END)





root=Tk()
root.geometry('700x600+250+30')
root.configure(bg='gold2')
root.title("Typing Speed Game created by Faizan Khan")
root.iconbitmap('icon.ico')

#variables
timeleft=60

logopic=PhotoImage(file='logo.png')
piclabel=Label(root,image=logopic,bg='gold2')
piclabel.place(x=220,y=50)

fontlabel=Label(root,text="",font=('arial',25,'italic bold'),
                bg='gold2',fg='red',width=35)
fontlabel.place(x=0,y=10)
labelSlider()
random.shuffle(words)
wordlabel=Label(root,text=words[0],font=('cooper black',38,'italic bold'),bg='gold2')
wordlabel.place(x=350,y=350,anchor=CENTER )

scorelabel=Label(root,text='Words',font=('castellar',28,' bold'),bg='gold2')
scorelabel.place(x=30,y=100)

scorelabelcount=Label(root,text=i,font=('castellar',28,'italic bold'),bg='gold2')
scorelabelcount.place(x=80,y=180)

timelabel=Label(root,text='Timer',font=('castellar',28,'bold'),bg='gold2')
timelabel.place(x=510,y=100)

timelabelcount=Label(root,text=timeleft,font=('castellar',28,'italic bold'),bg='gold2')
timelabelcount.place(x=550,y=180)

gameplay_detaillabel=Label(root,text='Type Word And Hit Enter',font=('chiller',30,'italic bold'),
                           bg='gold2',fg='red')
gameplay_detaillabel.place(x=210,y=460)

wordEntry=Entry(root,font=('arial',25,'italic bold'),bd='10',justify=CENTER)
wordEntry.place(x=160,y=390)
wordEntry.focus_set()

poorpic = PhotoImage(file='poor.png')

goodpic = PhotoImage(file='good.png')

propic = PhotoImage(file='pro.png')

poorLabel = Label(root,bg='gold2')
poorLabel.place(x=80, y=490)


poor1Label = Label(root,bg='gold2')
poor1Label.place(x=540, y=490)

root.bind('<Return>',play_game)
root.mainloop()