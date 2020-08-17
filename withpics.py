# -*- coding: utf-8 -*-
"""
Created on Fri Aug 7 16:26:39 2020

@author: DELL
"""

import tkinter as tk
#from tkinter.ttk import *
from PIL import Image, ImageTk

nxt_test='False'

import mysql.connector as ms
con=ms.connect(host='localhost',user='root',passwd='apr4pm',database= 'cafe')
if con.is_connected():
    print('y')
    
curs=con.cursor()

lst_bill=[]
lst_log=[]


win=tk.Tk()
win.title('cafe')
win.geometry('1495x650')

fr_title = tk.Frame(master=win,relief='groove',bg='purple',borderwidth=6)
fr_title.grid(columnspan=20,sticky='w')

lbl_title=tk.Label(fr_title,fg='midnightblue',bg='khaki1',text='Aroma Mocha',font=('ink free',50),width=41)
lbl_title.grid()

fr_buy=tk.Frame(bg='#dce1e7',borderwidth=4,relief='ridge')
#fr_buy.grid(row=1,column=1,columnspan=19,rowspan=18,sticky='nsew',padx=3)

v1= tk.IntVar()
v1.set(1)
v2= tk.IntVar()
v2.set(1)

def job(a=v1,b=v2):
    try:
        global fr_active
        for child in fr_active.winfo_children():
            child.destroy()
    except:
        global fr_buy
        for child in fr_buy.winfo_children():
            child.forget()
        fr_active=tk.Frame(master=win,relief='raised',bg='#dce1e7',borderwidth=4)
        fr_active.grid(row=1,column=1,sticky='nsew',columnspan=20,rowspan=18)
        
    
    lst=['ol','bl','le','Full Name','Sex','Nationality','Date Of Birth','Qualification',
         'Position Applied For','Prior Experience','Employment Desired','Email Address','Contact Number']
    
    '''fr_active=tk.Frame(win,relief='sunken',bg='whitesmoke')
    fr_active.grid(row=1,column=1,padx=5,sticky='nsew',columnspan=19)
    '''
    lbl_inst=tk.Label(fr_active,text='Please nether your details and we will get back to you shortly.',fg='brown',font=('papyrus',15))
    lbl_inst.grid(column=1,columnspan=30)
    

    for i in range(3,13):
        lbl=tk.Label(fr_active,text=lst[i]+':',fg='brown',font=('papyrus',20))
        ent=tk.Entry(fr_active,width=40,font=('verdana',20))
        lbl.grid(row=i,column=1,sticky='ew',padx=10,pady=2)
        ent.grid(row=i,column=2,columnspan=8)
        if i==4:
            v1= tk.IntVar()
            v1.set(1)
            rad1=tk.Radiobutton(fr_active,text='Male',variable=a,value=1,font=('papyrus',20))
            rad2=tk.Radiobutton(fr_active,text='Female',variable=a,value=2,font=('papyrus',20))
            lbl.grid(row=i,column=1,sticky='ew',padx=10,pady=2)
            ent.destroy()
            rad1.grid(row=4,column=2)
            rad2.grid(row=4,column=3)
        if i==7:
            var = tk.StringVar(fr_active)
            var.set("Undergraduate")  
            ent.destroy()
            opnm_qua = tk.OptionMenu(fr_active, var,'Undergraduate','Graduate','Higher')
            opnm_qua.config(font=('papyrus',15))
            menu = fr_active.nametowidget(opnm_qua.menuname)
            menu.config(font=('papyrus',15))
            opnm_qua.grid(row=7,column=2,pady=5)
            
        if i==8:
            var = tk.StringVar(fr_active)
            var.set("Cashier")  
            ent.destroy()
            opnm_pos = tk.OptionMenu(fr_active, var, 'Cashier', 'Barista','Accountant')
            opnm_pos.config(font=('papyrus',15))
            menu = fr_active.nametowidget(opnm_pos.menuname)
            menu.config(font=('papyrus',15))
            opnm_pos.grid(row=8,column=2,pady=5)
        if i==10:
            v2= tk.IntVar()
            v2.set(1)
            rad1=tk.Radiobutton(fr_active,text='Part Time',variable=b,value=1,font=('papyrus',20))
            rad2=tk.Radiobutton(fr_active,text='Full Time',variable=b,value=2,font=('papyrus',20))
            ent.destroy()
            rad1.grid(row=10,column=2)              
            rad2.grid(row=10,column=3)
            
            
        
    
    def sub():
        pass 
    
    def cl():
        job() #coz job will kinda refresh entire page essentially clearing it
    
    but_cl=tk.Button(master=fr_active,text='Clear',width=20,height=2,bg='paleturquoise1',command=cl)
    but_cl.grid(sticky='se',column=4,pady=35,row=14,padx=5)
    
    but_sub=tk.Button(master=fr_active,text='Submit',width=20,height=2,bg='paleturquoise1')
    but_sub.grid(sticky='se',column=2,pady=35,padx=5,row=14)


