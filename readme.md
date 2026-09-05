# 🥊 LLM Arena — Compare Two LLMs Side by Side

An interactive **LLM comparison application** built with **Python, Gradio, OpenRouter, and Groq**.

The application sends the **same user prompt to two different Large Language Models**, displays their responses side-by-side, and allows users to vote for the response they prefer.

This project demonstrates how multiple LLM APIs can be integrated into a single application to create a simple **LLM evaluation / model comparison platform**.

---

## 🚀 Project Overview

With the rapid growth of Large Language Models, choosing the right model for a particular task can be challenging.

Different models can vary in:

- Response quality
- Reasoning ability
- Response speed
- Accuracy
- Creativity
- Cost
- Instruction following

This project provides a simple interface where users can submit one prompt and compare responses from two different models.

### Workflow

```text
                User Prompt
                     │
                     ▼
             ┌───────────────┐
             │   Gradio UI   │
             └───────┬───────┘
                     │
             Same Prompt
              ┌──────┴──────┐
              ▼             ▼
       ┌─────────────┐ ┌─────────────┐
       │  OpenRouter │ │    Groq     │
       │   Nemotron  │ │ GPT-OSS 120B│
       └──────┬──────┘ └──────┬──────┘
              │               │
              ▼               ▼
        Model A Response  Model B Response
              │               │
              └───────┬───────┘
                      ▼
               Side-by-Side
                 Comparison
                      │
                      ▼
                 User Vote
```

---

# ✨ Features

- 🥊 Compare two LLMs using the same prompt
- 🤖 OpenRouter model integration
- ⚡ Groq model integration
- 🖥️ Interactive Gradio interface
- 🔐 API keys managed through environment variables
- 👍 / 👎 voting system
- 📊 Side-by-side response comparison
- 🌐 Public sharing using Gradio `share=True`
- 🐍 Built completely using Python

---

# 🤖 Models Used

## Model A — OpenRouter

Provider:

**OpenRouter**

Model:

```text
nvidia/nemotron-3-super-120b-a12b:free
```

The model is accessed through the OpenAI-compatible OpenRouter API endpoint.

---

## Model B — Groq

Provider:

**Groq**

Model:

```text
openai/gpt-oss-120b
```

The model is accessed through Groq's OpenAI-compatible API.

> Model availability and API access can change over time. Check the provider documentation if a model becomes unavailable.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Gradio | Web UI |
| OpenAI Python SDK | API client |
| OpenRouter | LLM API provider |
| Groq | LLM API provider |
| python-dotenv | Environment variable management |
| NumPy | Array utilities |

---

# 📁 Project Structure

```text
LLM-Arena/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/llm-arena.git
```

Move into the project directory:

```bash
cd llm-arena
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet:

```bash
pip install numpy gradio openai python-dotenv
```

---

# 🔑 API Keys Setup

This project requires API keys from:

- OpenRouter
- Groq

Create a `.env` file in the project root.

```env
OPENROUTER_API_KEY=your_openrouter_api_key
GROQ_API_KEY=your_groq_api_key
```

### ⚠️ Important

Never commit your `.env` file to GitHub.

Add this to `.gitignore`:

```text
.env
venv/
__pycache__/
```

---

# ▶️ Running the Application

Run:

```bash
python app.py
```

The Gradio application will start locally.

Because the application uses:

```python
demo.launch(share=True)
```

Gradio will also generate a temporary public URL that can be shared with others.

---

# 🖥️ Application Interface

The application contains:

### Prompt Input

Users enter a question or instruction.

Example:

```text
Explain RAG in simple terms.
```

### Battle Button

Click:

```text
⚔️ Battle!
```

The same prompt is sent to both models.

### Model A

The response generated through OpenRouter is displayed on the left.

### Model B

The response generated through Groq is displayed on the right.

### Voting

Users can select:

```text
👍
👎
```

to indicate which response they prefer.

---

# 🔄 How the Code Works

## 1. Load Environment Variables

```python
from dotenv import load_dotenv

