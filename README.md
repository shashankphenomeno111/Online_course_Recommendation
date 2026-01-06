# 🎓 Course Recommendation System

![Course Recommendation Banner](https://raw.githubusercontent.com/shashankphenomeno111/Online_course_Recommendation/main/banner.png)

<div align="center">

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Hugging_Face-yellow)](https://huggingface.co/spaces/shashankphenomenon/course-recommendation-system)
[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red.svg)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4-orange.svg)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

**AI-Powered Personalized Learning Recommendation Platform**

[Live Demo](https://huggingface.co/spaces/shashankphenomenon/course-recommendation-system) • [Documentation](#-documentation) • [Features](#-key-features) • [Models](#-models)

</div>

---

## 🎯 Project Overview

A comprehensive course recommendation system that analyzes **100,000 user interactions** to provide personalized course suggestions using **Machine Learning**. The project includes:

- 📊 **3 Recommendation Algorithms** (Content-Based, Collaborative Filtering, Hybrid)
- 🎨 **Professional Dashboard** with 6 recommendation methods
- 📈 **Comprehensive Evaluation** using 5 different metrics
- 🚀 **Production-Ready Deployment** with Streamlit

---

## 🎬 Live Demo

🔗 **Try it now:** [Course Recommendation System - Live Dashboard](https://huggingface.co/spaces/shashankphenomenon/course-recommendation-system)

Experience the interactive dashboard with real-time recommendations, visualizations, and model comparisons!

---

## ✨ Key Features

### 🤖 **Multiple Recommendation Strategies**
- **Hybrid Model** - Best overall performance (RMSE: 0.68, Precision@10: 75%)
- **Collaborative Filtering** - Based on similar user behavior (NMF)
- **Content-Based** - Course similarity using TF-IDF
- **Popular Courses** - Most enrolled
- **Trending Now** - High engagement
- **Top Rated** - Highest quality

### 📊 **Interactive Dashboard**
- Dataset upload functionality
- 10+ interactive Plotly visualizations
- Real-time recommendations
- Model comparison with radar charts
- Download recommendations as CSV

### 📈 **Comprehensive Analysis**
- Exploratory Data Analysis with visualizations
- Statistical insights and correlations
- Model performance comparisons
- Detailed evaluation metrics

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/course-recommendation-system.git
cd course-recommendation-system

# Install dependencies
pip install -r requirements.txt
```

### Run the Dashboard

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

### Run the Analysis Notebook

```bash
jupyter notebook course_recommendation_system_sklearn.ipynb
```

---

## 📊 Project Structure

```
course-recommendation-system/
├── app.py                                      # Streamlit dashboard (main application)
├── course_recommendation_system_sklearn.ipynb  # Analysis & modeling notebook
├── INTERVIEW_PREP_GUIDE.ipynb                  # Comprehensive interview guide
├── processed_courses.csv                       # Dataset (100K interactions)
├── requirements.txt                            # Python dependencies
├── PROJECT_SUMMARY.md                          # Complete project documentation
├── INTERVIEW_CHEAT_SHEET.md                    # Interview preparation guide
├── EVALUATION_METRICS_EXPLAINED.md             # Metrics explanation
├── DASHBOARD_GUIDE.md                          # Dashboard usage guide
└── README_SKLEARN.md                           # Notebook technical details
```

---

## 🎓 Dataset

- **Size:** 100,000 user-course interaction records
- **Courses:** ~10,000 unique courses
- **Users:** ~17,000 unique users
- **Features:** 14 columns including ratings, enrollment, difficulty, price

### Features:
- User demographics (age, gender, education)
- Course attributes (name, instructor, difficulty, price)
- Interaction metrics (rating, time spent, completion status)

---

## 🤖 Models

### 1. Content-Based Filtering
- **Algorithm:** TF-IDF + Cosine Similarity
- **Features:** Course name, instructor, difficulty
- **Performance:** RMSE 0.85, Coverage 100%
- **Best for:** Explainability, cold start

### 2. Collaborative Filtering (NMF)
- **Algorithm:** Non-negative Matrix Factorization
- **Components:** 20 latent factors
- **Performance:** RMSE 0.72, Precision 68%
- **Best for:** Accuracy

### 3. Hybrid Model ⭐
- **Algorithm:** Weighted combination (40% content + 60% collaborative)
- **Performance:** RMSE 0.68, Precision@10 75%
- **Best for:** Production deployment

---

## 📈 Performance Metrics

| Model | RMSE ↓ | MAE ↓ | Precision@10 ↑ | Coverage ↑ | Diversity ↑ |
|-------|--------|-------|----------------|------------|-------------|
| Content-Based | 0.85 | 0.65 | 55% | 100% | 75% |
| Collaborative | 0.72 | 0.54 | 68% | 45% | 50% |
| **Hybrid** | **0.68** | **0.51** | **75%** | **65%** | **70%** |

**Winner:** Hybrid Model 🏆

---

## 🎨 Dashboard Features

### 1. 🏠 Dashboard
- Dataset overview with key metrics
- Rating distribution
- Difficulty pie chart
- Top instructors
- Price vs rating analysis
- Correlation heatmap

### 2. 🔍 Get Recommendations
- 6 recommendation methods
- User ID or course-based input
- Adjustable number of recommendations
- Beautiful course cards with ratings
- Download as CSV

### 3. 📊 Model Comparison
- Performance metrics table
- RMSE/MAE bar charts
- 5-dimensional radar chart
- Winner announcement

### 4. 📈 Analytics
- Enrollment trends
- User behavior insights
- Course performance analysis

---

## 💻 Technical Stack

- **Language:** Python 3.13
- **ML Libraries:** scikit-learn, NumPy, Pandas
- **Visualization:** Plotly, Matplotlib, Seaborn
- **Dashboard:** Streamlit
- **Algorithms:** NMF, TF-IDF, Cosine Similarity

---

## 📚 Documentation

- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Complete project overview
- **[INTERVIEW_CHEAT_SHEET.md](INTERVIEW_CHEAT_SHEET.md)** - Interview preparation guide
- **[EVALUATION_METRICS_EXPLAINED.md](EVALUATION_METRICS_EXPLAINED.md)** - Metrics deep dive
- **[DASHBOARD_GUIDE.md](DASHBOARD_GUIDE.md)** - How to use the dashboard
- **[INTERVIEW_PREP_GUIDE.ipynb](INTERVIEW_PREP_GUIDE.ipynb)** - Comprehensive technical guide

---

## 🎯 Use Cases

1. **E-Learning Platforms** - Personalized course suggestions
2. **Corporate Training** - Employee skill development
3. **University Systems** - Academic course planning
4. **Online Course Marketplaces** - User engagement

---

## 🚀 Future Enhancements

- [ ] Deep Learning with Neural Collaborative Filtering
- [ ] Sequential recommendations (course paths)
- [ ] Contextual features (time, season)
- [ ] A/B testing framework
- [ ] Real-time user feedback integration
- [ ] Mobile app deployment

---

## 📊 Screenshots

### Dashboard Overview
![Dashboard](screenshots/dashboard.png)

### Recommendations
![Recommendations](screenshots/recommendations.png)

### Model Comparison
![Model Comparison](screenshots/comparison.png)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Shashank**

- GitHub: [@shashankphenomeno111](https://github.com/shashankphenomeno111)
- LinkedIn: [Shashank - Data Scientist](https://www.linkedin.com/in/shashankdatascientist)

---

## 🙏 Acknowledgments

- Built as part of portfolio development
- Inspired by recommendation systems at Netflix, Amazon, YouTube
- Powered by scikit-learn and Streamlit

---

<div align="center">

⭐ **Star this repository if you found it helpful!**

Made with ❤️ using Machine Learning for personalized education

</div>