def fdb():
    try:
        global fr_active
        for child in fr_active.winfo_children():
            child.destroy()
    except:
        global fr_buy
        for child in fr_buy.winfo_children():
            child.forget()
        fr_active=tk.Frame(master=win,relief='raised',bg='#dce1e7',borderwidth=4)
        fr_active.grid(row=1,column=1,sticky='nsew',columnspan=20,rowspan=18)
    
    '''fr_fdb=tk.Frame(win,relief='ridge',bg='peachpuff',borderwidth=3)
    fr_fdb.grid(row=1,column=1,padx=2,sticky='nsew',columnspan=19)
    '''
    def cl():
        fdb()
    def sub():
        fdb1=open('%s.txt'%ent_name.get(),'w')
        fdb1.write(txt_fdb.get(1.0,tk.END))
        fdb1.close()
        lbl_res=tk.Label(fr_active,text='Your response has been recorded.',bg='palegreen',font=('cambria',15))
        lbl_res.grid(row=2,column=3)
        txt_fdb.delete(1.0,tk.END)
        ent_name.delete(0,tk.END)
        
    
    lbl_name=tk.Label(fr_active,text='Name:',font=('papyrus',15))
    lbl_name.grid(row=1,column=1,sticky='ew',padx=10,pady=2)
    
    ent_name=tk.Entry(fr_active,width=20,font=('verdana',15))
    ent_name.grid(row=1,column=2)
    
    lbl_inst=tk.Label(fr_active,text='Please enter your feedback below.',font=('cambria',15))
    lbl_inst.grid(row=2,column=2)
    
    but_cl=tk.Button(fr_active,text='Clear',width=20,height=2,bg='paleturquoise1',command=cl)
    but_cl.grid(row=6,column=15,sticky='n')
    but_sub=tk.Button(fr_active,text='Submit',width=20,height=2,bg='paleturquoise1',command=sub)
    but_sub.grid(row=7,column=15,sticky='ew')
    
    txt_fdb=tk.Text(fr_active,font=('verdana',15))
    txt_fdb.grid(row=6,columnspan=10,rowspan=20,padx=10)
    
    
