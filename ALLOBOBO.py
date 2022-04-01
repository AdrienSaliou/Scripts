from flask import Flask, render_template , render_template, url_for , request, redirect


app = Flask(__name__)

# Routing de toutes les pages HTML pour que l'application puisse nous rediriger sur les bonnes pages depuis le site

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/Contact', methods=['POST', 'GET'])
def contact():
    return render_template('Contact.html')

@app.route('/Qui nous sommes', methods=['POST', 'GET'])
def quiNousSommes():
    return render_template('Qui nous sommes.html')

@app.route('/FAQ', methods=['POST', 'GET'])
def faq():
    return render_template('FAQ.html')    

@app.route('/Nos solutions', methods=['POST', 'GET'])
def nosSolutions():
    return render_template('Nos solutions.html') 

@app.route('/Nos offres', methods=['POST', 'GET'])
def nosOffres():
    return render_template('Nos offres.html')

@app.route('/page docteur', methods=['POST', 'GET'])
def docteur():
    return render_template('page docteur.html')

@app.route('/page essential', methods=['POST', 'GET'])
def essential():
    return render_template('page essential.html')

@app.route('/page pharmacy', methods=['POST', 'GET'])
def pharmacy():
    return render_template('page pharmacy.html')



if __name__ == "__main__":
    app.run(debug=True)