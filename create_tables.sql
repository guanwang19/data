
-- Users Table (users/models.py)
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    full_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Courses Table (courses/models.py)
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    total_videos INT NOT NULL DEFAULT 32,
    total_duration INTERVAL NOT NULL DEFAULT '16 hours'
);
-- Videos Table
CREATE TABLE videos (
    video_id SERIAL PRIMARY KEY,
    course_id INT REFERENCES courses(course_id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    duration INTERVAL NOT NULL,
    video_url TEXT NOT NULL,
    video_order INT NOT NULL,
    UNIQUE(course_id, video_order)
);

-- User Progress Tracking
CREATE TABLE user_progress (
    progress_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    video_id INT REFERENCES videos(video_id) ON DELETE CASCADE,
    last_watched TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    watched_duration INTERVAL NOT NULL DEFAULT '0 seconds',
    UNIQUE(user_id, video_id)
);


-- Payments Table (PayPal Transactions)
CREATE TABLE payments (
payment_id SERIAL PRIMARY KEY,
user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
payment_status VARCHAR(50) CHECK (payment_status IN ('Pending', 'Completed', 'Failed')) NOT NULL,
payment_amount DECIMAL(10, 2) NOT NULL,
payment_method VARCHAR(50) NOT NULL DEFAULT 'PayPal',
transaction_id VARCHAR(255) UNIQUE NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Video Access Tokens (Secure Streaming)
CREATE TABLE video_access (
access_id SERIAL PRIMARY KEY,
user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
video_id INT REFERENCES videos(video_id) ON DELETE CASCADE,
access_token TEXT UNIQUE NOT NULL,
expires_at TIMESTAMP NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Chatbot Queries Log
CREATE TABLE chatbot_queries (
query_id SERIAL PRIMARY KEY,
user_id INT REFERENCES users(user_id) ON DELETE SET NULL,
query_text TEXT NOT NULL,
response_text TEXT NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Email Support Requests
CREATE TABLE support_emails (
email_id SERIAL PRIMARY KEY,
user_id INT REFERENCES users(user_id) ON DELETE SET NULL,
email_subject VARCHAR(255) NOT NULL,
email_body TEXT NOT NULL,
status VARCHAR(50) CHECK (status IN ('Pending', 'Resolved')) NOT NULL DEFAULT 'Pending',
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);