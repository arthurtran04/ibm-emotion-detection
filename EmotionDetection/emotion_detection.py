# Import necessary libraries
import json
import requests

# Define the emotion_detector function
def emotion_detector(text_to_analyze):
    # Define the URL for the Watson Emotion API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Define the payload for the API request
    myobj = {"raw_document": {"text": text_to_analyze}}
    
    # Define the headers for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Make the API request
    response = requests.post(url, json=myobj, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        formatted_response = json.loads(response.text)
        
        # Extract the emotions from the response
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get) if emotions else None
        
        # Return the emotions and dominant emotion
        return {
            'anger': emotions.get('anger'),
            'disgust': emotions.get('disgust'),
            'fear': emotions.get('fear'),
            'joy': emotions.get('joy'),
            'sadness': emotions.get('sadness'),
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        # Return None values if the request was not successful
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }