#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zahra Alahmedi
Osama Karim Kidwai
Eric Rawlins
CS465/665, W24
Project # 1
"""
# Import Module
from tkinter import *
import CS465_665_W24_IRproject_Group3_Inverted_index_with_input_and_soundex as IIS
import CS465_665_W24_IRproject_Group3top_words as tw
import CS465_665_W24_IRproject_Group3_all_words as aw

def on_button1():
    txt.delete('1.0', END)
    documents_folder = "mybook"
    searchTerm = modify.get()
    output_file = "distinct_words_in_each_doc.txt"
    inverted_index = IIS.create_inverted_index(documents_folder,  output_file)
    res = IIS.search_index(inverted_index, searchTerm)
    soundex = IIS.print_soundex(searchTerm)
    res.append(f"soundex for {searchTerm}, {soundex}", )
    txt.insert('1.0', res)
    
def on_button2():
    txt.delete('1.0', END)
    documents_folder= "mybook"
    word_occurrences = tw.count_word_occurrences_in_folder(documents_folder)
    output = []
    word_occurrences = sorted(word_occurrences.items(), key=lambda x: x[1], reverse=True)
    for rank, (word, frequency) in enumerate(word_occurrences, start=1):
        if rank in [100, 500, 1000]:
            output.append(f"Rank {rank}: {word} - Frequency: {frequency}")
    total_words, distinct_words = aw.distinct_word_count(documents_folder)
    output.append(f"total words in collection: {total_words}")
    output.append(f"distint words in collection: {distinct_words}")
    txt.insert('1.0', output)
     
# create root window
root = Tk()
 
# root window title and dimension
root.title("IR project")
# Set geometry(widthxheight)
root.geometry('500x500')
 
# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar 
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# adding Entry Field
txt = Entry(root, width=20)

Frm = Frame(root)
Label(Frm,text='Search Here:').pack(side=LEFT)
modify = Entry(Frm)

modify.pack(side=LEFT, fill=BOTH, expand=1)

modify.focus_set()

txt = Text(root)

txt.pack(side=BOTTOM, expand= TRUE)

# button widget with red color text inside
buttn = Button(Frm, text = "Search" , fg = "red", command=on_button1)
buttn.pack(side=RIGHT)
Frm.pack(side=TOP)

btn2 = Button(root, text = "Count", fg = "blue", command = on_button2)
# Set Button Grid

btn2.pack(side = TOP)

# Execute Tkinter
root.mainloop()


if __name__ == '__main__':
    app = Tk.App(redirect=False)
    frame = MyFrame()
    app.MainLoop()