-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: mariadb
-- Generation Time: Mar 12, 2026 at 05:10 PM
-- Server version: 10.6.20-MariaDB-ubu2004
-- PHP Version: 8.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `game_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `games`
--

CREATE TABLE `games` (
  `game_pk` char(32) NOT NULL,
  `game_title` varchar(155) NOT NULL,
  `game_platform` varchar(155) NOT NULL,
  `game_comment` varchar(255) NULL,
  UNIQUE KEY `game_title` (`game_title`),
  'game_image' varchar(255) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_pk` char(32) NOT NULL,
  `user_first_name` varchar(20) NOT NULL,
  `user_last_name` varchar(155) NOT NULL,
  `user_email` varchar(155) NOT NULL,
  `user_password` varchar(255) NOT NULL,
  `user_created_at` bigint(20) NOT NULL
  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_pk`, `user_first_name`, `user_last_name`, `user_email`, `user_password`, `user_created_at`) VALUES
('25b6a7ddc86e4f02b456083b477d974c', '123', 'aaa', 'sophia.anina@gmail.com', 'scrypt:32768:8:1$0AJUEWxfSrdxO23r$7b2dadb5543d18e88b565e041d864e4675c488f2232f05fcbd1a3a69f300bc4db5b13ce87e896064ba6c31e41dd44656cd86f71bd0c29edcbbfd508860854c4f', 1772754352),
('b4c6da57022d4f89a42dad31df70666b', 'Sophia', 'Kingston', 'sophia.anina@gmail.com', 'scrypt:32768:8:1$Ku15H2fl3DeVKg5Y$60f62c3b7c11fd094bffe50889d54d72b47d130ffdecca889110434cd4edf38faa0467284e51d71f46c32c061d4f5ee889e2aec9704b527e08176e40fc676c6c', 1773240157),
('cb68a4200134442aaed310847bb57444', 'Markus', 'Pedersen', 'markuszpedersen@gmail.com', 'scrypt:32768:8:1$TT7yRsw8zKeDI7Sj$93c6a1198bb06e4748901dd782915e30f5c01db50300c39354eb883bf409239182135551f2581cd11a14a34a7ec7de7daeffaae2ced2eb47706b0fc750719cfb', 1773240412);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
