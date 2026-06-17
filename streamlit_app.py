import streamlit as st
from optimum.onnxruntime import ORTModelForCausalLM
from transformers import AutoTokenizer, pipeline

st.set_page_config(page_title="AI Quote Generator", page_icon="✍️", layout="centered")

st.title("✍️ AI Philosophy & Quote Generator")
st.write("Type a prompt below, and the model will generate the rest of the quote.!")

@st.cache_resource
def load_onnx_pipeline():
    local_model_path = "./onnx_distilgpt2_quantized"
    model = ORTModelForCausalLM.from_pretrained(local_model_path,file_name="model_quantized.onnx", provider="CPUExecutionProvider")
    tokenizer = AutoTokenizer.from_pretrained(local_model_path)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

with st.spinner("🧠 Loading AI model weights..."):
    generator = load_onnx_pipeline()

st.sidebar.header("⚙️ Generation Settings")

max_length = st.sidebar.slider(
    "Maximum Word Count", 
    min_value=10, 
    max_value=100, 
    value=30, 
    step=5
)

temperature = st.sidebar.slider(
    "Creativity (Temperature)", 
    min_value=0.1, 
    max_value=1.5, 
    value=0.7, 
    step=0.1,
    help="Higher values make the quotes more random and creative. Lower values make them predictable."
)

prompt = st.text_input(
    "Enter a quote starter:", 
    placeholder="Life is like a...",
    value="The secret of getting ahead is"
)

if st.button("✨ Generate Quote", type="primary"):
    if prompt.strip() == "":
        st.warning("⚠️ Please type a prompt first!")
    else:
        with st.spinner("🔮 The AI is thinking..."):
            results = generator(
                prompt,
                max_length=max_length, 
                do_sample=True, 
                temperature=temperature,
                top_p=0.92,
                repetition_penalty=1.2,
                no_repeat_ngram_size=3
            )
            
            generated_text = results[0]['generated_text']
                        
            st.markdown(f"### “ {generated_text} ”")
