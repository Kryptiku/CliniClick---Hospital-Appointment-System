-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 14, 2023 at 02:00 PM
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
-- Table structure for table `appointmentrequeststbl`
--

CREATE TABLE `appointmentrequeststbl` (
  `apt_req_code` varchar(10) NOT NULL,
  `patient_code` varchar(10) DEFAULT NULL,
  `doctor_code` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `appointmentstbl`
--

CREATE TABLE `appointmentstbl` (
  `apt_req_code` varchar(10) NOT NULL,
  `patient_code` varchar(10) NOT NULL,
  `doctor_code` varchar(10) NOT NULL,
  `apt_date` date DEFAULT NULL,
  `apt_time` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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

-- --------------------------------------------------------

--
-- Table structure for table `medstbl`
--

CREATE TABLE `medstbl` (
  `meds_code` varchar(10) NOT NULL,
  `meds_name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `patienthistorytbl`
--

CREATE TABLE `patienthistorytbl` (
  `patient_history_code` varchar(10) NOT NULL,
  `patient_code` varchar(10) DEFAULT NULL,
  `doctor_code` varchar(10) DEFAULT NULL,
  `diagnosis` varchar(25) DEFAULT NULL,
  `meds_code` varchar(10) DEFAULT NULL,
  `diagnosis_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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

-- --------------------------------------------------------

--
-- Table structure for table `prescriptiontbl`
--

CREATE TABLE `prescriptiontbl` (
  `meds_code` varchar(10) NOT NULL,
  `patient_code` varchar(10) NOT NULL,
  `dosage` varchar(10) DEFAULT NULL,
  `frequency` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
-- Indexes for table `appointmentstbl`
--
ALTER TABLE `appointmentstbl`
  ADD PRIMARY KEY (`apt_req_code`,`patient_code`,`doctor_code`),
  ADD KEY `patient_code` (`patient_code`),
  ADD KEY `doctor_code` (`doctor_code`);

--
-- Indexes for table `doctortbl`
--
ALTER TABLE `doctortbl`
  ADD PRIMARY KEY (`doctor_code`);

--
-- Indexes for table `medstbl`
--
ALTER TABLE `medstbl`
  ADD PRIMARY KEY (`meds_code`);

--
-- Indexes for table `patienthistorytbl`
--
ALTER TABLE `patienthistorytbl`
  ADD PRIMARY KEY (`patient_history_code`),
  ADD KEY `patient_code` (`patient_code`),
  ADD KEY `meds_code` (`meds_code`);

--
-- Indexes for table `patienttbl`
--
ALTER TABLE `patienttbl`
  ADD PRIMARY KEY (`patient_code`);

--
-- Indexes for table `prescriptiontbl`
--
ALTER TABLE `prescriptiontbl`
  ADD PRIMARY KEY (`meds_code`,`patient_code`),
  ADD KEY `patient_code` (`patient_code`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appointmentrequeststbl`
--
ALTER TABLE `appointmentrequeststbl`
  ADD CONSTRAINT `appointmentrequeststbl_ibfk_1` FOREIGN KEY (`patient_code`) REFERENCES `patienttbl` (`patient_code`),
  ADD CONSTRAINT `appointmentrequeststbl_ibfk_2` FOREIGN KEY (`doctor_code`) REFERENCES `doctortbl` (`doctor_code`);

--
-- Constraints for table `appointmentstbl`
--
ALTER TABLE `appointmentstbl`
  ADD CONSTRAINT `appointmentstbl_ibfk_1` FOREIGN KEY (`apt_req_code`) REFERENCES `appointmentrequeststbl` (`apt_req_code`),
  ADD CONSTRAINT `appointmentstbl_ibfk_2` FOREIGN KEY (`patient_code`) REFERENCES `patienttbl` (`patient_code`),
  ADD CONSTRAINT `appointmentstbl_ibfk_3` FOREIGN KEY (`doctor_code`) REFERENCES `doctortbl` (`doctor_code`);

--
-- Constraints for table `patienthistorytbl`
--
ALTER TABLE `patienthistorytbl`
  ADD CONSTRAINT `patienthistorytbl_ibfk_1` FOREIGN KEY (`patient_code`) REFERENCES `patienttbl` (`patient_code`),
  ADD CONSTRAINT `patienthistorytbl_ibfk_2` FOREIGN KEY (`meds_code`) REFERENCES `prescriptiontbl` (`meds_code`);

--
-- Constraints for table `prescriptiontbl`
--
ALTER TABLE `prescriptiontbl`
  ADD CONSTRAINT `prescriptiontbl_ibfk_1` FOREIGN KEY (`meds_code`) REFERENCES `medstbl` (`meds_code`),
  ADD CONSTRAINT `prescriptiontbl_ibfk_2` FOREIGN KEY (`patient_code`) REFERENCES `patienttbl` (`patient_code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
