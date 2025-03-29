import json
import requests


def emotion_detector(text_to_analyze):
    '''
    This function predicts emotion for the specified text.
    '''
    # Define the URL for the emotion prediction service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    payload = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=payload, headers=header)

    # Create a result dictionary to store emotions and the dominant one among them
    result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    # If the response status code is 400, return result with everything set to None
    if response.status_code == 400:
        return result

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # Extract emotions from the response
    result['anger'] = formatted_response['emotionPredictions'][0]['emotion']['anger']
    result['disgust'] = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    result['fear'] = formatted_response['emotionPredictions'][0]['emotion']['fear']
    result['joy'] = formatted_response['emotionPredictions'][0]['emotion']['joy']
    result['sadness'] = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    # Find a dominant emotion
    dominant_score = 0.0
    for emotion, score in formatted_response['emotionPredictions'][0]['emotion'].items():
        if score > dominant_score:
            result['dominant_emotion'] = emotion
            dominant_score = score

    # Return the final result
    return result