def offers():
    try:
        global fr_active
        for child in fr_active.winfo_children():
            child.destroy()
    except:
        global fr_buy
        for child in fr_buy.winfo_children():
            child.forget()
        fr_active=tk.Frame(master=win,relief='raised',bg='#dce1e7',borderwidth=4)
        fr_active.grid(row=1,column=1,sticky='nsew',columnspan=20,rowspan=18)
        
        
        
    #fr_log.destroy()
    
    '''fr_off=tk.Frame(win,relief='ridge',bg='peachpuff',borderwidth=3)
    fr_off.grid(row=1,column=1,padx=2,sticky='nsew',columnspan=3)
    global fr_active
    fr_active.destroy()'''
    
    pht1=Image.open('cross.jpg').resize((400,500),Image.ANTIALIAS)
    pht11=ImageTk.PhotoImage(pht1)
    lbl1=tk.Label(fr_active,image=pht11)
    lbl1.image=pht11
    lbl1.grid(row=0,column=0)
    lbl11=tk.Label(fr_active,text='Buy TWO cups of black coffee \n and get a crossiant FREE!',bg='aliceblue',font=('ink free',17))
    lbl11.grid(row=1,column=0,pady=10)
    but1=tk.Button(fr_active, text='Buy now!',width=20,height=2,bg='paleturquoise1')
    but1.grid(row=2,column=0,pady=10)
    
    pht2=Image.open('chsck.jpg').resize((400,500),Image.ANTIALIAS)
    pht22=ImageTk.PhotoImage(pht2)
    lbl2=tk.Label(fr_active,image=pht22)
    lbl2.image=pht22
    lbl2.grid(row=0,column=1)
    lbl22=tk.Label(fr_active,text='Buy a slice of cheesecake,\nand get a second one at half price!',bg='aliceblue',font=('ink free',17))
    lbl22.grid(row=1,column=1)
    but1=tk.Button(fr_active, text='Buy now!',width=20,height=2,bg='paleturquoise1')
    but1.grid(row=2,column=1,pady=10)
    
    pht3=Image.open('mocha.jpg').resize((400,500),Image.ANTIALIAS)
    pht33=ImageTk.PhotoImage(pht3)
    lbl3=tk.Label(fr_active,image=pht33)
    lbl3.image=pht33
    lbl3.grid(row=0,column=2)
    lbl33=tk.Label(fr_active,text='Buy TWO mochas \nand choose the toppings for free!',bg='aliceblue',font=('ink free',17))
    lbl33.grid(row=1,column=2)
    but1=tk.Button(fr_active, text='Buy now!',width=20,height=2,bg='paleturquoise1')
    but1.grid(row=2,column=2,pady=11)
    
    lbl_emp=tk.Label(fr_active,bg='#dce1e7',height=2)
    lbl_emp.grid(row=3,column=2)
    

