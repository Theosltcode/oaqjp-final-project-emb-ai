"""
Serveur Flask pour l'application de détection d'émotions.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyse le texte fourni via la requête GET et renvoie les émotions.
    """
    # Récupération du texte depuis les paramètres d'URL (ex: /emotionDetector?textToAnalyze=...)
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Exécution de la détection d'émotions
    response = emotion_detector(text_to_analyze)
    
    # Extraire les valeurs pour construire la réponse formatée
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Chaîne de réponse au format exact demandé par l'exercice
    formatted_response = (
        f"Pour l'énoncé donné, la réponse du système est "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} et 'sadness': {sadness}. "
        f"L'émotion dominante est {dominant_emotion}."
    )
    
    return formatted_response

@app.route("/")
def render_index_page():
    """
    Affiche la page d'accueil index.html.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)