/*
Navicat MySQL Data Transfer

Source Server         : 103.44.61.204_3306
Source Server Version : 50173
Source Host           : 68.168.143.194:3306
Source Database       : notes

Target Server Type    : MYSQL
Target Server Version : 50173
File Encoding         : 65001

Date: 2018-08-14 11:16:39
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `USERNAME` varchar(15) NOT NULL DEFAULT '',
  `PASSWORD` varchar(20) NOT NULL,
  PRIMARY KEY (`USERNAME`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('nmgwap', 'nmgwap');
INSERT INTO `user` VALUES ('zhuxingm', '123456');
