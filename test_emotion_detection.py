from EmotionDetection.emotion_detection import emotion_detector
import unittest

# Test cases for the emotion detection model
class TestEmotionDetection(unittest.TestCase):
    # Test case 1: Check if the emotion detection model returns the correct dominant emotion for a given text
    def test_emotion_detection(self):
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1["dominant_emotion"], "joy")

        # Test case 2: Check if the emotion detection model returns the correct dominant emotion for a given text
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2["dominant_emotion"], "anger")

        # Test case 3: Check if the emotion detection model returns the correct dominant emotion for a given text
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3["dominant_emotion"], "disgust")

        # Test case 4: Check if the emotion detection model returns the correct dominant emotion for a given text
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4["dominant_emotion"], "sadness")

        # Test case 5: Check if the emotion detection model returns the correct dominant emotion for a given text
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5["dominant_emotion"], "fear")

# Run the test cases
unittest.main()