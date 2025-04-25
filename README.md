# Emotion Detection Application using IBM Watson NLP Library

## Introduction

## Table of Contents

- [Introduction](#introduction)
- [Prerequirements](#prerequirements)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Prerequirements

- IBM Cloud IDE
- IBM Watson NLP Library

## Project Structure

```
Emotion-Detection-App/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── .gitignore
├── static/
│   └── script.js
├── templates/
│   └── index.html
├── app.py
├── test_emotion_detection.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Features

- Emotion Detection Application using BERT model from IBM Watson NLP Library
- Deploy with Flask
- Basic routing
- Basic HTML, JavaScript and Bootstrap

## Installation

To run this project on IBM Cloud IDE, open the Terminal and follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/arthurtran04/Emotion-Detection-App.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the Flask application, run the `cd` command to change the directory to `Emotion-Detection-App` and run the `app.py` file:

   ```bash
   cd ./Emotion-Detection-App
   python3.11 app.py
   ```
In the Skills Network Toolkit, launch your application at the port `5000`:

<img width="600rem" alt="Terminal" src="https://github.com/user-attachments/assets/8e3a47e2-82a6-4583-9de4-71e440fce7c7" />

The UI:

<img width="600rem" alt="Webpage" src="https://github.com/user-attachments/assets/c3c409cf-53c0-49d8-8219-a735dcdefb8e" />

When you enter a text in the textbox, the webpage will display the sentiment analysis results including **POSITIVE**, **NEGATIVE** and **NEUTRAL**,</br>
they're attached with a score ranging from -1 to 1, representing the level of sentiment:
- score = -1 -> NEGATIVE
- score = 0 -> NEUTRAL
- score = 1 -> POSITIVE

1. Joy:</br>
    <img width="600rem" alt="Joy" src="https://github.com/user-attachments/assets/65b785a4-9dd4-4f2e-8f2f-5532ce798891" />
2. Anger:</br>
    <img width="600rem" alt="Anger" src="https://github.com/user-attachments/assets/28ebf4d3-6bff-4bd3-9240-a7f839fc6e01" />
3. Disgust:</br>
    <img width="600rem" alt="Disgust" src="https://github.com/user-attachments/assets/7a8745af-0130-447c-83aa-334b7b8fa319" />
4. Sadness:</br>
    <img width="600rem" alt="Sadness" src="https://github.com/user-attachments/assets/28ebf4d3-6bff-4bd3-9240-a7f839fc6e01" />
5. Fear:</br>
    <img width="600rem" alt="Fear" src="https://github.com/user-attachments/assets/7a8745af-0130-447c-83aa-334b7b8fa319" />

This model only works for English, so if you try to enter text in another language or an invalid text, the webpage will respond with **Invalid input! Try again.**

6. Invalid input:</br>
    <img width="600rem" alt="INVALID INPUT" src="https://github.com/user-attachments/assets/b496ed4e-2466-438d-9a55-59122789ae21" />

To stop the application, use `Ctrl + C` in the Terminal

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
