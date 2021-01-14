# Identifikasi Duplikat Pertanyaan Menggunakan Global Vector Dalam Bahasa Indonesia

Ini merupakan dokumentasi program ***Deep Learning*** yang saya buat berbasis web ataupun text

## Informasi

1. **Quora Indonesia** Dataset yang digunakan
2. **Wikipedia Indonesia** Merupakan corpus yang digunakan
3. **Global Vector (GloVe)** Word Embedding dalam program ini
4. **Bidirectional Long Short Term Memory (Bi-LSTM)** adalah model yang digunakan


## Requirements

1. **Google Colab**
2. **Streamlit**
3. **Ngrok**

## Mulai

Untuk membuat program [notebook program](https://github.com/anjasopo/identifikasi-duplikat-pertanyaan-indonesia-glove/blob/main/Identifikasi%20Duplikat%20Pertanyaan.ipynb)
Untuk cek validasi program yang dibuat [notebook cek program](https://github.com/anjasopo/identifikasi-duplikat-pertanyaan-indonesia-glove/blob/main/Cek%20Duplikat%20Pertanyaan.ipynb)

Langkah - langkah Cek :

1. Pastikan dalam Colab runtime sudah diubah ke GPU.
2. Install **streamlit**. Run `!pip install streamlit`
3. Install **ipykernel**. Run `!pip install ipykernel~=4.10`
6. Jalankan proses script `streamlit` untuk membuat program (`config, process dan app`)
9. Download **ngrok** and install
    ```
    !wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
    !unzip -qq ngrok-stable-linux-amd64.zip
    ```

10. Jalankan `!streamlit run app.py &>/dev/null&`. Terkadang perintah tidak bisa jalan, maka bisa dilakukan pengulangan untuk menjalankan perintahnya
11. Run 
    ```
    get_ipython().system_raw('./ngrok http 8501 &')
    ! curl -s http://localhost:4040/api/tunnels | python3 -c \
      "import sys, json; print(json.load(sys.stdin)['tunnels'][0]['public_url'])"
    ```
    Terkadang untuk men-generate URL terjadi errror maka bisa dilakukan dengan menjalankan ulang perintah ini.
    
    **Jangan dijalankan dulu.** Jalankan setelah program dibawah ini :
    
12. Jalankan streamlit : `!streamlit run app.py`. Teriakhir, **klik url** yang merupakan generate url dari ngrok.

# Hasil

## 1. Pertanyaan Duplikat
![Identifikasi Pertanyaan Bahasa Indonesia (Duplikat)](https://github.com/anjasopo/identifikasi-duplikat-pertanyaan-indonesia-glove/blob/main/Duplikat.jpg)

## 2. Pertanyaan Berbeda (Tidak Duplikat)
![Identifikasi Pertanyaan Bahasa Indonesia (Berbeda)](https://github.com/anjasopo/identifikasi-duplikat-pertanyaan-indonesia-glove/blob/main/Berbeda.jpg)

## 3. Visualisasi Word Embedding Pada Dataset (Quora Indonesia)
![Visualisasi Word Embedding (Glove) Quora Indonesia](https://github.com/anjasopo/identifikasi-duplikat-pertanyaan-indonesia-glove/blob/main/Visualisasi%20Word%20Embedding%20dataset.png)

Terimakasih!
