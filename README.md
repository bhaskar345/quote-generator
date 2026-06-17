# ✍️ AI Philosophy & Quote Generator

> Give it a few words, and watch it finish your thought. This app uses a quantized **DistilGPT-2** model running on **ONNX Runtime** to generate philosophical quotes and aphorisms from any starting prompt — fast, lightweight, and fully offline.

---

## ✨ What This App Does

Type the beginning of a quote — like *"The secret of getting ahead is"* — and the AI completes it in a thoughtful, quote-like style. Built with **Streamlit** for the UI and an **ONNX-quantized GPT-2** model for fast CPU-only inference, with no internet connection or API key required after setup.

| Feature | Description |
|---|---|
| 🪶 **Prompt-based generation** | Enter any quote starter and get an AI-generated continuation |
| 🎛️ **Adjustable creativity** | Control the `temperature` to make outputs more predictable or more imaginative |
| 📏 **Adjustable length** | Control the maximum word/token count of the generated quote |
| ⚡ **Fast & lightweight** | Runs on a quantized ONNX model — no GPU needed |

---

## 🗂️ Project Structure

```
quote-generator/
│
├── streamlit_app.py            # Main Streamlit application
├── requirements.txt            # Python dependencies
│
└── onnx_distilgpt2_quantized/
    ├── model_quantized.onnx        # Quantized ONNX model weights
    ├── config.json                 # Model configuration
    ├── tokenizer.json               # Tokenizer
    ├── tokenizer_config.json        # Tokenizer configuration
    └── special_tokens_map.json      # Special tokens mapping
```

---

## ⚙️ Installation

### Prerequisites

- Python **3.8+**
- `pip` package manager

### Step 1 — Clone or Download the Project

```bash
git clone https://github.com/bhaskar345/quote-generator.git
cd quote-generator
```

Or simply download and extract the project folder, then open a terminal inside it.

### Step 2 — Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv env

# Activate it
# On Windows:
env\Scripts\activate

# On macOS/Linux:
source env/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:

| Package | Purpose |
|---|---|
| `streamlit` | Web UI framework |
| `optimum[onnxruntime]` | Run the quantized ONNX GPT-2 model |
| `transformers` | Tokenizer and text-generation pipeline |

---

## 🚀 Running the App

Make sure your virtual environment is activated, then run:

```bash
streamlit run streamlit_app.py
```

The app will open automatically in your browser at:

```
http://localhost:8501
```

> 💡 **Note:** Ensure the `onnx_distilgpt2_quantized/` folder is present in the same directory as `streamlit_app.py`. The app loads the model and tokenizer from this folder at startup.

---

## 🖥️ Usage

1. **Open the app** in your browser after running the command above.
2. **Adjust the sidebar settings** (optional):
   - **Maximum Word Count** — controls how long the generated quote will be (10–100)
   - **Creativity (Temperature)** — higher values produce more random/creative text, lower values produce more predictable text (0.1–1.5)
3. **Enter a quote starter** in the text box, e.g.:
   - *"Life is like a..."*
   - *"The secret of getting ahead is"*
4. **Click "✨ Generate Quote"** — the AI will complete your prompt and display the full quote.

### Example

| Prompt | Settings | Generated Quote (example) |
|---|---|---|
| *"The secret of getting ahead is"* | Length: 30, Temp: 0.7 | *"The secret of getting ahead is getting started, and the secret of getting started is breaking your complex tasks into small manageable ones."* |
| *"Life is like a"* | Length: 25, Temp: 1.0 | *"Life is like a river — it never flows the same way twice."* |

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` with the venv activated |
| Model files not found | Ensure `onnx_distilgpt2_quantized/` is in the same directory as `streamlit_app.py` |
| App doesn't open in browser | Manually visit `http://localhost:8501` |
| Slow first load | Normal — the model is being loaded and cached on first run (`@st.cache_resource`) |
| Repetitive or odd output | Try increasing the temperature slider for more varied generations |

---

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io/) — for the effortless web UI
- [Hugging Face Optimum](https://huggingface.co/docs/optimum/index) — for ONNX export and runtime integration
- [ONNX Runtime](https://onnxruntime.ai/) — for fast, portable model inference
- [DistilGPT-2](https://huggingface.co/distilgpt2) — the base language model powering quote generation
