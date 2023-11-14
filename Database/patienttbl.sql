-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 14, 2023 at 03:29 PM
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
-- Database: `cliniclick_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `patienttbl`
--

CREATE TABLE `patienttbl` (
  `patient_code` varchar(10) NOT NULL,
  `patient_lastname` varchar(20) DEFAULT NULL,
  `patient_firstname` varchar(20) DEFAULT NULL,
  `patient_middlename` varchar(20) DEFAULT NULL,
  `patient_birthdate` date DEFAULT NULL,
  `patient_sex` varchar(10) DEFAULT NULL,
  `patient_contactnum` varchar(14) DEFAULT NULL,
  `patient_address` varchar(50) DEFAULT NULL,
  `patient_username` varchar(15) DEFAULT NULL,
  `patient_password` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patienttbl`
--

INSERT INTO `patienttbl` (`patient_code`, `patient_lastname`, `patient_firstname`, `patient_middlename`, `patient_birthdate`, `patient_sex`, `patient_contactnum`, `patient_address`, `patient_username`, `patient_password`) VALUES
('PA00000001', 'Acoba', 'Liza', 'Chavez', '1986-06-10', 'F', '09837194281', '130 Kalayaan Ave, Quezon City, Metro Manila', 'User1', 'Pass1'),
('PA00000002', 'Santos', 'Amelia', 'Theresa', '1986-07-21', 'F', '0941 700 8127', '412 Quirino Highway, Barangay Novaliches, Quezon C', 'User2', 'Pass2'),
('PA00000003', 'Gonzales', 'Sofia', 'Isadora', '1967-12-25', 'F', '0917 498 6216', '892 V. Mapa Street, Barangay Santa Mesa, Manila', 'User3', 'Pass3'),
('PA00000004', ' Rivera', 'Gabriela', ' Maria ', '1959-05-30', 'F', '0923 831 2894', '196 A. Bonifacio Street, Barangay San Juan, Quezon', 'User4', 'Pass4'),
('PA00000005', 'Santos', 'Lorenzo', 'Carlos', '1988-02-10', 'M', '0996 812 7781', '468 Mabini Avenue, Barangay Poblacion, Makati City', 'User5', 'Pass5'),
('PA00000006', 'Santos', 'Enrique', 'Javier', '1969-04-01', 'M', '0999 961 4711', '518 Rizal Street, Barangay Malate, Manila', 'User6', 'Pass6'),
('PA00000007', 'Cruz', 'Andres', 'Miguel', '1959-08-31', 'M', '0931 892 2291', '101 Magallanes Street, Barangay Bata, Bacolod City', 'User7', 'Pass7'),
('PA00000008', 'Hernandez', 'Beatriz', 'Isabel ', '1947-01-17', 'F', '0993 812 0825', '234 Taft Avenue, Barangay Ermita, Cebu City', 'User8', 'Pass8'),
('PA00000009', 'Salazar', 'Elena', 'Gabriela', '1975-07-23', 'F', '0941 923 8131', '576 Roxas Boulevard, Barangay Baclaran, Parañaque ', 'User9', 'Pass9'),
('PA00000010', 'Reyes', 'Pedro', 'Luis', '1969-11-13', 'M', '0917 812 8423', '890 Lacson Street, Barangay Santa Cruz, Manila', 'User10', 'Pass10');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `patienttbl`
--
ALTER TABLE `patienttbl`
  ADD PRIMARY KEY (`patient_code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
