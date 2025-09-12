CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL,
    name VARCHAR(20) NOT NULL,
    surname VARCHAR(20) NOT NULL
);

INSERT INTO users (username, password, name, surname) VALUES
('admin', 's3cr3tP@$$wd', 'Adminko', 'Adminić'),
('user1', 'pass1', 'Pera', 'Perić'),
('user2', 'pass2', 'Mina', 'Minić'),
('user3', 'pass3', 'Laza', 'Lazić');

CREATE TABLE profiles (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) UNIQUE NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'user',
    private BOOLEAN NOT NULL,
    gender CHAR NOT NULL,
    dob DATE NOT NULL,
    status VARCHAR(200)
);

INSERT INTO profiles (user_id, role, private, gender, dob, status) VALUES
(1, 'admin', TRUE, 'M', '1990-10-10', 'I am the admin and my profile is private.'),
(2, 'moderator', FALSE, 'M', '1992-01-01', 'I am user1 and my profile is public.'),
(3, 'user', FALSE, 'F', '1993-02-02', 'I am user2 and my profile is public.'),
(4, 'user', TRUE, 'M', '1994-03-03', 'I am user3 and my profile is private.');

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) NOT NULL,
    subject VARCHAR(200) NOT NULL,
    body TEXT NOT NULL
);

INSERT INTO messages (user_id, subject, body) VALUES
(1, '2FA backup codes', '123456, 654321, 987654, 456789'),
(1, 'Payroll Report Q3', 'Attached is the salary sheet for all employees.'),
(1, 'Confidential Project', 'Codename: Blackbird. Launch planned for December.'),
(2, 'Password reset', 'Here is your temporary password: tempPass!23'),
(2, 'Family Photos', 'Dropbox link: https://tinyurl.com/photos-secret'),
(3, 'Your order has shipped', 'Tracking number: 123456789.'),
(4, 'Private Chat Export', 'Conversation with Jane: "I can’t tell anyone about this..."'),
(4, 'Bank statement', 'Balance: $5,231.29. Last transaction: -$200 at ATM.');
