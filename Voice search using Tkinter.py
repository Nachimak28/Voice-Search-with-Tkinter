from tkinter import *
from tkinter import ttk
import webbrowser
import speech_recognition as sr
from pygame import mixer
#from keys import *


root = Tk()
root.title('Universal Search Bar')
root.iconbitmap('mic.ico')

photo = PhotoImage(file='microphone.png').subsample(15,15)

style = ttk.Style()
style.theme_use('winnative')

label1 = ttk.Label(root,text='Query:')
label1.grid(row=0,column=0)
entry1 = ttk.Entry(root,width=40)
entry1.grid(row=0,column=1, columnspan = 4)

btn2 = StringVar()

def callback():

    if btn2.get() == 'google' and entry1.get()!='':
        webbrowser.open('http://google.com/search?q='+entry1.get())
    elif btn2.get() == 'bing' and entry1.get()!='':
        webbrowser.open('https://www.bing.com/search?q='+entry1.get())
    elif btn2.get() == 'amz' and entry1.get()!='':
        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+entry1.get())
    elif btn2.get() == 'ytb' and entry1.get()!='':
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())
    else:
        pass

def get(event):

    if btn2.get() == 'google' and entry1.get()!='':
        webbrowser.open('http://google.com/search?='+entry1.get())
    elif btn2.get() == 'bing' and entry1.get()!='':
        webbrowser.open('http://bing.com/q='+entry1.get())
    elif btn2.get() == 'amz' and entry1.get()!='':
        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+entry1.get())
    elif btn2.get() == 'ytb' and entry1.get()!='':
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())
    else:
        pass

def buttonClick():
    mixer.init()
    mixer.music.load('chime1.mp3')
    mixer.music.play()

    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400


    with sr.Mircophone() as source:

        try:
            audio = r.listen(source,timeout=5)
            message = str(r.recognize_google(audio, key = google_api_key))
            mixer.music.load('chime2.mp3')
            mixer.music.load('chime2.mp3')
            mixer.music.play()
            entry1.focus()
            entry1.delete(0, END)
            entry1.insert(0, message)

            if btn2.get() == 'google':
                webbrowser.open('http://google.com/search?q='+message)
        
            elif btn2.get() == 'bing':
                webbrowser.open('http://bing.com/q='+message)

            elif btn2.get() == 'amz':
                webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+message)

            elif btn2.get() == 'ytb':
                webbrowser.open('https://www.youtube.com/results?search_query='+message)

            else:
                pass

        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')

        except sr.RequestError as e:
            print('Could not request results from Google Speech Recognition Service')

        else:
            pass    







    
entry1.bind('<Return>',get)


MyButton1 = ttk.Button(root, text='Search', width = 10, command=callback)
MyButton1.grid(row=0,column=6)


MyButton2 = ttk.Radiobutton(root,text='Google', value='google',variable=btn2)
MyButton2.grid(row=1,column=1,sticky=W)


MyButton3 = ttk.Radiobutton(root,text='Bing', value='bing',variable=btn2)
MyButton3.grid(row=1,column=2,sticky=E)

MyButton4 = ttk.Radiobutton(root,text='Amz', value='amz',variable=btn2)
MyButton4.grid(row=1,column=3)


MyButton5 = ttk.Radiobutton(root,text='Ytb', value='ytb',variable=btn2)
MyButton5.grid(row=1,column=4,sticky=E)

MyButton6 = Button(root,image=photo,command = buttonClick , bd = 0, activebackground = '#c1bfbf', overrelief = 'groove' , relief = 'sunken')
MyButton6.grid(row=0,column = 5)

entry1.focus()
root.wm_attributes('-topmost',1)
btn2.set('google')
root.mainloop()
