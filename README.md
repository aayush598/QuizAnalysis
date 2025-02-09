# **📖 Quiz Analysis (FastAPI + Streamlit + Gemini AI)**

![Render Deployment](https://img.shields.io/badge/Deployed_on-Render-blue?style=for-the-badge)  
![FastAPI](https://img.shields.io/badge/FastAPI-✔-green?style=for-the-badge)  
![Streamlit](https://img.shields.io/badge/Streamlit-✔-red?style=for-the-badge)  
![Gemini AI](https://img.shields.io/badge/Gemini_AI-✔-yellow?style=for-the-badge)

---

## **📌 Project Overview**

**Quiz Analysis** is a system that provides **real-time student performance insights** using:  
✅ **FastAPI** for API-based analytics  
✅ **Streamlit** for an interactive UI  
✅ **Gemini AI API** for personalized recommendations  
✅ **Render Deployment** for cloud hosting

🔗 **Live API Endpoint:** [https://quizanalysis.onrender.com/docs](https://quizanalysis.onrender.com/docs)  
🔗 **Live Streamlit App:** [https://quizanalysis.onrender.com](https://quizanalysis.onrender.com)

---

## **🚀 Features**

✅ **API-based quiz performance analytics** (FastAPI)  
✅ **Interactive Dashboard** (Streamlit)  
✅ **AI-powered insights using Google Gemini**  
✅ **Real-time quiz accuracy & topic tracking**  
✅ **Deployed on Render for cloud accessibility**

---

## **📂 Project Structure**

```
quiz_analysis/
│── api.py               # FastAPI backend
│── streamlit_ui.py      # Streamlit frontend
│── config.py            # Configuration settings
│── data_loader.py       # Loads data from JSON or API
│── analysis.py          # Performance analysis
│── insights.py          # AI-powered insights using Gemini API
│── utils.py             # Helper functions
│── requirements.txt     # Dependencies
│── Procfile             # Render process manager
│── start.sh             # Start both API & Streamlit UI
│── README.md            # Documentation
```

---

## **🛠️ Installation**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/aayush598/QuizAnalysis.git
cd QuizAnalysis
```

### **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### \*\*3️⃣ Create a .env File

Before running the project, create a .env file in the root directory and add the following:

```bash
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

CURRENT_QUIZ_FILE=quiz_data/current_quiz.json
HISTORICAL_QUIZ_FILE=quiz_data/historical_quiz.json
QUIZ_SUBMISSION_FILE=quiz_data/quiz_submission.json

CURRENT_QUIZ_LINK=https://jsonkeeper.com/b/LLQT
HISTORICAL_QUIZ_LINK=https://api.jsonserve.com/XgAgFJ
QUIZ_SUBMISSION_LINK=https://api.jsonserve.com/rJvd7g
```

### **3️⃣ Run FastAPI (Backend)**

```bash
uvicorn api:app  --port 8000 --reload
```

- Open **http://127.0.0.1:8000/docs** to access API documentation.

### **4️⃣ Run Streamlit (Frontend)**

```bash
streamlit run streamlit_ui.py
```

- Open **http://localhost:8501** to view the dashboard.

---

## **🌐 Deploy on Render**

### **1️⃣ Push to GitHub**

```bash
git add .
git commit -m "Renamed project to Quiz Analysis"
git push origin main
```

### **2️⃣ Deploy FastAPI**

- Go to **Render Dashboard** → **New Web Service**
- Select **GitHub Repo** (`QuizAnalysis`)
- Set:
  - **Runtime** → `Python`
  - **Start Command** → `bash start.sh`
  - **Environment Variables** → `GEMINI_API_KEY=<your-api-key>`
- Click **Deploy**

### **3️⃣ Deploy Streamlit**

- Create **another Render Web Service**
- Set:
  - **Runtime** → `Python`
  - **Start Command** → `streamlit run streamlit_ui.py --server.port 10000 --server.address 0.0.0.0`
- Click **Deploy**

---

## **🛠️ API Endpoints**

| Method  | Endpoint                  | Description                               |
| ------- | ------------------------- | ----------------------------------------- |
| **GET** | `/performance/historical` | Fetch historical performance data         |
| **GET** | `/performance/current`    | Fetch latest quiz performance             |
| **GET** | `/performance/submission` | Fetch latest quiz submission data         |
| **GET** | `/insights/ai`            | Generate AI-powered study recommendations |

---

## **📊 Usage in Streamlit**

- **Dashboard** for performance visualization
- **AI-powered study recommendations**
- **Accuracy trends** & **quiz insights**
- **Real-time API fetching from Render**

---

## **🧠 AI-Powered Insights**

Powered by **Google Gemini API**, this system provides:  
✅ **Personalized study suggestions**  
✅ **Performance improvement areas**  
✅ **Trend-based AI insights**

---

## **📜 License**

This project is licensed under the **MIT License**.

---

## **👨‍💻 Developed by**

🚀 **Aayush Gid**  
📧 Email: [aayushgid598@gmail.com](mailto:aayushgid598@gmail.com)  
🔗 **Deployed URL:** [https://quizanalysis.onrender.com](https://quizanalysis.onrender.com)  
🔗 **GitHub Repo:** [https://github.com/aayush598/QuizAnalysis.git](https://github.com/aayush598/QuizAnalysis.git)

---

## **🚀 Next Steps**

Would you like **Docker support** or **database integration** for better scalability? 🚀🔥

---

### **✅ 3️⃣ Update Project References**

🔹 **Rename GitHub repository to** `QuizAnalysis`.  
🔹 **Update Render service name to** `quizanalysis`.

---

### **✅ 4️⃣ Update in Code Files**

Replace all instances of **"student_performance_gemini"** with **"quiz_analysis"** in:

- `config.py`
- `start.sh`
- `api.py`
- `streamlit_ui.py`
- `README.md`

**Command to update references (Linux/Mac):**

```bash
grep -rl "student_performance_gemini" . | xargs sed -i 's/student_performance_gemini/quiz_analysis/g'
```

---

## **🎯 Final Steps**

1. ✅ **Push the changes to GitHub**
2. ✅ **Redeploy on Render**
3. ✅ **Update the new deployment links in README**

Let me know if you need **Docker support** or **additional features**! 🚀🔥
