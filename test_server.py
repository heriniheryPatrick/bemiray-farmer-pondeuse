from flask import Flask

app = Flask(__name__)

@app.route('/pondeuses')
def pondeuses():
    return "<h1>Test réussi ! Le serveur fonctionne sans erreur 403.</h1>", 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)