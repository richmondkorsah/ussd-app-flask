# MoMo App Development Log

## Overview

This document serves as a development log for the MoMo App project, which aims to create a user-friendly interface for a mobile money service using Flask, HTML, CSS, and JavaScript.

---

## Day 1: Project Initialization and App Setup

**Date**: [5th October, 2024]  
**Tasks Completed**:
- Created the main project directory named `ussd-app-flask`.
- Set up the Flask environment and ensured Flask was installed.
- Created the `app.py` file to handle the main Flask application logic.
- Verified that the Flask app was running successfully by accessing it in a web browser.

**Code Snippet**:
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Day 2: UI Development

**Date**: [6th October, 2024]  
**Tasks Completed**:
- Developed the `menu.html` file in the `templates` folder to create the app's UI.
- Designed sections for displaying account balance and buttons for various services.
- Linked the CSS and JavaScript files in the HTML template.

**Code Snippet**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MoMo App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style/style.css') }}">
</head>
<body>
    <div class="container">
        <h1>MoMo App</h1>
        <div class="balance">
            <p>Account Balance</p>
            <div class="balance-info">
                <span id="balance" class="hidden">**********</span>
                <button class="eye-button" onclick="toggleBalance()">&#128065;</button>
            </div>
            <small>Click on the eye icon to show/hide amount</small>
        </div>
        <div class="services">
            <button class="service-btn">Transfer Money</button>
            <button class="service-btn">Airtime & Bundles</button>
        </div>
    </div>
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
```

---

## Conclusion

The MoMo App project has made significant progress in the initial days, starting with the app setup and then moving on to UI development. The next steps will focus on adding interactivity and refining the user interface. Stay tuned to find out more on the project

## Social Media Links

Feel free to connect with me on social media:

    LinkedIn: https://www.linkedin.com/in/richmond-korsah-9a290b309/
    Instagram: @_.richie_kk._