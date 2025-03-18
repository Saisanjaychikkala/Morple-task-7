from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Chikkala Sai Sanjay"  # Replace with your name
    username = os.getenv("USER") or os.getenv("USERNAME")  # Get system username
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    

    # Run 'top' command and get output
    top_output = subprocess.getoutput("top -bn1")

    response = f"""
    <h1>Name: {name}</h1>
    <h2>User: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <h2>Top output:</h2>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

