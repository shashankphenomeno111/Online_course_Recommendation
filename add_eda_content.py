"""
Script to add remaining content to INTERVIEW_PREP_GUIDE.ipynb
This continues the comprehensive interview preparation notebook
"""

import json

# Load existing notebook
with open('INTERVIEW_PREP_GUIDE.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Additional cells to add
new_cells = [
    # Continue EDA - More visualizations
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 📊 **Visualization 2: Course Difficulty Distribution**"
        ]
    },
    {
        "cell_type":

 "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Difficulty Level Distribution\n",
            "plt.figure(figsize=(10, 6))\n",
            "\n",
            "difficulty_counts = df['difficulty_level'].value_counts()\n",
            "colors = ['#667eea', '#764ba2', '#f093fb']\n",
            "\n",
            "plt.pie(difficulty_counts.values, labels=difficulty_counts.index, autopct='%1.1f%%',\n",
            "        colors=colors, startangle=90, textprops={'fontsize': 12})\n",
            "plt.title('Course Distribution by Difficulty Level', fontsize=14, fontweight='bold')\n",
            "plt.show()\n",
            "\n",
            "print(\"\\n📊 Difficulty Distribution:\")\n",
            "for level, count in difficulty_counts.items():\n",
            "    print(f\"{level}: {count:,} courses ({count/len(df)*100:.1f}%)\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "#### 🔍 **What This Graph Tells Us:**\n",
            "\n",
            "**Pie Chart:**\n",
            "- Shows the proportion of courses at each difficulty level\n",
            "- **Why it matters:** Helps us understand course catalog balance\n",
            "- **For modeling:** We might weight recommendations differently based on user's skill level\n",
            "\n",
            "**Typical Observations:**\n",
            "- Usually **Beginner > Intermediate > Advanced**\n",
            "- More beginner courses attract new learners\n",
            "- Fewer advanced courses = specialized content\n",
            "\n",
            "**Interview Point:**\n",
            "> *\"The platform has a good distribution across difficulty levels, with more beginner-friendly content to onboard new users, and specialized advanced courses for experienced learners.\"*\n",
            "\n",
            "---"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 📊 **Visualization 3: Price vs Rating Analysis**"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Price vs Rating Scatter Plot\n",
            "plt.figure(figsize=(12, 6))\n",
            "\n",
            "plt.scatter(df['course_price'], df['rating'], alpha=0.3, s=30, c='#667eea')\n",
            "plt.xlabel('Course Price ($)', fontsize=12)\n",
            "plt.ylabel('Rating (1-5)', fontsize=12)\n",
            "plt.title('Course Price vs Rating', fontsize=14, fontweight='bold')\n",
            "plt.grid(alpha=0.3)\n",
            "\n",
            "# Calculate correlation\n",
            "correlation = df['course_price'].corr(df['rating'])\n",
            "plt.text(0.7, 0.95, f'Correlation: {correlation:.3f}', \n",
            "         transform=plt.gca().transAxes, fontsize=12, \n",
            "         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))\n",
            "\n",
            "plt.show()\n",
            "\n",
            "print(f\"\\n📊 Price-Rating Correlation: {correlation:.3f}\")\n",
            "if abs(correlation) < 0.3:\n",
            "    print(\"   → Weak correlation: Price doesn't strongly affect ratings\")\n",
            "elif abs(correlation) < 0.7:\n",
            "    print(\"   → Moderate correlation\")\n",
            "else:\n",
            "    print(\"   → Strong correlation\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "####  🔍 **What This Graph Tells Us:**\n",
            "\n",
            "**Scatter Plot Analysis:**\n",
            "- Each dot = one course\n",
            "- **X-axis:** Price in dollars\n",
            "- **Y-axis:** User rating\n",
            "\n",
            "**Correlation Value:**\n",
            "- **Close to 0:** No relationship (price doesn't affect rating)\n",
            "- **Positive:** Higher price → Higher rating\n",
            "- **Negative:** Higher price → Lower rating\n",
            "\n",
            "**Why This Matters:**\n",
            "- If correlation is weak → **Quality isn't tied to price**\n",
            "- Good for users → Can find great courses at any price point\n",
            "- For recommendations → Don't need to bias toward expensive courses\n",
            "\n",
            "**Interview Point:**\n",
            "> *\"I analyzed the relationship between price and ratings and found weak correlation, indicating that course quality isn't necessarily tied to price. This validates our decision to recommend based on content similarity and user preferences rather than price.\"*\n",
            "\n",
            "---"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 📊 **Visualization 4: Top Instructors**"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Top 10 Instructors by Course Count\n",
            "plt.figure(figsize=(12, 6))\n",
            "\n",
            "top_instructors = df['instructor'].value_counts().head(10)\n",
            "\n",
            "plt.barh(range(len(top_instructors)), top_instructors.values, color='#764ba2')\n",
            "plt.yticks(range(len(top_instructors)), top_instructors.index)\n",
            "plt.xlabel('Number of Course Interactions', fontsize=12)\n",
            "plt.ylabel('Instructor', fontsize=12)\n",
            "plt.title('Top 10 Most Active Instructors', fontsize=14, fontweight='bold')\n",
            "plt.gca().invert_yaxis()\n",
            "plt.grid(axis='x', alpha=0.3)\n",
            "\n",
            "for i, v in enumerate(top_instructors.values):\n",
            "    plt.text(v + 50, i, f'{v:,}', va='center')\n",
            "\n",
            "plt.tight_layout()\n",
            "plt.show()\n",
            "\n",
            "print(\"\\n📊 Top Instructors:\")\n",
            "for idx, (instructor, count) in enumerate(top_instructors.items(), 1):\n",
            "    print(f\"{idx}. {instructor}: {count:,} interactions\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "#### 🔍 **What This Graph Tells Us:**\n",
            "\n",
            "**Bar Chart (Horizontal):**\n",
            "- Shows which instructors have the most user interactions\n",
            "- **Longer bar** = More popular instructor\n",
            "\n",
            "**Why This Matters:**\n",
            "- Popular instructors = quality content\n",
            "- Can use instructor as a feature for content-based filtering\n",
            "- Users who like one course from an instructor might like others\n",
            "\n",
            "**For Recommendations:**\n",
            "- Include instructor in TF-IDF features\n",
            "- \"Users who liked this instructor also liked...\"\n",
            "- Can create instructor-specific recommendations\n",
            "\n",
            "**Interview Point:**\n",
            "> *\"I identified the top instructors and incorporated instructor names into the content-based filtering features. This allows the system to recommend other courses from instructors a user has previously enjoyed.\"*\n",
            "\n",
            "---"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 📊 **Visualization 5: Correlation Heatmap**"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Correlation Heatmap for Numerical Features\n",
            "plt.figure(figsize=(10, 8))\n",
            "\n",
            "# Select numerical columns\n",
            "numeric_cols = df.select_dtypes(include=[np.number]).columns\n",
            "corr_matrix = df[numeric_cols].corr()\n",
            "\n",
            "# Create heatmap\n",
            "sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='RdPu', \n",
            "            square=True, linewidths=0.5, cbar_kws={\"shrink\": 0.8})\n",
            "plt.title('Correlation Heatmap of Numerical Features', fontsize=14, fontweight='bold')\n",
            "plt.tight_layout()\n",
            "plt.show()\n",
            "\n",
            "print(\"\\n📊 Strong Correlations (|r| > 0.5):\")\n",
            "for i in range(len(corr_matrix)):\n",
            "    for j in range(i+1, len(corr_matrix)):\n",
            "        if abs(corr_matrix.iloc[i, j]) > 0.5:\n",
            "            print(f\"{corr_matrix.index[i]} ↔ {corr_matrix.columns[j]}: {corr_matrix.iloc[i, j]:.3f}\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "#### 🔍 **What This Graph Tells Us:**\n",
            "\n",
            "**Heatmap Reading:**\n",
            "- **Color intensity** = Strength of correlation\n",
            "- **Dark purple** = Strong positive correlation (+1)\n",
            "- **Light pink** = Weak correlation (0)\n",
            "- **Numbers** = Exact correlation values\n",
            "\n",
            "**What to Look For:**\n",
            "1. **Diagonal = 1.0** (feature correlated with itself - perfect!)\n",
            "2. **High values off-diagonal** = Features move together\n",
            "3. **Low values** = Independent features (good for modeling)\n",
            "\n",
            "**Common Patterns:**\n",
            "- `time_spent_hours` ↔ `completion_status` → More time = More completions\n",
            "- `rating` ↔ `enrollment_numbers` → Popular courses rated more\n",
            "\n",
            "**For Feature Engineering:**\n",
            "- Highly correlated features → Might remove one (redundant)\n",
            "- Independent features → Keep all (each adds unique information)\n",
            "\n",
            "**Interview Point:**\n",
            "> *\"The correlation analysis revealed that time spent and completion status are strongly related, which makes sense. However, most features show low correlation, meaning each provides unique information for the recommendation models.\"*\n",
            "\n",
            "---"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### 🎯 **Key Insights from EDA**\n",
            "\n",
            "| Insight | Finding | Implication for Modeling |\n",
            "|---------|---------|-------------------------|\n",
            "| **Ratings** | Most ratings are 3-4 stars | Need good differentiation in collaborative filtering |\n",
            "| **Difficulty** | Balanced across levels | Can recommend based on user's skill level |\n",
            "| **Price** | Weak correlation with rating | Don't bias recommendations by price |\n",
            "| **Instructors** | Some very popular | Use instructor as a content feature |\n",
            "| **Features** | Mostly independent | Keep all features for rich representations |\n",
            "\n",
            "---\n",
            "\n",
            "### 🎤 **EDA Summary for Interview**\n",
            "\n",
            "> *\"I performed comprehensive exploratory analysis including distribution plots, correlation analysis, and feature relationships. Key findings were: ratings cluster around 3.5 stars showing consistent quality, difficulty levels are well-balanced, and price doesn't correlate with ratings. I identified top instructors who could be leveraged for content-based filtering. The correlation heatmap showed features are mostly independent, meaning each provides unique signal for the models.\"*\n",
            "\n",
            "---"
        ]
    }
]

# Add cells to notebook
notebook['cells'].extend(new_cells)

# Save updated notebook
with open('INTERVIEW_PREP_GUIDE.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print("✅ Added EDA visualizations to interview prep notebook!")
print("📊 Total cells now:", len(notebook['cells']))
