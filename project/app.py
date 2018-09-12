from flask import Flask, render_template,request
from sklearn.externals import joblib
from sklearn import svm, datasets
#load the data set
clf = svm.SVC()

iris = datasets.load_iris()
x,y = iris.data, iris.target
clf.fit(x,y)

joblib.dump(clf, 'model.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html',title='about')

import numpy as np
from scipy import misc
@app.route('/predict', methods = ['POST'])
def make_prediction():
    if request.method=='POST':
        file = request.files['image']

        if not file:
            return render_template('index.html', label = 'No file')
        img = misc.imread(file)
        img = img[:,:,:3]
        img = img.reshape(1,-1)

        prediction = model.predict(img)
        label = str(np.squeeze(prediction))
        if label == '10':
            label='0'
        return render_template('index.html', label = label, file = file)

if __name__ == '__main__':
    model = joblib.load('model.pkl')
    app.run(debug=True)
