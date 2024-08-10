#!pip install requests
#!pip install lxml
import pandas as pd 
import numpy as np 
import requests
import locale
locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')
from tkinter import *
import ttkbootstrap as tb
import warnings
warnings.filterwarnings("ignore")
#AK11
root=tb.Window(themename="superhero")
root.resizable(width=False,height=False)
root.attributes('-alpha',0.98)
root.title("1000 kelime")
root.geometry("600x550")


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
url = "https://www.openenglish.com.tr/blog/ingilizcede-en-cok-kullanilan-1000-kelime/"

response = requests.get(url, headers=headers)
tables=pd.read_html(response.text)
df=tables[0]
df.rename(columns={0:"ENG",1:"TR"},inplace=True)
df.drop(0,axis=0,inplace=True)
df_string =df.to_string()

global sayac
sayac=0
liste=list(range(1,1001))
liste=np.array(liste)
np.random.shuffle(liste)


def baslat():
    for widget in root.winfo_children():
        widget.destroy()
    
    
    def anlam_getir():
        global sayac
        label6.config(text=df.loc[liste[sayac]][1])
           
    
    def kelime_getir():
        global sayac
        sayac+=1
        button3=tb.Button(root,text="Türkçesini getir",bootstyle="outliner info",width=20,command=anlam_getir)  
        button3.place(x=265,y=167)
        label5.config(text=df.loc[liste[sayac]][0])
        
    label4=tb.Label(root,bootstyle="inverse-success",text="İngilizce",font=("Helvetica",40),foreground="black",width=10,anchor="center")
    label4.place(x=135,y=0)

    frame2=tb.Frame(root,bootstyle="danger",width=550,height=200)
    frame2.place(x=0,y=60)
    label5=tb.Label(frame2,bootstyle="inverse-dark",text="kelime yüklemek için yeni kelime butonuna tıklayın",font=("Helvetica",23),width=200,wraplength=600,foreground="light blue")
    label5.pack(padx=0,pady=15)

    button2=tb.Button(root,text="Yeni kelime",bootstyle="outliner success",width=20,command=kelime_getir)
    button2.place(x=109,y=167)
    button4=tb.Button(root,text="Çıkış",bootstyle="outliner danger",width=20,command=root.quit)
    button4.place(x=175,y=200)



    label4=tb.Label(root,bootstyle="inverse-primary",text="Türkçe",font=("Helvetica",40),foreground="black",width=10,anchor="center")
    label4.place(x=135,y=288)
    frame3=tb.Frame(root,bootstyle="danger",width=550,height=200)
    frame3.place(x=0,y=350)
    label6=tb.Label(frame3,bootstyle="inverse-dark",text="kelime yüklemek için yeni kelime butonuna tıklayın",font=("Helvetica",23),width=200,wraplength=600,foreground="light blue")
    label6.pack(padx=0,pady=15)




label1=tb.Label(root,text="İngilizce en sık kullanılan 1000(bin) kelime uygulaması",font=("Times",19,"bold italic"),bootstyle="inverse info",foreground="black")
label1.place(x=0,y=0)

label2=tb.Label(root,text="Uygulamaya Başlamak için aşağıdaki butona tıklayabilirsiniz",font=("Arial",14),bootstyle="inverse success",foreground="black")
label2.place(x=50,y=45)

button1=tb.Button(root,text="Başlat",bootstyle="outliner warning",width=40,command=baslat)
button1.place(x=140,y=80)

label3=tb.Label(root,text="Kelime listesi aşağıda ",font=("Times",18,"bold italic"),bootstyle="inverse info",foreground="black")  
label3.place(x=170,y=170)   

frame1=tb.Frame(root)
frame1.place(x=10,y=200,width=570,height=450)
text_widget1 = tb.Text(frame1, wrap=tb.NONE, font=("Times", 15), foreground="black")
text_widget1.insert(tb.END, df_string)
text_widget1.pack(side="left", fill="both", expand=True)


scrollbar1 = tb.Scrollbar(frame1, orient="vertical", command=text_widget1.yview)
scrollbar1.pack(side="right", fill="y")

text_widget1.config(yscrollcommand=scrollbar1.set)


root.mainloop()