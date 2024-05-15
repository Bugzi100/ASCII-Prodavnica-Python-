# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 20:47:22 2022

@author: Bagzi
"""

import mysql.connector
import hashlib

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="mydatabase"
    )

mycursor = db.cursor()

def signupProdavca():
    print("*** Formular za kreiranje naloga prodavca *** \n")
    ime_prodavca = input("Unesite vase ime: ")
    prezime_prodavca = input("Unesite vase prezime: ")
    plata_prodavca = input("Unesite vasu platu: ")
    
    username = input("Unesite zeljeno korisnicko ime (Minimum 6 karaktera i maksimalno 12 karaktera!): ")
    password = input("Unesite zeljenu lozinku (Minimum 6 karaktera i maksimalno 12 karaktera!): ")
    confirm_password = input("Potvrdite lozinku: ")
    print("\n")
    
    if (confirm_password == password and len(confirm_password) in range (6, 13) and len(username) in range(6, 13)):
        enc = confirm_password.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        
        Qk = "INSERT INTO Prodavac (ime, prezime, user, passwd, plata) VALUES (%s,%s,%s,%s,%s)"
        mycursor.execute(Qk, (ime_prodavca, prezime_prodavca, username, hash1, plata_prodavca,))
        db.commit()
        print("Uspesno ste napravili nalog!")
        print("\n")
    else:
        print("\n")
        print("Korisnicko ime/lozinka imaju vise od 6 ili manje od 12 karaktera, ili se lozinke ne podudaraju! \n")
        print("\n")
        
def loginProdavca():
    username = input("Unesite korisnicko ime: ")
    password = input("Unesite lozinku: ")
    
    pwd = password.encode()
    pwd_hash = hashlib.md5(pwd).hexdigest()
    Qpwd = "SELECT * FROM Prodavac WHERE user = %s AND passwd = %s"
    mycursor.execute(Qpwd, (username, pwd_hash,))
    nalog = mycursor.fetchone()
    if nalog:
        print("\n")
        print("Uspesno ste se ulogovali!")
        print("\n")
        return username
    else:
        print("\n")
        print("Desila se greska! Pokusajte ponovo!")
        print("\n")
        
def unosProizvoda():
    naziv = input("Unesite naziv proizvoda koji zelite da dodate: ")
    cena = eval(input("Unesite cenu proizvoda: "))
    na_lageru = eval(input("Unesite kolicinu proizvoda koji unosite u sistem: "))
    Qp = "INSERT INTO Proizvod (naziv, cena, popust, brojProdatih) VALUES(%s,%s,%s,%s)"
    while 1:
        try:
            mycursor.execute(Qp, (naziv, cena, 0, 0))
            db.commit()
            break
        except:
            print("Desila se greska! Vodite racuna da unesete naziv, kolicinu proizvoda na lageru i cenu u validnom formatu i pokusajte ponovo!")
            print("\n")
            break
    print("-----------------------------------------------------------------\n")
    print("Lista kategorija proizvoda i njihov identifikacioni brojevi: ")
    Qk = "SELECT * FROM Kategorija"
    mycursor.execute(Qk)
    for x in mycursor:
        print(x)
    kategorije = []
    broj = None
    while 1:
        broj = input("Unesite sve id brojeve kategorija kojima vas proizvod pripada (Ukucajte 0 za kraj!): ")
        if (broj != '0'):
            try:
                kategorije.append(int(broj))
            except:
                print(broj + " nije broj. Pokusajte ponovo!")
        else:
            if len(kategorije) > 0:
                break
            else:
                print("\n")
                print("Morate uneti bar jednu kategoriju!")
                continue
    Qfetch = "SELECT idProizvoda FROM Proizvod ORDER BY idProizvoda DESC LIMIT 1"
    mycursor.execute(Qfetch)
    poslednji_id = mycursor.fetchone()
    Qpk = "INSERT INTO ProizvodKategorija (idProizvoda, idKategorije, na_lageru) VALUES (%s,%s,%s)"
    for value in kategorije:
        mycursor.execute(Qpk, (poslednji_id[0], value, na_lageru))
        db.commit()
    print("\n")
    print("Uspesno ste uneli proizvod!")
    print("\n")
        
def dopunaKolicine():
    idbroj = input("Unesite id broj proizvoda u prodavnici za koji zelite uradite dopunu: ")
    kolicina = eval(input("Unesite za koliko zelite da dopunite proizvod: "))
    Q1 = "UPDATE ProizvodKategorija SET na_lageru = na_lageru + %s WHERE idProizvoda = %s"
    try:
        mycursor.execute(Q1, (kolicina, idbroj))
        db.commit()
        print("\n")
        print("Uspesno ste dopunili kolicinu proizvoda na lageru!")
        print("\n")
    except:
        print("\n")
        print("Desila se greska! Pokusajte ponovo sa unosom.")
        print("\n")
    
def promenaCene():
    naziv_proizvoda = input("Unesite tacno ime proizvoda ciju cenu zelite da promenite: ")
    Qp = "SELECT naziv FROM Proizvod WHERE naziv = %s"
    mycursor.execute(Qp, (naziv_proizvoda,))
    fetch = mycursor.fetchone()
    if fetch != None:
        nova_cena = input("Unesite novu cenu proizvoda: ")
        Qc = "UPDATE Proizvod SET cena = %s WHERE naziv = %s"
        try:
            mycursor.execute(Qc, (int(nova_cena), naziv_proizvoda,))
            db.commit()
            print("Cena " + naziv_proizvoda + " je uspesno promenjena!")
            print("\n")
        except:
            print("Doslo je do greske! Obratite paznju na format unete cene i pokusajte ponovo!")
            print("\n")
    else:
        print("Doslo je do greske! Obratite paznju na format unetog naziva proizvoda i pokusajte ponovo!")
        print("\n")

def dodavanjePopusta():
    proizvod = input("Unesite naziv proizvoda za koji zelite da unesete popust: ")
    Qp = "SELECT naziv FROM Proizvod WHERE naziv = %s"
    mycursor.execute(Qp, (proizvod,))
    fetch = mycursor.fetchone()
    if fetch != None:
        popust = input("Unesite popust u dinarima: ")
        Qpopust = "UPDATE Proizvod SET popust = %s WHERE naziv = %s"
        try:
            mycursor.execute(Qpopust, (int(popust), proizvod))
            db.commit()
            print("Popust je uspesno unet u sistem!")
            print("\n")
        except:
            print("Doslo je do greske! Obratite paznju na format unete cene i pokusajte ponovo!")
            print("\n")
    else:
        print("Doslo je do greske! Obratite paznju na format unetog naziva proizvoda i pokusajte ponovo!")
        print("\n")
        
def uklanjanjePopusta():
    proizvod = input("Unesite naziv proizvoda za koji zelite da uklonite popust: ")
    Qpopust = "UPDATE Proizvod SET popust = %s WHERE naziv = %s"
    if proizvod != None:
        try:
            mycursor.execute(Qpopust, (0, proizvod))
            db.commit()
            print("Popust je uspesno uklonjen iz sistema!")
            print("\n")
        except:
            print("Doslo je do greske! Obratite paznju na format unete cene i pokusajte ponovo!")
            print("\n")
    else:
        print("Doslo je do greske! Obratite paznju na format unetog naziva proizvoda i pokusajte ponovo!")
        print("\n")