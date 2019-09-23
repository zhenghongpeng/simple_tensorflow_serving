import tensorflow as tf
from keras.models import model_from_json
import pandas as pd
from keras.models import load_model
import numpy as np

model_dir = '/media/kevinpeng/cdrive/Users/kevin.peng/code/Depthshift_Depthjump_corrected/Newdata/DepthLogs_cartesian_new/result'


# The export path contains the name and the version of the model
# tf.keras.backend.set_learning_phase(0)  # Ignore dropout at inference

# load json and create model
# json_file = open('../models/keras_well/AnnModel/model_ann_full__2019_09_17_16_02_09.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# model = model_from_json(loaded_model_json)
# # load weights into new model
# model.load_weights("../models/keras_well/AnnModel/model_ann_full__2019_09_17_16_02_09.h5")
# print("Loaded model from disk")
#
#
# model = tf.keras.models.load_model('../models/keras_well/AnnModel/model_ann_full__2019_09_17_16_02_09.json')
# model = model

data = [-0.73907974,  0.30734958, -1.48759525, -1.41191009,  1.63201119,
       -3.08260906,  1.69228755,  0.14006269, -3.08371907, -0.29302639,
        1.64547556, -0.21070207, -1.24723066,  1.20729805, -0.16440292,
       -1.14380009,  1.38035798,  0.58098913, -1.56153634,  1.52001141,
       -2.09498595, -0.67419747,  0.11461625, -3.71976738, -1.80643255]

# Fetch the Keras session and save the model
# The signature definition is defined by the input and output tensors
# And stored with the default serving key
with tf.keras.backend.get_session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())
    tf.keras.backend.set_learning_phase(0)  # Ignore dropout at inference
    model = load_model(f"{model_dir}/ann.h5")
    outputs = {t.name: t for t in model.outputs}
    export_path = '../models/keras_well/AnnModel/2'
    tf.saved_model.simple_save(
        sess,
        export_path,
        inputs={'input_image': model.input},
        outputs={t.name: t for t in model.outputs})




