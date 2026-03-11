# 🛒 Walmart Store Sales Forecasting

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Machine Learning](https://img.shields.io/badge/ML-Regression%20%7C%20Time%20Series-orange?style=flat-square)
![Flask](https://img.shields.io/badge/Deployed-Flask%20App-green?style=flat-square&logo=flask)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat-square)

> **Predicting weekly department-level sales across 45 Walmart stores using historical markdown and holiday data — deployed as a live Flask web application.**

---

## 📌 Problem Statement

Retail chains like Walmart face a critical challenge: accurately forecasting sales to optimize inventory, staffing, and supply chain decisions — especially during high-impact holiday seasons.

This project builds an end-to-end machine learning solution to **predict weekly store sales** using 2+ years of historical data from 45 Walmart stores across different US regions. The model accounts for promotional markdowns, seasonal spikes (Super Bowl, Thanksgiving, Christmas, Labour Day), and store-level features.

---

## 🎯 Business Impact

- Helps Walmart plan **stock levels** and **warehouse space** before high-demand periods
- Identifies which stores and departments are most affected by **holiday markdowns**
- Enables **data-driven decisions** on regional promotions and resource allocation

---

## 📊 Dataset

Source: [Kaggle — Walmart Store Sales Forecasting](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)

| File | Description |
|------|-------------|
| `train.csv` | Historical weekly sales per store & department (Feb 2010 – Oct 2012) |
| `test.csv` | Target period for prediction |
| `features.csv` | Store-level features: Temperature, Fuel Price, CPI, Unemployment, MarkDowns |
| `stores.csv` | Store metadata: type (A/B/C) and size |

**Key Challenge:** Holiday weeks are weighted **5x higher** in evaluation (WMAE metric), making accurate holiday prediction critical.

---

## 🏗️ Project Architecture

```
Walmart-Store-Sales-Forecasting/
├── data/
│   ├── train.csv
│   ├── test.csv
│   ├── features.csv
│   └── stores.csv
├── templates/
│   └── index.html          # Flask frontend
├── static/
│   └── style.css
├── Walmart Store Sales Forecasting.ipynb   # Full EDA + Modelling
├── app.py                  # Flask application
├── model.pkl               # Serialized trained model
├── requirements.txt
└── Dockerfile
```

---

## 🔍 Approach

### 1. Exploratory Data Analysis (EDA)
- Analyzed **seasonal patterns** in weekly sales across stores and departments
- Identified **holiday spikes** — Thanksgiving consistently outperforms Christmas in actual sales
- Found that **January sales drop sharply** post-holiday season
- Examined impact of external factors: CPI, fuel price, unemployment, temperature

### 2. Feature Engineering
- Extracted time features: Week, Month, Year from date
- Engineered **holiday flags** for Super Bowl, Labour Day, Thanksgiving, Christmas
- Merged store metadata (type, size) with weekly sales and external features
- Handled **missing MarkDown values** (up to 4,140 nulls in some columns) using median imputation

### 3. Modelling
- Evaluated multiple regression approaches for time-series forecasting
- Applied **Random Forest Regressor** as the primary model due to its ability to capture non-linear relationships and feature interactions
- Used **cross-validation** with time-aware splits to prevent data leakage

### 4. Evaluation Metric
**WMAE (Weighted Mean Absolute Error)** — holiday weeks weighted 5x:

```
WMAE = (1 / Σwᵢ) × Σ wᵢ |yᵢ - ŷᵢ|
```

### 5. Deployment
- Serialized model using `pickle` → `model.pkl`
- Built a **Flask web app** for real-time sales prediction
- Containerized with **Docker** for portability
- Deployed on web (previously Heroku, migrating to Render)

---

## 📈 Results

| Metric | Value |
|--------|-------|
| Evaluation | WMAE (Weighted MAE) |
| Holiday Weight | 5× non-holiday weeks |
| Stores Covered | 45 stores, multiple departments |
| Prediction Period | Weekly |

> **Key Finding:** Holiday markdown events — especially Thanksgiving — are the single strongest predictor of sales spikes. Store type and size also significantly influence baseline weekly sales.

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.8+ |
| Data Processing | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| Modelling | Scikit-learn (Random Forest, Linear Regression) |
| Web Framework | Flask |
| Deployment | Docker, Heroku → Render |
| Notebook | Jupyter Notebook |

---

## 🚀 Running Locally

### Option 1: Standard Setup
```bash
# Clone the repository
git clone https://github.com/vicky60629/Walmart-Store-Sales-Forecasting.git
cd Walmart-Store-Sales-Forecasting

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```
Then open `http://localhost:5000` in your browser.

### Option 2: Docker
```bash
docker build -t walmart-forecasting .
docker run -p 5000:5000 walmart-forecasting
```

---

## 📸 App Preview

| Input Form | Prediction Output |
|-----------|------------------|
| ![Input](results/2020-06-16%2020_13_25-Settings.png) | ![Output](results/2020-06-16%2020_14_05-Settings.png) |

---

## 💡 Key Learnings & Future Improvements

**What worked well:**
- Feature engineering around holidays significantly improved prediction accuracy
- Random Forest handled the non-linear interactions between store size, type, and markdown events effectively

**Future enhancements:**
- [ ] Integrate **XGBoost / LightGBM** for potential performance gains
- [ ] Add **SARIMA / Prophet** for pure time-series baseline comparison
- [ ] Build interactive dashboard with **Streamlit or Plotly Dash**
- [ ] Incorporate external data: weather APIs, economic indicators
- [ ] Retrain with MLflow for experiment tracking

---

## 👨‍💻 About the Author

**Vicky Gupta** — Data Engineering Analyst @ Accenture (4.5 years) | Aspiring Data Scientist

Skilled in PySpark, ETL pipelines, and end-to-end ML systems. Passionate about building data products that solve real business problems.

🔗 [LinkedIn](https://www.linkedin.com/in/vicky-gupta-583016168/) | [GitHub](https://github.com/vicky60629)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

⭐ **If you found this project useful, please consider starring the repository!**
