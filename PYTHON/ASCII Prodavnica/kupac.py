# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 19:23:46 2022

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

def signupKupca():
    print("*** Formular za kreiranje naloga kupca *** \n")
    ime_kupca = input("Unesite vase ime: ")
    prezime_kupca = input("Unesite vase prezime: ")
    
    username = input("Unesite zeljeno korisnicko ime (Minimum 6 karaktera i maksimalno 12 karaktera!): ")
    password = input("Unesite zeljenu lozinku (Minimum 6 karaktera i maksimalno 12 karaktera!): ")
    confirm_password = input("Potvrdite lozinku: ")
    print("\n")
    
    if (confirm_password == password and len(confirm_password) in range (6, 13) and len(username) in range(6, 13)):
        enc = confirm_password.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        
        Qk = "INSERT INTO Kupac (imeKupca, prezimeKupca, userKupca, passwdKupca, kupon) VALUES (%s,%s,%s,%s,%s)"
        mycursor.execute(Qk, (ime_kupca, prezime_kupca, username, hash1, 0,))
        db.commit()
        print("Uspesno ste napravili nalog!")
        print("\n")
    
    else:
        print("\n")
        print("Korisnicko ime/lozinka imaju vise od 6 ili manje od 12 karaktera, ili se lozinke ne podudaraju! \n")
        print("\n")
        
def loginKupca():
    username = input("Unesite korisnicko ime: ")
    password = input("Unesite lozinku: ")
    
    pwd = password.encode()
    pwd_hash = hashlib.md5(pwd).hexdigest()
    Qpwd = "SELECT * FROM Kupac WHERE userKupca = %s AND passwdKupca = %s"
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
      
def pretragaProizvodaPoKategorijama():
    print("Lista kategorija proizvoda i njihov identifikacioni brojevi: ")
    Qk = "SELECT * FROM Kategorija"
    mycursor.execute(Qk)
    for x in mycursor:
        print(x)
    kategorije = []
    broj = None
    while 1:
        broj = input("Unesite sve id brojeve kategorija za koje zelite da uradite pretragu proizvoda (Ukucajte 0 za kraj!): ")
        if (broj != '0'):
            try:
                kategorije.append(int(broj))
            except:
                print("\n")
                print(broj + " nije broj. Pokusajte ponovo!")
        else:
            if len(kategorije) > 0:
                break
            else:
                print("\n")
                print("Morate uneti bar jednu kategoriju!")
                continue
    if len(kategorije) > 1:
        kategorije_tuple = tuple(kategorije)
        Qfetch = "SELECT p.idProizvoda, p.naziv, p.cena, k.idKategorije, k.nazivKategorije, pk.na_lageru FROM Proizvod p, Kategorija k, ProizvodKategorija pk WHERE pk.idProizvoda = p.idProizvoda AND pk.idKategorije = k.idKategorije AND k.idKategorije IN {}".format(kategorije_tuple)
        mycursor.execute(Qfetch)
    else:
        kategorije_tuple = kategorije[0]
        Qfetch = "SELECT p.idProizvoda, p.naziv, p.cena, k.idKategorije, k.nazivKategorije, pk.na_lageru FROM Proizvod p, Kategorija k, ProizvodKategorija pk WHERE pk.idProizvoda = p.idProizvoda AND pk.idKategorije = k.idKategorije AND k.idKategorije = %s"
        mycursor.execute(Qfetch, (kategorije_tuple,))
    proizvodi = mycursor.fetchall()
    print("\n")
    print("Proizvodi koji se nalaze u kategorijama koje ste uneli (ID proizvoda, naziv proizvoda, cena, ID kategorije, naziv kategorije i kolicina proizvoda na lageru):\n")
    for x in proizvodi:
        print(x)
    print("\n")
        
