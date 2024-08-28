"""
server.py

This module implements a Flask web server that provides an interface for
emotion detection. It includes routes to handle HTTP requests for emotion
analysis and render a web interface.

Routes:
- /emotionDetector: Receives text input, runs emotion detection, and returns
  the results or an error message if the text is invalid.
- /: Renders the HTML interface for user interaction.

Functions:
- emotion_detector_function: Handles requests to /emotionDetector, calls
  the emotion_detector function, and returns the analysis results.
- render_index_page: Renders the HTML interface at the root URL.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector") # Define App

@app.route("/emotionDetector")
def emotion_detector_function():
    ''' This code receives the text from HTML interface
        and runs sentiment analysis over it using the 
        function emotion_detector()
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    # Call emotion_detector function
    result = emotion_detector(text_to_analyse)
    # Extract values from result
    anger = result.get('anger')
    disgust = result.get('disgust')
    fear = result.get('fear')
    joy = result.get('joy')
    sadness = result.get('sadness')
    dominant_emotion = result.get('dominant_emotion')
    if dominant_emotion is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

@app.route("/", methods=["GET"])
def render_index_page():
    ''' This is the function to render the HTML interface '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
