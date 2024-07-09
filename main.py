from flask import Flask, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

# Set up OpenAI API key
client = OpenAI()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generateimages/<prompt>')
def generate(prompt):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        print(response)
        image_urls = [image.url for image in response.data]
        return jsonify({'data': image_urls})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
