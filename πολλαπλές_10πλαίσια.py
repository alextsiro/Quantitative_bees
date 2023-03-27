from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import pyomo.environ as pyo
import numpy as np
import tkinter as tk

window = Tk()

p1 = PhotoImage(file = 'C:/Users/Tsiro/Google Drive/Μελισσοσμήνη_Διπλωματική_Τσιροζίδης/logo.png')
window.iconphoto(False, p1)

var2= IntVar()
var3= IntVar()
window.title('Διπλωματική εργασία')
anaptyxi=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
arxika_melissia=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
window.geometry('800x750')
lbl = Label(window, text="Ανάπτυξη")
lbl.grid(column=2, row=2)
lbl = Label(window, text="Πλήθος")
lbl.grid(column=1, row=2)
var=[]
def acceptNumber(inp):
    if inp.isdigit():
        return True
    elif inp is "":
        return True
    elif inp is ".":
        return True
    else:
        return False
reg = window.register(acceptNumber)
entries=[Entry(window,textvariable=0, width=5),Entry(window,textvariable=0, width=10),Entry(window,textvariable=0, width=10)]
for i in range (3,21):
    var.append(IntVar())
    lbl = Label(window, text="Μελισσοσμήνη πληθικότητας %s πλαισίων " %i)
    lbl.grid(column=0, row=i)
    entries.append(Entry(window,textvariable=var[i-3], width=8))
    entries[i].grid(column=1, row=i)
    entries[i].config(validate="key", validatecommand =(reg, '%P'))
