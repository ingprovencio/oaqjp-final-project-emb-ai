
import requests
import json 
def emotion_detector(text_in):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": str(text_in) } }
    try:
        response = requests.post(URL, headers=HEADERS, json = input_json)
        response_json = response.json()
        return response_json['emotionPredictions'][0]['emotion']
    except Exception as e:
        print ('Error: ' + str(e))
        return None
package.emotion_detector = package.EmotionDetection
#print (emotion_detector("Me encanta esta nueva tecnología"))