load_dotenv()
```

This loads API keys from the `.env` file.

---

## 2. Create OpenRouter Client

```python
openrouter_client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)
```

The OpenAI Python SDK is used with OpenRouter's OpenAI-compatible API.

---

## 3. Create Groq Client

```python
groq_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
```

The same SDK is used to communicate with Groq.

---

## 4. Generic LLM Function

```python
def ask(client, model, prompt):
    time.sleep(1)

    try:
        r = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return r.choices[0].message.content

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
```

This function:

1. Receives an API client
2. Receives a model name
3. Receives the user prompt
4. Sends the request to the model
5. Extracts the generated response
6. Handles API errors

---

# 🥊 LLM Battle Function

```python
def battle(prompt):
```

The function sends the same prompt to both models.

### Model A

```python
m1 = 'nvidia/nemotron-3-super-120b-a12b:free'
```

The prompt is sent through OpenRouter.

### Model B

```python
m2 = "openai/gpt-oss-120b"
```

The prompt is sent through Groq.

The two responses are then returned to the Gradio interface.

---

# 📊 Voting System

The application provides a simple voting mechanism.

```python
def vote(label):
    return f"📊 Thanks! You voted: **{label}**"
```

Currently, votes are only displayed to the user and are **not persisted**.

---

# 💡 Future Improvements

The current application provides the basic LLM battle functionality. It can be extended into a more complete LLM evaluation platform.

### 1. Store Votes

Store votes in:

- SQLite
- PostgreSQL
- MongoDB
- CSV

Example:

```text
Prompt | Model | Vote | Timestamp
```

This would allow model performance to be analyzed over time.

---

### 2. Anonymous Model Evaluation

Instead of displaying:

```text
Model A
Model B
```

hide the model names from users.

Users select their preferred response without knowing which model generated it.

This reduces potential model-name bias.

---

### 3. Add More Models

Additional models can be added from:

- OpenRouter
- Groq
- OpenAI
- Anthropic
- Google Gemini

This could turn the project into a multi-model LLM benchmark platform.

---

### 4. Automated Evaluation

Instead of relying only on human votes, add an LLM-as-a-Judge system.

Possible evaluation criteria:

```text
Accuracy
Relevance
Coherence
Reasoning
Completeness
Helpfulness
```

---

### 5. Response Time Comparison

Record:

```text
Model
Response Time
Token Usage
Cost
User Rating
```

This would allow users to compare models based on both **quality and performance**.

---

### 6. Model Leaderboard

Create a leaderboard:

```text
Model              Win Rate
--------------------------------
Nemotron           62%
GPT-OSS 120B       38%
```

With enough user votes, this could become a useful model comparison dashboard.

---

# 🎯 Learning Outcomes

Through this project, I learned how to:

- Work with multiple LLM APIs
- Use OpenAI-compatible APIs
- Integrate OpenRouter
- Integrate Groq
- Manage API keys securely
- Build interactive interfaces using Gradio
- Handle API exceptions
- Compare LLM responses
- Implement basic human feedback collection
- Build an LLM evaluation workflow

---

# 🔮 Future Scope

The project can eventually evolve into a complete:

## LLM Evaluation & Benchmarking Platform

Possible architecture:

```text
                User Prompt
                     │
                     ▼
              Prompt Manager
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
   OpenRouter       Groq        Other APIs
       │             │             │
       └─────────────┼─────────────┘
                     ▼
              Response Evaluator
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
    Human Evaluation       LLM-as-Judge
          │                     │
          └──────────┬──────────┘
                     ▼
               Score Database
                     │
                     ▼
                Leaderboard
```

---

# 📌 Example Use Cases

This application can be used for:

- LLM model comparison
- Prompt experimentation
- AI education
- Model benchmarking
- Human preference collection
- LLM evaluation research
- Comparing response quality
- Testing models for specific use cases

---

# ⚠️ Security

Do not expose API keys directly in Python code.

### ❌ Avoid

```python
api_key="sk-xxxxxxxx"
```

### ✅ Use

```python
api_key=os.getenv("GROQ_API_KEY")
```

and store the key in `.env`.

Also make sure `.env` is included in `.gitignore`.

---

# 📝 Requirements

Example `requirements.txt`:

```text
numpy
pandas
gradio
openai
python-dotenv
```

---

# 👨‍💻 Author

**Dnyaneshwar Magar**

Machine Learning | AI | Generative AI | LLM Applications

---

# ⭐ Live Deployment Link:



# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

💬 Share your feedback

🤝 Connect with me on LinkedIn

---

## 📜 License

This project is intended for educational and demonstration purposes.