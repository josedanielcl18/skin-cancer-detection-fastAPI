import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

from keras.preprocessing import image 


# def read_image(image):
#     return mpimg.imread(image)

def read_image(img_name):
    img = image.load_img(img_name, target_size=(224,224))
    img = image.img_to_array(img)
    img = img/255.0
    return img


def format_image(image):
    return tf.image.resize(image[tf.newaxis, ...], [224, 224]) / 255.0


def get_category(img):
    """Write a Function to Predict the Class Name

    Args:
        img [jpg]: image file

    Returns:
        [str]: Prediction
    """

    path = 'app/static/models/'
    tflite_model_file = 'converted_model.tflite'

    # Load TFLite model and allocate tensors.
    with open(path + tflite_model_file, 'rb') as fid:
        tflite_model = fid.read()

    # Interpreter interface for TensorFlow Lite Models.
    interpreter = tf.lite.Interpreter(model_content=tflite_model)
    interpreter.allocate_tensors()

    # Gets model input and output details.
    input_index = interpreter.get_input_details()[0]
    output_index = interpreter.get_output_details()[0]
    #print('input_index', input_index)
    #print('output_index', output_index)

    print(img)
    input_img = read_image(img)
    input_img = np.expand_dims(input_img, axis=0)
    interpreter.resize_tensor_input(0, [1, 224, 224, 3])
    interpreter.allocate_tensors()
    #format_img = format_image(input_img)
    # Sets the value of the input tensor
#    interpreter.set_tensor(input_index, format_img)
    interpreter.set_tensor(input_index['index'], input_img)
    # Invoke the interpreter.
    interpreter.invoke()

    predictions_array = interpreter.get_tensor(output_index['index'])
    print(predictions_array) #.round().reshape(-1)
    #predicted_label = np.argmax(predictions_array)
    predicted_label = int(predictions_array.round().reshape(-1))
    print(predicted_label)

    #class_names = ['rock', 'paper', 'scissors']
    class_names = ['Benign', 'Malignant']

    return class_names[predicted_label]


def plot_category(img, current_time):
    """Plot the input image

    Args:
        img [jpg]: image file
    """
    read_img = mpimg.imread(img)
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(ROOT_DIR + f'/static/test_images/{current_time}')
    print(file_path)

    if os.path.exists(file_path):
        os.remove(file_path)

    plt.imsave(file_path, read_img)
