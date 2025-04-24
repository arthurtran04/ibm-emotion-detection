'''
This is a Flask application that uses the emotion_detection module to detect emotions in text.
It provides a web interface for users to input text and get the emotion detection results.
'''
# Import necessary modules
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Create a Flask application
app = Flask("Emotion Detector")

# Define the route for the main page
@app.route("/")
def render_index_page():
    '''
    This function renders the index.html page.
    '''
    # Render the index.html page
    return render_template("index.html")

# Define the route for the emotion detection
@app.route("/emotionDetector")
def emo_detector():
    '''
    This function detects the emotion in the text.
    '''
    # Get the text to analyze from the request
    text_to_analyze = request.args.get("textToAnalyze")

    # Detect the emotion in the text
    response = emotion_detector(text_to_analyze)

    # Get the scores and the dominant emotion
    anger, disgust, fear, joy, sadness, dominant = response.values()

    # If the dominant emotion is None, return an error message
    if dominant is None:
        return 'Invalid text! Please try again!'
    # Return the results
    return f"For the given statement, the system response is 'anger': {anger}, " + \
           f"'disgust': {disgust}, " + \
           f"'fear': {fear}, " + \
           f"'joy': {joy}, " + \
           f"'sadness': {sadness}. " + \
           f"The dominant emotion is {dominant}."

# Run the application
if __name__ == "__main__":
    app.run(debug=False)
