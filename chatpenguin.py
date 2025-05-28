from openai import OpenAI
import streamlit as st
import pandas as pd

# 👉 URL fija del archivo CSV
CSV_URL = 'https://raw.githubusercontent.com/samathacqs2/ChatPenguin/refs/heads/main/palmer_penguins.csv'

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

# Cargar automáticamente el CSV desde la URL
try:
    df = pd.read_csv(CSV_URL)
    st.session_state["df"] = df
    st.success("✅ Dataset cargado exitosamente desde URL.")
except Exception as e:
    st.error(f"❌ Error al cargar el archivo CSV: {e}")
    st.stop()

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")



if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hola, que te interesa saber los pinguinos de Palmer?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Has tu pregunta sobre pinguinos de Palmer"):
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
      # Crear contexto desde las primeras filas del CSV
    df = st.session_state["df"]
    preview = df.to_string(index=False)
    columns_info = ", ".join(df.columns)

    context = f"""
Eres un asistente especializado que responde preguntas exclusivamente sobre el siguiente dataset.

Columnas del dataset: {columns_info}

Aquí hay una muestra del contenido del dataset:
{preview}

Reglas importantes:
- Si la pregunta no está relacionada con el dataset (sus columnas, sus valores o análisis posibles), responde amablemente que no puedes ayudar con temas fuera del dataset.
- Si la pregunta sí está relacionada, responde de manera clara, usando solo la información visible del dataset.


Responde a la siguiente pregunta del usuario basándote únicamente en el contenido del dataset:
"""
    client = OpenAI(api_key=openai_api_key)

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt},
        ]
    )
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

# HOW TO RUN THE APP
# Open terminal (Open in integrated terminal)
# Go to the folder where the my_chatbot.py file is located
# Run the following command: streamlit run my_chatbot.py