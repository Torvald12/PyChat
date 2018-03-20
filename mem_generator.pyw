import facebook
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter as Tk
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import warnings
warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)
import math
import matplotlib.pyplot as plt
from tkinter import messagebox

#=======================================
def get_selected_currency(event):
    selected = combobox_currency.get()
    currency_entry.insert(END, selected)
    return selected

def get_selected_speed(event):
    selected = combobox_speed.get()
    currency_entry.insert(END, selected)
    return selected

def get_selected_action(event):
    selected = combobox_action.get()
    currency_entry.insert(END, selected)
    return selected

#=======================================
def get_selected_nessesarity(event):
    selected = combobox_nessesarity.get()
    weapon_entry.insert(END, selected)
    return selected

def get_selected_forbid(event):
    selected = combobox_forbid.get()
    weapon_entry.insert(END, selected)
    return selected

#========================================
def get_selected_nessesity(event):
    selected = combobox_nessesity.get()
    law_entry.insert(END, selected)
    return selected

def get_selected_rapid(event):
    selected = combobox_rapid.get()
    law_entry.insert(END, selected)
    return selected

def get_selected_act(event):
    selected = combobox_act.get()
    law_entry.insert(END, selected)
    return selected

#++++++++++++++++++++++++++++++++++++++++
def get_reactions():
    post_id = post_id_entry.get()
    #reaction_comments = graph.get_object(id=post_id, fields='comments')
    shares = graph.get_object(id=post_id, fields='shares')
    shares = shares.get('shares')
    shares = shares.get('count')
    reactions = graph.get_object(id=post_id, fields='reactions')
    reactions = reactions.get('reactions')
    reactions = reactions.get('data')
    reactions_array = []

    i = 0
    while i < len(reactions):
        reaction_type = reactions[i].get('type')
        reactions_array.append(reaction_type)
        i += 1

    mas = []
    for item in reactions_array:
        react = reactions_array.count(item)
        mas.append((item, react))

    reaction_dict = dict(mas)

    reaction_list = []
    reaction_list.append(reaction_dict.get('LIKE'))
    reaction_list.append(reaction_dict.get('LOVE'))
    reaction_list.append(reaction_dict.get('WOW'))
    reaction_list.append(reaction_dict.get('HAHA'))
    reaction_list.append(reaction_dict.get('SAD'))
    reaction_list.append(reaction_dict.get('ANGRY'))

    i = 0
    while i < len(reaction_list):
        if reaction_list[i] == None:
            reaction_list[i] = 0
        i += 1

    label_reaction['text'] = 'SHARES: ' + str(shares) + '\nLike: ' + str(reaction_list[0]) + '\nLove: ' + str(reaction_list[1]) + '\nWow: ' + str(reaction_list[2]) + '\nHa-ha: ' + str(reaction_list[3]) + '\nSad: ' + str(reaction_list[4]) + '\nAngry: ' + str(reaction_list[5])


    ax = figure.add_subplot(111)
    ax.clear()

    objects = ('LIKE', 'LOVE', 'WOW', 'HAHA', 'SAD', 'ANGRY')
    y_pos = np.arange(len(objects))  # the x locations for the groups

    barchart = ax.bar(y_pos, reaction_list, align='center', alpha=0.5)
    barchart[0].set_color('green')
    barchart[1].set_color('green')
    barchart[2].set_color('blue')
    barchart[3].set_color('blue')
    barchart[4].set_color('red')
    barchart[5].set_color('red')

    ax.set_xticks(np.arange(len(objects)))
    ax.set_xticklabels(objects, fontdict=None, minor=False)

    ax.yaxis.grid()

    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    Ym = sum(reaction_list)
    post_from_id = graph.get_object(id=post_id, fields='from')
    post_from_id = post_from_id.get('from')
    post_from_id = post_from_id.get('id')
    Dm = graph.get_object(id=post_from_id, fields='friends')
    Dm = Dm.get('friends', None)
    Dm = Dm.get('summary', None)
    Dm = Dm.get('total_count', None)
    V_Dm = (Ym/Dm)*100
    V_Dm = float('{:.2f}'.format(V_Dm))
    label_effectivity['text'] = 'Ефективність джерела впливу становить ' + str(V_Dm) + '%'

