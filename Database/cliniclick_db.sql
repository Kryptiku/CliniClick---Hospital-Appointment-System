-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 21, 2023 at 07:29 AM
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
('AR00000001', 'PA00000001', 'DO00000009'),
('AR00000002', 'PA00000006', 'DO00000006'),
('AR00000003', 'PA00000007', 'DO00000008'),
('AR00000004', 'PA00000004', 'DO00000001'),
('AR00000005', 'PA00000003', 'DO00000009');

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

--
-- Dumping data for table `patienthistorytbl`
--

INSERT INTO `patienthistorytbl` (`patient_history_code`, `patient_code`, `doctor_code`, `diagnosis`, `meds_code`, `diagnosis_date`) VALUES
('PH00000001', 'PA00000006', 'DO00000002', 'Common Colds', 'MD00000001', '2023-11-21'),
('PH00000002', 'PA00000006', 'DO00000003', 'UTI', 'MD00000004', '2023-11-20');

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
('PA00000001', 'Acoba', 'Liza', 'Chavez', '1986-06-10', 'F', '0983 719 4281', '130 Kalayaan Ave, Quezon City, Metro Manila', 'User1', 'Pass1'),
('PA00000002', 'Santos', 'Amelia', 'Theresa', '1986-07-21', 'F', '0941 700 8127', '412 Quirino Highway, Barangay Novaliches, Quezon C', 'User2', 'Pass2'),
('PA00000003', 'Gonzales', 'Sofia', 'Isadora', '1967-12-25', 'F', '0917 498 6216', '892 V. Mapa Street, Barangay Santa Mesa, Manila', 'User3', 'Pass3'),
('PA00000004', ' Rivera', 'Gabriela', ' Maria ', '1959-05-30', 'F', '0923 831 2894', '196 A. Bonifacio Street, Barangay San Juan, Quezon', 'User4', 'Pass4'),
('PA00000005', 'Santos', 'Lorenzo', 'Carlos', '1988-02-10', 'M', '0996 812 7781', '468 Mabini Avenue, Barangay Poblacion, Makati City', 'User5', 'Pass5'),
('PA00000006', 'Santos', 'Enrique', 'Javier', '1969-04-01', 'M', '0999 961 4711', '518 Rizal Street, Barangay Malate, Manila', 'User6', 'Pass6'),
('PA00000007', 'Cruz', 'Andres', 'Miguel', '1959-08-31', 'M', '0931 892 2291', '101 Magallanes Street, Barangay Bata, Bacolod City', 'User7', 'Pass7'),
('PA00000008', 'Hernandez', 'Beatriz', 'Isabel ', '1947-01-17', 'F', '0993 812 0825', '234 Taft Avenue, Barangay Ermita, Cebu City', 'User8', 'Pass8'),
('PA00000009', 'Salazar', 'Elena', 'Gabriela', '1975-07-23', 'F', '0941 923 8131', '576 Roxas Boulevard, Barangay Baclaran, Parañaque ', 'User9', 'Pass9'),
('PA00000010', 'Reyes', 'Pedro', 'Luis', '1969-11-13', 'M', '0917 812 8423', '890 Lacson Street, Barangay Santa Cruz, Manila', 'User10', 'Pass10');

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
-- Dumping data for table `prescriptiontbl`
--

INSERT INTO `prescriptiontbl` (`meds_code`, `patient_code`, `dosage`, `frequency`) VALUES
('MD00000001', 'PA00000006', '250 mg', '3x a day'),
('MD00000004', 'PA00000005', '50 g', '2x a week');

-- --------------------------------------------------------

--
-- Table structure for table `stafftbl`
--

CREATE TABLE `stafftbl` (
  `staff_code` varchar(10) NOT NULL,
  `staff_lastname` varchar(20) DEFAULT NULL,
  `staff_firstname` varchar(20) DEFAULT NULL,
  `staff_middlename` varchar(20) DEFAULT NULL,
  `staff_username` varchar(15) DEFAULT NULL,
  `staff_password` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stafftbl`
--

INSERT INTO `stafftbl` (`staff_code`, `staff_lastname`, `staff_firstname`, `staff_middlename`, `staff_username`, `staff_password`) VALUES
('ST00000001', 'Dimayuga', 'Kristel', 'Rivera', 'staff1', 'staff1'),
('ST00000002', 'Mirabel', 'Kevin Hans Aurick', 'Santillana', 'staff2', 'staff2');

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
  ADD KEY `meds_code` (`meds_code`),
  ADD KEY `doctor_code` (`doctor_code`);

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
-- Indexes for table `stafftbl`
--
ALTER TABLE `stafftbl`
  ADD PRIMARY KEY (`staff_code`);

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
  ADD CONSTRAINT `patienthistorytbl_ibfk_2` FOREIGN KEY (`doctor_code`) REFERENCES `doctortbl` (`doctor_code`);

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
