# Remove TF dependency
from PIL import Image
import numpy as np
import tflite_runtime.interpreter as tflite
import requests
from io import BytesIO
# Remove tensorflow dependency


def preprocess_input_img(x):
    x /= 127.5
    x -= 1.
    return x

def img_to_np(img):
    img_arr = np.array(img, dtype='float32')
    img_1 = np.array([img_arr])
    return img_1


def load_img_from_path(path):
    with Image.open(path) as img:
        img = img.resize((150, 150), Image.NEAREST)

    return img_to_np(img)


def load_img_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img_to_np(img)

def predict(img):
    X = preprocess_input_img(img)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()

    return dict(zip(classes, float_predictions))


classes = ['dress',
           'hat',
           'longsleeve',
           'outwear',
           'pants',
           'shirt',
           'shoes',
           'shorts',
           'skirt',
           't-shirt']


# load the tflite model
interpreter = tflite.Interpreter(
    model_path='./saved_models/clothing-model.tflite')
# load the weights from the model to memory
interpreter.allocate_tensors()
input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

path = "./images/hat.jpg"
url = "https://whyy.org/wp-content/uploads/2019/12/bright-daylight-environment-forest-240040-1-150x150.jpg"
print(predict(load_img_from_path(path)))
print(predict(load_img_from_url(url)))