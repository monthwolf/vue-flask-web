/*
Navicat MySQL Data Transfer

Source Server         : 103.44.61.204_3306
Source Server Version : 50173
Source Host           : 68.168.143.194:3306
Source Database       : notes

Target Server Type    : MYSQL
Target Server Version : 50173
File Encoding         : 65001

Date: 2018-08-14 11:16:55
*/

SET FOREIGN_KEY_CHECKS=0;
SET global time_zone = '+8:00';
-- ----------------------------
-- Table structure for `user_data`
-- ----------------------------
DROP TABLE IF EXISTS `user_data`;
CREATE TABLE `user_data` (
  -- 键名         类型      是否能为空  默认值
  -- `USERNAME` varchar(8)  NOT NULL    DEFAULT ''
 `USERNAME` varchar(15) NOT NULL DEFAULT '',
 `CONTENT` text NOT NULL DEFAULT '',
 `IMG` varchar(100) NULL,
 `CREATE_TIME` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_data
-- ----------------------------
INSERT INTO `user_data` VALUES ('undefine', 'ref和reactive都可以做响应式 ref:一般用在定义基本类型和引用类型，如果是引用类型底层会借助reactive形成proxy代理对象,可以直接复制整个对象，如table的数据请求回来，需要将数据整体赋值个响应对象这时如果使用的是reactive就无法进行响应。', NULL,"2023-10-25 10:01:01");
INSERT INTO `user_data` VALUES ('nmgwap', '123456', NULL,"2023-10-25 13:00:00");
INSERT INTO `user_data` VALUES ('undefine', '123456',NULL,"2023-10-25 00:00:00");
