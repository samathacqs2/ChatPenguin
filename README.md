# 🐧 ChatPenguin — Streamlit Chatbot for the Palmer Penguins Dataset

**ChatPenguin** is a Streamlit-powered chatbot that uses the OpenAI API to answer questions about the [Palmer Penguins dataset](https://github.com/allisonhorst/palmerpenguins). It loads the dataset automatically from a GitHub-hosted CSV and provides an interactive chat interface where users can explore and analyze the data conversationally.

---

## 💬 What It Does

- Loads the **Palmer Penguins** dataset directly from a remote CSV file.
- Displays a preview of the data in a Streamlit app.
- Uses **OpenAI's GPT model** to respond to user questions based **only** on the dataset content.
- Filters out-of-scope questions (e.g., not related to penguins or dataset columns).
- Built entirely in Python using Streamlit and the OpenAI Python SDK.

---

## 📁 Project Files

```
├── chatpenguin.py             # Main Streamlit app
├── modelo_regresion.pkl       # Trained regression model (optional/not used in current chatbot)
├── palmer_penguins.csv        # Original dataset (also loaded from a remote URL)
├── requirements.txt           # Python dependencies
├── SamiKeyPair.pem            # SSH key (⚠️ do not share this publicly)
└── README.md                  # Project documentation
```

---

## 🚀 How to Run This App

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/chatpenguin.git
   cd chatpenguin
   ```

2. **(Optional) Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run chatpenguin.py
   ```

5. **Enter your OpenAI API key** in the sidebar of the app to begin chatting.

---

## 🔐 Note About Security

- `SamiKeyPair.pem` is likely an SSH private key. **Never expose this file publicly.**
- Consider adding it to your `.gitignore` file.

---

## 📊 About the Dataset

The [Palmer Penguins dataset](https://github.com/allisonhorst/palmerpenguins) provides data for 344 penguins from three species — Adelie, Chinstrap, and Gentoo — collected from islands in the Palmer Archipelago, Antarctica. It’s a popular alternative to the Iris dataset for classification tasks.

---

## 🧠 How It Works

When a user asks a question, the app:

1. Loads the dataset preview and column names.
2. Builds a context prompt for GPT to restrict answers to **only** what’s in the dataset.
3. Sends the prompt and question to the `gpt-3.5-turbo` model.
4. Displays the response in the chat interface.

---

## 📝 Example Questions You Can Ask

- What are the average body mass values by species?
- Which island has the most Gentoo penguins?
- What are the column names in this dataset?

---

## ⚠️ Disclaimer

This app is intended for **educational and demonstration purposes only**.  
It is **not** suitable for production use or sensitive data analysis.

---

## 📬 Contact

For questions, feedback, or ideas, feel free to open an issue or contact the author through GitHub.
