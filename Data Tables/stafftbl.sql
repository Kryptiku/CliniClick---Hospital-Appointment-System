-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 15, 2023 at 04:55 PM
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
-- Indexes for table `stafftbl`
--
ALTER TABLE `stafftbl`
  ADD PRIMARY KEY (`staff_code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
