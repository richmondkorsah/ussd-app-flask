# MoMo App Frontend

## Overview

The MoMo App Frontend is a modern web application designed to simulate a mobile money service interface. Built with Flask, HTML, CSS, and JavaScript, this app provides users with a clean and user-friendly experience for managing their mobile money transactions.

## Features

- **Account Balance Display**: Users can view their account balance, which can be toggled between hidden and visible states.
- **Service Buttons**: Access various services such as transferring money, paying bills, and cashing out.
- **Responsive Design**: The UI adapts to different screen sizes for a consistent experience across devices.

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (with a modern design), JavaScript
- **Static Assets**: Managed through Flask's static file handling

## Project Structure
This is how the structure of the project looks like
```
project/
│
├── app.py                    # The main Flask app
├── templates/
│   └── menu.html             # The HTML template for the MoMo app UI
|    └── transfer.html
│
├── static/
│   ├── style/
│   │   └── style.css          # The CSS file for the app's styling
│   ├── js/
│   │   └── script.js          # The JavaScript file for UI behavior
│
└── README.md                  # This documentation file
```