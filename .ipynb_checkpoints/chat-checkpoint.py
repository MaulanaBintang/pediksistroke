import streamlit as st
from transformers import pipeline, set_seed

# Inisialisasi generator teks dengan model bahasa pra-dilatih
generator = pipeline('text-generation', model='gpt-2')

# Fungsi untuk menghasilkan respons dari chatbot
def chatbot_response(prompt_text):
    # Menghasilkan teks dengan model bahasa
    set_seed(42)
    responses = generator(prompt_text, max_length=50, num_return_sequences=1)
    return responses[0]['generated_text']

# Membuat sidebar untuk input user
st.sidebar.title("Chatbot Copilot")
user_input = st.sidebar.text_area("Masukkan pesan Anda di sini:", key='user_input')

# Tombol untuk mengirim pesan
if st.sidebar.button('Kirim'):
    # Menampilkan pesan user
    st.sidebar.text_area("Pesan Anda:", value=user_input, key='user_msg', height=100)

    # Mendapatkan respons chatbot
    response = chatbot_response(user_input)

    # Menampilkan respons chatbot
    st.sidebar.text_area("Respons Copilot:", value=response, key='bot_response', height=100)

# Menjalankan aplikasi Streamlit
if __name__ == '__main__':
    st.title('Selamat datang di Chatbot Copilot')
    st.write('Chatbot ini menggunakan model bahasa GPT-2 untuk menghasilkan respons.')