# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 20:49:03 2022

@author: Bagzi
"""

import mysql.connector
import matplotlib.pyplot as plt

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="mydatabase"
    )

mycursor = db.cursor()

def pretragaSvihProizvoda():
    print("Lista svih proizvoda (ID proizvoda, naziv, cena i kolicina proizvoda na lageru): ")
    Qp = "SELECT idProizvoda, naziv, cena FROM Proizvod"
    try:
        mycursor.execute(Qp)
    except:
        print("\n")
        print("U prodavnici jos uvek ne postoje proizvodi!")
        print("\n")
    for x in mycursor:
        print(x)
    print("\n")
    print("Lista svih kategorija (ID kategorije i naziv): ")
    Qk = "SELECT * FROM Kategorija"
    mycursor.execute(Qk)
    for y in mycursor:
        print(y)
    print("\n")
    print("ID proizvoda (prvi broj), ID kategorija u kojima je proizvod dostupan (drugi broj) i kolicina proizvoda na lageru (treci broj):")
    Qpk = "SELECT * FROM ProizvodKategorija"
    try:
        mycursor.execute(Qpk)
    except:
        print("\n")
    for z in mycursor:
        print(z)
    print("\n")  

def grafikon():
    Q1 = "SELECT naziv, brojProdatih FROM Proizvod ORDER BY brojProdatih ASC LIMIT 5"
    mycursor.execute(Q1)

    proizvodi = []
    prodati = []

    for x in mycursor:
        proizvodi.append(x[0])
        prodati.append(x[1])
    
    plt.bar(proizvodi, prodati)
    plt.xlabel('proizvodi')
    plt.xticks(rotation = 90)
    plt.ylabel('prodato komada')
    plt.title("TOP 5 NAJPRODAVANIJIH PROIZVODA")
    plt.show()