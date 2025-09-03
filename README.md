# AI Maturity Assessment Web Application

A Django-based web application for conducting AI maturity assessments, powered by MongoDB Atlas.

## Prerequisites
- Python 3.x
- MongoDB Atlas account
- Git

## Installation

1. **Clone the repository and navigate to project directory:**
   ```bash
   cd path/to/your/ai_maturity_app
   ```

2. **Set up virtual environment:**
   ```bash
   python -m venv env

   venv\Scripts\activate  # Windows
   
   source env/bin/activate  # Unix/macOS
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MongoDB:**
- Create `.env` file
- Add your MongoDB Atlas credentials:
   ```
   MONGODB_URI=<mongodb_uri>
   MONGODB_NAME=<mongodb_name>
    ```

5. **Start the application:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application at [http://localhost:8000](http://localhost:8000)**

<!-- ## Features
- 12 assessment categories with 5 questions each
- Real-time scoring with MongoDB storage
- Interactive radar charts for results
- Personalized recommendations
- Responsive design for all devices

## Need Help?
Check our [documentation](docs/README.md) or create an issue in the repository. -->

<!-- # AI Maturity Assessment Web Application

Django web application for conducting AI maturity assessments with MongoDB Atlas backend.

## Setup Instructions
1. **Navigate to your project directory***
   - cd path\to\your\project

# 2. Create and activate a virtual environment
python -m venv env
source env/bin/activate  # For Unix/macOS
# OR
venv\Scripts\activate      # For Windows (use in Command Prompt or PowerShell)

# 3. Install project dependencies
pip install -r requirements.txt

# 4. Update .env file with MongoDB Atlas credentials
# Open the .env file and replace <username>, <password>, <cluster> with your MongoDB credentials

# 5. Run the application
python manage.py runserver

# 6. Access the application at
# http://localhost:8000 -->

<!-- 1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure MongoDB Atlas**
   - Update `.env` file with your MongoDB Atlas connection string
   - Replace `username`, `password`, and `cluster` with your credentials

3. **Run the Application**
   ```bash
   To Run the Application:
   Install dependencies: pip install -r requirements.txt
   Update .env with your MongoDB Atlas credentials
   Run: python manage.py runserver

Access at http://localhost:8000
   venv\Scripts\activate
   ```
   ```bash
   python manage.py runserver
   ```

4. **Access the Application**
   - Open browser to `http://localhost:8000`
   - Start the assessment and complete all 12 categories -->

## Features

- **Interactive Assessment**: 12 categories with 5 questions each
- **Real-time Scoring**: Automatic calculation and storage in MongoDB
- **Visual Results**: Radar chart comparing to industry benchmarks
- **Personalized Recommendations**: Tailored next steps based on maturity level
- **Responsive Design**: Works on desktop and mobile devices

## Application Structure

- `assessment/models.py` - MongoDB integration and scoring logic
- `assessment/questions.py` - Assessment questions and options
- `assessment/views.py` - Django views handling user interactions
- `templates/` - HTML templates with Tailwind CSS styling

## Assessment Categories

1. AI Vision & Strategic Intent
2. Leadership & Governance
3. Investment & Strategic Intent
4. Data Infrastructure & Quality
5. AI Use Cases & Adoption
6. Talent & Culture
7. Responsible AI & Risk
8. Measurement, Scaling & ROI
9. AI Operating Model
10. Technology & AI Infrastructure
11. Decision Maturity
12. Metric Maturity

## Scoring System

- Each question scored 1-5 (Nascent to Advanced)
- Category scores averaged across 5 questions
- Overall maturity level calculated from all categories
- Industry benchmarks provided for comparison 