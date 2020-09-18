-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-09-2020 a las 05:02:06
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `banco_cartago`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cuentas`
--

CREATE TABLE `cuentas` (
  `id` int(255) NOT NULL,
  `usuario_cedula` int(255) NOT NULL,
  `numero_cuenta` int(255) NOT NULL,
  `saldo` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cuentas`
--

INSERT INTO `cuentas` (`id`, `usuario_cedula`, `numero_cuenta`, `saldo`) VALUES
(22, 2147483647, 27186164, 40000),
(23, 27318901, 69864819, 110000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos_transacciones`
--

CREATE TABLE `tipos_transacciones` (
  `id` int(255) NOT NULL,
  `tipo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipos_transacciones`
--

INSERT INTO `tipos_transacciones` (`id`, `tipo`) VALUES
(1, 'TRANSFERENCIA'),
(2, 'RETIRO'),
(3, 'DEPOSITO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transacciones`
--

CREATE TABLE `transacciones` (
  `id` int(255) NOT NULL,
  `cuenta_id` int(255) NOT NULL,
  `cuenta_remitente` int(12) DEFAULT NULL,
  `tipo_id` int(255) NOT NULL,
  `monto` float DEFAULT NULL,
  `fecha_hora` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `transacciones`
--

INSERT INTO `transacciones` (`id`, `cuenta_id`, `cuenta_remitente`, `tipo_id`, `monto`, `fecha_hora`) VALUES
(56, 22, NULL, 3, 100000, '2020-09-17 23:42:19'),
(57, 22, NULL, 2, 50000, '2020-09-17 23:43:44'),
(58, 22, 69864819, 1, 10000, '2020-09-17 23:44:27'),
(59, 23, NULL, 3, 100000, '2020-09-17 23:45:39');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `cedula` int(255) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellidos` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pass` varchar(255) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`cedula`, `nombre`, `apellidos`, `email`, `pass`, `fecha`) VALUES
(27318901, 'RAMIRO', 'MORALES', '270429@270429.390', '270429@270429.39027042919999', '2020-09-17'),
(2147483647, 'JUAN', 'MORALES', '092765s@092765s.390', '092765s@092765s.390j17n19999', '2020-09-17');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cuentas`
--
ALTER TABLE `cuentas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_numero_cuenta` (`numero_cuenta`),
  ADD KEY `fk_usuario_cedula` (`usuario_cedula`);

--
-- Indices de la tabla `tipos_transacciones`
--
ALTER TABLE `tipos_transacciones`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `transacciones`
--
ALTER TABLE `transacciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_cuentas_id` (`cuenta_id`),
  ADD KEY `fk_tipos_id` (`tipo_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`cedula`),
  ADD UNIQUE KEY `uq_cedula` (`cedula`),
  ADD UNIQUE KEY `uq_email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cuentas`
--
ALTER TABLE `cuentas`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `tipos_transacciones`
--
ALTER TABLE `tipos_transacciones`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `transacciones`
--
ALTER TABLE `transacciones`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cuentas`
--
ALTER TABLE `cuentas`
  ADD CONSTRAINT `fk_usuario_cedula` FOREIGN KEY (`usuario_cedula`) REFERENCES `usuarios` (`cedula`);

--
-- Filtros para la tabla `transacciones`
--
ALTER TABLE `transacciones`
  ADD CONSTRAINT `fk_cuentas_id` FOREIGN KEY (`cuenta_id`) REFERENCES `cuentas` (`id`),
  ADD CONSTRAINT `fk_tipos_id` FOREIGN KEY (`tipo_id`) REFERENCES `tipos_transacciones` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
