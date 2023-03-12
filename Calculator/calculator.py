#Importando Tkinter

from tkinter import *
from tkinter import ttk

#Table of the Colors using Color Picker

cor1 = '#3b3b3b' #black
cor2 = '#feffff' #white
cor3 = '#38576b' #Azul carregado
cor4 = '#ECEFF1' #Cinzento
cor5 = '#FFAB40' #Orange


#Configuração da Calculador
janela = Tk()
janela.title ("Calculator")
janela.geometry ("235x318")
janela.config (bg=cor1)

#Display
frame_display = Frame(janela, width=235, height=50, bg=cor3)
frame_display.grid(row=0, column=0)

#Keyboard
frame_keyboard = Frame(janela, width=235, height=268)
frame_keyboard.grid(row=1, column=0)


#Variavel todos valores
todos_valores = ''



#Função Global

def entrada_valores(event):
    
    global todos_valores

    todos_valores = todos_valores + str(event)
        
    # Impressão do Valor na tela
    valor_texto.set(todos_valores)

#Funções Aritiméticas

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(resultado)

#Função Display Clear

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

#Label
valor_texto = StringVar()
app_label = Label(frame_display, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 '), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

#Buttons
b_clear = Button (frame_keyboard, command=limpar_tela, text="C", width=17, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_clear.place(x=0, y=0)

b_div = Button (frame_keyboard, text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores('/'))
b_div.place(x=177, y=0)

b_7 = Button (frame_keyboard, text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores('7'))
b_7.place(x=0, y=52)

b_8 = Button (frame_keyboard, text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores('8'))
b_8.place(x=59, y=52)

b_9 = Button (frame_keyboard, text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores('9'))
b_9.place(x=118, y=52)

b_mult = Button (frame_keyboard, text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores('*'))
b_mult.place(x=177, y=52)

b_4 = Button (frame_keyboard, text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores('4'))
b_4.place(x=0, y=104)

b_5 = Button (frame_keyboard, text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores('5'))
b_5.place(x=59, y=104)

b_6 = Button (frame_keyboard, text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores('6'))
b_6.place(x=118, y=104)

b_sub = Button (frame_keyboard, text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores('-'))
b_sub.place(x=177, y=104)

b_1 = Button (frame_keyboard, text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores('1'))
b_1.place(x=0, y=156)

b_2 = Button (frame_keyboard, text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores('2'))
b_2.place(x=59, y=156)

b_3 = Button (frame_keyboard, text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores('3'))
b_3.place(x=118, y=156)

b_adic = Button (frame_keyboard, text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores('+'))
b_adic.place(x=177, y=156)

b_0 = Button (frame_keyboard, text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores('0'))
b_0.place(x=0, y=208)

b_comma = Button (frame_keyboard, text=",", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command = lambda: entrada_valores(','))
b_comma.place(x=118, y=208)

b_equal = Button (frame_keyboard, command = calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_equal.place(x=177, y=208)




#Mantém a janela aberta
janela.mainloop()