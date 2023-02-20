CREATE DATABASE  IF NOT EXISTS `character_project_schema` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `character_project_schema`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: character_project_schema
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
-- Table structure for table `characters`
--

DROP TABLE IF EXISTS `characters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `characters` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `race` varchar(255) DEFAULT NULL,
  `classname` varchar(255) DEFAULT NULL,
  `level` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_characters_users_idx` (`user_id`),
  CONSTRAINT `fk_characters_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `characters`
--

LOCK TABLES `characters` WRITE;
/*!40000 ALTER TABLE `characters` DISABLE KEYS */;
INSERT INTO `characters` VALUES (1,'Duke','Changeling','Bard',7,'2023-02-14 17:35:36','2023-02-19 19:36:40',1),(2,'Conan','Human','Barbarian',10,'2023-02-14 18:21:34','2023-02-18 23:21:08',1),(4,'Bertha','Half-Elf','Paladin',6,'2023-02-14 18:23:30','2023-02-14 18:23:30',2),(8,'Drizzt','Dark Elf','Hunter',20,'2023-02-19 19:38:58','2023-02-19 19:38:58',4),(9,'Gandalf','Elf','Wizard',20,'2023-02-19 19:40:38','2023-02-19 19:40:38',5),(10,'Gimli','Dwarf','Fighter',15,'2023-02-19 19:47:16','2023-02-19 19:47:16',5);
/*!40000 ALTER TABLE `characters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Matthew','Hensley','m@h.com','$2b$12$a7Cqglfw2yI2almfKPQ.4.TM6ChPf7HGQsyxon1DTFJsLnYcSTZ2W','2023-02-14 16:45:12','2023-02-14 16:45:12'),(2,'Test','User','t@u.com','$2b$12$gvksh3mszLZg17/MYsudm.NunlDCxv1dlgumTYWI9ZNNod2wgRUQu','2023-02-14 18:22:54','2023-02-14 18:22:54'),(3,'newguy','guynew','n@g.com','$2b$12$1eMLDtn1pUKm29.kwO/vReYdsOt1pqTDw2AkAqmRV4YI1tAFVTtQS','2023-02-16 16:06:59','2023-02-16 16:06:59'),(4,'Test','Person','t@p.com','$2b$12$M108HMA73Yk7gbO2tuBr6ORjFLH42yuSQxoi9ysEuAJmELo846YlS','2023-02-19 19:38:23','2023-02-19 19:38:23'),(5,'Tom','Foolery','t@f.com','$2b$12$qcYhIYq4Y2U46IpzbVXIO.AuFzKaaNkfI.21p8a2hOEK5VGzJAbIu','2023-02-19 19:40:14','2023-02-19 19:40:14');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-20 17:45:37