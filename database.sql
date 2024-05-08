DROP DATABASE ugroup_database;

-- Create a database
CREATE DATABASE ugroup_database;

-- Use the database
USE ugroup_database;

-- Create a table to store worksheets
CREATE TABLE Worksheet (
    worksheet_id INT PRIMARY KEY AUTO_INCREMENT,
    worksheet_name VARCHAR(255) NOT NULL
);

-- Create a table to store question types
CREATE TABLE QuestionType (
    question_type_id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(50) NOT NULL
);

-- Create a table to store questions
CREATE TABLE Question (
    question_id INT PRIMARY KEY AUTO_INCREMENT,
    worksheet_id INT,
    question_prompt TEXT NOT NULL,
    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,
    correct_answer TEXT,
    question_type_id INT NOT NULL,
    FOREIGN KEY (worksheet_id) REFERENCES Worksheet(worksheet_id),
    FOREIGN KEY (question_type_id) REFERENCES QuestionType(question_type_id)
);

-- Insert sample data into the Worksheet table
INSERT INTO Worksheet (worksheet_name) VALUES 
('January 2023'),
('February 2023'),
('March 2023'),
('April 2023'),
('May 2023');

-- Insert sample data into the QuestionType table
INSERT INTO QuestionType (type_name) VALUES 
('multiple-choice'),
('short-answer'),
('dropdown'),
('select-all');

-- Insert sample data into the Question table
INSERT INTO Question (worksheet_id, question_prompt, option_a, option_b, option_c, option_d, correct_answer, question_type_id) VALUES
(1, 'What is the nearest planet to the Sun?', 'Mercury', 'Venus', 'Earth', 'Mars', 'A', 1), 
(1, 'How many moons does Earth have?', 'One', 'Two', 'Three', 'Four', 'C', 1), 
(1, 'What color is the planet Mars?', 'Red', 'Blue', 'Green', 'Yellow', 'A', 1), 
(1, 'Name the largest ocean on Earth.', 'Atlantic', 'Pacific', 'Indian', 'Arctic', 'B', 1), 
(1, 'What is the capital city of France?', 'Paris', 'Berlin', 'London', 'Madrid', 'A', 1),
(2, 'Which planet is known as the "Morning Star" or "Evening Star"?', 'Mercury', 'Venus', 'Earth', 'Mars', 'B', 1), 
(2, 'What is the capital city of Italy?', 'Rome', 'Paris', 'Berlin', 'Madrid', 'A', 1), 
(2, 'What is the name of the largest desert in the world?', 'Sahara', 'Gobi', 'Kalahari', 'Arabian', 'A', 1), 
(2, 'Who was the first person to walk on the moon?', 'Neil Armstrong', 'Buzz Aldrin', 'Michael Collins', 'Yuri Gagarin', 'A', 1),
(3, 'What is the tallest mountain in the world?', 'Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse', 'A', 1), 
(3, 'Which country is known as the "Land of the Rising Sun"?', 'Japan', 'China', 'South Korea', 'Vietnam', 'A', 1), 
(3, 'Name the largest rainforest in the world.', 'Amazon', 'Congo', 'Borneo', 'Daintree', 'A', 1), 
(3, 'What is the chemical symbol for water?', 'H2O', 'CO2', 'NaCl', 'O2', 'A', 1), 
(4, 'What is the name of the fourth planet from the Sun?', 'Mercury', 'Venus', 'Earth', 'Mars', 'D', 1), 
(4, 'True or False: The Sun is a planet.', NULL, NULL, NULL, NULL, 'F', 2), 
(4, 'What is the largest animal on Earth?', 'Blue Whale', 'African Elephant', 'Giraffe', 'Killer Whale', 'A', 1), 
(4, 'Name the smallest planet in our solar system.', 'Mercury', 'Venus', 'Earth', 'Mars', 'A', 1), 
(4, 'Which country is known as the "Land of the Midnight Sun"?', 'Norway', 'Sweden', 'Finland', 'Iceland', 'A', 1), 
(5, 'Which planet is the largest in our solar system?', 'Mercury', 'Venus', 'Earth', 'Jupiter', 'D', 1), 
(5, 'Name the largest continent on Earth.', 'Asia', 'Africa', 'North America', 'Europe', 'A', 1), 
(5, 'What color is a polar bear''s fur?', 'White', 'Black', 'Brown', 'Gray', 'A', 1), 
(5, 'What is the capital city of Australia?', 'Sydney', 'Melbourne', 'Canberra', 'Perth', 'C', 1); 

-- Table to store group_members
CREATE TABLE GroupMembers(
    
    group_id INT PRIMARY KEY AUTO_INCREMENT,
    member_name VARCHAR(255) NOT NULL

); 

-- Table to store group member answers
CREATE TABLE GroupAnswers(

    group_answer CHAR(1),
    group_short_answer TEXT


);













