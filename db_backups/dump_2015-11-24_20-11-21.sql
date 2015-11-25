-- MySQL dump 10.13  Distrib 5.6.25, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: rpg
-- ------------------------------------------------------
-- Server version	5.6.25-0ubuntu0.15.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cityknowledge`
--

LOCK TABLES `cityknowledge` WRITE;
/*!40000 ALTER TABLE `cityknowledge` DISABLE KEYS */;
/*!40000 ALTER TABLE `cityknowledge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `continent`
--

LOCK TABLES `continent` WRITE;
/*!40000 ALTER TABLE `continent` DISABLE KEYS */;
/*!40000 ALTER TABLE `continent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `creature`
--

LOCK TABLES `creature` WRITE;
/*!40000 ALTER TABLE `creature` DISABLE KEYS */;
/*!40000 ALTER TABLE `creature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `creatureingredient`
--

LOCK TABLES `creatureingredient` WRITE;
/*!40000 ALTER TABLE `creatureingredient` DISABLE KEYS */;
/*!40000 ALTER TABLE `creatureingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `creatureitem`
--

LOCK TABLES `creatureitem` WRITE;
/*!40000 ALTER TABLE `creatureitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `creatureitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `creatureknowledge`
--

LOCK TABLES `creatureknowledge` WRITE;
/*!40000 ALTER TABLE `creatureknowledge` DISABLE KEYS */;
/*!40000 ALTER TABLE `creatureknowledge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `creaturestat`
--

LOCK TABLES `creaturestat` WRITE;
/*!40000 ALTER TABLE `creaturestat` DISABLE KEYS */;
/*!40000 ALTER TABLE `creaturestat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ingredient`
--

LOCK TABLES `ingredient` WRITE;
/*!40000 ALTER TABLE `ingredient` DISABLE KEYS */;
/*!40000 ALTER TABLE `ingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ingredientknowledge`
--

LOCK TABLES `ingredientknowledge` WRITE;
/*!40000 ALTER TABLE `ingredientknowledge` DISABLE KEYS */;
/*!40000 ALTER TABLE `ingredientknowledge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `ingredientstat`
--

LOCK TABLES `ingredientstat` WRITE;
/*!40000 ALTER TABLE `ingredientstat` DISABLE KEYS */;
/*!40000 ALTER TABLE `ingredientstat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `itemingredient`
--

LOCK TABLES `itemingredient` WRITE;
/*!40000 ALTER TABLE `itemingredient` DISABLE KEYS */;
/*!40000 ALTER TABLE `itemingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `itemknowledge`
--

LOCK TABLES `itemknowledge` WRITE;
/*!40000 ALTER TABLE `itemknowledge` DISABLE KEYS */;
/*!40000 ALTER TABLE `itemknowledge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `itemstat`
--

LOCK TABLES `itemstat` WRITE;
/*!40000 ALTER TABLE `itemstat` DISABLE KEYS */;
/*!40000 ALTER TABLE `itemstat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `itemsubtype`
--

LOCK TABLES `itemsubtype` WRITE;
/*!40000 ALTER TABLE `itemsubtype` DISABLE KEYS */;
/*!40000 ALTER TABLE `itemsubtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `itemtype`
--

LOCK TABLES `itemtype` WRITE;
/*!40000 ALTER TABLE `itemtype` DISABLE KEYS */;
/*!40000 ALTER TABLE `itemtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `knowledge`
--

LOCK TABLES `knowledge` WRITE;
/*!40000 ALTER TABLE `knowledge` DISABLE KEYS */;
/*!40000 ALTER TABLE `knowledge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `legend`
--

LOCK TABLES `legend` WRITE;
/*!40000 ALTER TABLE `legend` DISABLE KEYS */;
/*!40000 ALTER TABLE `legend` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `legendknowledge`
--

LOCK TABLES `legendknowledge` WRITE;
/*!40000 ALTER TABLE `legendknowledge` DISABLE KEYS */;
/*!40000 ALTER TABLE `legendknowledge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `magic`
--

LOCK TABLES `magic` WRITE;
/*!40000 ALTER TABLE `magic` DISABLE KEYS */;
/*!40000 ALTER TABLE `magic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `magicknowledge`
--

LOCK TABLES `magicknowledge` WRITE;
/*!40000 ALTER TABLE `magicknowledge` DISABLE KEYS */;
/*!40000 ALTER TABLE `magicknowledge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `personitem`
--

LOCK TABLES `personitem` WRITE;
/*!40000 ALTER TABLE `personitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `personitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `personmagic`
--

LOCK TABLES `personmagic` WRITE;
/*!40000 ALTER TABLE `personmagic` DISABLE KEYS */;
/*!40000 ALTER TABLE `personmagic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `personstat`
--

LOCK TABLES `personstat` WRITE;
/*!40000 ALTER TABLE `personstat` DISABLE KEYS */;
/*!40000 ALTER TABLE `personstat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `place`
--

LOCK TABLES `place` WRITE;
/*!40000 ALTER TABLE `place` DISABLE KEYS */;
/*!40000 ALTER TABLE `place` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `placeitem`
--

LOCK TABLES `placeitem` WRITE;
/*!40000 ALTER TABLE `placeitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `placeitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `placeknowledge`
--

LOCK TABLES `placeknowledge` WRITE;
/*!40000 ALTER TABLE `placeknowledge` DISABLE KEYS */;
/*!40000 ALTER TABLE `placeknowledge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `region`
--

LOCK TABLES `region` WRITE;
/*!40000 ALTER TABLE `region` DISABLE KEYS */;
/*!40000 ALTER TABLE `region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `regioncreature`
--

LOCK TABLES `regioncreature` WRITE;
/*!40000 ALTER TABLE `regioncreature` DISABLE KEYS */;
/*!40000 ALTER TABLE `regioncreature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `regionknowledge`
--

LOCK TABLES `regionknowledge` WRITE;
/*!40000 ALTER TABLE `regionknowledge` DISABLE KEYS */;
/*!40000 ALTER TABLE `regionknowledge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `regionvegetation`
--

LOCK TABLES `regionvegetation` WRITE;
/*!40000 ALTER TABLE `regionvegetation` DISABLE KEYS */;
/*!40000 ALTER TABLE `regionvegetation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `spell`
--

LOCK TABLES `spell` WRITE;
/*!40000 ALTER TABLE `spell` DISABLE KEYS */;
/*!40000 ALTER TABLE `spell` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `spellstat`
--

LOCK TABLES `spellstat` WRITE;
/*!40000 ALTER TABLE `spellstat` DISABLE KEYS */;
/*!40000 ALTER TABLE `spellstat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `stat`
--

LOCK TABLES `stat` WRITE;
/*!40000 ALTER TABLE `stat` DISABLE KEYS */;
/*!40000 ALTER TABLE `stat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `userknowledge`
--

LOCK TABLES `userknowledge` WRITE;
/*!40000 ALTER TABLE `userknowledge` DISABLE KEYS */;
/*!40000 ALTER TABLE `userknowledge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `vegetation`
--

LOCK TABLES `vegetation` WRITE;
/*!40000 ALTER TABLE `vegetation` DISABLE KEYS */;
/*!40000 ALTER TABLE `vegetation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `vegetationingredient`
--

LOCK TABLES `vegetationingredient` WRITE;
/*!40000 ALTER TABLE `vegetationingredient` DISABLE KEYS */;
/*!40000 ALTER TABLE `vegetationingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `vegetationknowledge`
--

LOCK TABLES `vegetationknowledge` WRITE;
/*!40000 ALTER TABLE `vegetationknowledge` DISABLE KEYS */;
/*!40000 ALTER TABLE `vegetationknowledge` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-24 20:38:21
