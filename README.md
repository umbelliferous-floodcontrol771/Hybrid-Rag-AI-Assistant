# 🤖 Hybrid-Rag-AI-Assistant - Smart AI Help with Vector Search

[![Download](https://img.shields.io/badge/Download-Hybrid--Rag--AI--Assistant-4CAF50?style=for-the-badge&logo=github)](https://github.com/umbelliferous-floodcontrol771/Hybrid-Rag-AI-Assistant)

---

## 🔎 What is Hybrid-Rag-AI-Assistant?

Hybrid-Rag-AI-Assistant is a desktop application that helps you get answers and information quickly by combining several AI tools. It uses vector search, Wikipedia information, and smart language models to provide helpful responses. The app runs on your Windows PC and requires no programming knowledge.

This tool is built with Python and uses technologies like FAISS for fast search, Streamlit for the interface, and several AI methods behind the scenes. It aims to give you clear answers by combining local data search and online knowledge sources.

---

## 💻 System Requirements

Before installing, make sure your PC meets these requirements:

- Windows 10 or newer (64-bit)
- At least 4 GB of RAM (8 GB recommended)
- 2 GHz or faster processor
- 1 GB free disk space
- Internet connection for fetching Wikipedia data and AI processing
- Python 3.8 or newer installed (easy to install if you don’t have it)

---

## 🚀 Getting Started: Download and Run

### Step 1: Download the application

Go to the download page by clicking the big button below:

[![Download](https://img.shields.io/badge/Download-Hybrid--Rag--AI--Assistant-blue?style=for-the-badge&logo=github)](https://github.com/umbelliferous-floodcontrol771/Hybrid-Rag-AI-Assistant)

This link will take you to the GitHub repository where you can get the app.

### Step 2: Get the files

On the GitHub page:

- Click **Code** (green button) on the top right
- Select **Download ZIP**
- Save the ZIP file to your desktop or downloads folder

### Step 3: Extract the files

- Right-click the ZIP file
- Select **Extract All**
- Choose a folder where you want to keep the app files
- Click **Extract**

### Step 4: Install Python (if needed)

Hybrid-Rag-AI-Assistant requires Python. If you don’t have it:

- Visit https://www.python.org/downloads/
- Download the latest version for Windows
- Run the installer and check “Add Python to PATH”
- Complete the install wizard

### Step 5: Run the application

- Open the extracted folder
- Find the file named `run_app.bat` or `start.bat`
- Double-click it to launch the app

The app will open in your web browser using Streamlit’s interface. You can now use the AI assistant.

---

## ⚙️ How to Use Hybrid-Rag-AI-Assistant

### Ask questions

Type your question in the box and press Enter or click the send button. The app will search local data and Wikipedia to find answers.

### Switch between tools

The assistant uses several methods:

- Vector Search (fast local search)
- Wikipedia tool (fetches live info from Wikipedia)
- Language model routing (chooses the best AI model for your question)

You don’t have to do anything to switch between these. The app decides automatically.

### Reset or clear chat

Use the provided buttons to clear the conversation if you want to start over.

---

## 🛠 Troubleshooting

- If the app does not open, make sure Python is installed and added to your system path.
- If you see an error about missing packages, open a Windows command prompt in the app folder and type:  
  `pip install -r requirements.txt`
- Slow responses may mean your internet connection is weak.
- If the app window closes immediately, double-click `run_app.bat` from File Explorer instead of running from command prompt directly.

---

## 📁 What’s Inside This Package?

- Python files (`.py`): The core AI code and logic.
- `requirements.txt`: List of Python packages needed.
- `run_app.bat`: A batch file to start the app.
- README.md: This file.
- Other supporting files for AI tools and data.

No setup beyond installing Python and packages is needed.

---

## 🔧 How It Works (Simple Explanation)

- **Vector Search**: The app converts your question into a form that computers can search quickly in local data.
- **Wikipedia Tool**: It fetches up-to-date facts from Wikipedia on demand.
- **Language Model Routing**: The app chooses the best AI language model based on your question type. This gives more accurate answers.

All these parts run quietly in the background. You only see the chat interface.

---

## 📋 Updating the Application

To update to the latest version:

- Go back to the [GitHub page](https://github.com/umbelliferous-floodcontrol771/Hybrid-Rag-AI-Assistant)
- Download the newest ZIP file
- Extract it to your folder, replacing old files

---

## 👨‍💻 Advanced Users

If you want to run or modify the code, open the folder in any code editor or IDE like Visual Studio Code.

You can install all Python dependencies with:

```
pip install -r requirements.txt
```

You can run the app by typing in the command prompt while inside the folder:

```
streamlit run main.py
```

---

## 🏷 Topics

This app relates to:

- agentic-ai  
- ai  
- faiss-vector-database  
- generative-ai  
- langchain  
- nlp  
- python  
- rag-chatbot  
- streamlit  
- vector-embeddings

Use these keywords if you want to search for similar projects or learn more.

---

## 📥 Download Link (Again)

For easy access, use this link to download the app files:

[https://github.com/umbelliferous-floodcontrol771/Hybrid-Rag-AI-Assistant](https://github.com/umbelliferous-floodcontrol771/Hybrid-Rag-AI-Assistant)