def buy():
    global fr_active
    fr_active.destroy()
    #for child in fr_active.winfo_children():
     #   child.destroy()
    global fr_buy
    fr_buy=tk.Frame(bg='#dce1e7',borderwidth=4,relief='ridge')
    fr_buy.grid(row=1,column=1,columnspan=19,rowspan=18,sticky='nsew',padx=3)
    
    def next_bev():
        for child in fr_buy.winfo_children():
            child.grid_forget()
            
        lbl_inf=tk.Label(fr_buy,text='Choose from our wide variety of products!',fg='brown',font=('papyrus',19))
        lbl_inf.grid(row=0,column=1,sticky='ew')
        nxt=Image.open('nxt.png').resize((60,90),Image.ANTIALIAS)
        img_nxt=ImageTk.PhotoImage(nxt)
        but_nxt=tk.Button(fr_buy,image=img_nxt,height=90,width=60,bg='white',command=next_pst)
        but_nxt.image=img_nxt
        but_nxt.grid(row=1,column=3,rowspan=4,padx=3)
        
        pht7=Image.open(r'.\Food\blk.jpg').resize((250,250),Image.ANTIALIAS)
        pht77=ImageTk.PhotoImage(pht7)
        lbl7=tk.Label(fr_buy,image=pht77)
        lbl7.image=pht77
        lbl7.grid(row=1,column=0,padx=30)
        lbl77=tk.Label(fr_buy,text='Black Coffee- AED 5',bg='aliceblue',font=('ink free',17))
        lbl77.grid(row=2,column=0,pady=2)
        but7=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('1','beverages'))
        but7.grid(row=3,column=0)
        
        pht8=Image.open(r'.\Food\mch.jpg').resize((250,250),Image.ANTIALIAS)
        pht88=ImageTk.PhotoImage(pht8)
        lbl8=tk.Label(fr_buy,image=pht88)
        lbl8.image=pht88
        lbl8.grid(row=1,column=1)
        lbl88=tk.Label(fr_buy,text='Mocha- AED 8',bg='aliceblue',font=('ink free',17))
        lbl88.grid(row=2,column=1,pady=2)
        but8=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('2','beverages'))
        but8.grid(row=3,column=1)
        
        pht9=Image.open(r'.\Food\cap.jpg').resize((250,250),Image.ANTIALIAS)
        pht99=ImageTk.PhotoImage(pht9)
        lbl9=tk.Label(fr_buy,image=pht99)
        lbl9.image=pht99
        lbl9.grid(row=1,column=2)
        lbl99=tk.Label(fr_buy,text='Cappuccino- AED 7',bg='aliceblue',font=('ink free',17))
        lbl99.grid(row=2,column=2,pady=2)
        but9=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('3','beverages'))
        but9.grid(row=3,column=2)
        
        pht10=Image.open(r'.\Food\tea.jpg').resize((250,250),Image.ANTIALIAS)
        pht100=ImageTk.PhotoImage(pht10)
        lbl10=tk.Label(fr_buy,image=pht100)
        lbl10.image=pht100
        lbl10.grid(row=4,column=0,padx=30)
        lbl100=tk.Label(fr_buy,text='Black Tea- AED 5',bg='aliceblue',font=('ink free',17))
        lbl100.grid(row=5,column=0,pady=2)
        but10=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('4','beverages'))
        but10.grid(row=6,column=0)
        
        pht11=Image.open(r'.\Food\lem.jpg').resize((250,250),Image.ANTIALIAS)
        pht110=ImageTk.PhotoImage(pht11)
        lbl11=tk.Label(fr_buy,image=pht110)
        lbl11.image=pht110
        lbl11.grid(row=4,column=1,padx=10)
        lbl110=tk.Label(fr_buy,text='Lemon Tea- AED 6',bg='aliceblue',font=('ink free',17))
        lbl110.grid(row=5,column=1,pady=2)
        but11=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('5','beverages'))
        but11.grid(row=6,column=1)
        
        pht12=Image.open(r'.\Food\bub.jpg').resize((250,250),Image.ANTIALIAS)
        pht120=ImageTk.PhotoImage(pht12)
        lbl12=tk.Label(fr_buy,image=pht120)
        lbl12.image=pht120
        lbl12.grid(row=4,column=2,padx=10)
        lbl120=tk.Label(fr_buy,text='Bubble Tea- AED 15',bg='aliceblue',font=('ink free',17))
        lbl120.grid(row=5,column=2,pady=2)
        but12=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('6','beverages'))
        but12.grid(row=6,column=2)
        
    def next_pst():
        for child in fr_buy.winfo_children():
            child.grid_forget()
            
        lbl_inf=tk.Label(fr_buy,text='Choose from our wide variety of products!',fg='brown',font=('papyrus',19))
        lbl_inf.grid(row=0,column=1,sticky='ew')
        #nxt=Image.open('nxt.png').resize((60,90),Image.ANTIALIAS)
        #img_nxt=ImageTk.PhotoImage(nxt)
        but_nxt=tk.Button(fr_buy,text='Proceed to Checkout',height=2,width=20,bg='paleturquoise1',command=checkout)
        #but_nxt.image=img_nxt
        but_nxt.grid(row=1,column=3,rowspan=4,padx=3)
        
        pht13=Image.open(r'.\Food\crs.jpg').resize((250,250),Image.ANTIALIAS)
        pht130=ImageTk.PhotoImage(pht13)
        lbl13=tk.Label(fr_buy,image=pht130)
        lbl13.image=pht130
        lbl13.grid(row=1,column=0,padx=30)
        lbl130=tk.Label(fr_buy,text='Crossiant- AED 5',bg='aliceblue',font=('ink free',17))
        lbl130.grid(row=2,column=0,pady=2)
        but13=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('1','pastries'))
        but13.grid(row=3,column=0)
        
        pht14=Image.open(r'.\Food\don.jpg').resize((250,250),Image.ANTIALIAS)
        pht140=ImageTk.PhotoImage(pht14)
        lbl14=tk.Label(fr_buy,image=pht140)
        lbl14.image=pht140
        lbl14.grid(row=1,column=1)
        lbl140=tk.Label(fr_buy,text='Doughnut- AED 4',bg='aliceblue',font=('ink free',17))
        lbl140.grid(row=2,column=1,pady=2)
        but14=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('2','pastries'))
        but14.grid(row=3,column=1)
        
        pht9=Image.open(r'.\Food\pum.jpg').resize((250,250),Image.ANTIALIAS)
        pht99=ImageTk.PhotoImage(pht9)
        lbl9=tk.Label(fr_buy,image=pht99)
        lbl9.image=pht99
        lbl9.grid(row=1,column=2)
        lbl99=tk.Label(fr_buy,text='Pumpkin Pie- AED 10',bg='aliceblue',font=('ink free',17))
        lbl99.grid(row=2,column=2,pady=2)
        but9=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('3','pastries'))
        but9.grid(row=3,column=2)
        
        pht10=Image.open(r'.\Food\cin.jpg').resize((250,250),Image.ANTIALIAS)
        pht100=ImageTk.PhotoImage(pht10)
        lbl10=tk.Label(fr_buy,image=pht100)
        lbl10.image=pht100
        lbl10.grid(row=4,column=0,padx=30)
        lbl100=tk.Label(fr_buy,text='Cinnamon Rolls- AED 9',bg='aliceblue',font=('ink free',17))
        lbl100.grid(row=5,column=0,pady=2)
        but10=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('4','pastries'))
        but10.grid(row=6,column=0)
        
        pht11=Image.open(r'.\Food\plm.jpg').resize((250,250),Image.ANTIALIAS)
        pht110=ImageTk.PhotoImage(pht11)
        lbl11=tk.Label(fr_buy,image=pht110)
        lbl11.image=pht110
        lbl11.grid(row=4,column=1,padx=10)
        lbl110=tk.Label(fr_buy,text='Palmiers- AED 6',bg='aliceblue',font=('ink free',17))
        lbl110.grid(row=5,column=1,pady=2)
        but11=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('5','pastries'))
        but11.grid(row=6,column=1)
        
        pht12=Image.open(r'.\Food\mac.jpg').resize((250,250),Image.ANTIALIAS)
        pht120=ImageTk.PhotoImage(pht12)
        lbl12=tk.Label(fr_buy,image=pht120)
        lbl12.image=pht120
        lbl12.grid(row=4,column=2,padx=10)
        lbl120=tk.Label(fr_buy,text='Macarons- AED 15',bg='aliceblue',font=('ink free',17))
        lbl120.grid(row=5,column=2,pady=2)
        but12=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('6','pastries'))
        but12.grid(row=6,column=2) 
    
    def checkout():
        for child in fr_buy.winfo_children():
            child.grid_forget()
        lbl_inf=tk.Label(fr_buy,text='Thank you for shopping with us!\n Please view your bill below:',fg='brown',font=('papyrus',19))
        lbl_inf.grid(row=0,column=1,sticky='ew',columnspan=4,padx=5)
        txt_bill=tk.Text(fr_buy,font=('verdana',15))
        txt_bill.grid(row=4,columnspan=10,rowspan=20,padx=10)
        txt_bill.insert(1.0,' '*31+'Aroma Mocha')
        txt_bill.insert(3.0,'\n\nSl.No    Item')
        #spc=' '*int(12-len(str(dat[1])))
        
    
    def add(name,tbl):
        global lst_bill
        try:
            q='select item,price,allergens from {} where sl_no={};'.format(tbl,name)
            curs.execute(q)
            dat=list(curs.fetchone())
            print(dat)
            lst_bill.append(dat)
        except TypeError:
            print('type prollo')
    
          
