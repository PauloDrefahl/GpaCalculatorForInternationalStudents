from tkinter import *
from tkinter import ttk
import time

#===============================================================
#inicializa tela de login
jpas = Tk()
jpas.title("GPA by Paulo Drefahl")

#PROGRAMA PRINCIPAL GPA-------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class janela:

    def __init__(self,master=None):
        self.frame = Frame(master)
        self.frame.pack()
        self.frame1 = Frame(self.frame,width=1000,height=100,bd=8,relief='raise').pack(side=TOP)
        self.j2 = Label(self.frame1, text='GPA CALCULATOR', font='Arial 45').place(x=380, y=10)
        self.frame2 = Frame(self.frame,width=1300,height=700,bg='#A59F9D',bd=10, relief='ridge').pack(side=BOTTOM)
        self.frame3 = Frame(self.frame2, width=200, height=200, bg='#A59F9D', bd=10, relief='raise').place(x=80, y=200)
        self.fn = DoubleVar()
        self.fn1 = DoubleVar()
        self.fn2 = DoubleVar()
        self.fn3 = DoubleVar()
        self.fn4 = DoubleVar()
        self.fn5 = DoubleVar()
        self.fn6 = DoubleVar()
        self.fn7 = DoubleVar()
        self.fn8 = DoubleVar()
        self.fn9 = DoubleVar()
        self.fn10 = DoubleVar()
        self.fn11 = DoubleVar()
        self.fn12 = DoubleVar()
        self.fn13 = DoubleVar()
        self.fn14 = DoubleVar()
        self.fn15 = DoubleVar()
        self.fns = DoubleVar()
        self.fns1 = DoubleVar()
        self.fns2 = DoubleVar()
        self.fns3 = DoubleVar()
        self.fns4 = DoubleVar()
        self.fns5 = DoubleVar()
        self.fns6 = DoubleVar()
        self.fns7 = DoubleVar()
        self.fns8 = DoubleVar()
        self.fns9 = DoubleVar()
        self.fns10 = DoubleVar()
        self.fns11 = DoubleVar()
        self.fns12 = DoubleVar()
        self.fns13 = DoubleVar()
        self.fns14 = DoubleVar()
        self.fns15 = DoubleVar()
        self.fnn = DoubleVar()
        self.fnn1 = DoubleVar()
        self.fnn2 = DoubleVar()
        self.fnn3 = DoubleVar()
        self.fnn4 = DoubleVar()
        self.fnn5 = DoubleVar()
        self.fnn6 = DoubleVar()
        self.fnn7 = DoubleVar()
        self.fnn8 = DoubleVar()
        self.fnn9 = DoubleVar()
        self.fnn10 = DoubleVar()
        self.fnn11 = DoubleVar()
        self.fnn12 = DoubleVar()
        self.fnn13 = DoubleVar()
        self.fnn14 = DoubleVar()
        self.fnn15 = DoubleVar()
        self.botaodeescolha()
