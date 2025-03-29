'''
Route handlers for Emotion Detector web application
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")


@app.route("/")
def home():
    '''
    Route handler for home page.
    '''
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    '''
    Route handler for detecting emotion using emotion_detector() api.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the label is None, indicating an error or invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Return response with success status code
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion "
        f"is {response['dominant_emotion']}."
    )


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
