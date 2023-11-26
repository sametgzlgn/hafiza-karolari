import tkinter as tk
import random
import time
import threading
import simpleaudio

sekans = ""
cevap = ""
butonlar = []
zorluk = 5
ping = simpleaudio.WaveObject.from_wave_file("ping.wav")
hata = simpleaudio.WaveObject.from_wave_file("yanlis.wav")
dogru = simpleaudio.WaveObject.from_wave_file("dogru.wav")
can = 3

def sekans_olustur():
    global sekans,butonlar,zorluk
    time.sleep(1)
    sekans = ""
    for i in butonlar:
        i["state"] = tk.DISABLED
        i["bg"] = "white"
    while len(sekans) < zorluk:
        sayi = random.randint(0,len(butonlar) - 1)
        sekans += str(sayi)
        butonlar[sayi]["bg"] = "blue"
        ping.play()
        time.sleep(1)
        butonlar[sayi]["bg"] = "white"
        time.sleep(0.3)
    for i in butonlar:
        i["state"] = tk.ACTIVE

def kontrol():
    global sekans,cevap,zorluk,can,hata,dogru
    thr2 = threading.Thread(target=sekans_olustur)
    if can == 0:
        exit("Oyun bitti!")
    if len(cevap) == len(sekans) and cevap == sekans:
        cevap = ""
        dogru.play()
        zorluk += 1
        thr2.start()
    if len(cevap) == len(sekans) and cevap != sekans:
        cevap = ""
        can -= 1
        zorluk -= 1
        hata.play()
        thr2.start()

def ekle(btn):
    global cevap
    kontrol()
    ping.play()
    cevap += str(btn)

pencere = tk.Tk()
pencere.title("Hafıza Karoları")
pencere.resizable(False,False)
buton0 = tk.Button(width=10,height=5,command=lambda:ekle(0))
butonlar.append(buton0)
buton0.grid(column=0,row=0)
buton1 = tk.Button(width=10,height=5,command=lambda:ekle(1))
butonlar.append(buton1)
buton1.grid(column=1,row=0)
buton2 = tk.Button(width=10,height=5,command=lambda:ekle(2))
butonlar.append(buton2)
buton2.grid(column=2,row=0)
buton3 = tk.Button(width=10,height=5,command=lambda:ekle(3))
butonlar.append(buton3)
buton3.grid(column=0,row=1)
buton4 = tk.Button(width=10,height=5,command=lambda:ekle(4))
butonlar.append(buton4)
buton4.grid(column=1,row=1)
buton5 = tk.Button(width=10,height=5,command=lambda:ekle(5))
butonlar.append(buton5)
buton5.grid(column=2,row=1)
buton6 = tk.Button(width=10,height=5,command=lambda:ekle(6))
butonlar.append(buton6)
buton6.grid(column=0,row=2)
buton7 = tk.Button(width=10,height=5,command=lambda:ekle(7))
butonlar.append(buton7)
buton7.grid(column=1,row=2)
buton8 = tk.Button(width=10,height=5,command=lambda:ekle(8))
butonlar.append(buton8)
buton8.grid(column=2,row=2)
thr = threading.Thread(target=sekans_olustur)
thr.start()
pencere.mainloop()