###################### Next page:Beverages ##################################

        
    
    lbl_inf=tk.Label(fr_buy,text='Choose from our wide variety of products!',fg='brown',font=('papyrus',19))
    lbl_inf.grid(row=0,column=1,sticky='ew')
    nxt=Image.open('nxt.png').resize((60,90),Image.ANTIALIAS)
    img_nxt=ImageTk.PhotoImage(nxt)
    but_nxt=tk.Button(fr_buy,image=img_nxt,height=90,width=60,bg='white',command=next_bev)
    but_nxt.image=img_nxt
    but_nxt.grid(row=1,column=3,rowspan=4,padx=3)
    
        
    pht1=Image.open(r'.\Food\org.jpg').resize((250,250),Image.ANTIALIAS)
    pht11=ImageTk.PhotoImage(pht1)
    lbl1=tk.Label(fr_buy,image=pht11)
    lbl1.image=pht11
    lbl1.grid(row=1,column=0)
    lbl11=tk.Label(fr_buy,text='Orange Cake- AED 20',bg='aliceblue',font=('ink free',17))
    lbl11.grid(row=2,column=0,pady=2)
    but1=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('1','cakes'))
    but1.grid(row=3,column=0)
    
    pht2=Image.open(r'.\Food\brw.jpg').resize((250,250),Image.ANTIALIAS)
    pht22=ImageTk.PhotoImage(pht2)
    lbl2=tk.Label(fr_buy,image=pht22)
    lbl2.image=pht22
    lbl2.grid(row=1,column=1)
    lbl22=tk.Label(fr_buy,text='Brownies - AED 10',bg='aliceblue',font=('ink free',17))
    lbl22.grid(row=2,column=1,pady=2)
    but2=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('2','cakes'))
    but2.grid(row=3,column=1)
    
    pht3=Image.open(r'.\Food\red.jpg').resize((250,250),Image.ANTIALIAS)
    pht33=ImageTk.PhotoImage(pht3)
    lbl3=tk.Label(fr_buy,image=pht33)
    lbl3.image=pht33
    lbl3.grid(row=1,column=2)
    lbl33=tk.Label(fr_buy,text='Red Velvet Cake- AED 30',bg='aliceblue',font=('ink free',17))
    lbl33.grid(row=2,column=2,pady=2)
    but3=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('3','cakes'))
    but3.grid(row=3,column=2)
    
    pht4=Image.open(r'.\Food\blu.jpg').resize((250,250),Image.ANTIALIAS)
    pht44=ImageTk.PhotoImage(pht4)
    lbl4=tk.Label(fr_buy,image=pht44)
    lbl4.image=pht44
    lbl4.grid(row=4,column=0)
    lbl44=tk.Label(fr_buy,text='Blueberry Cheesecake- AED 30',bg='aliceblue',font=('ink free',17))
    lbl44.grid(row=5,column=0,pady=2)
    but4=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('4','cakes'))
    but4.grid(row=6,column=0)
    
    pht5=Image.open(r'.\Food\chs.jpg').resize((250,250),Image.ANTIALIAS)
    pht55=ImageTk.PhotoImage(pht5)
    lbl5=tk.Label(fr_buy,image=pht55)
    lbl5.image=pht55
    lbl5.grid(row=4,column=1)
    lbl55=tk.Label(fr_buy,text='ChocoOreo Cheesecake- AED 37',bg='aliceblue',font=('ink free',17))
    lbl55.grid(row=5,column=1,pady=2)
    but5=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('5','cakes'))
    but5.grid(row=6,column=1)
    
    pht6=Image.open(r'.\Food\rsp.jpg').resize((250,250),Image.ANTIALIAS)
    pht66=ImageTk.PhotoImage(pht6)
    lbl6=tk.Label(fr_buy,image=pht66)
    lbl6.image=pht66
    lbl6.grid(row=4,column=2)
    lbl66=tk.Label(fr_buy,text='Raspberry Cheesecake- AED 35',bg='aliceblue',font=('ink free',17))
    lbl66.grid(row=5,column=2,pady=2)
    but6=tk.Button(fr_buy, text='Add to cart',width=20,height=2,bg='paleturquoise1',command=lambda:add('6','cakes'))
    but6.grid(row=6,column=2,pady=5)
    


