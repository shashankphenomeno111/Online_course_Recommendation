"""
Add Preprocessing and Model Development sections to interview notebook
"""

import json

with open('INTERVIEW_PREP_GUIDE.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

preprocessing_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "<a id=\"4\"></a>\n",
            "## 4️⃣ Data Preprocessing\n",
            "\n",
            "### 🎯 **Why Preprocess Data?**\n",
            "\n",
            "Machine Learning models need data in specific formats:\n",
            "- **Text → Numbers** (algorithms work with numbers)\n",
            "- **Consistent scales** (some algorithms sensitive to scale)\n",
            "- **Clean format** (no missing values, proper types)\n",
            "\n",
            "---\n",
            "\n",
            "### 🔄 **Our Preprocessing Pipeline**\n",
            "\n",
            "```\n",
            "Raw Data\n",
            "   ↓\n",
            "1. Label Encoding (difficulty_level, gender, education)\n",
            "   ↓\n",
            "2. Feature Engineering (combine course features)\n",
            "   ↓\n",
            "3. TF-IDF Vectorization (text to numbers)\n",
            "   ↓\n",
            "4. User-Item Matrix Creation\n",
            "   ↓\n",
            "Ready for Modeling!\n",
            "```\n",
            "\n",
            "---"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 📝 **Step 1: Label Encoding**\n",
            "\n",
            "**What:** Convert categorical text to numbers\n",
            "\n",
            "**Why:** Algorithms can only work with numerical data\n",
            "\n",
            "**How:** Assign each unique value a number\n",
            "\n",
            "**Example:**\n",
            "```\n",
            "Difficulty:     Label:\n",
            "Beginner    →   0\n",
            "Intermediate →  1  \n",
            "Advanced    →   2\n",
            "```"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "from sklearn.preprocessing import LabelEncoder\n",
            "\n",
            "# Create label encoder\n",
            "le_difficulty = LabelEncoder()\n",
            "le_gender = LabelEncoder()\n",
            "le_education = LabelEncoder()\n",
            "\n",
            "# Encode categorical variables\n",
            "df['difficulty_encoded'] = le_difficulty.fit_transform(df['difficulty_level'])\n",
            "df['gender_encoded'] = le_gender.fit_transform(df['gender'])\n",
            "df['education_encoded'] = le_education.fit_transform(df['education_level'])\n",
            "\n",
            "print(\"✅ Label Encoding Complete!\")\n",
            "print(\"\\n📊 Difficulty Mapping:\")\n",
            "for i, label in enumerate(le_difficulty.classes_):\n",
            "    print(f\"   {label} → {i}\")\n",
            "\n",
            "print(\"\\n📊 Sample of encoded data:\")\n",
            "df[['difficulty_level', 'difficulty_encoded', 'gender', 'gender_encoded']].head()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "#### 🎤 **Interview Talking Point:**\n",
            "\n",
            "> *\"I used Label Encoding to convert categorical variables like difficulty level, gender, and education into numerical format. This allows the algorithms to process these features mathematically while preserving the unique categories.\"*\n",
            "\n",
            "---"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 📝 **Step 2: Feature Engineering for Content-Based**\n",
            "\n",
            "**Goal:** Combine course features into one text field\n",
            "\n",
            "**Why:** TF-IDF works on text, so we combine:\n",
            "- Course name\n",
            "- Instructor name  \n",
            "- Difficulty level\n",
            "\n",
            "**Result:** Rich text representation of each course"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Create unique courses dataframe\n",
            "df_unique = df.drop_duplicates(subset='course_id')\n",
            "\n",
            "# Combine features into single text field\n",
            "df_unique['combined_features'] = (\n",
            "    df_unique['course_name'] + ' ' + \n",
            "    df_unique['instructor'] + ' ' + \n",
            "    df_unique['difficulty_level']\n",
            ")\n",
            "\n",
            "print(f\"✅ Created {len(df_unique):,} unique course profiles\")\n",
            "print(\"\\n📝 Sample combined features:\")\n",
            "print(df_unique[['course_name', 'combined_features']].head(3).to_string())"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "#### 🔍 **Example:**\n",
            "\n",
            "**Original:**\n",
            "- Course: \"Python for Beginners\"\n",
            "- Instructor: \"Emma Harris\"\n",
            "- Difficulty: \"Beginner\"\n",
            "\n",
            "**Combined:**\n",
            "- \"Python for Beginners Emma Harris Beginner\"\n",
            "\n",
            "**Why This Works:**\n",
            "- Courses with similar **names** will be similar\n",
            "- Courses from same **instructor** will be similar  \n",
            "- Courses at same **difficulty** will be similar\n",
            "\n",
            "---"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 📝 **Step 3: TF-IDF Vectorization**\n",
            "\n",
            "**TF-IDF** = Term Frequency - Inverse Document Frequency\n",
            "\n",
            "**What it does:**\n",
            "- Converts text to numerical vectors\n",
            "- Gives weight to important words\n",
            "- Reduces weight of common words\n",
            "\n",
            "**Example:**\n",
            "```\n",
            "\"Python for Beginners\" → [0.5, 0.8, 0, 0.6, 0, ...]\n",
            "\"Java for Beginners\"   → [0, 0.8, 0.5, 0.6, 0, ...]\n",
            "```\n",
            "\n",
            "**Why:**\n",
            "- Word \"Beginners\" appears in both → Lower weight (common)\n",
            "- Words \"Python\", \"Java\" → Higher weight (distinctive)"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "from sklearn.feature_extraction.text import TfidfVectorizer\n",
            "\n",
            "# Initialize TF-IDF Vectorizer\n",
            "tfidf = TfidfVectorizer(stop_words='english')\n",
            "\n",
            "# Fit and transform\n",
            "tfidf_matrix = tfidf.fit_transform(df_unique['combined_features'])\n",
            "\n",
            "print(\"✅ TF-IDF Vectorization Complete!\")\n",
            "print(f\"\\n📊 Matrix Shape: {tfidf_matrix.shape}\")\n",
            "print(f\"   → {tfidf_matrix.shape[0]:,} courses\")\n",
            "print(f\"   → {tfidf_matrix.shape[1]:,} unique words (features)\")\n",
            "print(f\"   → Sparsity: {(1 - tfidf_matrix.nnz / (tfidf_matrix.shape[0] * tfidf_matrix.shape[1])) * 100:.2f}%\")\n",
            "\n",
            "print(\"\\n📝 Sample vocabulary:\")\n",
            "print(list(tfidf.vocabulary_.keys())[:10])"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "#### 🎤 **Interview Talking Point:**\n",
            "\n",
            "> *\"I used TF-IDF vectorization to convert course text features into numerical vectors. This created a sparse matrix of about X thousand features, where each course is represented by the importance-weighted words in its title, instructor name, and difficulty level. The high sparsity (~99%) is normal for text data and efficiently handled by sparse matrix representations.\"*\n",
            "\n",
            "---"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 📝 **Step 4: Cosine Similarity Matrix**\n",
            "\n",
            "**Purpose:** Measure how similar courses are to each other\n",
            "\n",
            "**Cosine Similarity:**\n",
            "- Measures angle between vectors\n",
            "- Range: 0 (completely different) to 1 (identical)\n",
            "- Works well for text data\n",
            "\n",
            "**Visual:**\n",
            "```\n",
            "Course A: →\n",
            "Course B: ↗  (Small angle = Similar = High score)\n",
            "Course C: ↓  (Large angle = Different = Low score)\n",
            "```"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "from sklearn.metrics.pairwise import cosine_similarity\n",
            "\n",
            "# Calculate cosine similarity\n",
            "cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)\n",
            "\n",
            "print(\"✅ Cosine Similarity Matrix Created!\")\n",
            "print(f\"\\n📊 Matrix Shape: {cosine_sim.shape} (square matrix)\")\n",
            "print(f\"   Each cell = similarity between two courses\")\n",
            "\n",
            "# Show sample similarities\n",
            "print(\"\\n📝 Sample: First course's similarities:\")\n",
            "print(f\"   With itself: {cosine_sim[0, 0]:.3f} (should be 1.0)\")\n",
            "print(f\"   With course 2: {cosine_sim[0, 1]:.3f}\")\n",
            "print(f\"   With course 3: {cosine_sim[0, 2]:.3f}\")\n",
            "\n",
            "# Find most similar course to the first one\n",
            "similar_indices = cosine_sim[0].argsort()[::-1][1:6]  # Top 5, excluding itself\n",
            "print(\"\\n🎯 Top 5 most similar courses to:\", df_unique['course_name'].iloc[0])\n",
            "for idx in similar_indices:\n",
            "    print(f\"   {df_unique['course_name'].iloc[idx]} (similarity: {cosine_sim[0, idx]:.3f})\")"
        ]
    }
]

notebook['cells'].extend(preprocessing_cells)

with open('INTERVIEW_PREP_GUIDE.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print("✅ Added Preprocessing section!")
print("📊 Total cells:", len(notebook['cells']))
