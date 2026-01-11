# gemini_chatbot
# CLI AI Assistant using Google Gemini

A command-line based AI assistant built in Python that uses **Google Gemini API** to answer user queries directly from the terminal.

The project demonstrates how to integrate a Large Language Model (LLM) into a simple CLI workflow using environment variables and Google’s SDK.

---

## 🚀 Features

- Command-line AI interaction
- Simple and minimal Python script
- Uses Google Gemini for text generation
- No frontend, no frameworks
- Designed for learning API integration and CLI tooling

---

## 🛠️ Tech Stack

- Python 3.x
- Google Gemini API
- `google-genai` SDK

---

## 📁 Project Structure

.
├── ask.py # Main CLI script
└── README.md # Project documentation

yaml
Copy code

---

## ▶️ How the Project Works

1. The user provides a question as a command-line argument.
2. The script reads the Gemini API key from an environment variable.
3. The query is sent to a Gemini model.
4. The generated response is printed in the terminal.

Example usage:
```bash
python ask.py "What is quantum computing in simple terms?"
⚙️ Setup (Intended)
Install dependencies:

bash
Copy code
pip install google-genai
Set the API key:

bash
Copy code
setx GEMINI_API_KEY "YOUR_API_KEY"
Run the script:

bash
Copy code
python ask.py "Your question here"
❗ Current Status: Not Working Without Billing
⚠️ Important Note

This project previously worked without billing enabled, but Google has updated its API access policy.

What changed:
Gemini API access is now restricted to billing-enabled Google Cloud projects

Even “free” Gemini models require billing to be enabled

Without billing, API requests return errors such as:

404 model not found

API version v1beta not supported

Key clarification:
Gemini still works in the browser (AI Studio chat)

Gemini does not work via API without billing enabled

This is an account-level restriction, not a bug in the code

As a result, the current implementation will not execute successfully unless billing is enabled on the associated Google Cloud project.

🧠 Why This Is Not a Code Issue
API key is valid

SDK usage is correct

Environment variables are set correctly

Errors originate from backend access restrictions imposed by Google

This behavior is due to policy changes, not incorrect implementation.

📌 Future Scope
Re-enable Gemini integration after billing is enabled

Add proper error handling and status messages

Extend CLI to support chat history

Make backend configurable

📄 License
This project is intended for educational and experimental purposes.

markdown
Copy code


