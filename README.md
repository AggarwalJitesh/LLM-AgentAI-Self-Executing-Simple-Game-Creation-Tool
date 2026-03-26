
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
**TicTacToe**
<img width="1057" height="149" alt="Screenshot 2026-03-26 at 11 05 11 PM" src="https://github.com/user-attachments/assets/cc3e5060-a0fa-4d8d-a054-0292359d1756" />

<img width="572" height="839" alt="Screenshot 2026-03-26 at 11 06 40 PM" src="https://github.com/user-attachments/assets/2711bcc8-f909-4337-ad5c-3fe2e2bd5c78" />

<img width="572" height="839" alt="Screenshot 2026-03-26 at 11 06 15 PM" src="https://github.com/user-attachments/assets/209877bd-25bd-41ba-a78d-aa751b6d3df3" />

**Connect4**

<img width="1016" height="127" alt="Screenshot 2026-03-26 at 11 07 49 PM" src="https://github.com/user-attachments/assets/ec22f9fa-5876-4644-a1ec-fd4ddd5f71f2" />

<img width="570" height="827" alt="Screenshot 2026-03-26 at 11 12 36 PM" src="https://github.com/user-attachments/assets/9e6464ec-6ec7-4917-a895-d2a665038af9" />

<img width="570" height="827" alt="Screenshot 2026-03-26 at 11 12 21 PM" src="https://github.com/user-attachments/assets/426b8ce7-2c73-4810-ad00-0ebff5f32d56" />


**2048 Game**

<img width="1043" height="279" alt="Screenshot 2026-03-26 at 11 21 24 PM" src="https://github.com/user-attachments/assets/839e7339-ca2f-49c1-b3e2-5e2c1766667e" />
<img width="570" height="827" alt="Screenshot 2026-03-26 at 11 20 30 PM" src="https://github.com/user-attachments/assets/df576cf5-752b-49df-8c62-5b0e06a06dd9" />

<img width="570" height="827" alt="Screenshot 2026-03-26 at 11 21 00 PM" src="https://github.com/user-attachments/assets/07517de1-ee2a-4bab-99ec-e2ad3da362b1" />

<img width="372" height="410" alt="Screenshot 2026-03-26 at 11 21 39 PM" src="https://github.com/user-attachments/assets/b98e187b-39ee-4b25-a410-edb9c7164a1c" />



