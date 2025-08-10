# 🎯 YouTube Video to Blog Creator  

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)  
[![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?logo=openai&logoColor=white)](https://openai.com/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)  
[![LangChain](https://img.shields.io/badge/LangChain-Framework-green)](https://www.langchain.com/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  

---

## 📌 Overview  
The **YouTube Video to Blog Creator** is a Generative AI application that automates the process of converting YouTube videos into structured, high-quality blog articles.  
It integrates **CrewAI** for transcription and **OpenAI models** for summarization, content structuring, and natural language generation.  

This project streamlines content creation by transforming unstructured video data into polished, written blogs — enabling **efficient, scalable, and AI-driven content production**.  

---

## 🚀 Features  
- 🎥 **Video-to-Text Conversion** – Transcribes YouTube video audio into text using CrewAI.  
- 📝 **AI-Powered Summarization** – Uses OpenAI models to generate concise, coherent blog content.  
- 🔄 **Automated Workflow** – From transcription to blog formatting in one seamless pipeline.  
- 🌐 **Scalable Solution** – Suitable for content creators, marketing teams, and educators.  

---

## 🛠 Tech Stack  
- **Languages:** Python  
- **Frameworks/Tools:** CrewAI, OpenAI API, LangChain  
- **Deployment:** Streamlit (for UI)  
- **Other:** YouTube video processing  

---

## 📂 Project Workflow  
1. **Input:** Provide the YouTube video URL.  
2. **Transcription:** CrewAI converts audio to raw text.  
3. **Summarization:** OpenAI API condenses and organizes text.  
4. **Blog Formatting:** Generates a final article with proper headings and paragraphs.  
5. **Output:** Download or view the AI-generated blog post.  

---


## 📦 Installation & Usage  
```bash
# Clone the repository

# Navigate to the project folder
cd YouTube-Video-to-Blog-Creator

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
