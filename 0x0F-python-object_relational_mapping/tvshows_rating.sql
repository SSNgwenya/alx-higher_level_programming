-- tvshows_rating.sql

-- Check if the database name is provided as an argument
SET @db_name = '$1';
IF @db_name IS NULL OR @db_name = '' THEN
    SELECT 'Error: Please provide the database name as an argument.';
    LEAVE;
END IF;

-- Query to list shows by their rating
SELECT tv_shows.title, SUM(tv_show_ratings.rating) AS rating_sum
FROM $1.tv_shows
INNER JOIN $1.tv_show_ratings
ON tv_shows.id = tv_show_ratings.tv_show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;

