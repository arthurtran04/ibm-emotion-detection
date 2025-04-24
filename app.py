from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    anger_score, disgust_score, fear_score, joy_score, sadness_score, dominant_emotion = response.values()
    if dominant_emotion is None:
        return 'Invalid text! Please try again!'
    return f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run(debug=False)