-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 23, 2021 at 11:04 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dailycoder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `Sr_no` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_number` varchar(50) NOT NULL,
  `message` text NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`Sr_no`, `name`, `email`, `phone_number`, `message`, `date`) VALUES
(1, 'drishti', 'xyz@gmail.com', '980000000', 'Hello. Would really like to connect', '2020-11-30 13:27:03'),
(2, 'Julia', 'julia@gmail.com', '980000000', 'Really liked your Blog', '2020-12-05 18:01:34'),
(3, 'Dharti', 'xyz@gmail.com', '4657334', 'Nice Blogs', '2021-06-24 02:27:17');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `Sr_no` int(11) NOT NULL,
  `title` text NOT NULL,
  `subtitle` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `imageurl` varchar(20) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`Sr_no`, `title`, `subtitle`, `slug`, `content`, `imageurl`, `date`) VALUES
(1, 'What do you mean by Stocks', 'Lets go over to learn more about stocks ', 'Regarding-stocks', '                  Stock (also capital stock) of a corporation, is all of the shares into which ownership of the corporation is divided.[1] In American English, the shares are collectively known as \"stock\".[1] A single share of the stock represents fractional ownership of the corporation in proportion to the total number of shares. This typically entitles tstockholder to that fraction of the company\'s earnings, proceeds from liquidation of assets (after discharge of all senior claims such as secured and unsecured debt),[2] or voting power, often dividing these up in proportion to the amount of money each stockholder has invested. Not all stock is necessarily equal, as certain classes of stock may be issued for example without voting rights, with enhanced voting rights, or with a certain priority to receive profits or liquidation proceeds before or after other classes of shareholders. \r\n              ', 'post-bg.jpg', '2020-12-25 02:24:29'),
(2, 'All about Fruit Juices', 'For all the yummy juices recipes head over', 'about-juices', 'Juice is a drink made from the extraction or pressing of the natural liquid contained in fruit and vegetables. It can also refer to liquids that are flavored with concentrate or other biological food sources, such as meat or seafood, such as clam juice. Juice is commonly consumed as a beverage or used as an ingredient or flavoring in foods or other beverages, as for smoothies. Juice emerged as a popular beverage choice after the development of pasteurization methods enabled its preservation without using fermentation (which is used in wine production).[1] The largest fruit juice consumers are New Zealand (nearly a cup, or 8 ounces, each day) and Colombia (more than three quarters of a cup each day). ', 'post-bg.jpg', '2020-12-05 19:40:49'),
(3, 'Beautiful places to explore', 'Find out beautiful places you can explore ', 'travel-post', 'Travel is the movement of people between distant geographical locations. Travel can be done by foot, bicycle, automobile, train, boat, bus, airplane, ship or other means, with or without luggage, and can be one way or round trip.[1][2] Travel can also include relatively short stays between successive movements, as in the case of tourism.', 'post-bg.jpg', '2020-12-05 19:46:21');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`Sr_no`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`Sr_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `Sr_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `Sr_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
