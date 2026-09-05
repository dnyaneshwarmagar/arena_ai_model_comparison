
import os
import time
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
port = int(os.environ.get("PORT", 7860))

openrouter_client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),   # your OpenRouter key
    base_url="https://openrouter.ai/api/v1"    # OpenRouter endpoint
)

groq_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),      # your Groq API key
    base_url="https://api.groq.com/openai/v1"
)

import time

def ask(client, model, prompt):
    time.sleep(1)  # prevent hitting rate limits
    try:
        r = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return r.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {str(e)}"


def battle(prompt):
    m1 = 'nvidia/nemotron-3-super-120b-a12b:free'
    try:
        a = ask(openrouter_client, m1, prompt)
        a = f"🟢 OpenRouter ({m1})\n\n{a}"
    except Exception as e:
        a = f"⚠️ OpenRouter error: {str(e)}"

    m2 = "openai/gpt-oss-120b"
    try:
        b = ask(groq_client, m2, prompt)
        b = f"🔵 Groq ({m2})\n\n{b}"
    except Exception as e:
        b = f"⚠️ Groq error: {str(e)}"

    return a, b



def vote(label):
    return f"📊 Thanks! You voted: **{label}**"   # in real apps, save this to a file/DB

with gr.Blocks(title="LLM Arena") as demo:
    gr.Markdown("# 🥊 LLM Arena — one prompt, two models")
    prompt = gr.Textbox(label="Ask both models the same thing")
    go = gr.Button("⚔️ Battle!", variant="primary")

    with gr.Row():
        with gr.Column():
            gr.Markdown("### 🤖 Model A (OpenRouter)")
            out_a = gr.Markdown()
            with gr.Row():
                up_a   = gr.Button("👍")
                down_a = gr.Button("👎")
        with gr.Column():
            gr.Markdown("### 🤖 Model B (Groq)")
            out_b = gr.Markdown()
            with gr.Row():
                up_b   = gr.Button("👍")
                down_b = gr.Button("👎")

    verdict = gr.Markdown()

    go.click(battle, inputs=prompt, outputs=[out_a, out_b])
    up_a.click(lambda: vote("👍 Mistral"), outputs=verdict)
    down_a.click(lambda: vote("👎 Mistral"), outputs=verdict)
    up_b.click(lambda: vote("👍 Groq"), outputs=verdict)
    down_b.click(lambda: vote("👎 Groq"), outputs=verdict)

demo.launch(server_name="0.0.0.0", server_port=port)   # → local + public link 🎉
