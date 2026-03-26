# PRIVATE PASSWORD ANALYZER WITH OSINT TARGETED FEEDBACK


This project analyzes the strength of a password by its tecnical factors (length, variety, ...)
and common elements (first and last names, geographical sites, ...). It evaluates whether a 
password contains information that could be discovered with Open Source Inteligence (OSINT), 
and thus providing its according score. The aim of this project is to estimate the "real" risk
of using a given password, not just its complexity.

## Characteristics:

    - Password strength scoring (0-100)
    - OSINT-based risk detection (slightly spanish oriented)
    - Intuitive and simple feedback
    - Simple web interface using flask

## Instalation:

On Terminal or Cmd run:

1.- Clone repository:
```bash
git clone https://github.com/2010Nick91/ai-password-and-email-analyzer.git
```
then
```bash
cd ai-password-and-email-analyzer
```

2.- Create a virtual environment:
```bash
python3 -m venv venv
```

3.- Activate the virtual environment:

- Linux / macOS:
```bash
source venv/bin/activate
```
- Windows:
```bash
venv\Scripts\activate
```

4.- Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage:

1.- Run the flask application:
```bash
python3 app.py
```

2.- Then, open your browser and go to
```bash
http://127.0.0.1:5000/
```
or
```bash
http://localhost
```

3.- Enter a password and analyze its risk.

## Example:

Input:
```bash
JuanPablo20!
```

Output:
- Score: 69/100
- Good length
- Excellent variety
- Common_elements : pablo, juan
- Moderate risk overall

## Project structure:

```bash
analysis/          # Password analysis logic
templates/         # HTML interface
app.py             # Flask application
requirements.txt   # Dependencies
```

## Limitations:.txt # Dependencies
Limitations
System relies on predefined list of common elements

Does not perform real-time OSINT analysis

False positives may occur

Scoring system is not scientifically validated

- System relies on predefined list of common elements
- Does not perform real-time OSINT analysis
- False positives may be common due to various reasons
- Scoring system is not scientifically validated