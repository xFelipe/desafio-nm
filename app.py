from flask import Flask

app = Flask(__name__)

@app.route('/send-image', methods=['POST'])
def send_image():
    return 'Hello world!'


if __name__ == '__main__':
    app.run(debug=True)
