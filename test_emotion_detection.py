"""Unit tests for the emotion detector application."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_emotion_detector_joy(self):
        """Verify that the dominant emotion for a joyful statement is joy."""
        result = emotion_detector("Me alegra que esto haya sucedido")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_emotion_detector_anger(self):
        """Verify that the dominant emotion for an angry statement is anger."""
        result = emotion_detector("Estoy realmente enojado por esto")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_emotion_detector_disgust(self):
        """Verify that the dominant emotion for a disgusting statement is disgust."""
        result = emotion_detector("Me siento disgustado solo de escuchar sobre esto")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_emotion_detector_sadness(self):
        """Verify that the dominant emotion for a sad statement is sadness."""
        result = emotion_detector("Estoy tan triste por esto")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_emotion_detector_fear(self):
        """Verify that the dominant emotion for a fearful statement is fear."""
        result = emotion_detector("Tengo mucho miedo de que esto suceda")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()