# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 20:41:43 2022

@author: Bagzi
"""

import mysql.connector
import kupac
import prodavac
import korisnici

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="mydatabase"
    )

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")

#mycursor.execute("CREATE TABLE Prodavac (idProdavca int PRIMARY KEY AUTO_INCREMENT, ime VARCHAR(50), prezime VARCHAR(50), user VARCHAR(50), passwd VARCHAR(50), plata int NOT NULL)")
#mycursor.execute("CREATE TABLE Kupac (idKupca int PRIMARY KEY AUTO_INCREMENT, imeKupca VARCHAR(50), prezimeKupca VARCHAR(50), userKupca VARCHAR(50), passwdKupca VARCHAR(255), kupon int NOT NULL)")
#mycursor.execute("CREATE TABLE Proizvod (idProizvoda int PRIMARY KEY AUTO_INCREMENT, naziv VARCHAR(50), cena int NOT NULL, popust int NOT NULL, brojProdatih int NOT NULL)")
#mycursor.execute("CREATE TABLE Kategorija (idKategorije int PRIMARY KEY AUTO_INCREMENT, nazivKategorije VARCHAR(50))")
#mycursor.execute("CREATE TABLE ProizvodKategorija (idProizvoda int, idKategorije int, na_lageru int)")
#Q1 = "SELECT p.* FROM Proizvod p INNER JOIN ProizvodKategorija pk ON p.idProizvoda = pk.idProizvoda WHERE p.cena = @cena AND pk.idKategorije in (@Kategorija)"
#mycursor.execute(Q1)

#kategorije = ['PS4 igra', 'PS5 Igra', 'Xbox One Igra', 'Xbox Series X Igra', 'Switch Igra', 'PC Igra', 'PS4 Konzola', 'PS5 Konzola', 'Xbox One Konzola', 'Xbox Series X Konzola', 'Switch Konzola']
#for x in kategorije:
    #Q2 = "INSERT INTO Kategorija (nazivKategorije) VALUES (%s)"
    #mycursor.execute(Q2, (x,))
#db.commit()

print("Dobrodosli u prodavnicu ASCII!")
korisnici.grafikon()
username = None
while 1:
    print("Unesite 1 za pristup prodavnici kao kupac...")
    print("Unesite 2 za administrativni pristup...")
    korisnik = eval(input("Unesite vas izbor: "))
    print("\n")
    if (korisnik == 1):
        print("Uz specijalnu akciju, za svakih potrosenih 7000 dinara dobijate popust u iznosu od 500 dinara na sledecu kupovinu! SAMO UKOLIKO STE ULOGOVANI U KORISNICKI NALOG!")
        print("\n")
        while 1:
            print("********* Login System Kupca *********")
            print("Unesite 1 da napravite nalog...")
            print("Unesite 2 da se ulogujete u postojeci nalog...")
            print("Unesite 3 da izadjete iz login sistema i nastavite sa kupovinom bez korisnickog naloga...")
            login = eval(input("Unesite vas izbor: "))
            print("\n")
            if login == 1:
                kupac.signupKupca()
                continue
            elif login == 2:
                username = kupac.loginKupca()
            elif login == 3:
                break
            else:
                print("Pogresno ste uneli broj! Pokusajte ponovo.")
                print("\n")
                continue
        while 1:
            print("********* Pretraga proizvoda *********")
            print("Unesite 1 za prikaz svih proizvoda...")
            print("Unesite 2 za pretragu proizvoda po kategorijama...")
            print("Unesite 3 za pretragu specificnog proizvoda...")
            pretraga = eval(input("Unesite vas izbor: "))
            print("\n")
            if pretraga == 1:
                korisnici.pretragaSvihProizvoda()
            elif pretraga == 2:
                kupac.pretragaProizvodaPoKategorijama()
            elif pretraga == 3:
                kupac.pretragaSpecificnogProizvoda()
            else:
                print("Pogresno ste uneli broj! Pokusajte ponovo.")
                print("\n")
                continue
            while 1:
                print("********* Kupovina proizvoda *********")
                print("Unesite 1 za kupovinu proizvoda...")
                print("Unesite 2 za povratak na pretragu proizvoda...")
                kupovina = eval(input("Unesite vas izbor: "))
                print("\n")
                if kupovina == 1:
                    racun = kupac.kupovinaProizvoda()
                    if username is not None:
                        try:
                            Qkupon = "SELECT kupon FROM Kupac WHERE userKupca = %s"
                            mycursor.execute(Qkupon, (username,))
                            kupon = mycursor.fetchone()
                            racun = racun - kupon
                            adresa = input("Unesite adresu i broj za isporuku proizvoda: ")
                            print("Vas racun iznosi", racun, "dinara. Proizvod ce biti isporucen na adresu", adresa,".")
                            print("\n")
                            Qkupon2 = "UPDATE Kupac SET kupon = %s WHERE userKupca = %s"
                            mycursor.execute(Qkupon2, (0, username))
                            db.commit()
                            if racun >= 7000:
                                koeficijent = int(racun / 7000)
                                popust = koeficijent * 500
                                Qp = "UPDATE Kupac SET kupon = %s WHERE userKupca = %s"
                                mycursor.execute(Qp, (popust, username))
                                db.commit()
                                print("Uz vasu kupovinu ste dobili", popust, "dinara popusta na vasu sledecu kupovinu!")
                                print("\n")
                        except:
                            continue
                    else:
                        adresa = input("Unesite adresu i broj za isporuku proizvoda: ")
                        print("Vas racun iznosi", racun, "dinara. Proizvod ce biti isporucen na adresu", adresa,".")
                        print("\n")
                elif kupovina == 2:
                    break
                else:
                    print("\n")
                    print("Pogresno ste uneli broj! Pokusajte ponovo.")
                    print("\n")
                    continue
    
    elif (korisnik == 2):
        pristup = input("Unesite administrativnu sifru: ")
        print("\n")
        if (pristup == 'admin'):
            while 1:
                print("********* Login System Prodavca *********")
                print("Unesite 1 da napravite novi nalog...")
                print("Unesite 2 da se ulogujete u postojeci nalog...")
                print("Unesite bilo koji karakter da izadjete iz login sistema...")
                ch = input("Unesite vas izbor: ")
                print("\n")
                if ch == '1':
                    prodavac.signupProdavca()
                elif ch == '2':
                    user = prodavac.loginProdavca()
                    if user is not None:
                        while 1:
                            print("********* Administrativne funkcije *********")
                            print("Unesite 1 za prikaz svih proizvoda u prodavnici...")
                            print("Unesite 2 za unos novog proizvoda...")
                            print("Unesite 3 za dopunu kolicine odredjenog proizvoda u prodavnici...")
                            print("Unesite 4 za promenu cene postojeceg proizvoda...")
                            print("Unesite 5 za dodavanje popusta na proizvod...")
                            print("Unesite 6 za uklanjanje popusta sa proizvoda...")
                            print("Unesite 7 da izadjete iz menija administrativnih funkcija...")
                            admin = eval(input("Unesite vas izbor: "))
                            print("\n")
                            if admin == 1:
                                korisnici.pretragaSvihProizvoda()
                            elif admin == 2:
                                prodavac.unosProizvoda()
                            elif admin == 3:
                                prodavac.dopunaKolicine()
                            elif admin == 4:
                                prodavac.promenaCene()
                            elif admin == 5:
                                prodavac.dodavanjePopusta()
                            elif admin == 6:
                                prodavac.uklanjanjePopusta()
                            elif admin == 7:
                                break
                            else:
                                print("\n")
                                print("Pogresno ste uneli broj! Pokusajte ponovo.")
                                print("\n")
                else:
                    break
        else:
            print("\n")
            print("Pogresna sifra! Pokusajte ponovo.")
            print("\n")
            continue
        
    else:
        print("Pogresno ste uneli broj! Pokusajte ponovo.")
        print("\n")
        continue