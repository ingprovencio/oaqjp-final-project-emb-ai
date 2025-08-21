import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
           
    def test_joy(self):
        emotion = emotion_detector("I am glad this happened")
        self.assertEqual(emotion['dominant_emotion'], 'joy', "Expected 'joy' but got something else!")
    def test_anger(self):
        emotion = emotion_detector("I am really mad about this")
        self.assertEqual(emotion['dominant_emotion'], 'anger', "Expected 'anger' but got something else!")

    def test_disgust(self):
        emotion = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(emotion['dominant_emotion'], 'disgust', "Expected 'disgust' but got something else!")

    def test_sadness(self):
        emotion = emotion_detector("I am so sad about this")
        self.assertEqual(emotion['dominant_emotion'], 'sadness', "Expected 'sadness' but got something else!")

    def test_fear(self):
        emotion = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(emotion['dominant_emotion'], 'fear', "Expected 'fear' but got something else!")
    

if __name__ == '__main__':
    unittest.main()