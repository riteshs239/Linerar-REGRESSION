## import libraries
from tkinter import * #tkinter will help to create GUI
from gtts import gTTS # gtts stands for Google Text-to-Speech
from playsound import playsound
################### Initialized window####################
root = Tk()
root.geometry('350x200')
root.resizable(0,0)
root.config(bg = 'sky blue')
root.title('TEXT_TO_SPEECH')
##heading
Label(root, text = 'TEXT_TO_SPEECH' , font='arial 20 bold' , bg ='sky blue').pack()
#label
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='sky blue').place(x=20,y=70)
##text variable
Msg = StringVar()
#Entry
entry_field = Entry(root,textvariable =Msg, width ='30', font ='arial 15 bold')
entry_field.place(x=10 , y=100)
###################define function##############################
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('sound.mp3')
    playsound('sound.mp3')
def Exit():
    root.destroy()
def Reset():
    Msg.set("")
#Button
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, width =5).place(x=30, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit).place(x=260,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=135 , y =140)
#infinite loop to run program
root.mainloop()