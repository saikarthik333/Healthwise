# 🧠 HealthWise Pro: AI Symptom Checker & Doctor Locator

An intelligent web application built with Streamlit that predicts medical conditions from symptoms, provides general remedies, finds nearby doctors using OpenStreetMap, and generates a downloadable health report.

---

## ✨ Key Features

-   **Symptom-Based Prediction**: Uses a machine learning model (`RandomForestClassifier`) to predict potential diseases based on user-selected symptoms.
-   **Remedy & Specialist Suggestions**: Provides a list of general, non-prescriptive remedies and recommends the appropriate medical specialist for the predicted condition.
-   **Nearby Doctor Locator**: Integrates with the free and open-source OpenStreetMap to find and display nearby doctors and hospitals on an interactive map.
-   **PDF Report Generation**: Allows users to download a comprehensive summary of their analysis, including symptoms, prediction, and remedies, in a clean PDF format.

---

## 🛠️ Tech Stack

-   **Backend**: Python
-   **Web Framework**: Streamlit
-   **Machine Learning**: Scikit-learn, Pandas
-   **Geocoding & Mapping**: Geopy, OpenStreetMap
-   **PDF Generation**: FPDF2

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

-   Python 3.8 or higher
-   `pip` package manager

### Installation & Setup

1.  **Clone the repository (or download the source code):**
    ```bash
    git clone [https://github.com/your-username/Healthwise.git](https://github.com/your-username/Healthwise.git)
    cd Healthwise
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Train the Machine Learning Model:**
    This is a one-time step that creates the saved model files.
    ```bash
    python train_model.py
    ```
    You should see a success message confirming that `model.pkl` and `symptoms.pkl` have been saved.

5.  **Run the Streamlit Application:**
    ```bash
    streamlit run app.py
    ```
    The application will automatically open in your default web browser.

---

## 📁 Project Structure

<pre>
<code>
Healthwise/
│
├── data/
│   └── dataset.csv         # The training dataset
│
├── models/
│   ├── model.pkl           # Saved trained ML model
│   └── symptoms.pkl        # Saved list of symptoms
│
├── components/
│   ├── __init__.py
│   ├── maps.py             # Logic for OpenStreetMap API
│   ├── prediction.py       # Logic for ML prediction
│   └── recommendation.py   # Logic for specialist, remedies, PDF
│
├── app.py                  # Main Streamlit application file
├── train_model.py          # Script to train the ML model
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
</code>
</pre>

---

## ⚠️ Disclaimer

This application is an AI-powered proof of concept and is **not a substitute for professional medical advice, diagnosis, or treatment**. Always seek the advice of a qualified health provider with any questions you may have regarding a medical condition.



