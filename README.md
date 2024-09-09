# GenAI Chat Completion

**GenAI Chat Completion** is a powerful and fast AI-based chat application built using Streamlit. This app allows users to interact with various state-of-the-art open-source Large Language Models (LLMs) and compare their response times. It provides a user-friendly interface where users can select multiple models, ask questions, and receive responses from each model, along with their respective inference times.

## Features

### 1. **Model Selection**
- Users can select one or more models from the following options:
  - `gemma-7b-it`
  - `gemma2-9b-it`
  - `Mixtral-8x7b-32768`
  - `llama3-70b-8192`
  - `llama3-8B`
  - `llama-3.1-70b-versatile`
  - `llama-3.1-8b-instant`
  - `llama3-groq-8b-8192-tool-use-preview`
  - `llama3-groq-70b-8192-tool-use-preview`

### 2. **Default Questions**
- Users can quickly query the models using predefined questions, such as:
  - "What is generative AI?"
  - "What is ML and DL?"
  - "What are neural networks?"
  
### 3. **Natural Language Query**
- In addition to predefined questions, users can input their own questions in a chat-like interface and receive responses from the selected models.

### 4. **Response Time Tracking**
- The app records the inference time for each selected model and displays it in both the main interface and the sidebar.
- The inference time is visualized using a bar chart to allow easy comparison between models.

### 5. **Visualization of Inference Times**
- The app generates a visual plot of the response times for all selected models using Seaborn. This makes it easy to see which models are faster or slower in generating a response.

### 6. **Clear User Interface**
- The app’s interface is clean and intuitive, with sidebar controls for model selection, default questions, and information about the app.
  
### 7. **Developer Information**
- Information about the developer and a link to the developer’s LinkedIn profile is provided in the sidebar for easy connection and feedback.

## Installation and Setup

Follow these steps to install and run the GenAI Chat Completion app on your local machine.

### Prerequisites
- Python 3.8 or higher
- Virtual environment (optional but recommended)

### Step 1: Clone the Repository

```bash
https://github.com/tech-rakesh-ai/FastestGenai.git
cd FastestGenai
```

### Step 2: Create and Activate a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure your `requirements.txt` includes the following dependencies:

```text
streamlit
matplotlib
seaborn
groq
```

### Step 4: Set Up API Key

Create a file called `.streamlit/secrets.toml` in the root directory and add your Groq API key:

```toml
[secrets]
GROQ_API_KEY = "your-groq-api-key"
```

Replace `your-groq-api-key` with the actual API key you obtained from Groq.

### Step 5: Run the Application

Start the Streamlit app by running:

```bash
streamlit run app.py
```

The application will launch in your browser, allowing you to select models, input questions, and compare model performance.

## How to Use

1. **Select Models**: Use the sidebar to select one or more models from the available options. You can compare responses from multiple models at once.
2. **Ask a Question**: Either use the predefined questions by clicking on the buttons or input your own query in the chat box.
3. **View Results**: The selected models will generate responses, and the app will display them along with the response time for each model.
4. **Compare Inference Time**: If more than one model is selected, a bar chart will visualize the inference times, allowing you to compare their performance.

## Application Structure

```bash
genai-chat-completion/
│
├── app.py                     # Main application script
├── requirements.txt            # List of dependencies
└── .streamlit/
    └── secrets.toml            # API key configuration (not included in repo)
```

## Key Components

- **Model Selection**: Users can select one or more models using checkboxes in the sidebar.
- **Inference Time Visualization**: Response times for all selected models are plotted using Seaborn and displayed as a bar chart.
- **AI Chat Completion**: The app interacts with the Groq API to generate responses from the selected models, allowing for side-by-side comparison.
  
## Future Enhancements
- Support for more LLMs and backends (e.g., OpenAI, Hugging Face models).
- Expand the list of default questions and allow users to save common queries.
- Implement streaming responses for real-time interaction with LLMs.
  
## Developer

This app was developed by **Rakesh Kumar**.  
Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/m-rakesh-kr/) to provide feedback and discuss improvements.

## License

MIT License © 2024 GenAI Chat Completion.
