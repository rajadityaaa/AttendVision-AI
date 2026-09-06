# 🎙️ AttendVision AI — Smart AI Attendance System
### Dual Biometric Attendance Verification using Face & Voice Recognition

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![PyTorch](https://img.shields.io/badge/PyTorch-CPU-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Supabase](https://img.shields.io/badge/Supabase-Database-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)

**AttendVision AI** is a multi-modal biometric attendance management system built with Streamlit, Python, and Supabase. It eliminates proxy attendance by combining facial recognition computer vision with voice utterance speaker identification.

---

## 🌟 Key Features

### 📸 Computer Vision Face Recognition
* **Group Photo Recognition**: Process high-resolution classroom photos to detect and recognize multiple student faces simultaneously using 128-dimensional dlib facial embeddings.
* **SVM Machine Learning Classifier**: Support Vector Machine (`scikit-learn`) classifier dynamically trained on registered student embeddings with strict Euclidean distance thresholding.

### 🎙️ Speaker Voice Recognition
* **Utterance & Bulk Speaker Audio Identification**: Powered by `Resemblyzer` and `librosa` for deep voice embedding extraction.
* **Silence-based Audio Segmentation**: Automatically splits class recordings into speech bursts (`top_db` energy detection) and matches each speaker against registered student voice profiles.

### 👨‍🏫 Teacher Management Portal
* **Course & Subject Management**: Create, view, and organize classes by code and section.
* **Biometric Attendance Processing**: Mark attendance automatically via single/group photos or voice recording uploads.
* **Session Details & Manual Overrides**: Inspect attendance breakdown per session and manually correct student status if required.
* **QR Code & Join Link Generator**: Generate QR codes (`segno`) and direct URLs with `join-code` query parameters for instant student self-enrollment.

### 🎓 Student Self-Service Portal
* **One-Click Course Joining**: Join courses effortlessly using course codes or scanned QR links.
* **Biometric Profile Self-Registration**: Self-enroll face embeddings via live webcam capture or photo upload.
* **Voice Profile Enrollment**: Upload or record voice samples to train speaker recognition models.
* **Personal Attendance Log**: View attendance history, percentage stats, and course-wise records.

---

## 🏗️ Project Architecture & Directory Structure

```
Intelligent-AI-Attendance--Face---Voice-Recognition/
├── app.py                      # Main entrypoint & Streamlit page router
├── requirements.txt            # Python dependencies (CPU-optimized PyTorch)
├── packages.txt                # System dependencies for deployment
├── .streamlit/
│   └── secrets.toml            # Supabase API keys & secrets configuration
├── img/                        # App assets & logos
└── src/
    ├── components/             # Reusable UI dialogs & modals
    │   ├── dialog_add_photo.py
    │   ├── dialog_attendance_detail.py
    │   ├── dialog_attendance_results.py
    │   ├── dialog_auto_enroll.py
    │   ├── dialog_browse_courses.py
    │   ├── dialog_course_students.py
    │   ├── dialog_create_subject.py
    │   ├── dialog_enroll.py
    │   ├── dialog_share_subject.py
    │   ├── dialog_voice_attendance.py
    │   ├── dialog_voice_update.py
    │   ├── footer.py
    │   ├── header.py
    │   └── subject_card.py
    ├── database/               # Database integration layer
    │   ├── config.py           # Supabase client initialization
    │   └── db.py               # CRUD database operations & authentication
    ├── pipelines/              # AI Biometric Pipelines
    │   ├── face_pipeline.py    # Dlib face detection & SVM classifier
    │   └── voice_pipeline.py   # Resemblyzer voice embedding & speaker ID
    ├── screens/                # Streamlit views / screens
    │   ├── home_screen.py      # Main landing & portal selector
    │   ├── teacher_screen.py   # Teacher portal dashboard
    │   └── student_screen.py   # Student portal & profile management
    └── ui/                     # CSS styles & visual themes
        └── base_layout.py
```

---

## 🛠️ Tech Stack & Libraries

* **Frontend & Web Framework**: [Streamlit](https://streamlit.io/)
* **Face Recognition**: `dlib-bin`, `face_recognition_models`, `scikit-learn` (SVM)
* **Voice Recognition**: `Resemblyzer`, `librosa`, `soundfile`
* **Deep Learning Framework**: `torch` (PyTorch CPU build)
* **Database & Auth**: `supabase-py`, `bcrypt`
* **Image & QR Utilities**: `Pillow`, `segno`

---

## 🗄️ Database Setup (Supabase)

AttendVision AI uses **Supabase** (PostgreSQL) for backend data management. Execute the following SQL script in your Supabase SQL Editor to set up the necessary tables:

```sql
-- 1. Teachers Table
CREATE TABLE teachers (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. Students Table
CREATE TABLE students (
    student_id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    face_embedding JSONB DEFAULT NULL,
    voice_embedding JSONB DEFAULT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. Subjects Table
CREATE TABLE subjects (
    subject_id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    subject_code TEXT NOT NULL,
    name TEXT NOT NULL,
    section TEXT NOT NULL,
    teacher_id BIGINT REFERENCES teachers(id) ON DELETE CASCADE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. Subject Students (Enrollment Junction Table)
CREATE TABLE subject_students (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    student_id BIGINT REFERENCES students(student_id) ON DELETE CASCADE,
    subject_id BIGINT REFERENCES subjects(subject_id) ON DELETE CASCADE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Attendance Logs Table
CREATE TABLE attendance_logs (
    id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    student_id BIGINT REFERENCES students(student_id) ON DELETE CASCADE,
    subject_id BIGINT REFERENCES subjects(subject_id) ON DELETE CASCADE,
    status TEXT NOT NULL CHECK (status IN ('Present', 'Absent')),
    timestamp TIMESTAMPTZ DEFAULT NOW()
);
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python **3.10+** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/Intelligent-AI-Attendance--Face---Voice-Recognition.git
cd Intelligent-AI-Attendance--Face---Voice-Recognition
```

### 3. Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
> **Note**: `requirements.txt` installs CPU-only PyTorch to keep memory footprint light and compatible with Streamlit Cloud deployments.

### 5. Configure Credentials
Create a `.streamlit/secrets.toml` file in the root directory:

```toml
SUPABASE_URL = "https://your-supabase-project.supabase.co"
SUPABASE_KEY = "your-supabase-anon-or-service-role-key"
```

### 6. Run the Application
```bash
streamlit run app.py
```

Access the app in your browser at `http://localhost:8501`.

---

## 💻 Usage Instructions

### For Teachers:
1. Select **Teacher Portal** from the home screen.
2. Sign up for a teacher account or log in with your credentials.
3. Click **+ Create Subject** to set up a new subject.
4. Share the course QR code or auto-generated link with students.
5. Take attendance by uploading a **group class photo** or **class audio clip**.
6. Review, edit, and save attendance logs.

### For Students:
1. Select **Student Portal** from the home screen.
2. Enter your student name or select your registered profile.
3. Use **Enroll Course** or open a shared join link to enroll in classes.
4. Upload your face photo and voice recording to register your biometric profiles.
5. Track your overall attendance records and class statistics.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
