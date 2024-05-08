<!-- Install node packages, this is needed to the Express server -->
Go into terminal and run: 
npm install 

<!-- Run schema file to create database locally -->
log into MySQL and follow commands
mysql> CREATE DATABASE UGroupDatabase;
mysql> USE UGroupDatabase;
mysql> source schema.sql;
If you want to check your data is saved/created
mysql> SELECT * FROM Questions;

<!-- Run server.js file to start server -->
Go to server.js file and update lines 16/17 to be your username/password you use to log in to mysql locally.
Go into terminal and run: 
node server.js
Open http://localhost:4000 in your browser and voila! 

<!-- Steps for running python in virtual environment -->
python3 -m venv path/to/venv
source path/to/venv/bin/activate
python3 server.py
pip install Flask
pip install pymysql