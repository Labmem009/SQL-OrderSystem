/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80011
 Source Host           : localhost:3306
 Source Schema         : baoleme

 Target Server Type    : MySQL
 Target Server Version : 80011
 File Encoding         : 65001

 Date: 30/06/2018 01:40:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for dish
-- ----------------------------
DROP TABLE IF EXISTS `dish`;
CREATE TABLE `dish`  (
  `dishid` int(11) NOT NULL AUTO_INCREMENT,
  `dishname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `shopid` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `price` decimal(10, 2) NULL DEFAULT NULL,
  PRIMARY KEY (`dishid`) USING BTREE,
  INDEX `shopid`(`shopid`) USING BTREE,
  CONSTRAINT `dish_ibfk_1` FOREIGN KEY (`shopid`) REFERENCES `shop` (`shopid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 51 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of dish
-- ----------------------------
INSERT INTO `dish` VALUES (2, '想面筋', '1', 14.00);
INSERT INTO `dish` VALUES (9, '炒河粉', '11', 0.00);
INSERT INTO `dish` VALUES (10, '炒面', '11', 0.00);
INSERT INTO `dish` VALUES (11, '炒饭', '11', 112.00);
INSERT INTO `dish` VALUES (13, '23333', '1', 23.00);
INSERT INTO `dish` VALUES (14, '玉米炒葡萄', '1', 11.00);
INSERT INTO `dish` VALUES (15, 'dish', '1', 19.00);
INSERT INTO `dish` VALUES (17, '扬州炒饭', '1', 11.00);
INSERT INTO `dish` VALUES (18, '蓝莓山药', '1', 10.50);
INSERT INTO `dish` VALUES (20, '板烧鸡腿堡', '金拱门', 14.50);
INSERT INTO `dish` VALUES (21, '巨无霸汉堡', '金拱门', 20.00);
INSERT INTO `dish` VALUES (22, '薯条', '金拱门', 6.00);
INSERT INTO `dish` VALUES (23, '麦辣鸡翅', '金拱门', 8.00);
INSERT INTO `dish` VALUES (24, '上校鸡块', 'KFC', 10.50);
INSERT INTO `dish` VALUES (25, '嫩牛五方', 'KFC', 12.00);
INSERT INTO `dish` VALUES (26, '薯条', 'KFC', 7.00);
INSERT INTO `dish` VALUES (27, ' 劲辣鸡腿堡', 'KFC', 18.00);
INSERT INTO `dish` VALUES (28, '新奥尔良烤翅', 'KFC', 11.50);
INSERT INTO `dish` VALUES (29, '玉米炒葡萄', '河东饭店', 4.50);
INSERT INTO `dish` VALUES (30, '蓝莓山药', '河东饭店', 3.50);
INSERT INTO `dish` VALUES (31, '原谅色鸡腿', '河东饭店', 5.00);
INSERT INTO `dish` VALUES (32, '生煎包子', '河东饭店', 6.00);
INSERT INTO `dish` VALUES (33, '鸭血粉丝', '河东饭店', 10.00);
INSERT INTO `dish` VALUES (34, '大排面', '河西面馆', 5.50);
INSERT INTO `dish` VALUES (35, '葱油拌面', '河西面馆', 8.00);
INSERT INTO `dish` VALUES (36, '牛蛙面', '河西面馆', 14.00);
INSERT INTO `dish` VALUES (37, '辣肉面', '河西面馆', 5.00);
INSERT INTO `dish` VALUES (38, '大肠面', '河西面馆', 7.00);
INSERT INTO `dish` VALUES (39, '烤面筋', '撸串烧烤', 3.00);
INSERT INTO `dish` VALUES (40, '烤鸡翅', '撸串烧烤', 5.00);
INSERT INTO `dish` VALUES (41, '烤茄子', '撸串烧烤', 6.00);
INSERT INTO `dish` VALUES (42, '粉丝扇贝', '撸串烧烤', 7.00);
INSERT INTO `dish` VALUES (43, '扬州炒饭', '撸串烧烤', 8.00);
INSERT INTO `dish` VALUES (44, '炒饭', '丽娃饭店', 5.00);
INSERT INTO `dish` VALUES (45, '炒河粉', '丽娃饭店', 6.00);
INSERT INTO `dish` VALUES (46, '炒面', '丽娃饭店', 6.00);
INSERT INTO `dish` VALUES (47, '黄焖鸡米饭', '丽娃饭店', 10.00);
INSERT INTO `dish` VALUES (48, '腐竹黄焖鸡米饭', '丽娃饭店', 12.00);
INSERT INTO `dish` VALUES (49, '麦乐鸡', '金拱门', 13.00);
INSERT INTO `dish` VALUES (50, '麦香鸡', '金拱门', 6.00);

-- ----------------------------
-- Table structure for order_detail
-- ----------------------------
DROP TABLE IF EXISTS `order_detail`;
CREATE TABLE `order_detail`  (
  `orderid` int(11) NOT NULL,
  `dishid` int(11) NOT NULL,
  PRIMARY KEY (`orderid`, `dishid`) USING BTREE,
  INDEX `dishid`(`dishid`) USING BTREE,
  CONSTRAINT `order_detail_ibfk_1` FOREIGN KEY (`orderid`) REFERENCES `orders` (`orderid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `order_detail_ibfk_2` FOREIGN KEY (`dishid`) REFERENCES `dish` (`dishid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of order_detail
-- ----------------------------
INSERT INTO `order_detail` VALUES (1, 11);
INSERT INTO `order_detail` VALUES (18, 22);
INSERT INTO `order_detail` VALUES (18, 49);

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders`  (
  `orderid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `shopid` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `cost` double(10, 2) NULL DEFAULT NULL,
  `carriage` double(10, 0) NULL DEFAULT NULL,
  `raiderid` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `ok` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '0',
  `com` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '0',
  PRIMARY KEY (`orderid`) USING BTREE,
  INDEX `userid`(`userid`) USING BTREE,
  INDEX `shopid`(`shopid`) USING BTREE,
  INDEX `raiderid`(`raiderid`) USING BTREE,
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`shopid`) REFERENCES `shop` (`shopid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`raiderid`) REFERENCES `raider` (`raiderid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES (1, '1', '1', 13.00, 5, '1', '0', '0');
INSERT INTO `orders` VALUES (2, '2', '1', 13.00, 5, '1', '1', '1');
INSERT INTO `orders` VALUES (5, '2', '1', 13.00, 5, '1', '1', '1');
INSERT INTO `orders` VALUES (6, '2', '1', 13.00, 5, '1', '1', '1');
INSERT INTO `orders` VALUES (7, '2', '1', 13.00, 5, '1', '1', '0');
INSERT INTO `orders` VALUES (8, '2', '1', 13.00, 5, '1', '0', '0');
INSERT INTO `orders` VALUES (12, '2', '1', 13.00, 5, '1', '0', '0');
INSERT INTO `orders` VALUES (14, '2', '1', 13.00, 5, '1', '1', '1');
INSERT INTO `orders` VALUES (15, 'labmeme', '11', 0.00, 5, '1', '0', '0');
INSERT INTO `orders` VALUES (16, '长者', '丽娃饭店', 18.00, 5, '骑士一号', '1', '1');
INSERT INTO `orders` VALUES (17, 'labmem001', '金拱门', 28.50, 5, '骑士一号', '1', '1');
INSERT INTO `orders` VALUES (18, 'labmem009', '金拱门', 14.00, 5, '骑士一号', '1', '1');

-- ----------------------------
-- Table structure for raider
-- ----------------------------
DROP TABLE IF EXISTS `raider`;
CREATE TABLE `raider`  (
  `raiderid` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `keyword` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`raiderid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of raider
-- ----------------------------
INSERT INTO `raider` VALUES ('1', NULL, '1');
INSERT INTO `raider` VALUES ('raider0', '13358148415', 'raider');
INSERT INTO `raider` VALUES ('嘿嘿嘿', NULL, 'hhhh');
INSERT INTO `raider` VALUES ('骑士一号', '13358148015', 'qishi');

-- ----------------------------
-- Table structure for raider_comment
-- ----------------------------
DROP TABLE IF EXISTS `raider_comment`;
CREATE TABLE `raider_comment`  (
  `userid` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `raiderid` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `orderid` int(11) NOT NULL,
  `content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`orderid`) USING BTREE,
  INDEX `userid`(`userid`) USING BTREE,
  INDEX `raiderid`(`raiderid`) USING BTREE,
  CONSTRAINT `raider_comment_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `raider_comment_ibfk_2` FOREIGN KEY (`raiderid`) REFERENCES `raider` (`raiderid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `raider_comment_ibfk_3` FOREIGN KEY (`orderid`) REFERENCES `orders` (`orderid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of raider_comment
-- ----------------------------
INSERT INTO `raider_comment` VALUES ('2', '1', 2, 'å¥½');
INSERT INTO `raider_comment` VALUES ('2', '1', 5, '快');
INSERT INTO `raider_comment` VALUES ('2', '1', 6, '');
INSERT INTO `raider_comment` VALUES ('长者', '骑士一号', 16, '快');
INSERT INTO `raider_comment` VALUES ('labmem001', '骑士一号', 17, '快');
INSERT INTO `raider_comment` VALUES ('labmem009', '骑士一号', 18, '很慢');

-- ----------------------------
-- Table structure for shop
-- ----------------------------
DROP TABLE IF EXISTS `shop`;
CREATE TABLE `shop`  (
  `shopid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `keyword` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`shopid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of shop
-- ----------------------------
INSERT INTO `shop` VALUES ('1', '1', '1');
INSERT INTO `shop` VALUES ('11', '11', '11');
INSERT INTO `shop` VALUES ('KFC', '枣阳路456号', 'kfc');
INSERT INTO `shop` VALUES ('丽娃饭店', '金沙江路456号', 'liwa');
INSERT INTO `shop` VALUES ('撸串烧烤', '枣阳路123号', 'luchuan');
INSERT INTO `shop` VALUES ('河东饭店', '中山北路345号', 'hedong');
INSERT INTO `shop` VALUES ('河西面馆', '中山北路234号', 'hexi');
INSERT INTO `shop` VALUES ('金拱门', '环球港B2', 'jingong');

-- ----------------------------
-- Table structure for shop_comment
-- ----------------------------
DROP TABLE IF EXISTS `shop_comment`;
CREATE TABLE `shop_comment`  (
  `userid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `shopid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `orderid` int(11) NOT NULL,
  PRIMARY KEY (`orderid`) USING BTREE,
  INDEX `userid`(`userid`) USING BTREE,
  INDEX `shopid`(`shopid`) USING BTREE,
  CONSTRAINT `shop_comment_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `shop_comment_ibfk_2` FOREIGN KEY (`shopid`) REFERENCES `shop` (`shopid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `shop_comment_ibfk_3` FOREIGN KEY (`orderid`) REFERENCES `orders` (`orderid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of shop_comment
-- ----------------------------
INSERT INTO `shop_comment` VALUES ('2', '1', '好吃', 5);
INSERT INTO `shop_comment` VALUES ('2', '1', '好吃', 14);
INSERT INTO `shop_comment` VALUES ('长者', '丽娃饭店', '好吃', 16);
INSERT INTO `shop_comment` VALUES ('labmem001', '金拱门', '好吃', 17);
INSERT INTO `shop_comment` VALUES ('labmem009', '金拱门', '难吃', 18);

-- ----------------------------
-- Table structure for shopcart
-- ----------------------------
DROP TABLE IF EXISTS `shopcart`;
CREATE TABLE `shopcart`  (
  `userid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `shopid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `dishid` int(11) NOT NULL,
  PRIMARY KEY (`dishid`, `userid`) USING BTREE,
  INDEX `userid`(`userid`) USING BTREE,
  INDEX `shopid`(`shopid`) USING BTREE,
  CONSTRAINT `shopcart_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `user` (`userid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `shopcart_ibfk_2` FOREIGN KEY (`shopid`) REFERENCES `shop` (`shopid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `shopcart_ibfk_3` FOREIGN KEY (`dishid`) REFERENCES `dish` (`dishid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of shopcart
-- ----------------------------
INSERT INTO `shopcart` VALUES ('2', '11', 9);
INSERT INTO `shopcart` VALUES ('2', '11', 10);
INSERT INTO `shopcart` VALUES ('11', '11', 11);
INSERT INTO `shopcart` VALUES ('2', '11', 11);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `userid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `phone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `keyword` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`userid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', '第五宿舍', '13358148015', 'zhangzhe');
INSERT INTO `user` VALUES ('10', '1', '1', '1');
INSERT INTO `user` VALUES ('11', '11', '11', '11');
INSERT INTO `user` VALUES ('12', 'dfdf', NULL, '12');
INSERT INTO `user` VALUES ('2', '1', '1', '3');
INSERT INTO `user` VALUES ('3', '1', '1', '1');
INSERT INTO `user` VALUES ('4', '1', '1', '1');
INSERT INTO `user` VALUES ('5', '1', '1', '1');
INSERT INTO `user` VALUES ('6', '1', '1', '1');
INSERT INTO `user` VALUES ('7', '1', '1', '1');
INSERT INTO `user` VALUES ('8', '1', '1', '1');
INSERT INTO `user` VALUES ('9', '1', '1', '1');
INSERT INTO `user` VALUES ('aaa', 'dddd', '13', '1');
INSERT INTO `user` VALUES ('boy', 'hhhh', '111', '111');
INSERT INTO `user` VALUES ('hhhhh', 'hhhhhh', NULL, 'hhhh');
INSERT INTO `user` VALUES ('labmem001', '华师大', '13358148015', '0001');
INSERT INTO `user` VALUES ('labmem009', '中山北路', '111111', '009');
INSERT INTO `user` VALUES ('labmeme', '中山北路3663号', '13358148015', 'zhubao');
INSERT INTO `user` VALUES ('wewewewewe', 'sdfsdfsdf', NULL, '1111');
INSERT INTO `user` VALUES ('长者', '华师大', '11111111111', '1');

-- ----------------------------
-- View structure for uncom
-- ----------------------------
DROP VIEW IF EXISTS `uncom`;
CREATE ALGORITHM = UNDEFINED DEFINER = `root`@`localhost` SQL SECURITY DEFINER VIEW `uncom` AS select `orders`.`orderid` AS `orderid`,`orders`.`userid` AS `userid`,`orders`.`shopid` AS `shopid`,`orders`.`cost` AS `cost`,`orders`.`carriage` AS `carriage`,`orders`.`raiderid` AS `raiderid`,`orders`.`ok` AS `ok`,`orders`.`com` AS `com` from `orders` where ((`orders`.`com` = '0') and (`orders`.`ok` = '1'));

-- ----------------------------
-- View structure for unok
-- ----------------------------
DROP VIEW IF EXISTS `unok`;
CREATE ALGORITHM = UNDEFINED DEFINER = `root`@`localhost` SQL SECURITY DEFINER VIEW `unok` AS select `orders`.`orderid` AS `orderid`,`orders`.`userid` AS `userid`,`orders`.`shopid` AS `shopid`,`orders`.`cost` AS `cost`,`orders`.`carriage` AS `carriage`,`orders`.`raiderid` AS `raiderid`,`orders`.`ok` AS `ok`,`orders`.`com` AS `com` from `orders` where (`orders`.`ok` = '0');

-- ----------------------------
-- Procedure structure for SumCart
-- ----------------------------
DROP PROCEDURE IF EXISTS `SumCart`;
delimiter ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `SumCart`( IN users VARCHAR ( 20 ), IN shop VARCHAR ( 20 ), OUT summ INT )
BEGIN
SELECT
	sum( price ) 
FROM
	shopcart
	JOIN dish ON dish.dishid = shopcart.dishid 
WHERE
	shopcart.shopid = shop 
	AND userid = USER;

SET summ = sum( price );
DELETE 
FROM
	shopcart 
WHERE
	userid = users 
	AND shopid = shop;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
