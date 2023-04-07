import random
import json
import requests
import tkinter as tk
import webbrowser

url = "https://takumin287877.github.io/illust-odai/odai.json"
odaijson = requests.get(url)
odaijson = odaijson.json()
print(odaijson)

def res():#入力関数
    global odais1, odais2, odais3, odaijson
    odais1 = (odaijson["odai1"][(random.randint(1, len(odaijson))-1)])
    odais2 = (odaijson["odai2"][(random.randint(1, len(odaijson))-1)])
    odais3 = (odaijson["odai3"][(random.randint(1, len(odaijson))-1)])
    
    print(odais1,odais2,odais3)
    cl()
    textbox1.insert(0,(odais1))
    textbox2.insert(0,(odais2))
    textbox3.insert(0,(odais3))
    
root = tk.Tk()
root.title("ランダムイラスト")
root.geometry("500x500")
root.resizable(False, False)  # リサイズ不可

textbox1 = tk.Entry(width=50)
textbox2 = tk.Entry(width=50)
textbox3 = tk.Entry(width=50)

def cl():#初期化関数
    textbox1.delete(0,tk.END)
    textbox2.delete(0,tk.END)
    textbox3.delete(0,tk.END)

def tweet():
    url = ("https://twitter.com/intent/tweet?text=" + odais1 + odais2 + odais3)
    webbrowser.open(url,new=0,autoraise=True)

button = tk.Button(text="新しいお代にする。", width=60, command=res)
tweetbt = tk.Button(text="ツイートする!",width=50,command=tweet)
textbox1.pack()
textbox2.pack()
textbox3.pack()
button.pack()
tweetbt.pack()
root.mainloop()
