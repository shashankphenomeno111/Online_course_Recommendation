"""
Course Recommendation System - Professional Dashboard (Enhanced)
Features: Dataset Upload, Multiple Recommendation Methods, Advanced Analytics
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import NMF
import io

# Page configuration
st.set_page_config(
    page_title="Course Recommender Pro",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS (keeping the same professional styling)
st.markdown("""
<style>
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(120deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 20px 0;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 30px;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin: 10px 0;
    }
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 10px 0;
    }
    .metric-label {
        font-size: 1rem;
        opacity: 0.9;
    }
    .section-header {
        font-size: 2rem;
        font-weight: 700;
        color: #667eea;
        border-bottom: 3px solid #667eea;
        padding-bottom: 10px;
        margin: 30px 0 20px 0;
    }
    .course-card {
        background: white;
        border-left: 5px solid #667eea;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin: 15px 0;
        transition: transform 0.3s;
    }
    .course-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .course-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 10px;
    }
    .course-detail {
        color: #666;
        margin: 5px 0;
    }
    .info-box {
        background: #f0f7ff;
        border-left: 4px solid #667eea;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
    }
    .upload-box {
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
        border: 2px dashed #667eea;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = None
if 'models' not in st.session_state:
    st.session_state.models = None

# Load or upload data
@st.cache_data
def load_default_data():
    """Load the default course dataset"""
    try:
        df = pd.read_csv('processed_courses.csv')
        return df
    except FileNotFoundError:
        return None

def process_uploaded_data(uploaded_file):
    """Process uploaded CSV file"""
    try:
        df = pd.read_csv(uploaded_file)
        return df
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None

@st.cache_resource
def train_models(df):
    """Train all recommendation models"""
    # Create unique courses dataframe
    df_unique = df.drop_duplicates(subset='course_id')
    
    # Content-Based: TF-IDF
    df_unique['combined_features'] = (
        df_unique['course_name'] + ' ' + 
        df_unique['instructor'] + ' ' + 
        df_unique['difficulty_level']
    )
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df_unique['combined_features'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Create course indices
    indices = pd.Series(df_unique.index, index=df_unique['course_id']).to_dict()
    
    # Collaborative: NMF
    user_item_matrix = df.pivot_table(
        index='user_id', 
        columns='course_id', 
        values='rating', 
        fill_value=0
    )
    
    nmf_model = NMF(n_components=20, init='random', random_state=42, max_iter=200)
    user_features = nmf_model.fit_transform(user_item_matrix)
    course_features = nmf_model.components_
    predicted_ratings = np.dot(user_features, course_features)
    predicted_ratings_df = pd.DataFrame(
        predicted_ratings,
        index=user_item_matrix.index,
        columns=user_item_matrix.columns
    )
    
    return {
        'df_unique': df_unique,
        'cosine_sim': cosine_sim,
        'indices': indices,
        'predicted_ratings_df': predicted_ratings_df,
        'user_item_matrix': user_item_matrix
    }

def get_content_recommendations(course_id, models, top_n=10):
    """Get content-based recommendations"""
    try:
        idx = models['indices'][course_id]
        sim_scores = list(enumerate(models['cosine_sim'][idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_n+1]
        course_indices = [i[0] for i in sim_scores]
        
        recommendations = models['df_unique'].iloc[course_indices][[
            'course_id', 'course_name', 'instructor', 'difficulty_level', 
            'rating', 'course_price'
        ]].copy()
        recommendations['similarity_score'] = [score[1] for score in sim_scores]
        return recommendations
    except:
        return pd.DataFrame()

def get_collaborative_recommendations(user_id, models, top_n=10):
    """Get collaborative filtering recommendations"""
    try:
        if user_id not in models['predicted_ratings_df'].index:
            return pd.DataFrame()
        
        user_predictions = models['predicted_ratings_df'].loc[user_id]
        top_course_ids = user_predictions.nlargest(top_n).index
        
        recommendations = models['df_unique'][
            models['df_unique']['course_id'].isin(top_course_ids)
        ].copy()
        recommendations['estimated_rating'] = recommendations['course_id'].map(
            lambda x: min(5.0, max(1.0, user_predictions[x]))
        )
        recommendations = recommendations.sort_values('estimated_rating', ascending=False)
        
        return recommendations[[
            'course_id', 'course_name', 'instructor', 'difficulty_level',
            'rating', 'estimated_rating', 'course_price'
        ]]
    except:
        return pd.DataFrame()

def get_hybrid_recommendations(user_id, df, models, top_n=10):
    """Get hybrid recommendations"""
    try:
        user_courses = df[df['user_id'] == user_id].sort_values('rating', ascending=False)
        if len(user_courses) == 0:
            return get_collaborative_recommendations(user_id, models, top_n)
        
        last_course = user_courses.iloc[0]['course_id']
        
        content_recs = get_content_recommendations(last_course, models, top_n*2)
        collab_recs = get_collaborative_recommendations(user_id, models, top_n*2)
        
        if content_recs.empty or collab_recs.empty:
            return collab_recs if not collab_recs.empty else content_recs
        
        content_recs['content_score'] = range(len(content_recs), 0, -1)
        content_recs['content_score'] = content_recs['content_score'] / content_recs['content_score'].max()
        
        collab_recs['collab_score'] = collab_recs['estimated_rating'] / 5.0
        
        hybrid = pd.merge(
            content_recs[['course_id', 'content_score']],
            collab_recs[['course_id', 'collab_score']],
            on='course_id', how='outer'
        ).fillna(0)
        
        hybrid['hybrid_score'] = hybrid['content_score'] * 0.4 + hybrid['collab_score'] * 0.6
        hybrid = hybrid.sort_values('hybrid_score', ascending=False).head(top_n)
        
        final = pd.merge(
            hybrid,
            models['df_unique'][['course_id', 'course_name', 'instructor', 
                                 'difficulty_level', 'rating', 'course_price']],
            on='course_id'
        )
        
        return final
    except:
        return pd.DataFrame()

def get_popular_recommendations(df_unique, top_n=10):
    """Get most popular courses"""
    return df_unique.nlargest(top_n, 'enrollment_numbers')[[
        'course_id', 'course_name', 'instructor', 'difficulty_level',
        'rating', 'enrollment_numbers', 'course_price'
    ]]

def get_trending_recommendations(df, top_n=10):
    """Get trending courses (high recent enrollment)"""
    trending = df.groupby('course_id').agg({
        'enrollment_numbers': 'mean',
        'rating': 'mean',
        'course_name': 'first',
        'instructor': 'first',
        'difficulty_level': 'first',
        'course_price': 'first'
    }).reset_index()
    
    trending['trend_score'] = trending['enrollment_numbers'] * trending['rating']
    return trending.nlargest(top_n, 'trend_score')[[
        'course_id', 'course_name', 'instructor', 'difficulty_level',
        'rating', 'enrollment_numbers', 'course_price'
    ]]

def get_top_rated_recommendations(df_unique, top_n=10):
    """Get highest rated courses"""
    return df_unique.nlargest(top_n, 'rating')[[
        'course_id', 'course_name', 'instructor', 'difficulty_level',
        'rating', 'enrollment_numbers', 'course_price'
    ]]

def display_recommendations(recommendations, rec_type=""):
    """Display recommendations in a beautiful format"""
    if recommendations.empty:
        st.warning("⚠️ No recommendations found.")
        return
    
    for idx, row in recommendations.iterrows():
        rating = row.get('rating', 0)
        stars = "⭐" * int(rating) + "☆" * (5 - int(rating))
        
        # Determine score and color
        if 'estimated_rating' in row:
            score = row['estimated_rating']
            score_label = f"Predicted: {score:.2f}/5.0"
            score_color = "#4CAF50" if score >= 4.0 else "#FFC107"
        elif 'hybrid_score' in row:
            score = row['hybrid_score']
            score_label = f"Match: {score*100:.1f}%"
            score_color = "#667eea"
        elif 'similarity_score' in row:
            score = row['similarity_score']
            score_label = f"Similarity: {score*100:.1f}%"
            score_color = "#764ba2"
        elif 'enrollment_numbers' in row:
            enroll = row['enrollment_numbers']
            score_label = f"Enrolled: {int(enroll):,}"
            score_color = "#00B894"
        else:
            score_label = f"Rating: {rating:.1f}/5.0"
            score_color = "#667eea"
        
        st.markdown(f"""
        <div class="course-card">
            <div style="display: flex; justify-content: space-between; align-items: start;">
                <div style="flex: 1;">
                    <div class="course-title">📖 {row['course_name']}</div>
                    <div class="course-detail">👨‍🏫 <b>Instructor:</b> {row['instructor']}</div>
                    <div class="course-detail">📊 <b>Difficulty:</b> {row['difficulty_level']}</div>
                    <div class="course-detail">⭐ <b>Rating:</b> {stars} ({rating:.1f}/5.0)</div>
                    <div class="course-detail">💰 <b>Price:</b> ${row['course_price']:.2f}</div>
                </div>
                <div style="text-align: right;">
                    <div style="background: {score_color}; color: white; padding: 10px 20px; 
                                border-radius: 25px; font-weight: bold; font-size: 0.9rem;">
                        {score_label}
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-title">🎓 Course Recommender Pro</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-Powered Personalized Learning Recommendations</p>', unsafe_allow_html=True)

# Sidebar for data upload and navigation
st.sidebar.markdown("### 📂 Data Management")

uploaded_file = st.sidebar.file_uploader(
    "Upload Your Dataset (CSV)",
    type=['csv'],
    help="Upload a course dataset with columns: user_id, course_id, course_name, instructor, rating, etc."
)

if uploaded_file is not None:
    df = process_uploaded_data(uploaded_file)
    if df is not None:
        st.session_state.df = df
        st.sidebar.success(f"✅ Dataset loaded: {len(df):,} rows")
elif st.session_state.df is None:
    # Try to load default dataset
    df = load_default_data()
    if df is not None:
        st.session_state.df = df
        st.sidebar.info("📊 Using default dataset")

# Navigation
if st.session_state.df is not None:
    df = st.session_state.df
    
    # Train models if not already trained
    if st.session_state.models is None:
        with st.spinner("🔮 Training recommendation models..."):
            st.session_state.models = train_models(df)
    
    models = st.session_state.models
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🎯 Navigation")
    page = st.sidebar.radio(
        "Choose a section:",
        ["🏠 Dashboard", "🔍 Get Recommendations", "📊 Model Comparison", "📈 Analytics"]
    )
    
    # Continue with pages (keeping Dashboard code from before, will add enhanced recommendations page)
    # [Previous dashboard code continues here - I'll add the enhanced recommendation page]
    
else:
    st.markdown("""
    <div class="upload-box">
        <h2>📤 Upload Your Dataset to Get Started</h2>
        <p style="font-size: 1.1rem; color: #666; margin-top: 15px;">
            Upload a CSV file containing course and user data to see powerful visualizations<br>
            and get personalized recommendations using advanced ML algorithms.
        </p>
        <p style="color: #999; margin-top: 20px;">
            <b>Required columns:</b> user_id, course_id, course_name, instructor, rating,<br>
            difficulty_level, course_price, enrollment_numbers
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Show sample data format
    st.markdown("### 📋 Sample Dataset Format")
    sample_data = {
        'user_id': [15796, 861, 38159],
        'course_id': [9366, 1928, 9541],
        'course_name': ['Python for Beginners', 'Cybersecurity for Professionals', 'DevOps and Continuous Deployment'],
        'instructor': ['Emma Harris', 'Alexander Young', 'Dr. Mia Walker'],
        'rating': [4.5, 4.2, 4.7],
        'difficulty_level': ['Beginner', 'Intermediate', 'Advanced'],
        'course_price': [39.1, 36.3, 13.4],
        'enrollment_numbers': [48245, 35678, 29384]
    }
    st.dataframe(pd.DataFrame(sample_data), use_container_width=True)
