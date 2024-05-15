CREATE DATABASE  IF NOT EXISTS `mydatabase` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mydatabase`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: mydatabase
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `kategorija`
--

DROP TABLE IF EXISTS `kategorija`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kategorija` (
  `idKategorije` int NOT NULL AUTO_INCREMENT,
  `nazivKategorije` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idKategorije`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kategorija`
--

LOCK TABLES `kategorija` WRITE;
/*!40000 ALTER TABLE `kategorija` DISABLE KEYS */;
INSERT INTO `kategorija` VALUES (1,'PS4 igra'),(2,'PS5 Igra'),(3,'Xbox One Igra'),(4,'Xbox Series X Igra'),(5,'Switch Igra'),(6,'PC Igra'),(7,'PS4 Konzola'),(8,'PS5 Konzola'),(9,'Xbox One Konzola'),(10,'Xbox Series X Konzola'),(11,'Switch Konzola');
/*!40000 ALTER TABLE `kategorija` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kupac`
--

DROP TABLE IF EXISTS `kupac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kupac` (
  `idKupca` int NOT NULL AUTO_INCREMENT,
  `imeKupca` varchar(50) DEFAULT NULL,
  `prezimeKupca` varchar(50) DEFAULT NULL,
  `userKupca` varchar(50) DEFAULT NULL,
  `passwdKupca` varchar(255) DEFAULT NULL,
  `kupon` int NOT NULL,
  PRIMARY KEY (`idKupca`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kupac`
--

LOCK TABLES `kupac` WRITE;
/*!40000 ALTER TABLE `kupac` DISABLE KEYS */;
INSERT INTO `kupac` VALUES (4,'Dejana','Mirkov','dejaki001','cfa7d92b922dbb4e8b1e8923f344552d',500),(6,'duda','dudic','bababaraba12','41d2d74050797ce4e55f8e193b85be75',0),(7,'Marko','Baba','marko123','8346c66834f77a8872d416e172d87de0',0);
/*!40000 ALTER TABLE `kupac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prodavac`
--

DROP TABLE IF EXISTS `prodavac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prodavac` (
  `idProdavca` int NOT NULL AUTO_INCREMENT,
  `ime` varchar(50) DEFAULT NULL,
  `prezime` varchar(50) DEFAULT NULL,
  `user` varchar(50) DEFAULT NULL,
  `passwd` varchar(50) DEFAULT NULL,
  `plata` int NOT NULL,
  PRIMARY KEY (`idProdavca`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prodavac`
--

LOCK TABLES `prodavac` WRITE;
/*!40000 ALTER TABLE `prodavac` DISABLE KEYS */;
INSERT INTO `prodavac` VALUES (10,'Ivana','Maric','ivana123','76cb47f0a703dc933346259343022623',52392),(11,'Zorica','Ilic','zoka222','af16327efd56fe9eb2ad608ab2d5a0b4',44909),(12,'Dejan','Julic','dejan123','fccbff9eecc7e8e4fe3ec6a2f0f27b21',33900),(13,'Dusan','Lalic','dusan007','e8a2e71dfc508f180cb9d2511ac209d0',40909);
/*!40000 ALTER TABLE `prodavac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proizvod`
--

DROP TABLE IF EXISTS `proizvod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proizvod` (
  `idProizvoda` int NOT NULL AUTO_INCREMENT,
  `naziv` varchar(50) DEFAULT NULL,
  `cena` int NOT NULL,
  `popust` int NOT NULL,
  `brojProdatih` int NOT NULL,
  PRIMARY KEY (`idProizvoda`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proizvod`
--

LOCK TABLES `proizvod` WRITE;
/*!40000 ALTER TABLE `proizvod` DISABLE KEYS */;
INSERT INTO `proizvod` VALUES (7,'Cyberpunk 2077',3990,0,0);
/*!40000 ALTER TABLE `proizvod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proizvodkategorija`
--

DROP TABLE IF EXISTS `proizvodkategorija`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proizvodkategorija` (
  `idProizvoda` int DEFAULT NULL,
  `idKategorije` int DEFAULT NULL,
  `na_lageru` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proizvodkategorija`
--

LOCK TABLES `proizvodkategorija` WRITE;
/*!40000 ALTER TABLE `proizvodkategorija` DISABLE KEYS */;
INSERT INTO `proizvodkategorija` VALUES (7,1,15),(7,2,15),(7,3,15),(7,4,15),(7,6,15);
/*!40000 ALTER TABLE `proizvodkategorija` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-04 18:13:05
