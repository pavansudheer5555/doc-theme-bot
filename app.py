from flask import Flask, render_template
import subprocess

app = Flask(__name__)

# Start Streamlit UI
def run_streamlit():
    subprocess.Popen(["streamlit", "run", "document_ui.py"])

@app.route('/')
def home():
    return "<h1>Flask is running! Click <a href='http://localhost:8501'>here</a> to open Streamlit.</h1>"

if __name__ == '__main__':
    run_streamlit()
    app.run(debug=True)