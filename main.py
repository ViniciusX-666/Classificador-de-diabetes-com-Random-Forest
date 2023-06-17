from flask import Flask, render_template, request, jsonify
import pickle

modelo = pickle.load(open('modelo.sav', 'rb'))

colunas = ['gender', 'age', 'hypertension', 'heart_disease','smoking_history','bmi','HbA1c_level','blood_glucose_level']

app = Flask('meu_app')

@app.route('/')
def index():
    return render_template('novo.html', titulo='Verifique se você possui diabetes')

@app.route('/classifica/', methods=['POST'])
def classifica():
    dados = request.form
    dados_input = [float(dados[col]) for col in colunas]

    classe = modelo.predict([dados_input])
    if classe == 0:
        resultado = 'Parabéns, você não possui diabetes.'
    else:
        resultado = 'Possui diabetes.'

    return render_template('resultado.html', titulo='Verifique se você possui diabetes', resultado=resultado)


app.run()