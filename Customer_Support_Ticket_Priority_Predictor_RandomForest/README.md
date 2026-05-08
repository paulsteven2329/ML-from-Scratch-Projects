# 🎫 AI Ticket Priority Prediction System

A Machine Learning project that predicts customer support ticket priority using a Random Forest Classifier.

The system classifies tickets into:

- High Priority
- Medium Priority
- Low Priority

based on ticket text and customer-related information.

---

# 🚀 Project Objective

Customer support teams receive many tickets daily.

This project helps automate ticket prioritization so urgent issues can be handled faster.

Example:

| Ticket | Predicted Priority |
|---|---|
| "Server down urgent help" | High |
| "Need invoice copy" | Low |
| "Cannot login to account" | Medium |

---

# 🧠 Machine Learning Concept

This project uses:

## Random Forest Classifier

Random Forest combines multiple Decision Trees.

Each tree makes a prediction, and the majority vote becomes the final prediction.

Advantages:
- Good accuracy
- Handles mixed data types
- Reduces overfitting
- Works well for classification tasks

---

# 🛠 Tech Stack

- Python
- Pandas
- Scikit-Learn
- Jupyter Notebook
- TF-IDF Vectorizer
- Random Forest Classifier

---

# 📂 Project Structure

```bash
ticket-priority-predictor/
│
├── data/
│   └── tickets.csv
│
├── notebook/
│   └── ticket_priority_prediction.ipynb
│
├── models/
│   └── random_forest_model.pkl
│
├── screenshots/
│   └── output.png
│
├── README.md
│
└── requirements.txt
```

---

# ⚙️ ML Workflow

## 1. Data Collection

Dataset contains:
- Ticket Text
- Customer Type
- Waiting Hours
- Previous Tickets
- Priority Label

---

## 2. Data Preprocessing

### Text Processing
Ticket messages are converted into numerical vectors using:

- TF-IDF Vectorization

### Categorical Encoding
Customer type is encoded using:

- OneHotEncoder

---

## 3. Model Training

The Random Forest model is trained on processed ticket data.

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

---

# 📊 Features Used

| Feature | Description |
|---|---|
| ticket_text | Customer issue description |
| customer_type | Free / Premium / Enterprise |
| hours_waiting | Waiting time |
| previous_tickets | Number of past tickets |

---

# 🎯 Prediction Labels

| Label | Meaning |
|---|---|
| High | Urgent issue |
| Medium | Important issue |
| Low | Minor/general issue |

---

# 📈 Model Evaluation

Evaluation Metrics:
- Accuracy Score
- Classification Report
- Confusion Matrix

---

# 🧪 Example Prediction

Input:

```text
"Payment failed and customer cannot access service urgent"
```

Output:

```text
High Priority
```

---

# ▶️ How To Run

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/ticket-priority-predictor.git
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
ticket_priority_prediction.ipynb
```

---

# 📦 requirements.txt

```txt
pandas
scikit-learn
jupyter
```

---

# 🔥 Future Improvements

- Streamlit Dashboard
- FastAPI Deployment
- Deep Learning NLP Models
- Real-time Ticket API
- SLA Prediction
- Ticket Auto-Assignment
- Email Integration

---

# 📚 Learning Outcomes

This project helped in understanding:

- Random Forest Algorithm
- NLP Basics
- Text Vectorization
- ML Pipelines
- Classification Problems
- Real-world ML Systems

---

# 🤝 Contributing

Pull requests are welcome.

For major changes, please open an issue first.

---

# ⭐ Support

If you like this project, give it a star ⭐ on GitHub.

---

# 👨‍💻 Author

Built with Python and Machine Learning.