def bifurcation_point():
    e = math.e
    try:
        percent = int(bifurcation_percent.get())
        T = int(bifurcation_T.get())
        t = int(bifurcation_t.get())
        N0 = int(bifurcation_N0.get())
        k = float(bifurcation_k.get())
    except ValueError:
        messagebox.showinfo("ValueError", "Enter the correct value")
        return
    except AttributeError:
        messagebox.showinfo("AttributeError", "Enter all values")
        return

    ax_bifurcation = figure_bifurcation.add_subplot(111)
    ax_bifurcation.clear()

    try:
        bif_point_N = (N0 * percent) / 100
        bif_point_t = -T/(math.log(bif_point_N/(abs(k)*N0), e))
        bif_point_t = abs(bif_point_t)
        #print('t: ', bif_point_t, '\nN: ', bif_point_N)
        if k < 0:
            bif_point_N *= -1
        #print((e ** (-T / t)) * N0 * k)
        t = np.arange(0.001, t, 1)  # Массив значений аргумента
        plt.plot(t, (e ** (-T / t)) * N0 * k)  # Построение графика
        plt.scatter(bif_point_t, bif_point_N, color='red')
        plt.xlabel(r'$t$')  # Метка по оси x в формате TeX
        plt.ylabel(r'$N(t)$')  # Метка по оси y в формате TeX
        plt.title('Динаміка інформаційного впливу на соціальну частину СТС')  # Заголовок в формате TeX
        plt.grid(True)  # Сетка
        plt.show()  # Показать график
    except ZeroDivisionError:
        messagebox.showinfo('ZeroDivisionError', 'При k=0 впливу немає')

    ax_bifurcation.yaxis.grid()

root = tk.Tk()
root.title('Mem generator')

file = open('access_token.txt', 'r')
access_token = file.read()
file.close()
graph = facebook.GraphAPI(access_token=access_token, version='2.8')

main_nb = ttk.Notebook(root)
main_nb.pack(fill='both', expand='yes')

generation = Frame(root)
getting_reaction = Frame(root)
bifurcation_frame = Frame(root)
bifurcation_frame.pack(expand='yes')

main_nb.add(generation, text='Згенерувати мем')
main_nb.add(getting_reaction, text='Реакція на мем')
main_nb.add(bifurcation_frame, text='Точка біфуркації')

nb = ttk.Notebook(generation)
nb.pack(fill='both', expand='yes')

currency_frame = Frame(generation)
law_frame = Frame(generation)
weapon_frame = Frame(generation)

nb.add(currency_frame, text='Курс валюти')
nb.add(weapon_frame, text='Носіння зброї у США')
nb.add(law_frame, text='Прийняття закону')

#==========================================================
combobox_currency = ttk.Combobox(master=currency_frame, values=["Курс долара ", "Курс гривні ", "Курс фунта ", "Курс рубля "])
combobox_currency.set("--Валюта--")
combobox_currency.bind('<<ComboboxSelected>>', get_selected_currency)
combobox_currency.pack()

combobox_speed = ttk.Combobox(master=currency_frame, values=["невпинно ", "стрімко ", "повільно ", "швидко ", "поступово "])
combobox_speed.set("--Швидкість зміни--")
combobox_speed.bind('<<ComboboxSelected>>', get_selected_speed)
combobox_speed.pack()

combobox_action = ttk.Combobox(master=currency_frame, values=["зростає ", "спадає ", "стабільний ", "змінюється ", "не змінюється ", "стабілізується ", "слабшає ", "зміцнюється "])
combobox_action.set("--Дія--")
combobox_action.bind('<<ComboboxSelected>>', get_selected_action)
combobox_action.pack()

#==========================================================
combobox_nessesarity = ttk.Combobox(master=weapon_frame, values=["Необхідно ", "Потрібно ", "Не потрібно ", "Не можна "])
combobox_nessesarity.set("--Необхідність--")
combobox_nessesarity.bind('<<ComboboxSelected>>', get_selected_nessesarity)
combobox_nessesarity.pack()

combobox_forbid = ttk.Combobox(master=weapon_frame, values=["забороняти ", "залишати без змін ", "обговорити проблему ", "дозволяти ", "розширити дозвіл на "])
combobox_forbid.set("--Дія--")
combobox_forbid.bind('<<ComboboxSelected>>', get_selected_forbid)
combobox_forbid.pack()

#==========================================================
combobox_nessesity = ttk.Combobox(master=law_frame, values=["Необхідно ", "Потрібно ", "Не потрібно ", "Не можна ", "Не на часі "])
combobox_nessesity.set("--Необхідність--")
combobox_nessesity.bind('<<ComboboxSelected>>', get_selected_nessesity)
combobox_nessesity.pack()

