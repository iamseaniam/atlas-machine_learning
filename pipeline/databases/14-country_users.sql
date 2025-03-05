-- creates a table "users" 
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country TEXT NOT NULL CHECK (country IN ('US', 'CO', 'TN')) DEFAULT 'US'
);
