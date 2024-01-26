from flask import Flask, request, jsonify
from main import getReview

app = Flask(__name__)

@app.route('/', methods=['POST'])
def summarize_text():
    try:
        # Get the text from the request
        text = request.json['gadget']

        #get reviews 
        response = getReview(text) 
        # Return the summarized text as JSON
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
