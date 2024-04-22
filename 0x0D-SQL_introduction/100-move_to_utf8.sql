-- Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in my MySQL server.

-- Alters the database character set and collation
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Switches to the hbtn_0c_0 database
USE `hbtn_0c_0`;

-- Alters the table character set and collation
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modifies the column 'name' to use utf8mb4 character set and collation
ALTER TABLE `first_table` CHANGE `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