def pretragaSpecificnogProizvoda():
    proizvod = input("Unesite tacno ime proizvoda koji zelite da pretrazite: ")
    print("\n")
    Qp = "SELECT naziv, cena FROM Proizvod WHERE naziv=%s"
    try:
        print("Proizvod koji ste uneli i njegova cena u dinarima: ")
        mycursor.execute(Qp, (proizvod,))
        pr = mycursor.fetchone()
        print(pr)
        print("\n")
        print("Kategorije proizvoda i njihovi identifikacioni brojevi: ")
        Qk = "SELECT * FROM Kategorija"
        mycursor.execute(Qk)
        for kat in mycursor:
            print(kat)
        print("\n")
        print("ID proizvoda koji ste uneli (prvi broj), id brojevi dostupnih kategorija za njega (drugi broj) i kolicina proizvoda na lageru (treci broj):")
        Qpk = "SELECT pk.idProizvoda, pk.idKategorije, pk.na_lageru FROM ProizvodKategorija pk, Proizvod p WHERE pk.idProizvoda = p.idProizvoda AND p.idProizvoda=%s"
        Qid = "SELECT idProizvoda FROM Proizvod WHERE naziv=%s"
        mycursor.execute(Qid, (proizvod,))
        id_p = mycursor.fetchone()[0]
        mycursor.execute(Qpk, (id_p,))
        for pk in mycursor:
            print(pk)
        print("\n")
    except:
        print("\n")
        print("Proizvod koji ste uneli ne postoji u prodavnici!")
        print("\n")

def kupovinaProizvoda():
    racun = 0
    while 1:
        proizvod = eval(input("Unesite ID proizvoda koji zelite da kupite: "))
        kategorija = eval(input("Unesite ID kategorije proizvoda: "))
        kolicina = eval(input("Unesite kolicinu zeljenog proizvoda: "))
        print("\n")
        try:
            Q1 = "SELECT pk.idProizvoda, pk.idKategorije, pk.na_lageru FROM ProizvodKategorija pk, Proizvod p, Kategorija k WHERE pk.idProizvoda = p.idProizvoda AND pk.idKategorije = k.idKategorije AND p.idProizvoda=%s AND k.idKategorije=%s"
            mycursor.execute(Q1, (proizvod, kategorija))
            kol = mycursor.fetchone()[2]
            if (kol - kolicina >= 0):
                nova_kolicina = kol - kolicina
                Q2 = "SELECT cena FROM Proizvod WHERE idProizvoda=%s"
                mycursor.execute(Q2, (proizvod,))
                cena_jednog = mycursor.fetchone()[0]
                Q3 = "SELECT popust FROM Proizvod WHERE idProizvoda=%s"
                mycursor.execute(Q3, (proizvod,))
                popust = mycursor.fetchone()[0]
                ukupna_cena = int(kolicina * (cena_jednog - popust))
                
                racun += ukupna_cena
                Q4 = "UPDATE ProizvodKategorija SET na_lageru=%s WHERE idProizvoda=%s AND idKategorije=%s"
                mycursor.execute(Q4, (nova_kolicina, proizvod, kategorija))
                db.commit()
                Q5 = "UPDATE Proizvod SET brojProdatih = brojProdatih + %s WHERE idProizvoda = %s"
                mycursor.execute(Q5, (kolicina, proizvod))
                db.commit()
                while 1:
                    print("Unesite 1 za dodavanje proizvoda u korpu...")
                    print("Unesite 2 za placanje...")
                    placanje = eval(input("Unesite vas izbor: "))
                    if placanje == 1:
                        break
                    elif placanje == 2:
                        return racun
                    else:
                        print("\n")
                        print("Pogresno ste uneli broj! Pokusajte ponovo.")
                        continue
            else:
                print("\n")
                print("Kolicina koju ste odabrali prelazi kolicinu proizvoda na lageru!")
                continue
        except:
            print("\n")
            print("Doslo je do greske! Pokusajte ponovo sa unosom proizvoda.")
            continue            