import pickle

from flask import Flask, render_template, request, redirect

app = Flask(__name__)
 print(app)
model = pickle.load(open('model.pkl','rb'))
 print(model)

@app.route('/')
def index_page():
    print(model)
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict_logic():

    if request.method == 'POST':
        duration = float(request.form.get('duration'))
        listens = float(request.form.get('listens'))
        acousticness = float(request.form.get('acousticness'))
        danceability = float(request.form.get('danceability'))
        energy = float(request.form.get('energy'))
        instrumentalness = float(request.form.get('instrumentalness'))
        liveness = float(request.form.get('liveness'))
        speechiness = float(request.form.get('speechiness'))
        tempo = float(request.form.get('tempo'))
        valence = float(request.form.get('valence'))
    pred_name = model.predict([[duration,listens,acousticness, danceability, energy, instrumentalness, liveness, speechiness, tempo, valence]]).tolist()[0]
    return render_template('index.html', pred_name=pred_name)



if __name__ == '__main__':
    app.run(debug=True)
