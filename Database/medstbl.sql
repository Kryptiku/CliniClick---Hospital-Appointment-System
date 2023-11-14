-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 14, 2023 at 02:48 PM
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
-- Table structure for table `medstbl`
--

CREATE TABLE `medstbl` (
  `meds_code` varchar(10) NOT NULL,
  `meds_name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `medstbl`
--

INSERT INTO `medstbl` (`meds_code`, `meds_name`) VALUES
('MD00000001', 'Mediflexin'),
('MD00000002', 'Healzitol'),
('MD00000003', 'Vitaloxin'),
('MD00000004', 'Curevance'),
('MD00000005', 'Relievox'),
('MD00000006', 'Revitamed'),
('MD00000007', 'Tranquilix'),
('MD00000008', 'Painfreeza'),
('MD00000009', 'Energixar'),
('MD00000010', 'Serenitol');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `medstbl`
--
ALTER TABLE `medstbl`
  ADD PRIMARY KEY (`meds_code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
