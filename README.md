# 🫁 Lung Disease Diagnosis System (Frontend)

An AI-powered web application for detecting **Pneumonia** from Chest X-ray images using a deep learning custom CNN model. The frontend is built using **Streamlit** and communicates with the deployed FAST API to provide real-time predictions.

---

## 📌 Features

- 🫁 AI-powered Chest X-ray diagnosis
- 📤 Upload Chest X-ray images (JPG, JPEG, PNG)
- 🤖 Real-time prediction using deployed BentoML API
- 📊 Confidence score visualization
- 👤 Patient information form
- 📄 Download professional PDF diagnosis report
- 📜 Prediction history
- 💻 Responsive Streamlit interface
- ☁️ FASR API integration with AWS EC2

---

## 🏗️ System Architecture

```
                Streamlit Frontend
                        │
            Upload Chest X-ray Image
                        │
                  HTTP POST Request
                        │
                AWS EC2 (BentoML API)
                        │
                PyTorch CNN Model
                        │
         Prediction + Confidence Score
                        │
        PDF Report + Prediction History
```

---

## 🛠️ Tech Stack

### Frontend

- Streamlit
- Pandas
- Pillow
- Requests
- ReportLab
- SQLite

### Backend

- PyTorch
- BentoML
- Docker
- AWS EC2
- Amazon ECR

---

## 📂 Project Structure

```
lung_disease_frontend/
│
├── assets/
│   └── style.css
│
├── components/
│   ├── footer.py
│   ├── hero.py
│   ├── patient_form.py
│   ├── prediction.py
│   ├── sidebar.py
│   ├── stats.py
│   └── uploader.py
│
├── utils/
│   ├── api.py
│   ├── database.py
│   └── report.py
│
├── app.py
├── requirements.txt
├── lung_disease.db
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/vicky060403/Lungs_Disease_Digonosis-Frontend.git

cd lung-disease-frontend
```

---

### Create Virtual Environment

```bash
py -3.10 -m venv .venv
```

Activate

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Backend API

Open

```
utils/api.py
```

Replace

```python
API_URL = "http://YOUR_PUBLIC_IP/predict"
```

with your deployed BentoML endpoint.

Example

```python
API_URL = "http://13.201.23.111/predict"
```

---

### Run the Application

```bash
streamlit run app.py
```

---

## 🩺 How to Use

1. Enter patient information.
2. Upload a Chest X-ray image.
3. Click **Analyze Chest X-ray**.
4. Wait for the AI prediction.
5. View:
   - Prediction
   - Confidence Score
   - Recommendation
6. Download the PDF report.

---

## 📄 PDF Report Includes

- Patient Information
- Date & Time
- Uploaded X-ray
- AI Prediction
- Confidence Score
- Risk Level
- Recommendation
- Medical Disclaimer

---

## 🔌 Backend Repository

The frontend communicates with the BentoML backend via REST API.

Backend Repository:

```
https://github.com/vicky060403/Lungs_Disease_Digonosis
```

---

## 📈 Future Improvements

- User Authentication
- Multi-class Lung Disease Detection
- Doctor Dashboard
- PostgreSQL Integration
- Cloud Storage for Reports
- Explainable AI (Grad-CAM)
- Model Monitoring Dashboard

---

## 👨‍💻 Developed By

**Vicky Kumar**

LinkedIn: https://www.linkedin.com/in/vicky-kumar-95aa4b283

GitHub: https://github.com/vicky060403/>

---

## ⭐ If you found this project useful, consider giving it a star on GitHub.