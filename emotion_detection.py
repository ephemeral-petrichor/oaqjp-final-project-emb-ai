"""Emotion detection using the Watson NLP EmotionPredict service."""

import json

import requests

EMOTION_URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"


def emotion_detector(text_to_analyze):
    """Detect emotions in the given text and return a formatted score dictionary.

    Args:
        text_to_analyze (str): The text to analyze for emotion detection.

    Returns:
        dict: A dictionary with the scores for anger, disgust, fear, joy and
            sadness, plus the dominant emotion.
    """
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(EMOTION_URL, json=input_json, headers=headers, timeout=10)
    formatted_response = json.loads(response.text)
    emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]
    anger_score = emotion_scores["anger"]
    disgust_score = emotion_scores["disgust"]
    fear_score = emotion_scores["fear"]
    joy_score = emotion_scores["joy"]
    sadness_score = emotion_scores["sadness"]
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }