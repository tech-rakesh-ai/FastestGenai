import time
import streamlit as st
from groq import Groq
import matplotlib.pyplot as plt
import seaborn as sns

client = Groq(api_key=st.secrets['GROQ_API_KEY'])

st.set_page_config(page_title="GenAI Chat Completion", page_icon=":robot_face:")

models = {
    "gemma-7b-it": "gemma-7b-it",
    "gemma2-9b-it": "gemma2-9b-it",
    "mixtral-8x7b-32768": "Mixtral-8x7b-32768",
    "llama3-70b-8192": "llama3-70b-8192",
    "llama-3.1-70b-versatile": "llama-3.1-70b-versatile",
    "llama3-8B": "llama3-8b-8192",
    "llama-3.1-8b-instant": "llama-3.1-8b-instant",
    "llama3-groq-8b-8192-tool-use-preview": "llama3-groq-8b-8192-tool-use-preview",
    "llama3-groq-70b-8192-tool-use-preview": "llama3-groq-70b-8192-tool-use-preview"
}


# Center-align the main title
st.sidebar.title("Fastest GenAI :robot_face:")

# Add checkboxes for model selection
st.sidebar.title("Select Models")
selected_models = [model for model in models.keys() if st.sidebar.checkbox(model)]

# Add default questions as buttons
default_questions = ["What is generative AI?", "What is ML and DL?", "What are neural networks?"]
default_question = None

st.title("Ask a question")
cols = st.columns(len(default_questions))
for i, question in enumerate(default_questions):
    if cols[i].button(question):
        default_question = question

# Chat input for user to enter a message
user_message = st.chat_input("Try It!")

# Use the default question if clicked, otherwise use the user's input
if default_question:
    user_message = default_question

# Check if user has entered a message or clicked a default question

if selected_models:
    if user_message:
        response_times = []
        responses = []

        for model_name in selected_models:
            model_id = models[model_name]
            start = time.process_time()
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "user", "content": user_message}
                ],
                model=model_id
            )
            elapsed_time = time.process_time() - start
            response_times.append((model_name, elapsed_time))
            responses.append((model_name, chat_completion.choices[0].message.content))

        if len(selected_models) > 1:
            # Plot inference times using seaborn
            model_names, times = zip(*response_times)
            fig, ax = plt.subplots(figsize=(4, 2))  # Adjusted size for better readability
            sns.barplot(x=times, y=model_names, ax=ax, palette="viridis", hue=model_names, dodge=False, legend=False)
            ax.set_xlabel('Inference Time (s)', fontsize=5)
            ax.set_ylabel('Models', fontsize=5)
            ax.set_title('Inference Time by Model', fontsize=8)
            sns.despine(left=True, bottom=True)

            st.pyplot(fig)

            # Display responses
            response_cols = st.columns(len(selected_models))
            for i, (model_name, response) in enumerate(responses):
                response_cols[i].success(f"{model_name}:\n\n{response}")

            # Display response times and selected models in the sidebar
            st.sidebar.title("Model and Response Time")
            for model_name, elapsed_time in response_times:
                st.sidebar.info(f"**{model_name}:** {elapsed_time:.4f} seconds")

        else:
            col1, col2 = st.columns(2)
            col1.info(f"**Selected Model:** {selected_models[0]}")
            col2.info(f"**Response Time:** {response_times[0][1]:.4f} seconds")
            st.success(responses[0][1])
else:
    st.warning("Please select a model first!")

st.sidebar.title("About")
st.sidebar.info(
    "This app demonstrates AI-powered fastest chat completion using different open LLMs.\n\n"
    "Enter a message, and the AI will generate a response based on the model selected.\n\n"
    "Choose one or more models using the checkboxes below."
)

st.sidebar.divider()
st.sidebar.write(
    "Developed🚀 by **Rakesh Kumar**\n"
    "\n Feel free to connect and share your feedback(✨)"
    "\n on LinkedIn: [Rakesh Kumar](https://www.linkedin.com/in/m-rakesh-kr/)"
)
st.sidebar.divider()

st.sidebar.text('© 2024 Gen AI Chat Completion.')
