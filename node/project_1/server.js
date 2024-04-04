const express = require('express');
const path = require('path');
const sqlite3 = require('sqlite3').verbose();

const app = express();
const PORT = process.env.PORT || 3000;

// Create and connect to the SQLite database
const db = new sqlite3.Database('calculations.db', (err) => {
    if (err) {
        console.error('Error opening database:', err.message);
    } else {
        console.log('Connected to the database.');
        // Create the calculations table if it doesn't exist
        db.run(`CREATE TABLE IF NOT EXISTS calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num1 REAL,
            num2 REAL,
            operator TEXT,
            result REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )`);
    }
});

// Serve the HTML file
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Add a calculation to the database
app.post('/calculate', (req, res) => {
    const { num1, num2, operator, result } = req.query;
    db.run(`INSERT INTO calculations (num1, num2, operator, result) VALUES (?, ?, ?, ?)`, [num1, num2, operator, result], (err) => {
        if (err) {
            console.error('Error inserting calculation into database:', err.message);
            res.status(500).send('Internal Server Error');
        } else {
            res.status(200).send('Calculation saved successfully');
        }
    });
});

// Get the last 20 calculations from the database
app.get('/calculations', (req, res) => {
    db.all(`SELECT * FROM calculations ORDER BY created_at DESC LIMIT 20`, (err, rows) => {
        if (err) {
            console.error('Error retrieving calculations from database:', err.message);
            res.status(500).send('Internal Server Error');
        } else {
            res.status(200).json(rows);
        }
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
