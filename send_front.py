from flask import Flask, render_template
from import_data import get_recommendations

# Create Flask app
app = Flask(__name__)


# Route for handling the results
@app.route('/results')
def results():
    # Call the function to get the results from the import_data.py file
    aws_personalize_results = get_recommendations()

    # Render the results in an HTML template
    # Replace 'results.html' with the name of your actual HTML template file
    return render_template('index.html', results=aws_personalize_results)


if __name__ == '__main__':
    # Run the Flask app on localhost with port 5000
    app.run(debug=True)
