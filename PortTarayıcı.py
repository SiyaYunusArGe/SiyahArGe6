#!/usr/bin/env python
import os
os.system ("apt.get install figlet")
os.system("clear")
print("""
  _____                   _       _______                                  _          _ 
 |  __ \                 | |     |__   __|                                (_)        (_)
 | |__) |   ___    _ __  | |_       | |      __ _   _ __    __ _   _   _   _    ___   _ 
 |  ___/   / _ \  | '__| | __|      | |     / _` | | '__|  / _` | | | | | | |  / __| | |
 | |      | (_) | | |    | |_       | |    | (_| | | |    | (_| | | |_| | | | | (__  | |
 |_|       \___/  |_|     \__|      |_|     \__,_| |_|     \__,_|  \__, | |_|  \___| |_|
                                                                    __/ |               
                                                                   |___/                

""")




print("""
Port Tarama Aracina Hosgeldiniz created by.SiyahYunus

1: 1. Seviye Tarama (1)
2: 2. Seviye Tarama (2)
3: 3. Seviye Tarama (3)
""")

islemnumara = raw_input("Tarama Hangi Seviyede Olsun ")

if(islemnumara == "1"): 
	hedefip = raw_input("Hedef Ip Giriniz: ")
	os.system("nmap " + hedefip)

elif(islemnumara == "2"):
	hedefip = raw_input("Hedef Ip Giriniz: ")
	os.system("nmap -sS -sV " + hedefip)

elif(islemnumara == "3"):
	hedefip = raw_input("Hedef Ip Giriniz ")
	os.system("nmap -O " + hedefip)
else:
	print(" Boyle bir komut yok. Lutfen TEKRAR deneyiniz!")	

