
# 🤖 GenAI-Shell-Agent
A Python-based AI agent powered by **Gemini 2.0 Flash** that can reason through tasks, execute local shell commands, and fetch real-time data via APIs.

## 🌟 Features
- **Self-Executing Loop:** The agent can "think" and decide whether it needs to use a tool or answer from its own knowledge.
- **Shell Integration:** Capability to create, read, and manage local files (HTML/CSS/JS) via `cat` and `ls` commands.
- **Real-time Data:** Integrated with a Bitcoin price fetcher using the CoinGecko API.
- **Project Scaffolding:** Can build entire web projects from a single prompt and open them in your browser.

---

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **LLM** | Google Gemini 2.0 Flash |
| **Language** | Python 3.x |
| **Networking** | Requests / Subprocess |
| **API** | Google GenAI SDK |

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- A Google Gemini API Key ([Get it here](https://aistudio.google.com/))

### 2. Installation
Clone the repository and install the required library:
```bash
git clone https://github.com/yourusername/genai-shell-agent.git
cd genai-shell-agent
pip install google-genai requests
```

### 3. Usage
Run the agent and give it a prompt:
```bash
python main.py
```
**Try asking:**
- *"Create a dark mode Tic-Tac-Toe game and open it."*
- *"What is the current price of Bitcoin?"*
- *"Create a python script that prints 'Hello World' and run it."*

---

## 🔧 How it Works
The agent follows the **ReAct (Reason + Act)** pattern. When a user submits a query, the agent:
1. **Analyzes** the intent.
2. **Selects** the appropriate tool (`execute_command` or `getBitcoinPrice`).
3. **Executes** the Python function locally.
4. **Observes** the output and sends it back to the LLM to provide a final response.

## Screen Shots
<img width="1057" height="149" alt="Screenshot 2026-03-26 at 11 05 11 PM" src="https://github.com/user-attachments/assets/cc3e5060-a0fa-4d8d-a054-0292359d1756" />

<img width="572" height="839" alt="Screenshot 2026-03-26 at 11 06 15 PM" src="https://github.com/user-attachments/assets/c7e9c15a-3c4b-4d9c-ba0e-4314f86d13d6" />
<img width="572" height="839" alt="Screenshot 2026-03-26 at 11 06 15 PM" src="https://github.com/user-attachments/assets/c7e9c15a-3c4b-4d9c-ba0e-4314f86d13d6" />
<img width="572" height="839" alt="Screenshot 2026-03-26 at 11 06 15 PM" src="https://github.com/user-attachments/assets/e9a7331e-d2fc-4a1c-83f9-a5bb138c60f5" />

