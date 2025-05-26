import streamlit as st
from tensorflow.keras.models import load_model
import pickle
import re
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import nltk
from nltk.corpus import stopwords

# ======== Preprocessing ========
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
STOPWORDS = set(stopwords.words("indonesian"))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9]", " ", text)
    text = " ".join([word for word in text.split() if word not in STOPWORDS])
    return text

# Path lokal di repo Streamlit Cloud
model_path = "my_model.keras"
tokenizer_path = "tokenizer_baru.pkl"

@st.cache_resource
def load_my_model(model_path, tokenizer_path):
    try:
        loaded_model = load_model(model_path)
        with open(tokenizer_path, 'rb') as f:
            loaded_tokenizer = pickle.load(f)
        return loaded_model, loaded_tokenizer
    except Exception as e:
        st.error(f"❌ Gagal memuat model atau tokenizer: {e}")
        return None, None

loaded_model, loaded_tokenizer = load_my_model(model_path, tokenizer_path)

MAX_LEN = 30

st.title("Deteksi Pertanyaan Duplikat")

if loaded_model and loaded_tokenizer:
    pertanyaan1_input = st.text_area("Masukkan Pertanyaan Pertama:", "")
    pertanyaan2_input = st.text_area("Masukkan Pertanyaan Kedua:", "")

    if st.button("Prediksi"):
        if pertanyaan1_input and pertanyaan2_input:
            pertanyaan1_cleaned = clean_text(pertanyaan1_input)
            pertanyaan2_cleaned = clean_text(pertanyaan2_input)

            q1_seq_test = loaded_tokenizer.texts_to_sequences([pertanyaan1_cleaned])
            q2_seq_test = loaded_tokenizer.texts_to_sequences([pertanyaan2_cleaned])

            q1_pad_test = pad_sequences(q1_seq_test, maxlen=MAX_LEN, padding='post')
            q2_pad_test = pad_sequences(q2_seq_test, maxlen=MAX_LEN, padding='post')

            input_for_prediction = [np.array(q1_pad_test), np.array(q2_pad_test)]
            prediction_prob = loaded_model.predict(input_for_prediction)

            threshold = 0.5
            probabilitas = prediction_prob[0][0]

            st.subheader("Hasil Prediksi:")
            st.write(f"Probabilitas Duplikat: {probabilitas:.4f}")

            if probabilitas > threshold:
                st.success("Hasil: Duplikat")
            else:
                st.info("Hasil: Tidak Duplikat")
        else:
            st.warning("Mohon masukkan kedua pertanyaan.")
else:
    st.error("Aplikasi tidak dapat berjalan karena model atau tokenizer gagal dimuat.")
