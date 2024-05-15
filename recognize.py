import fasttext

# Ładowanie pre-trenowanego modelu
model = fasttext.load_model('./trained_model.bin')

# Funkcja do rozpoznawania języka
def recognize_language(text):
    prediction = model.predict(text, k=3)
    print(prediction)
    language = prediction[0][0].replace('__label__', '')
    confidence = prediction[1][0]
    return language, confidence

# # Przykładowe użycie
# text = "Tekst w języku polskim."
# language, confidence = recognize_language(text)