combobox_rapid = ttk.Combobox(master=law_frame, values=["терміново ", "поступово "])
combobox_rapid.set("--Швидкість--")
combobox_rapid.bind('<<ComboboxSelected>>', get_selected_rapid)
combobox_rapid.pack()

combobox_act = ttk.Combobox(master=law_frame, values=["прийняти закон", "відкласти закон", "переглянути закон", "розглянути закон", "обговорити закон", "скаcувати закон", "змінити закон"])
combobox_act.set("--Дія--")
combobox_act.bind('<<ComboboxSelected>>', get_selected_act)
combobox_act.pack()

currency_entry = Entry(currency_frame, width=50)
law_entry = Entry(law_frame, width=50)
weapon_entry = Entry(weapon_frame, width=50)
currency_entry.pack()
law_entry.pack()
weapon_entry.pack()

currency_button = Button(currency_frame, text="Очистити поле", width=15, command=lambda: currency_entry.delete(0, END))
weapon_button = Button(weapon_frame, text="Очистити поле", width=15, command=lambda: weapon_entry.delete(0, END))
law_button = Button(law_frame, text="Очистити поле", width=15, command=lambda: law_entry.delete(0, END))
currency_button.pack()
weapon_button.pack()
law_button.pack()

currency_post = Button(currency_frame, text='Опублікувати мем', width=15, command=lambda: graph.put_wall_post(message=currency_entry.get(), profile_id='me'))
weapon_post = Button(weapon_frame, text='Опублікувати мем', width=15, command=lambda: graph.put_wall_post(message=weapon_entry.get(), profile_id='me'))
law_post = Button(law_frame, text='Опублікувати мем', width=15, command=lambda: graph.put_wall_post(message=law_entry.get(), profile_id='me'))
currency_post.pack()
weapon_post.pack()
law_post.pack()

#GETTING REACTION
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
label_post_id = Label(getting_reaction, font='TimesNewRoman 14')
label_post_id['text'] = "Введіть id поста:"
label_post_id.pack()

post_id_entry = Entry(getting_reaction, width=31)
post_id_entry.pack()

reaction_button = Button(getting_reaction, text='Отримати реакцію', width=15, command=get_reactions)
reaction_button.pack()

label_reaction = Label(getting_reaction, font='TimesNewRoman 14', justify=LEFT)
label_reaction.pack()

label_effectivity = Label(getting_reaction, font='TimesNewRoman 14', justify=LEFT)
label_effectivity.pack()

graph_frame = Frame(getting_reaction)
graph_frame.pack()
figure = Figure(figsize=(6, 3), dpi=100)
canvas = FigureCanvasTkAgg(figure, master=graph_frame)

#Bifuscation point
#===================================================================================================
figure_bifurcation = Figure(figsize=(6, 3), dpi=100)
canvas_bifurcation = FigureCanvasTkAgg(figure_bifurcation, master=graph_frame)

bifurcation_percent = Entry(bifurcation_frame, width=10)
bifurcation_percent.grid(column=1, row=0)
bifurcation_T = Entry(bifurcation_frame, width=10)
bifurcation_T.grid(column=1, row=1)
bifurcation_t = Entry(bifurcation_frame, width=10)
bifurcation_t.grid(column=1, row=2)
bifurcation_k = Entry(bifurcation_frame, width=10)
bifurcation_k.grid(column=1, row=3)
bifurcation_N0 = Entry(bifurcation_frame, width=10)
bifurcation_N0.grid(column=1, row=4)

label_percent = Label(bifurcation_frame, text='Експертна кількість людей: ').grid(column=0, row=0)
label_T = Label(bifurcation_frame, text='Збереження початкового стану τ: ').grid(column=0, row=1)
label_t = Label(bifurcation_frame, text='Дослідження стану СТС протягом t: ').grid(column=0, row=2)
label_k = Label(bifurcation_frame, text='Коефіцієнт емоційної складової мема k: ').grid(column=0, row=3)
label_N0 = Label(bifurcation_frame, text='Соціальна група N0: ').grid(column=0, row=4)

label_percent = Label(bifurcation_frame, text='%').grid(column=2, row=0)
label_T = Label(bifurcation_frame, text='годин').grid(column=2, row=1)
label_t = Label(bifurcation_frame, text='годин').grid(column=2, row=2)
label_k = Label(bifurcation_frame, text='').grid(column=2, row=3)
label_N0 = Label(bifurcation_frame, text='людей').grid(column=2, row=4)

bifurcation_button = Button(bifurcation_frame, text='Розрахувати', width=12, command=bifurcation_point).grid(column=0, row=5, columnspan=2)

root.mainloop()