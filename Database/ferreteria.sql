-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.32-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando estructura para tabla ferreteria.producto
CREATE TABLE IF NOT EXISTS `producto` (
  `CodigoProducto` int(11) NOT NULL AUTO_INCREMENT,
  `NombreProducto` varchar(100) NOT NULL,
  `Categoria` varchar(50) DEFAULT NULL,
  `Precio` decimal(10,2) NOT NULL,
  `Stock` int(11) NOT NULL,
  PRIMARY KEY (`CodigoProducto`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla ferreteria.producto: ~30 rows (aproximadamente)
INSERT INTO `producto` (`CodigoProducto`, `NombreProducto`, `Categoria`, `Precio`, `Stock`) VALUES
	(1, 'Martillo', 'Herramientas', 25.50, 47),
	(2, 'Taladro', 'Herramientas', 150.00, 20),
	(3, 'Tornillos (Caja)', 'Tornillería', 10.00, 200),
	(4, 'Llave Inglesa', 'Herramientas', 45.00, 15),
	(5, 'Cinta Métrica', 'Medición', 12.50, 77),
	(6, 'Sierra Circular', 'Corte', 350.00, 5),
	(7, 'Pegamento Epóxico', 'Adhesivos', 8.00, 115),
	(8, 'Alicates', 'Herramientas', 18.75, 26),
	(9, 'Destornillador', 'Herramientas', 12.00, 99),
	(10, 'Taladro Percutor', 'Herramientas', 200.00, 10),
	(11, 'Tornillo de Expansión', 'Tornillería', 15.00, 150),
	(12, 'Cuter', 'Corte', 5.50, 70),
	(13, 'Masilla Plástica', 'Adhesivos', 25.00, 40),
	(14, 'Lija Grano 220', 'Abrasivos', 2.50, 297),
	(15, 'Broca para Concreto', 'Herramientas', 18.00, 25),
	(16, 'Escalera de Aluminio', 'Accesorios', 450.00, 8),
	(17, 'Llave de Cruz', 'Herramientas', 30.00, 12),
	(18, 'Pistola de Silicona', 'Adhesivos', 28.00, 60),
	(19, 'Clavos (Caja)', 'Tornillería', 6.50, 250),
	(20, 'Guantes de Trabajo', 'Seguridad', 15.00, 100),
	(21, 'Mascarilla FFP2', 'Seguridad', 8.00, 148),
	(22, 'Lámpara de Trabajo LED', 'Iluminación', 120.00, 20),
	(23, 'Esmeril Angular', 'Herramientas', 550.00, 5),
	(24, 'Nivel Láser', 'Medición', 200.00, 10),
	(25, 'Flexómetro 5m', 'Medición', 20.00, 50),
	(26, 'Cinta Aislante (Pack)', 'Eléctrico', 10.00, 99),
	(27, 'Martillo de Goma', 'Herramientas', 18.50, 40),
	(28, 'Sierra Manual', 'Corte', 25.00, 29),
	(29, 'Disco de Corte para Metal', 'Abrasivos', 15.00, 50),
	(30, 'Caja de Herramientas', 'Accesorios', 350.00, 16);

-- Volcando estructura para tabla ferreteria.venta
CREATE TABLE IF NOT EXISTS `venta` (
  `IdVenta` int(11) NOT NULL AUTO_INCREMENT,
  `CodigoProducto` int(11) NOT NULL,
  `Cantidad` int(11) NOT NULL,
  `FechaVenta` date NOT NULL,
  `Total` decimal(10,2) NOT NULL,
  PRIMARY KEY (`IdVenta`),
  KEY `CodigoProducto` (`CodigoProducto`),
  CONSTRAINT `venta_ibfk_1` FOREIGN KEY (`CodigoProducto`) REFERENCES `producto` (`CodigoProducto`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla ferreteria.venta: ~11 rows (aproximadamente)
INSERT INTO `venta` (`IdVenta`, `CodigoProducto`, `Cantidad`, `FechaVenta`, `Total`) VALUES
	(1, 5, 3, '2024-05-06', 36.00),
	(2, 9, 1, '2024-04-12', 12.00),
	(3, 7, 2, '2024-03-02', 16.00),
	(4, 28, 1, '2024-11-15', 25.00),
	(5, 23, 5, '2024-06-06', 2750.00),
	(6, 21, 2, '2024-01-29', 16.00),
	(7, 14, 3, '2024-11-18', 6.00),
	(8, 7, 3, '2024-07-11', 24.00),
	(9, 26, 1, '2024-05-18', 10.00),
	(10, 8, 9, '2024-02-16', 162.00),
	(11, 1, 3, '2024-06-12', 75.00);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
