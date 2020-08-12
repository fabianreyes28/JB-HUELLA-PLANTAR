-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 12-08-2020 a las 03:48:07
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `base_huella`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Foto`
--

CREATE TABLE `Foto` (
  `num_muestra` int(11) NOT NULL,
  `id3` int(11) DEFAULT NULL,
  `foto_hsv` varchar(100) CHARACTER SET latin1 DEFAULT NULL,
  `foto_procesada` varchar(100) CHARACTER SET latin1 DEFAULT NULL,
  `foto_pie` varchar(100) CHARACTER SET latin1 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `Foto`
--

INSERT INTO `Foto` (`num_muestra`, `id3`, `foto_hsv`, `foto_procesada`, `foto_pie`) VALUES
(24, 1001, '../Imagenes_Huellas/Muestras_HSV/1001.png', '../Imagenes_Huellas/Muestras_procesada/1001.png', '../Imagenes_Huellas/Muestras_fotos/1001.png'),
(25, 1002, '../Imagenes_Huellas/Muestras_HSV/1002.png', '../Imagenes_Huellas/Muestras_procesada/1002.png', '../Imagenes_Huellas/Muestras_fotos/1002.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Muestra_dere`
--

CREATE TABLE `Muestra_dere` (
  `num_muestra` int(11) NOT NULL,
  `id2` int(11) DEFAULT NULL,
  `metodo` varchar(40) DEFAULT NULL,
  `largo_dere` float DEFAULT NULL,
  `x_dere` float DEFAULT NULL,
  `y_dere` float DEFAULT NULL,
  `clasificacion_dere` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `Muestra_dere`
--

INSERT INTO `Muestra_dere` (`num_muestra`, `id2`, `metodo`, `largo_dere`, `x_dere`, `y_dere`, `clasificacion_dere`) VALUES
(3, 1001, 'HC', 24.6, 9.5, 4.54, '52.21 pie normal'),
(4, 1002, 'HC', 24.53, 9.56, 4.33, '54.71 pie normal');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Muestra_izq`
--

CREATE TABLE `Muestra_izq` (
  `num_muestra` int(11) NOT NULL,
  `id1` int(11) DEFAULT NULL,
  `metodo1` varchar(40) DEFAULT NULL,
  `largo_izq` float DEFAULT NULL,
  `x_izq` float DEFAULT NULL,
  `y_izq` float DEFAULT NULL,
  `clasificacion_izq` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `Muestra_izq`
--

INSERT INTO `Muestra_izq` (`num_muestra`, `id1`, `metodo1`, `largo_izq`, `x_izq`, `y_izq`, `clasificacion_izq`) VALUES
(5, 1001, 'HC', 24.09, 9.04, 4.31, '52.32 pie normal'),
(6, 1002, 'HC', 24.33, 9.05, 4.12, '54.48 pie normal');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Registro`
--

CREATE TABLE `Registro` (
  `id` int(11) NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellidos` varchar(50) NOT NULL,
  `genero` varchar(10) NOT NULL,
  `peso` float NOT NULL,
  `altura` float NOT NULL,
  `talla_izq` int(3) NOT NULL,
  `talla_dere` int(3) NOT NULL,
  `telefono` bigint(11) NOT NULL,
  `ocupacion` varchar(20) NOT NULL,
  `observacion` varchar(200) NOT NULL DEFAULT current_timestamp(),
  `fecha` timestamp NOT NULL DEFAULT current_timestamp(),
  `edad` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `Registro`
--

INSERT INTO `Registro` (`id`, `nombres`, `apellidos`, `genero`, `peso`, `altura`, `talla_izq`, `talla_dere`, `telefono`, `ocupacion`, `observacion`, `fecha`, `edad`) VALUES
(1001, 'fa', 're', 'masculino', 55, 155, 55, 55, 55, 'ing', '', '2020-08-09 06:09:17', 55),
(1002, 're', 'er', 'masculino', 55, 55, 55, 55, 55, 'ing', '', '2020-08-10 22:33:14', 55);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Foto`
--
ALTER TABLE `Foto`
  ADD PRIMARY KEY (`num_muestra`),
  ADD KEY `fk_fcid3` (`id3`);

--
-- Indices de la tabla `Muestra_dere`
--
ALTER TABLE `Muestra_dere`
  ADD PRIMARY KEY (`num_muestra`),
  ADD KEY `fk_fcid2` (`id2`);

--
-- Indices de la tabla `Muestra_izq`
--
ALTER TABLE `Muestra_izq`
  ADD PRIMARY KEY (`num_muestra`),
  ADD KEY `fk_fcid1` (`id1`);

--
-- Indices de la tabla `Registro`
--
ALTER TABLE `Registro`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Foto`
--
ALTER TABLE `Foto`
  MODIFY `num_muestra` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `Muestra_dere`
--
ALTER TABLE `Muestra_dere`
  MODIFY `num_muestra` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `Muestra_izq`
--
ALTER TABLE `Muestra_izq`
  MODIFY `num_muestra` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Foto`
--
ALTER TABLE `Foto`
  ADD CONSTRAINT `fk_fcid3` FOREIGN KEY (`id3`) REFERENCES `Registro` (`id`);

--
-- Filtros para la tabla `Muestra_dere`
--
ALTER TABLE `Muestra_dere`
  ADD CONSTRAINT `fk_fcid2` FOREIGN KEY (`id2`) REFERENCES `Registro` (`id`);

--
-- Filtros para la tabla `Muestra_izq`
--
ALTER TABLE `Muestra_izq`
  ADD CONSTRAINT `fk_fcid1` FOREIGN KEY (`id1`) REFERENCES `Registro` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
