CREATE DATABASE IF NOT EXISTS dlc_logs;
USE dlc_logs;

CREATE TABLE IF NOT EXISTS remote_hosts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hostname VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS logs_archive (
    id INT AUTO_INCREMENT PRIMARY KEY,
    host_id INT,
    log_level ENUM('INFO', 'WARN', 'ERROR'),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (host_id) REFERENCES remote_hosts(id)
);
