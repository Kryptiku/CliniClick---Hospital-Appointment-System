-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 18, 2023 at 04:08 PM
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
-- Table structure for table `appointmentrequeststbl`
--

CREATE TABLE `appointmentrequeststbl` (
  `apt_req_code` varchar(10) NOT NULL,
  `patient_code` varchar(10) DEFAULT NULL,
  `doctor_code` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appointmentrequeststbl`
--

INSERT INTO `appointmentrequeststbl` (`apt_req_code`, `patient_code`, `doctor_code`) VALUES
('', NULL, NULL),
('AR00000001', 'PA00000001', 'DO00000009'),
('AR00000002', 'PA00000006', 'DO00000006'),
('AR00000003', 'PA00000007', 'DO00000008'),
('AR00000004', 'PA00000004', 'DO00000001'),
('AR00000005', 'PA00000003', 'DO00000009');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointmentrequeststbl`
--
ALTER TABLE `appointmentrequeststbl`
  ADD PRIMARY KEY (`apt_req_code`),
  ADD KEY `patient_code` (`patient_code`),
  ADD KEY `doctor_code` (`doctor_code`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appointmentrequeststbl`
--
ALTER TABLE `appointmentrequeststbl`
  ADD CONSTRAINT `appointmentrequeststbl_ibfk_1` FOREIGN KEY (`patient_code`) REFERENCES `patienttbl` (`patient_code`),
  ADD CONSTRAINT `appointmentrequeststbl_ibfk_2` FOREIGN KEY (`doctor_code`) REFERENCES `doctortbl` (`doctor_code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
