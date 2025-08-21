
import requests
import json 
def emotion_detector(text_in):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": str(text_in) } }
    try:
        response = requests.post(URL, headers=HEADERS, json = input_json)
        formatted_response = response.json()
        if response.status_code == 200:
            anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
            disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
            fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
            joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
            sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
            dominant_emotion = max(formatted_response['emotionPredictions'][0]['emotion'], key = formatted_response['emotionPredictions'][0]['emotion'].get)
        else:
            anger_score = None
            disgust_score = None
            fear_score = None
            joy_score = None
            sadness_score = None
            dominant_emotion = None
        return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
    except Exception as e:
        print ('Error: ' + str(e))
        return None
#package.emotion_detector = package.EmotionDetection
#print (emotion_detector("Me encanta esta nueva tecnología"))