def login():
   lst=[]
   id=int(ent_id.get())
   query='select password from `login details` where id ={};'.format(id)
   curs.execute(query)
   dat=curs.fetchone()
   print('result ka type hai',type(dat))
   lst+=dat
   print(lst,'type hai',type(lst[0]))
   print('id hai',id)
   print('id ka type hai',type(id))
   
   if ent_ps.get()==lst[0]:
       print('yo ya gadd in omie')
       staff()
   else:
       lbl_warn=tk.Label(fr_log,text='lol get da falooda oud',font=('ink free',13),bg='red',height=2,width=17)
       lbl_warn.grid(row=4,column=1,columnspan=2,pady=5)
   
   ent_id.delete(0,tk.END)
   ent_ps.delete(0,tk.END)
   
        
def staff():
    fr_active.destroy()  
    
    #global fr_buy
    fr_view=tk.Frame(bg='#dce1e7',borderwidth=4,relief='ridge')
    fr_view.grid(row=1,column=1,columnspan=19,rowspan=18,sticky='nsew',padx=3)
    
    
      
    



fr_opn=tk.Frame(win,relief='ridge',bg='#dce1e7',borderwidth=4,height=20)
fr_opn.grid(sticky='nsew')
fr_log=tk.Frame(bg='blue',borderwidth=4,relief='sunken')
fr_log.grid(column=0,sticky='nsew',pady=5)
#magenta4 darkviolet ffca3a
but_shop=tk.Button(master=fr_opn,text='Online Shop',width=20,height=2,bg='purple',fg='midnightblue',font=('ink free',15,'bold'),borderwidth=4,command=buy)
but_shop.grid(column=0,padx=20,pady=10)

