# -*- coding: utf-8 -*- 

import socket
from tkinter import *
from tkinter import ttk
from importlib import reload

from tkinter import messagebox
from datetime import datetime


def loopproc():
	chat.see(END)
	s.setblocking(False)
	try:
		message = s.recv(128).decode()
		chat.insert(END, message + '\n')
	except:
		root.after(1, loopproc)
		return
	root.after(1,loopproc)
	return

def sendproc(event):
    current_time = datetime.strftime(datetime.now(), "%H:%M:%S")
    nick_name = nickname.get()
    if (' ' in nick_name):
        messagebox.showinfo("Error", "Your nickname cannot contain spaces!")
    elif (len(nick_name) > 20 or len(nick_name) <= 0):
        messagebox.showinfo("Length", "Nickname length is to be from 1 to 20 symbols")
    else:
        sock.sendto(('[' + str(current_time) + ']' + nick_name + ': ' + text.get()).encode(), ('255.255.255.255', 11719))
        text.set('')

def smileswindow():
	smiles_window = Tk()
	smiles_window.title('Smiles')
	smiles_window.geometry('240x213+500+300')

	button_laugh = Button(smiles_window, text=':D', width=10, height=4, command=lambda: message_entry.insert(END, ':D')).grid(column=0, row=0)
	button_sad = Button(smiles_window, text=':(', width=10, height=4, command=lambda: message_entry.insert(END, ':(')).grid(column=0, row=1)
	button_kiss = Button(smiles_window, text=':*', width=10, height=4, command=lambda: message_entry.insert(END, ':*')).grid(column=0, row=2)
	button_smile = Button(smiles_window, text=':)', width=10, height=4, command=lambda: message_entry.insert(END, ':)')).grid(column=1, row=0)
	button_cute = Button(smiles_window, text=':3', width=10, height=4, command=lambda: message_entry.insert(END, ':3')).grid(column=1, row=1)
	button_angry = Button(smiles_window, text='>:(', width=10, height=4, command=lambda: message_entry.insert(END, '>:(')).grid(column=1, row=2)
	button_cry = Button(smiles_window, text=';(', width=10, height=4, command=lambda: message_entry.insert(END, ';(')).grid(column=2, row=0)
	button_wow = Button(smiles_window, text='0_0', width=10, height=4, command=lambda: message_entry.insert(END, '0_0')).grid(column=2, row=1)
	button_mouth = Button(smiles_window, text=':o', width=10, height=4, command=lambda: message_entry.insert(END, ':o')).grid(column=2, row=2)
	smiles_window.mainloop()

reload(sys)
sys.setdefaultencoding('utf-8')

root = Tk()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 11719))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

text = StringVar()
nickname = StringVar()
nickname.set('User')
text.set('')
root.title('Chat')
root.geometry('500x500')

chat = Text(root)
nickname_entry = Entry(root, textvariable=nickname)
message_entry = Entry(root, textvariable=text)
nickname_label = Label(root)
nickname_label['text'] = 'Your nickname: '
message_label = Label(root)
message_label['text'] = 'Your message: '

chat.pack(side='top', fill='both', expand='true')

smiles_button = ttk.Button(root, text="Choose a smile", command=smileswindow)
smiles_button.pack(side='bottom', fill='x', expand='false')
message_entry.pack(side='bottom', fill='x', expand='false')
message_label.pack(side='bottom', fill='x', expand='false')
nickname_entry.pack(side='bottom', fill='x', expand='false')
nickname_label.pack(side='bottom', fill='x', expand='false')

message_entry.bind('<Return>', sendproc)

message_entry.focus_set()

root.after(1, loopproc)
root.mainloop()
