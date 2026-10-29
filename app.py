from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>AWS CI/CD Lab</title>
        </head>
        <body>
            <h1>Hello from my AWS CI/CD application!</h1>
            <p>This application is running with Flask and Docker.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)