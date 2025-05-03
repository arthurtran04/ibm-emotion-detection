# Emotion Detection Application using IBM Watson NLP Library

## Introduction

This repository is home to an **Emotion Detection Application** powered by the **IBM Watson NLP Library**. With a foundation in **Python** and support from **HTML** and **JavaScript**, the project combines backend processing with an intuitive interface to detect emotions effectively. It’s a practical implementation of NLP for emotional insights.

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
Emotion-Detection/
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
- Using Flask for back-end development
- Basic HTML, JavaScript and Bootstrap
- Using Pylint for code analysis

## Installation

To run this project on IBM Cloud IDE, open the Terminal and follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/arthurtran04/Emotion-Detection.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the Flask application, run the `cd` command to change the directory to `Emotion-Detection` and run the `app.py` file:

   ```bash
   cd ./Emotion-Detection
   python3.11 app.py
   ```
In the Skills Network Toolkit, launch your application at the port `5000`:

<img width="600rem" alt="Terminal" src="https://github.com/user-attachments/assets/bfbb25a3-ebb1-4004-bdcb-037403976a00" />

The UI:

<img width="600rem" alt="Webpage" src="https://github.com/user-attachments/assets/a74776a8-5451-42b5-bbf7-093db1f490b2" />

When you enter a text in the textbox, the webpage will display the emotion detection results including:

- **Joy**
- **Anger**
- **Disgust**
- **Sadness**
- **Fear**

they're attached with a score ranging from 0 to 1, represents the probability of each emotion. An emotion with the highest score will be the dominant emotion.

1. Joy:</br>
    <img width="600rem" alt="Webpage" src="https://github.com/user-attachments/assets/a74776a8-5451-42b5-bbf7-093db1f490b2" />
2. Anger:</br>
    <img width="600rem" alt="Anger" src="https://github.com/user-attachments/assets/dac87915-e083-4cf8-a45a-fe853de48aa2" />
3. Disgust:</br>
    <img width="600rem" alt="Disgust" src="https://github.com/user-attachments/assets/042fb3a3-957a-427d-9390-4c373fca610e" />
4. Sadness:</br>
    <img width="600rem" alt="Sadness" src="https://github.com/user-attachments/assets/09be53ba-8ea1-47f8-ab1d-66e064d21e89" />
5. Fear:</br>
    <img width="600rem" alt="Fear" src="https://github.com/user-attachments/assets/e4ed274e-c83a-437a-a2fb-fb85fa54d32a" />

If you try to enter text in another language or an invalid text, the webpage may respond with **Invalid input! Try again.**

6. Invalid input:</br>
    <img width="600rem" alt="INVALID INPUT" src="https://github.com/user-attachments/assets/262e449f-aa24-4dec-b718-e8c4b2b87db1" />

To stop the application, use `Ctrl + C` in the Terminal

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
