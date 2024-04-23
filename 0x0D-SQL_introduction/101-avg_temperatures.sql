-- Convert hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Switch to the hbtn_0c_0 database
USE `hbtn_0c_0`;

-- Alter the table character set and collation
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modify the column 'name' to use utf8mb4 character set and collation
ALTER TABLE `first_table` MODIFY COLUMN `name` VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
