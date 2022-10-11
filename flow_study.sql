/*
 Navicat Premium Data Transfer

 Source Server         : flow_code
 Source Server Type    : MySQL
 Source Server Version : 50719
 Source Host           : 47.242.206.108:3306
 Source Schema         : nft

 Target Server Type    : MySQL
 Target Server Version : 50719
 File Encoding         : 65001

 Date: 11/10/2022 22:12:57
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for flow_block
-- ----------------------------
DROP TABLE IF EXISTS `flow_block`;
CREATE TABLE `flow_block`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `block_seals` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `timestamp` datetime NULL DEFAULT NULL,
  `collection_guarantees` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `block_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `height` bigint(20) NULL DEFAULT NULL,
  `signatures` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `parent_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `is_updated` int(2) NOT NULL DEFAULT 0,
  `fetch_time` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `height`(`height`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1200171 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flow_code
-- ----------------------------
DROP TABLE IF EXISTS `flow_code`;
CREATE TABLE `flow_code`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `contract_name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `contract_address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `contract_code` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `contract_type` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `is_process` int(11) NOT NULL DEFAULT 0 COMMENT '0未处理，',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 691 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flow_contract_address
-- ----------------------------
DROP TABLE IF EXISTS `flow_contract_address`;
CREATE TABLE `flow_contract_address`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `contract_name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `contract_address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `contract_code` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `is_process` int(11) NOT NULL DEFAULT 0 COMMENT '默认是0，未处理。1表示已经处理。',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `contract_address`(`contract_address`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 377 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flow_token_from
-- ----------------------------
DROP TABLE IF EXISTS `flow_token_from`;
CREATE TABLE `flow_token_from`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `from_address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `amount` float NULL DEFAULT NULL,
  `trans_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `from_address_trans`(`from_address`, `trans_id`) USING BTREE,
  INDEX `trans_id`(`trans_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5125942 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = 'Flow token 发送地址' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flow_token_from_to
-- ----------------------------
DROP TABLE IF EXISTS `flow_token_from_to`;
CREATE TABLE `flow_token_from_to`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `from_address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `amount` float NULL DEFAULT NULL,
  `trans_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `to_address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 907800 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = 'Flow token 发送地址' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flow_token_to
-- ----------------------------
DROP TABLE IF EXISTS `flow_token_to`;
CREATE TABLE `flow_token_to`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `to_address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `amount` float NULL DEFAULT NULL,
  `trans_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `from_address_trans`(`to_address`, `trans_id`) USING BTREE,
  INDEX `trans_id`(`trans_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 890923 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = 'Flow token 发送地址' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flow_trans_data
-- ----------------------------
DROP TABLE IF EXISTS `flow_trans_data`;
CREATE TABLE `flow_trans_data`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `trans_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '交易id',
  `user_address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '用户地址',
  `contract_name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '合约名称',
  `contract_address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '合约地址',
  `fetch_time` datetime NULL DEFAULT NULL,
  `height` bigint(20) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `contract_address`(`contract_address`) USING BTREE,
  INDEX `fetch_time`(`fetch_time`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 30289670 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flow_trans_data_copy1
-- ----------------------------
DROP TABLE IF EXISTS `flow_trans_data_copy1`;
CREATE TABLE `flow_trans_data_copy1`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `trans_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '交易id',
  `user_address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '用户地址',
  `contract_name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '合约名称',
  `contract_address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '合约地址',
  `fetch_time` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `contract_address`(`contract_address`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11736196 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for member
-- ----------------------------
DROP TABLE IF EXISTS `member`;
CREATE TABLE `member`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `email` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户mail',
  `password` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户密码，md5',
  `username` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户名',
  `regdate` datetime NOT NULL COMMENT '注册日期',
  `user_platform` int(4) NOT NULL COMMENT '用户来源（0代表aso,1代表用户微服务）',
  `nickname` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户昵称，微博为nickname，一般注册为email @ 前的字符串',
  `level` int(11) NOT NULL DEFAULT 20 COMMENT '用户等级',
  `phone_num` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户手机号码',
  `company` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '公司名',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for member_token
-- ----------------------------
DROP TABLE IF EXISTS `member_token`;
CREATE TABLE `member_token`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `email` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `token` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `login_time` datetime NOT NULL COMMENT '用户登录时间',
  `ip` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户ip',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `email`(`email`(255)) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户登录token库' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for opensea_asset
-- ----------------------------
DROP TABLE IF EXISTS `opensea_asset`;
CREATE TABLE `opensea_asset`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `token_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `image_url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `image_original_url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `background_color` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `external_link` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `asset_contract` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `owner` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `traits` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `last_sale` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `fetch_time` datetime NULL DEFAULT NULL,
  `next_cursor` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `page` int(11) NULL DEFAULT NULL,
  `token_metadata` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `permalink` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `image_cos_url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'cos链接',
  `contract_address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `cid` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'ipfs cid,图片的',
  `nft_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '新的nft_id',
  `tx_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'mint的交易id',
  `nft_metadata_url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'nft的元数据链接',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `permalink`(`permalink`) USING BTREE,
  INDEX `contract_address`(`contract_address`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15619452 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for opensea_asset_1
-- ----------------------------
DROP TABLE IF EXISTS `opensea_asset_1`;
CREATE TABLE `opensea_asset_1`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `token_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `image_url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `image_original_url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `background_color` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `external_link` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `asset_contract` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `owner` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `traits` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `last_sale` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `fetch_time` datetime NULL DEFAULT NULL,
  `next_cursor` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `page` int(11) NULL DEFAULT NULL,
  `token_metadata` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `permalink` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `image_cos_url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'cos链接',
  `contract_address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `cid` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'ipfs cid,图片的',
  `nft_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '新的nft_id',
  `tx_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'mint的交易id',
  `nft_metadata_url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT 'nft的元数据链接',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `contract_address`(`contract_address`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for opensea_collection
-- ----------------------------
DROP TABLE IF EXISTS `opensea_collection`;
CREATE TABLE `opensea_collection`  (
  `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `createdDate` datetime NULL DEFAULT NULL,
  `slug` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `logo` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `relayId` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `chain` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `item_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `statsV2` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `nativePaymentAsset` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `fetch_time` datetime NULL DEFAULT NULL,
  `rank` int(11) NULL DEFAULT NULL COMMENT '榜单排名',
  `is_process` int(11) NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `slug`(`slug`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 66237 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
