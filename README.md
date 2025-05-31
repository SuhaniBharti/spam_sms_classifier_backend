#  SMS Spam Classifier Backend (FastAPI)

[live link - https://spamdetection-gamma.vercel.app ]

This is a **FastAPI backend** for a machine learning model that classifies SMS messages as **Spam** or **Ham** (not spam). It exposes a `/predict` endpoint that receives a message and returns the classification result. This backend can be easily connected with a **React frontend**.

---

##  Features

- Accepts SMS messages via a REST API
-  Uses a trained ML model for classification
-  Built with FastAPI for high performance
-  Easily consumable by frontend apps (like React)

---

##  Project Structure

```
UCO BANK HAKETHON/
├── app/
│   ├── predict.py          # Contains prediction logic
│   └── schemas.py          # Pydantic schemas for input validation
├── model/
│   └── message classifier model.pkl  # Pretrained ML model
├── main.py                 # Entry point for FastAPI
├── requirements.txt        # Project dependencies
├── Spam_SMS.csv            # Dataset used for model training
├── SMS spam classifier.ipynb # Jupyter notebook for training
├── .gitignore              # Ignore virtual env and cache
└── myenv/                  # Python virtual environment (ignored)
```

---

##  Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/a-sksingh113/spam_sms_classifier_backend.git
cd spam_sms_classifier_backend
```

### 2. Create Virtual Environment
```bash
python -m venv myenv
# Windows
myenv\Scripts\activate
# macOS/Linux
source myenv/bin/activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Run the API Server
```bash
uvicorn main:app --reload
```

### 5. API is Live At
- Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Predict Endpoint: `http://127.0.0.1:8000/predict`

---

##  API Usage

### POST `/predict`

**Request:**
```json
{
  "message": "Congratulations! You've won a free iPhone!"
}
```

**Response:**
```json
{
  "prediction": "spam"
}
```

---

##  React Frontend Example

```js
const handleSubmit = async () => {
  const res = await fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: text })
  });
   const data = await response.json();
  setPrediction(data.prediction);
};
```

---

##  Important Notes

- Keep `message classifier model.pkl` in the `model/` directory.
- Only backend logic is here. Frontend (e.g. React) must be created separately.
- Make sure `uvicorn` is installed to run FastAPI.

---

##  License

ALL RIGHTS RESERVED @Data_Seekers team


This project is licensed under the **MIT License**.
