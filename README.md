## **📖 Student Performance Analysis (FastAPI + Streamlit + Gemini AI)**

![Render Deployment](https://img.shields.io/badge/Deployed_on-Render-blue?style=for-the-badge)  
![FastAPI](https://img.shields.io/badge/FastAPI-✔-green?style=for-the-badge)  
![Streamlit](https://img.shields.io/badge/Streamlit-✔-red?style=for-the-badge)  
![Gemini AI](https://img.shields.io/badge/Gemini_AI-✔-yellow?style=for-the-badge)

---

### **📌 Project Overview**

This project provides **student performance analysis** using:  
✅ **FastAPI** for API-based analytics  
✅ **Streamlit** for an interactive UI  
✅ **Gemini AI API** for personalized recommendations  
✅ **Render Deployment** for cloud hosting

🔗 **Live API Endpoint:** [https://your-api-url.onrender.com/docs](#)  
🔗 **Live Streamlit App:** [https://your-streamlit-url.onrender.com](#)

---

## **🚀 Features**

✅ **API for student performance analytics** (FastAPI)  
✅ **Interactive Dashboard** (Streamlit)  
✅ **AI-powered insights using Google Gemini**  
✅ **Real-time quiz performance tracking**  
✅ **Easy cloud deployment on Render**

---

## **📂 Project Structure**

```
student_performance/
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
git clone https://github.com/your-username/student-performance-api.git
cd student-performance-api
```

### **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3️⃣ Run FastAPI (Backend)**

```bash
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
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
git commit -m "Deploy FastAPI & Streamlit to Render"
git push origin main
```

### **2️⃣ Deploy FastAPI**

- Go to **Render Dashboard** → **New Web Service**
- Select **GitHub Repo** (`student-performance-api`)
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

## **👨‍💻 Author**

🚀 Developed by **[Your Name](https://github.com/your-username)**  
📧 Contact: [your-email@example.com](#)

---

Would you like **Docker support** for containerized deployment? 🚀🔥
