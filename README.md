💎 Diamond Price Predictor
This is an end-to-end Machine Learning web application that predicts diamond prices based on their physical attributes.

🚀 Features
Machine Learning: SVR (Support Vector Regression) model trained with Scikit-Learn.

API: High-performance backend using FastAPI.

Modern UI: Interactive "Antigravity" inspired interface with glassmorphism and mouse-tracking glow.

Preprocessing: Integrated Label Encoding and Standard Scaling.

🛠️ Tech Stack
Backend: Python, FastAPI, Uvicorn

ML: Scikit-Learn, Pandas, Pickle

Frontend: HTML5, CSS3 (Glassmorphism), Jinja2

📦 Installation & Usage
Clone the repository:

Bash
git clone https://github.com/Mert-exe/diamond-price-predictor.git
cd diamond-price-predictor
Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
uvicorn app:app --reload
Access the app at: http://127.0.0.1:8000

📂 Project Structure
app.py: Main FastAPI application.

diamond_model_complete.pkl: Serialized model, encoders, and scaler.

templates/: UI files (HTML/CSS).

requirements.txt: Project dependencies.
