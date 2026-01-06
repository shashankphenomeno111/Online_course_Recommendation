# Alternative Collaborative Filtering using scikit-learn's NMF
# This replaces the surprise library with a pure scikit-learn implementation

import numpy as np
import pandas as pd
from sklearn.decomposition import NMF
from sklearn.metrics import mean_squared_error, mean_absolute_error

class SimpleCollaborativeFilter:
    """
    Collaborative Filtering using Non-negative Matrix Factorization (NMF)
    Alternative to surprise library's SVD
    """
    def __init__(self, n_factors=20, random_state=42):
        self.n_factors = n_factors
        self.model = NMF(n_components=n_factors, init='random', random_state=random_state, max_iter=200)
        self.user_factors = None
        self.item_factors = None
        self.user_mapping = {}
        self.item_mapping = {}
        self.reverse_user_mapping = {}
        self.reverse_item_mapping = {}
        
    def fit(self, user_item_matrix):
        """Fit the model on user-item interaction matrix"""
        # Store mappings
        self.user_mapping = {user: idx for idx, user in enumerate(user_item_matrix.index)}
        self.item_mapping = {item: idx for idx, item in enumerate(user_item_matrix.columns)}
        self.reverse_user_mapping = {idx: user for user, idx in self.user_mapping.items()}
        self.reverse_item_mapping = {idx: item for item, idx in self.item_mapping.items()}
        
        # Fit NMF
        self.user_factors = self.model.fit_transform(user_item_matrix.values)
        self.item_factors = self.model.components_
        
        return self
    
    def predict(self, user_id, item_id):
        """Predict rating for a user-item pair"""
        if user_id not in self.user_mapping or item_id not in self.item_mapping:
            return 3.0  # Default prediction
        
        user_idx = self.user_mapping[user_id]
        item_idx = self.item_mapping[item_id]
        
        prediction = np.dot(self.user_factors[user_idx], self.item_factors[:, item_idx])
        # Clip to rating scale
        return min(5.0, max(1.0, prediction))
    
    def recommend(self, user_id, n=10, exclude_items=None):
        """Get top N recommendations for a user"""
        if user_id not in self.user_mapping:
            return []
        
        user_idx = self.user_mapping[user_id]
        user_vector = self.user_factors[user_idx]
        
        # Compute scores for all items
        scores = np.dot(user_vector, self.item_factors)
        
        # Get top items
        top_indices = np.argsort(scores)[::-1]
        
        recommendations = []
        for idx in top_indices:
            item_id = self.reverse_item_mapping[idx]
            if exclude_items and item_id in exclude_items:
                continue
            recommendations.append((item_id, scores[idx]))
            if len(recommendations) >= n:
                break
        
        return recommendations

print("✅ Alternative Collaborative Filtering class created!")
print("   Uses NMF from scikit-learn instead of surprise library")
