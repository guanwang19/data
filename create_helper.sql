--Retrieve a User's Course Progress
SELECT u.user_id, u.full_name, c.title AS course_title, 
       COUNT(up.video_id) AS videos_watched, 
       c.total_videos AS total_videos,
       ROUND((COUNT(up.video_id) * 100.0 / c.total_videos), 2) AS progress_percentage
FROM users u
JOIN user_progress up ON u.user_id = up.user_id
JOIN videos v ON up.video_id = v.video_id
JOIN courses c ON v.course_id = c.course_id
WHERE u.user_id = 1 -- Replace with actual user ID
GROUP BY u.user_id, u.full_name, c.title, c.total_videos;


--Retrieve the Most Watched Videos
SELECT v.video_id, v.title, c.title AS course_title, COUNT(up.video_id) AS views
FROM videos v
JOIN user_progress up ON v.video_id = up.video_id
JOIN courses c ON v.course_id = c.course_id
GROUP BY v.video_id, v.title, c.title
ORDER BY views DESC
LIMIT 10;

--Get the Average Watch Time for Each Course

SELECT c.course_id, c.title AS course_title,
       AVG(up.watched_duration) AS avg_watch_time
FROM courses c
JOIN videos v ON c.course_id = v.course_id
JOIN user_progress up ON v.video_id = up.video_id
GROUP BY c.course_id, c.title;

--