-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 14, 2023 at 02:39 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cliniclick_hospital_appointment_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `doctortbl`
--

CREATE TABLE `doctortbl` (
  `doctor_code` varchar(10) NOT NULL,
  `doctor_lastname` varchar(20) DEFAULT NULL,
  `doctor_firstname` varchar(20) DEFAULT NULL,
  `doctor_middlename` varchar(20) DEFAULT NULL,
  `doctor_specialty` varchar(20) DEFAULT NULL,
  `doctor_sex` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctortbl`
--

INSERT INTO `doctortbl` (`doctor_code`, `doctor_lastname`, `doctor_firstname`, `doctor_middlename`, `doctor_specialty`, `doctor_sex`) VALUES
('DO00000001', 'Miranda', 'Mark James', 'Salva', 'Neurology', 'M'),
('DO00000002', 'Anderson', 'Olivia Grace', 'Santos', 'Orthopedics', 'F'),
('DO00000003', 'Patel', 'Ethan Michael', 'Reyes', 'Urology', 'M'),
('DO00000004', 'Mitchell', 'Ava Marie', 'Cruz', 'Pathology', 'F'),
('DO00000005', 'Williams', 'Noah', 'Alexander', 'Otolaryngology', 'M'),
('DO00000006', 'Rodriguez', 'Zoe Elizabeth', 'Aquino', 'Pediatrics', 'F'),
('DO00000007', 'Chen', 'Liam Christoph', 'Ramos', 'Gastroenterology', 'M'),
('DO00000008', 'Davis', 'Sophia Anne', 'Gonzales', 'Oncology', 'F'),
('DO00000009', 'Martinez', ' Lucas', 'Jameson', 'Cardiology', 'M'),
('DO00000010', 'Herrera', 'Isabella Rose', 'Torres', 'Pulmonology', 'F');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `doctortbl`
--
ALTER TABLE `doctortbl`
  ADD PRIMARY KEY (`doctor_code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
