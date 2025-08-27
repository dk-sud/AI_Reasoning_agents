# 🤖 AI Agents Projects (Agno-based)

This README combines two independent yet powerful AI agent projects using the `agno` agent framework, OpenAI/Groq models, and built-in tools for real-world knowledge extraction, reasoning, and financial reporting.

---

## 📁 Projects Overview

### 1. 📉 Financial Reasoning Agent
- Performs in-depth analysis of a company's financial performance.
- Uses OpenAI's LLM + `yfinance` data + reasoning tools.
- Responds in Markdown tables with detailed metrics, recommendations, and indicators.

**Key File:** `reasoning_agent.py`

---

### 2. 🌍 Trade Policy News Agent
- Explores the impact of USA's tariffs on India using real-time search.
- Uses Groq model and DuckDuckGo search tooling for live updates.
- Answers economic/trade queries with a concise summary.

**Key File:** `main.py`

---

## 🧠 Tech Stack

| Component        | Technology/Tool                     |
|------------------|-------------------------------------|
| LLM Models       | OpenAI Chat API, Groq API           |
| Agent Framework  | [`agno`](https://pypi.org/project/agno/)                       |
| Tools Used       | DuckDuckGo, YFinance, Reasoning     |
| Env Management   | `python-dotenv`                     |

---

## ⚙️ Setup Instructions

1. **Install dependencies**

```bash
pip install agno python-dotenv
```

2. **Set environment variables**

Create a `.env` file in the root directory with:

```dotenv
GROQ_API_KEY=your-groq-api-key
OPENAI_API_KEY=your-openai-api-key
```

---

## ▶️ How to Run

### Run the Financial Analyst Agent:

```bash
python reasoning_agent.py
```

### Run the Trade News Agent:

```bash
python main.py
```

---

## 🔍 Example Prompts

### Financial Analyst:
- "Analyze and prepare a report summary of AMD's performance in the last quarter of last financial year."

### Trade Tariff News:
- "What will get cheaper and what is expensive with US tariffs?"

---

## 📝 Output Style

- Markdown table format
- Streamed intermediate reasoning steps
- Structured and human-friendly responses

---

## 💡 Customization Ideas

- Add more tooling (e.g., Google News, Arxiv for research agents)
- Enable multi-agent collaboration (e.g., reasoner + summarizer)
- Integrate with dashboards or chat interfaces

---

## 📜 License

MIT License
