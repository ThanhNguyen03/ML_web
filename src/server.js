const express = require('express');
const fetch = require('node-fetch').default; // Note the .default
const path = require('path');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Endpoint for predictions
app.post('/predict', async (req, res) => {
    const { income, spending } = req.body;

    // Validate input
    if (typeof income !== 'number' || typeof spending !== 'number') {
        return res.status(400).send('Invalid input data');
    }

    try {
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ income, spending })
        });
        const data = await response.json();
        res.json(data);
    } catch (error) {
        console.error('Error:', error);
        res.status(500).send('Error making prediction');
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
