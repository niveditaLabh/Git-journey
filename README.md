## Sign Language Translator

A comprehensive Python application that translates between sign language video and text using hand gesture recognition and generates 3D animations for sign language interpretation.

### Features

✅ **Video to Text Translation**
- Real-time hand gesture recognition using MediaPipe
- Camera feed processing for live sign language recognition
- Support for pre-recorded videos
- Gesture sequence analysis and conversion to text

✅ **Text to Sign Language Animation**
- Convert written text to sign language animations
- 3D hand position and orientation tracking
- Multiple gesture support (hello, goodbye, thank you, love, etc.)
- Animation export to JSON and Blender formats

✅ **Advanced Gesture Recognition**
- Machine learning-based gesture classification
- Feature extraction from hand landmarks
- Hand shape and orientation analysis
- Movement detection between frames

### Project Structure

```
├── sign_language_translator.py      # Main translator module
├── gesture_recognition_advanced.py  # ML-based gesture recognition
├── 3d_animation_generator.py        # 3D animation generation
├── requirements.txt                 # Python dependencies
├── gestures.json                    # Gesture dictionary
├── gesture_model.pkl                # Trained ML model (generated)
└── README.md                        # This file
```

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/niveditaLabh/Git-journey.git
cd Git-journey
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Verify installation:**
```bash
python -c "import cv2, mediapipe; print('All dependencies installed!')"
```

### Usage

#### 1. Video to Text Translation

**Using Webcam:**
```python
from sign_language_translator import SignLanguageTranslator

translator = SignLanguageTranslator()
translator.video_to_text(video_source=0)
```

**Using Pre-recorded Video:**
```python
translator.video_to_text(video_source="path/to/video.mp4")
```

**Command Line:**
```bash
python sign_language_translator.py
# Select option 1 for video to text
```

#### 2. Text to Animation

**Generate Animation:**
```python
from sign_language_translator import SignLanguageTranslator

translator = SignLanguageTranslator()
animation_sequence = translator.text_to_animation("hello everyone")
```

**Command Line:**
```bash
python sign_language_translator.py
# Select option 2 for text to animation
# Enter your text
```

#### 3. Advanced ML-based Recognition

```python
from gesture_recognition_advanced import GestureRecognitionML

ml_recognizer = GestureRecognitionML()

# Extract features from landmarks
features = ml_recognizer.extract_features(hand_landmarks)

# Predict gesture
gesture, confidence = ml_recognizer.predict_gesture(hand_landmarks)
print(f"Recognized: {gesture} (Confidence: {confidence:.2%})")
```

#### 4. Generate 3D Animations

```python
from 3d_animation_generator import SignLanguageAnimationGenerator

generator = SignLanguageAnimationGenerator()

# Generate animation for text
animation_data = generator.generate_animation_sequence("thank you")

# Export to JSON
generator.export_animation_to_json(animation_data, "animation.json")

# Export for Blender
generator.export_animation_to_blender(animation_data, "animation.py")
```

### Supported Gestures

| Gesture | Meaning | Hand Shape |
|---------|---------|-----------|
| `hello` | Hello/Hi | Open palm, waving motion |
| `goodbye` | Goodbye/Bye | Open palm, waving (right) |
| `thank_you` | Thank You | Open hands, moving up-down |
| `love` | Love/Heart | Both hands forming heart |
| `yes` | Yes/Agreement | Thumbs up with nodding |
| `no` | No/Disagreement | Open hand with shaking |
| `peace` | Peace | V-shaped fingers |
| `good` | Good | Thumbs up |
| `bad` | Bad | Thumbs down |
| `help` | Help | Both hands reaching up |

### How It Works

#### Video to Text Pipeline

1. **Hand Detection**: Uses MediaPipe to detect hand landmarks in each frame
2. **Feature Extraction**: Extracts 21 hand landmarks (3D coordinates)
3. **Gesture Recognition**: Classifies gestures using:
   - Simple rule-based recognition (initial)
   - ML-based classification (advanced)
4. **Sequence Analysis**: Combines gestures to form meaningful text
5. **Output**: Converts gesture sequence to text

#### Text to Animation Pipeline

1. **Text Parsing**: Splits input text into words
2. **Word-to-Gesture Mapping**: Maps each word to a gesture
3. **Animation Generation**: Creates 3D animation frames for each gesture
4. **Sequence Creation**: Combines individual gesture animations
5. **Export**: Saves animation data in various formats (JSON, Blender)

### Output Files

The application generates several output files:

- `translation_output.txt` - Translated text from video
- `animation_sequence.json` - Animation frame data
- `gesture_model.pkl` - Trained ML model for gesture recognition
- `sign_language_animation.json` - Exported animation data
- `sign_language_blender.py` - Blender-compatible animation script

### Requirements

- Python 3.7+
- OpenCV 4.8+
- MediaPipe 0.10+
- NumPy 1.24+
- Scikit-learn 1.3+
- TensorFlow 2.13+ (optional, for advanced models)

### Limitations & Future Improvements

**Current Limitations:**
- Single-hand recognition (dual-hand support in progress)
- Limited gesture vocabulary (can be expanded)
- Basic animation (more realistic models needed)
- No facial expressions (can be added with MTCNN)

**Future Enhancements:**
- [ ] Dual-hand gesture recognition
- [ ] Facial expression detection
- [ ] Real-time 3D rendering
- [ ] Integration with sign language datasets (ASL, BSL, etc.)
- [ ] Web interface for easier access
- [ ] Mobile app version
- [ ] Support for multiple sign languages
- [ ] Improved ML models for better accuracy

### Troubleshooting

**Issue: Camera not working**
```python
# Test camera
import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if not ret:
    print("Camera not accessible")
cap.release()
```

**Issue: No gestures recognized**
- Ensure adequate lighting
- Keep hands clearly visible
- Move hands slowly for better tracking

**Issue: Model not found**
- Train a new model first or use rule-based recognition
- Check gesture_model.pkl file exists

### Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

### License

This project is open source and available under the MIT License.

### References

- [MediaPipe Hand Detection](https://google.github.io/mediapipe/solutions/hands)
- [Sign Language Recognition Papers](https://arxiv.org/)
- [ASL Dataset](https://www.kaggle.com/datasets/grassknoted/asl-alphabet)

### Contact

For questions or suggestions, please open an issue on GitHub.

---

**Made with ❤️ by Nivedita**