but_offers=tk.Button(master=fr_opn,text='Offers',width=20,height=2,bg='violetred',fg='midnightblue',font=('ink free',15,'bold'),borderwidth=4,command=offers)
but_offers.grid(column=0,padx=20,pady=10)

but_job=tk.Button(master=fr_opn,text='Job Application',width=20,height=2,bg='orchid1',fg='midnightblue',font=('ink free',15,'bold'),borderwidth=4,command=job)
but_job.grid(column=0,padx=20,pady=10)

but_fdb=tk.Button(master=fr_opn,text='Feedback',width=20,height=2,bg='plum1',fg='midnightblue',font=('ink free',15,'bold'),borderwidth=4,command=fdb)
but_fdb.grid(column=0,padx=20,pady=10)

lbl_log=tk.Label(fr_log,text='Enter Login Details', bg='aquamarine2',width=20,height=2,font=('ink free',15))
lbl_log.grid(padx=20,pady=10,sticky='nsew',columnspan=4)

lbl_id= tk.Label(fr_log,text='ID:',bg='aquamarine2',width=5,height=2,font=('ink free',11,'bold'))
lbl_id.grid(sticky='w',padx=5)
ent_id= tk.Entry(fr_log,width=23,font=('verdana',11))
ent_id.grid(row=1,column=1,sticky='w',padx=5,columnspan=6)



lbl_ps= tk.Label(fr_log,text='Pass:',bg='aquamarine2',width=5,height=2,font=('ink free',11,'bold'))
lbl_ps.grid(sticky='w',padx=5,pady=10)
ent_ps= tk.Entry(fr_log,width=23,show='*',font=('verdana',11))
ent_ps.grid(row=2,column=1,sticky='w',padx=5,columnspan=6)


but_sub=tk.Button(fr_log,text='Submit',width=10,height=2,bg='paleturquoise1',command=login)
but_sub.grid(row=3,column=1,sticky='e')

fr_active=tk.Frame(master=win,relief='raised',bg='#dce1e7',borderwidth=4)
fr_active.grid(row=1,column=1,sticky='nsew',columnspan=20,rowspan=18)

txt_abt=tk.Text(fr_active, font=('papyrus',25), borderwidth=4)
abt1=open('About.txt')
abt=abt1.read()
txt_abt.insert(tk.END,abt)
txt_abt.grid(rowspan=18,columnspan=10)

print('bill list:',lst_bill)

win.mainloop()














