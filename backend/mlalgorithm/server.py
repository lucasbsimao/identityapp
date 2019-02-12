from mlalgorithm import Model
from flask import Flask

app = Flask(__name__)

model = Model()

@app.route('/predict/<int:id>', methods=['GET'])
def train(id):
    model.create_model()
    return str(id)

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
    # model.create_model()
    