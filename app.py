from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
    
@app.route('/ubicacion')
def ubicacion():
    return render_template('ubicacion.html')

if __name__ == '__main__':
     app.run(debug=True)
