"""
Advanced Gesture Recognition Module
Uses machine learning for more accurate sign language recognition
"""

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
from pathlib import Path


class GestureRecognitionML:
    """Machine learning-based gesture recognition"""
    
    def __init__(self, model_path="gesture_model.pkl"):
        """Initialize the ML-based gesture recognizer"""
        self.model_path = Path(model_path)
        self.model = None
        self.scaler = StandardScaler()
        self.gesture_labels = [
            "hello", "goodbye", "thank you", "yes", "no", 
            "love", "peace", "good", "bad", "help"
        ]
        
        if self.model_path.exists():
            self.load_model()
        else:
            print("No trained model found. Train a model first.")
    
    def extract_features(self, hand_landmarks):
        """
        Extract features from hand landmarks for ML model
        Features include:
        - Distance between key points
        - Angles between fingers
        - Hand shape characteristics
        """
        if hand_landmarks is None or len(hand_landmarks) == 0:
            return None
        
        landmarks = hand_landmarks[0]  # Use first hand
        features = []
        
        # 1. Extract coordinate features (normalized)
        for landmark in landmarks:
            features.extend([landmark[0], landmark[1], landmark[2]])
        
        # 2. Calculate distances between key landmarks
        key_distances = self._calculate_distances(landmarks)
        features.extend(key_distances)
        
        # 3. Calculate angles between fingers
        angles = self._calculate_angles(landmarks)
        features.extend(angles)
        
        return np.array(features).reshape(1, -1)
    
    def _calculate_distances(self, landmarks):
        """Calculate distances between key points"""
        distances = []
        key_points = [0, 4, 8, 12, 16, 20]  # Wrist and finger tips
        
        for i in range(len(key_points)):
            for j in range(i+1, len(key_points)):
                p1 = landmarks[key_points[i]]
                p2 = landmarks[key_points[j]]
                dist = np.sqrt(sum((p1[k] - p2[k])**2 for k in range(3)))
                distances.append(dist)
        
        return distances
    
    def _calculate_angles(self, landmarks):
        """Calculate angles between fingers"""
        angles = []
        
        # Calculate angle between thumb and index, index and middle, etc.
        finger_tips = [4, 8, 12, 16, 20]
        
        for i in range(len(finger_tips)-1):
            tip1 = landmarks[finger_tips[i]]
            tip2 = landmarks[finger_tips[i+1]]
            palm = landmarks[0]
            
            # Vector from palm to tip1
            v1 = tip1 - palm
            # Vector from palm to tip2
            v2 = tip2 - palm
            
            # Calculate angle
            cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-6)
            angle = np.arccos(np.clip(cos_angle, -1.0, 1.0))
            angles.append(angle)
        
        return angles
    
    def predict_gesture(self, hand_landmarks):
        """Predict gesture from hand landmarks using trained model"""
        if self.model is None:
            return "Model not trained"
        
        features = self.extract_features(hand_landmarks)
        if features is None:
            return None
        
        # Scale features
        features_scaled = self.scaler.transform(features)
        
        # Predict
        prediction = self.model.predict(features_scaled)
        confidence = self.model.predict_proba(features_scaled).max()
        
        gesture = self.gesture_labels[prediction[0]] if prediction[0] < len(self.gesture_labels) else "Unknown"
        
        return gesture, confidence
    
    def train_model(self, training_data, labels):
        """
        Train the ML model
        training_data: List of extracted features
        labels: Corresponding gesture labels
        """
        # Fit scaler
        self.scaler.fit(training_data)
        training_data_scaled = self.scaler.transform(training_data)
        
        # Train Random Forest
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(training_data_scaled, labels)
        
        # Save model
        self.save_model()
        print("Model trained and saved successfully!")
    
    def save_model(self):
        """Save trained model to disk"""
        with open(self.model_path, 'wb') as f:
            pickle.dump((self.model, self.scaler), f)
    
    def load_model(self):
        """Load trained model from disk"""
        with open(self.model_path, 'rb') as f:
            self.model, self.scaler = pickle.load(f)
        print("Model loaded successfully!")


class HandPoseAnalyzer:
    """Analyze hand pose for detailed gesture understanding"""
    
    @staticmethod
    def get_hand_shape(landmarks):
        """Determine overall hand shape"""
        if landmarks is None:
            return "unknown"
        
        # Count extended fingers
        finger_tips = [4, 8, 12, 16, 20]
        palm_base = landmarks[0]
        
        extended_count = 0
        for tip_idx in finger_tips:
            if landmarks[tip_idx][1] < palm_base[1]:  # Tip above palm base
                extended_count += 1
        
        if extended_count == 5:
            return "open_hand"
        elif extended_count == 0:
            return "closed_fist"
        elif extended_count == 2:
            return "peace_sign"
        elif extended_count == 1:
            return "pointing"
        else:
            return "partial_open"
    
    @staticmethod
    def get_hand_orientation(landmarks):
        """Determine hand orientation (palm up, palm down, etc.)"""
        if landmarks is None:
            return "unknown"
        
        # Use palm center and some key points
        palm = landmarks[0]
        middle_tip = landmarks[12]
        
        # Calculate orientation based on y-coordinate difference
        if middle_tip[1] < palm[1]:
            return "palm_up"
        else:
            return "palm_down"
    
    @staticmethod
    def get_hand_movement(prev_landmarks, curr_landmarks):
        """Calculate hand movement between frames"""
        if prev_landmarks is None or curr_landmarks is None:
            return "stationary"
        
        # Calculate distance moved
        prev_palm = prev_landmarks[0]
        curr_palm = curr_landmarks[0]
        
        distance = np.sqrt(sum((curr_palm[i] - prev_palm[i])**2 for i in range(3)))
        
        if distance < 0.01:
            return "stationary"
        elif distance < 0.05:
            return "slow_movement"
        else:
            return "fast_movement"