#-----------------------------------------------------------------------------------------------------------------------
    def receber(self):
        self.receber9 = []
        self.receber9.append(self.fn.get())
        self.receber9.append(self.fn1.get())
        self.receber9.append(self.fn2.get())
        self.receber9.append(self.fn3.get())
        self.receber9.append(self.fn4.get())
        self.receber9.append(self.fn5.get())
        self.receber9.append(self.fn6.get())
        self.receber9.append(self.fn7.get())
        self.receber9.append(self.fn8.get())
        self.receber9.append(self.fn9.get())
        self.receber9.append(self.fn10.get())
        self.receber9.append(self.fn11.get())
        self.receber9.append(self.fn12.get())
        self.receber9.append(self.fn13.get())
        self.receber9.append(self.fn14.get())
        self.receber9.append(self.fn15.get())
        self.notasf9 = []
        for fns in self.receber9:
            if fns >= 9:
                self.notasf9.append('A')
            elif fns < 9 and fns >= 7:
                self.notasf9.append('B')
            elif fns < 7 and fns >= 5:
                self.notasf9.append('C')
            elif fns < 5 and fns >= 3:
                self.notasf9.append('D')
            elif fns < 3 and fns>0.1:
                self.notasf9.append('F')
            else:
                pass
        self.receber1 = []
        self.receber1.append(self.fns.get())
        self.receber1.append(self.fns1.get())
        self.receber1.append(self.fns2.get())
        self.receber1.append(self.fns3.get())
        self.receber1.append(self.fns4.get())
        self.receber1.append(self.fns5.get())
        self.receber1.append(self.fns6.get())
        self.receber1.append(self.fns7.get())
        self.receber1.append(self.fns8.get())
        self.receber1.append(self.fns9.get())
        self.receber1.append(self.fns10.get())
        self.receber1.append(self.fns11.get())
        self.receber1.append(self.fns12.get())
        self.receber1.append(self.fns13.get())
        self.receber1.append(self.fns14.get())
        self.receber1.append(self.fns15.get())
        self.notasf1 = []
        for fns in self.receber1:
            if fns >= 9:
                self.notasf1.append('A')
            elif fns < 9 and fns >= 7:
                self.notasf1.append('B')
            elif fns < 7 and fns >= 5:
                self.notasf1.append('C')
            elif fns < 5 and fns >= 3:
                self.notasf1.append('D')
            elif fns < 3 and fns > 0.1:
                self.notasf1.append('F')
            else:
                pass
        self.receber2 = []
        self.receber2.append(self.fnn.get())
        self.receber2.append(self.fnn1.get())
        self.receber2.append(self.fnn2.get())
        self.receber2.append(self.fnn3.get())
        self.receber2.append(self.fnn4.get())
        self.receber2.append(self.fnn5.get())
        self.receber2.append(self.fnn6.get())
        self.receber2.append(self.fnn7.get())
        self.receber2.append(self.fnn8.get())
        self.receber2.append(self.fnn9.get())
        self.receber2.append(self.fnn10.get())
        self.receber2.append(self.fnn11.get())
        self.receber2.append(self.fnn12.get())
        self.receber2.append(self.fnn13.get())
        self.receber2.append(self.fnn14.get())
        self.receber2.append(self.fnn15.get())
        self.notasf2 = []
        for fns in self.receber2:
            if fns >= 9:
                self.notasf2.append('A')
            elif fns < 9 and fns >= 7:
                self.notasf2.append('B')
            elif fns < 7 and fns >= 5:
                self.notasf2.append('C')
            elif fns < 5 and fns >= 3:
                self.notasf2.append('D')
            elif fns < 3 and fns > 0.1:
                self.notasf2.append('F')
            else:
                pass
        self.result9 = round((self.notasf9.count('A') * 4 + self.notasf9.count('B') * 3 + self.notasf9.count(
            'C') * 2 + self.notasf9.count('D') * 1 + self.notasf9.count('F') * 0) / len(self.notasf9), 2)
        Label(self.frame4, text=self.result9, font='Arial 25').place(x=225, y=520)
        if self.fnn.get() > 0:
            self.result1 = round((((self.notasf1.count('A') * 4 + self.notasf1.count('B') * 3 + self.notasf1.count(
                'C') * 2 + self.notasf1.count('D') * 1 + self.notasf1.count('F') * 0) / len(
                self.notasf1)) + self.result9) / 2, 2)
            self.result2 = round((((self.notasf2.count('A') * 4 + self.notasf2.count('B') * 3 + self.notasf2.count(
                'C') * 2 + self.notasf2.count('D') * 1 + self.notasf2.count('F') * 0) / len(
                self.notasf2)) + self.result9+self.result1) / 3, 2)
            Label(self.frame4, text=self.result2, font='Arial 25').place(x=225, y=520)
        elif self.fn.get() > 0:
            self.result1 = round((((self.notasf1.count('A') * 4 + self.notasf1.count('B') * 3 + self.notasf1.count(
            'C') * 2 + self.notasf1.count('D') * 1 + self.notasf1.count('F') * 0) / len(self.notasf1))+self.result9)/2, 2)
            Label(self.frame4, text=self.result1, font='Arial 25').place(x=225, y=520)
    def notas9(self):
        Button(text='Resetar Calculo', command=self.resetb).place(x=60, y=600)
        self.lbl9 = Label(text='Notas 9ºano',font='Arial 18').place(x=395,y=200)
        n9=(Entry(self.frame2, textvar=self.fn).place(x=400,y=260))
        n91=(Entry(self.frame2,textvar=self.fn1).place(x=400, y=280))
        n92=(Entry(self.frame2,textvar=self.fn2).place(x=400, y=300))
        n93=(Entry(self.frame2,textvar=self.fn3).place(x=400, y=320))
        n94=(Entry(self.frame2,textvar=self.fn4).place(x=400, y=340))
        n95=(Entry(self.frame2,textvar=self.fn5).place(x=400, y=360))
        n96=(Entry(self.frame2,textvar=self.fn6).place(x=400, y=380))
        n97=(Entry(self.frame2,textvar=self.fn7).place(x=400, y=400))
        n98=(Entry(self.frame2,textvar=self.fn8).place(x=400, y=420))
        n99=(Entry(self.frame2,textvar=self.fn9).place(x=400, y=440))
        n910=(Entry(self.frame2,textvar=self.fn10).place(x=400, y=460))
        n911=(Entry(self.frame2,textvar=self.fn11).place(x=400, y=480))
        n912=(Entry(self.frame2,textvar=self.fn12).place(x=400, y=500))
        n913=(Entry(self.frame2,textvar=self.fn13).place(x=400, y=520))
        n914=(Entry(self.frame2,textvar=self.fn14).place(x=400, y=540))
        n915=(Entry(self.frame2,textvar=self.fn15).place(x=400, y=560))
        self.n9b = Button(text='enviar notas',command=self.receber).place(x=400, y=600)
        self.frame5 = Frame(self.frame, width=300, heigh=100, bd=7, relief='raise').place(x=30, y=490)
        self.frame4 = Frame(self.frame, width=200, height=800, bd=10,relief='raise').place(x=360, y=180)
        self.labelgpa9= Label(self.frame5,text='Seu GPA:',font='Arial 25').place(x=60,y=520)
    def notas1(self):
        self.notas9()
        self.lbl1 = Label(text='Notas 1ºano', font='Arial 18').place(x=600, y=200)
        n1 = (Entry(self.frame2, textvar=self.fns).place(x=600, y=260))
        n11 = (Entry(self.frame2, textvar=self.fns1).place(x=600, y=280))
        n12 = (Entry(self.frame2, textvar=self.fns2).place(x=600, y=300))
        n13 = (Entry(self.frame2, textvar=self.fns3).place(x=600, y=320))
        n14 = (Entry(self.frame2, textvar=self.fns4).place(x=600, y=340))
        n15 = (Entry(self.frame2, textvar=self.fns5).place(x=600, y=360))
        n16 = (Entry(self.frame2, textvar=self.fns6).place(x=600, y=380))
        n17 = (Entry(self.frame2, textvar=self.fns7).place(x=600, y=400))
        n18 = (Entry(self.frame2, textvar=self.fns8).place(x=600, y=420))
        n19 = (Entry(self.frame2, textvar=self.fns9).place(x=600, y=440))
        n110 = (Entry(self.frame2, textvar=self.fns10).place(x=600, y=460))
        n111 = (Entry(self.frame2, textvar=self.fns11).place(x=600, y=480))
        n112 = (Entry(self.frame2, textvar=self.fns12).place(x=600, y=500))
        n113 = (Entry(self.frame2, textvar=self.fns13).place(x=600, y=520))
        n114 = (Entry(self.frame2, textvar=self.fns14).place(x=600, y=540))
        n115 = (Entry(self.frame2, textvar=self.fns15).place(x=600, y=560))
        self.frame41 = Frame(self.frame, width=200, height=800, bd=10, relief='raise').place(x=575, y=180)
    def notas2(self):
        self.notas9()
        self.notas1()
        self.lbl2 = Label(text='Notas 2ºano', font='Arial 18').place(x=820, y=200)
        n21 = (Entry(self.frame2, textvar=self.fnn).place(x=820, y=260))
        n21 = (Entry(self.frame2, textvar=self.fnn1).place(x=820, y=280))
        n22 = (Entry(self.frame2, textvar=self.fnn2).place(x=820, y=300))
        n23 = (Entry(self.frame2, textvar=self.fnn3).place(x=820, y=320))
        n24 = (Entry(self.frame2, textvar=self.fnn4).place(x=820, y=340))
        n25 = (Entry(self.frame2, textvar=self.fnn5).place(x=820, y=360))
        n26 = (Entry(self.frame2, textvar=self.fnn6).place(x=820, y=380))
        n27 = (Entry(self.frame2, textvar=self.fnn7).place(x=820, y=400))
        n28 = (Entry(self.frame2, textvar=self.fnn8).place(x=820, y=420))
        n29 = (Entry(self.frame2, textvar=self.fnn9).place(x=820, y=440))
        n210 = (Entry(self.frame2, textvar=self.fnn10).place(x=820, y=460))
        n211 = (Entry(self.frame2, textvar=self.fnn11).place(x=820, y=480))
        n212 = (Entry(self.frame2, textvar=self.fnn12).place(x=820, y=500))
        n213 = (Entry(self.frame2, textvar=self.fnn13).place(x=820, y=520))
        n214 = (Entry(self.frame2, textvar=self.fnn14).place(x=820, y=540))
        n215 = (Entry(self.frame2, textvar=self.fnn15).place(x=820, y=560))
        self.frame41 = Frame(self.frame, width=200, height=800, bd=10, relief='raise').place(x=795, y=180)