combo = [Combobox(window),Combobox(window),Combobox(window)]
for i in range (3,21):
    combo.append(Combobox(window,width=5))
    combo[i]['values']= (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    combo[i] .grid(column=2, row=i, padx=1, pady=1)
    if(i<=7):
        combo[i].current(0)
    elif(i<=10):
        combo[i].current(1)
    elif(i<=20):
        combo[i].current(2)

lbl = Label(window, text="Διάρκεια Μελισσοκομικής Άνοιξης ")
lbl.grid(column=0, row=26)
entr2 = Entry(window,textvariable=var2,width=8)
entr2.grid(column=1, row=26)
entr2.config(validate="key", validatecommand =(reg, '%P'))

lbl = Label(window, text="Περίοδος Επιθεωρήσεων")
lbl.grid(column=0, row=27)
entr3 = Entry(window,textvariable=var3,width=8)
entr3.grid(column=1, row=27)
entr3.config(validate="key", validatecommand =(reg, '%P'))
diarkeia_melissokomikis_anoixis=0
meres_episkepsewn=0
def clicked_ok():
    for i in range (3,21):
        arxika_melissia[i]=int(entries[i].get())
        anaptyxi[i]=int(combo[i].get())
        #print(arxika_melissia[i])
        #print(anaptyxi[i])
    diarkeia_melissokomikis_anoixis=int(entr2.get())
    meres_episkepsewn=int(entr3.get())
    #print(meres_episkepsewn)
    #print(diarkeia_melissokomikis_anoixis)
    vimata=diarkeia_melissokomikis_anoixis//meres_episkepsewn
    plithikotita_meta_tin_anadiataxi = range(0,21)
    model = pyo.ConcreteModel()
    model.Con=pyo.ConstraintList()
    print('Το πλήθος των επισκέψεων θα είναι: %s ' % vimata )

    plithos_vimatwn = range(0,vimata+1)
    model.meta=pyo.Var(plithikotita_meta_tin_anadiataxi, plithos_vimatwn,domain=pyo.NonNegativeIntegers)
    #model.apofasis=pyo.Var(plithikotita_meta_tin_anadiataxi, plithos_vimatwn,domain=pyo.Binary)
    model.nea=pyo.Var(plithos_vimatwn,domain=pyo.NonNegativeIntegers, initialize=0)    
    #model.w=pyo.Var(plithikotita_meta_tin_anadiataxi, plithos_vimatwn,domain=pyo.NonNegativeIntegers, initialize=0)
    


    #σύνολικό πλήθος μελισσοσμηνών
    s=0
    for i in range (3,21):
        s=s+arxika_melissia[i]
    print('Το πλήθος των μελισσοσμηνών είναι %s' %s )
    s=int(s)  
    max_anaptyxi=0
    for i in range (3,21):
        if anaptyxi[i]>max_anaptyxi:
            max_anaptyxi=int(anaptyxi[i])     
    print('Η μεγαλύτερη ανάπτυξη είναι: %s ' % max_anaptyxi)

    plithikotita_prin_tin_anadiataxi = range(0,21+max_anaptyxi)
    model.prin=pyo.Var(plithikotita_prin_tin_anadiataxi,plithos_vimatwn,domain=pyo.NonNegativeIntegers)

    #Ελέγχουμε τι πληθικότητας μελισσοσμήνη θα υπάρχουν πριν την αναδιάταξη (μετά την ανάπτυξη)
    test=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range (3,21):
        test[i+anaptyxi[i]]=1
    for i in range (3,21+max_anaptyxi):
        if(test[i]==1):
            print("Πρίν απο την αναδιάταξη είναι πιθακό να έχουμε μελισσοσμήνη πληθικότητας %s " % i)    

    # Αντικειμενική Συνάρτηση
    model.Obj = pyo.Objective(expr = sum(model.nea[p] for p in range (0,vimata+1)), sense = pyo.maximize)

    #Αρχική κατάσταση

    model.Con.add(expr = model.nea[0]==0)
    for i in range (0,21+max_anaptyxi):    
        model.Con.add(expr = model.prin[i,0]==0) 
    #for i in range (0,21):
    #   model.Con.add(expr = model.apofasis[i,0]==0)
    for i in range (0,21):
        model.Con.add(expr = model.meta[i,0]==arxika_melissia[i])    

    #περιορισμός πολύ μικρών μελισσοσμηνών
    for p in range (0,vimata+1):
        for i in range (0,3):
            model.Con.add(expr = model.prin[i,p]==0)
            model.Con.add(expr = model.meta[i,p]==0)
            #model.Con.add(expr = model.apofasis[i,p]==0)
            #model.Con.add(expr = model.w[i,p]==0)

    #Περιορισμοί μεταξύ βημάτων(εξέλιξης)
    for p in range (0,vimata):
        for i in range (3,21): 
            model.Con.add(expr = model.prin[i+anaptyxi[i],p+1]==model.meta[i,p])
            
        for i in range (3,21+max_anaptyxi):   
            if test[i]==0:
                model.Con.add(expr = model.prin[i,p+1]==0)
    #for p in range (1,vimata+1):
     #   for i in range (3,21): 
      #      model.Con.add(expr = model.w[i,p]>=0)
       #     model.Con.add(expr = model.w[i,p]>=model.meta[i,p]+s*model.meta[i,p]-s)
        #    model.Con.add(expr = model.w[i,p]<=model.apofasis[i,p]*s)
         #   model.Con.add(expr = model.w[i,p]<=model.meta[i,p])  
       
    #περιορισμοί αναδιάταξης : πλαισίων και βασσιλισσών            
    for p in range (1,vimata+1):   
        #πλαίσια         
        model.Con.add(expr = sum(i*model.prin[i,p] for i in range (0,21+max_anaptyxi))==model.nea[p]+sum(i*model.meta[i,p] for i in range (0,21)))
    #βασσίλισσες
        model.Con.add(expr = sum(model.prin[i,p] for i in range (0,21+max_anaptyxi))==sum(model.meta[i,p] for i in range (0,21)))

#    for p in range (1,vimata+1):
#        model.Con.add(expr = sum(model.meta[i,p] for i in range(0,21))==1)
       
#περιορισμός αποδοτικών μελισσοσμηνών κατα το πέρας της μελισσοκομικής άνοιξης        
    model.Con.add(expr = s ==model.meta[10,vimata])
    
    opt = pyo.SolverFactory('glpk')
    opt.solve(model)

    print("Η τιμή της αντικειμενικής συνάρτησης είναι: ")
    print(pyo.value(model.Obj))

    print("Η βέλτιστη λύση είναι")
    for i in range (0,vimata+1):
        print(model.nea[i].value)

    print("ο πίνακας πρίν")
    for p in range (0,vimata+1):
        print('στο βήμα  %s ' %p)
        for i in range (0,21+max_anaptyxi):
            print(model.prin[i,p].value)
        
    print ("ο πίνακας μετά")
    for p in range (0,vimata+1):
        print('στο βήμα  %s ' %p)
        for i in range (0,21):
            print(model.meta[i,p].value)
    lbl = Label(window, text="Σύνολο")
    lbl.grid(column=3, row=24+max_anaptyxi+1)
    lbl = Label(window, text=pyo.value(model.Obj))
    lbl.grid(column=4, row=24+max_anaptyxi+1)
    for p in range (1,vimata+1):
        lbl = Label(window, text="Στο βήμα")
        lbl.grid(column=2*p+1, row=2)
        lbl = Label(window, text=p)
        lbl.grid(column=2*(p+1), row=2)
        
        for i in range (3,21):           
            lbl = Label(window, text=int(model.meta[i,p].value))
            lbl.grid(column=2*(p+1), row=i)
            lbl = Label(window, text="νέα:")
            lbl.grid(column=2*p+1, row=23+max_anaptyxi+1)
            lbl = Label(window, text=int(model.nea[p].value))
            lbl.grid(column=2*(p+1), row=23+max_anaptyxi+1)
        for i in range (3,21+max_anaptyxi):           
            lbl = Label(window, text=int(model.prin[i,p].value))
            lbl.grid(column=2*p+1, row=i)
        
#    print(model.meta[i,p].value)
#    for i in range(3,21):
#       arxika_melissia[i]=int(int)
#      if (arxika_melissia[i]<0):
#           messagebox.showinfo('Message title','Message content')

lbl = Label(window, text=" ")
lbl.grid(column=0, row=21)
    
btn = Button(window, text="Οκ", command=clicked_ok, width=10)  
        
btn.grid(column=3, row=48)
 
#def clicked2():    
#    messagebox.showinfo('Message title','Message content')

#btn2 = Button(window, text="Click Me", command=clicked2)
#btn2.grid(column=4, row=0)

window.mainloop()
