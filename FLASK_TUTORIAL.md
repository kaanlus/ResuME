# Flask Tutorial: Create a Flask Web App with Markdown

## Step 1: Install Flask

To get started with Flask, you need to install it. You can install Flask using pip, the Python package manager, by running the following command in your terminal or command prompt:

```python
pip install flask
```

## Step 2: Create a Flask Script

Once Flask is installed, you can create a Flask script in a new Python file, for example, `app.py`. Here's an example of a Flask script written in markdown:

```python
from flask import Flask

# Create Flask app
app = Flask(__name__)

# Route for handling the homepage
@app.route('/')
def home():
    return '''
# Welcome to Flask Markdown

This is a **Flask** web application that uses markdown for formatting text.

## Example Heading

You can use markdown to format text in various ways, such as **bold**, *italic*, [links](https://www.example.com), lists, and more.

### Example List

- Item 1
- Item 2
- Item 3

> This is a blockquote

## Example Code

```python
def hello():
    return "Hello, Flask Markdown!"
```

In this example, we create a Flask web application that renders a markdown-formatted text as the homepage. The `@app.route('/')` decorator defines a route for the homepage, and the function `home()` returns a markdown-formatted text as the response.

You can customize the markdown text in the `home()` function according to your needs, including headings, lists, code blocks, tables, and more. Flask will automatically convert the markdown text to HTML and render it in the browser.

## Step 3: Run the Flask App

To run the Flask app, save the Flask script to a Python file (e.g., `app.py`) and run the following command in your terminal or command prompt:

```python
python app.py
```

This will start the Flask app on localhost with port 5000 by default. You can then access the app in your web browser by navigating to `http://127.0.0.1:5000/` or `http://localhost:5000/`.

That's it! You've created a Flask web application that uses markdown for formatting text. You can further customize the Flask app by adding more routes, views, templates, and logic as needed for your specific use case.

Note: This is a basic example and may need to be adapted to your specific requirements. Please refer to the official Flask documentation (https://flask.palletsprojects.com/) for more details on how to build web applications with Flask in a production environment.

##
*Any questions or issues about this project contact __Ben SF#8953__ on Discord*\
###
*- Ben Smith-Foley*\
*RPI Class of 2025, BS Computer Science*\
*smithb15@rpi.edu*