#-----------------------------------------------------------------------------------------------------------------------

    def botaodeescolha(self):
        self.lblsit = Label(self.frame2, text='Situação escolar',font='Arial 15',bd=8).place(x=100,y=180)
        self.sit_a = Radiobutton(self.frame2,text='1ano',bg='#A59F9D',font='Arial 15',value=1,command=self.notas9).place(x=120,y=230)
        self.sit_b = Radiobutton(self.frame2, text='2ano',bg='#A59F9D',font='Arial 15',value=2,command=self.notas1).place(x=120, y=260)
        self.sit_c = Radiobutton(self.frame2, text='3ano',bg='#A59F9D',font='Arial 15',value=3,command=self.notas2).place(x=120, y=290)
        self.sit_d = Radiobutton(self.frame2,text='Formado',bg='#A59F9D',font='Arial 15',value=4).place(x=120,y=320)

#-----------------------------------------------------------------------------------------------------------------------

    def resetb(self):
        pass


#LOGIN------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

def bt_oksenha():
    p1 = 'Paulo'


def bt_entrar(passw1=None):
    p1=str(passwd.get())
    p2=str(confpas.get())
    if p1 == 'Paulo' and  p2 == '1234':
        lb["text"] = str("Login Efetuado com Sucesso")
        time.sleep(0)
        jpas.destroy()
        jpas.mainloop()
        root = Tk()
        janela(root)
        root.title('GPA by Paulo Drefahl')
        root.mainloop()

    else:
        lb["text"] = str("Senha incorreta")

lbl = Label(jpas, text ='Login: ')
lbl.grid(row=0,column=0)

lbl2 = Label(jpas, text ='Senha: ')
lbl2.grid(row=1,column=0)

passwd = Entry(jpas)
passwd.grid(row=0,column=1)

confpas = Entry(jpas)
confpas.grid(row=1,column=1)

btentrar = Button(jpas, text="Login", command=bt_entrar)
btentrar.grid(row=2,column=1)


lb = Label(jpas, text="")
lb.grid(row=3,column=1)

jpas.geometry("200x100+100+100")
jpas.mainloop()
#Encerra tela de login
#==================================================================

