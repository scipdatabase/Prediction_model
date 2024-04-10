#!/usr/bin/env python
# coding: utf-8

# import libraries
import pandas as pd
import numpy as np
from keras.models import model_from_json
from sklearn.preprocessing import LabelEncoder
import joblib  # To save and load LabelEncoder
import sys

# Model upload

# load json and create model
json_file = open('model_elu.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model_elu.h5")
print("Loaded model from disk")
le = joblib.load('label_encoder.pkl')


# Classification

def preprocess_categorical_features(data, le):
    # Assuming 'Parameter' is a categorical feature in your dataset
    data['Parameter'] = le.transform(data['Parameter'])
    return data

# Load the data for making predictions with the model
filename = sys.argv[1]  # Assuming the filename is the first command line argument
X_test1 = pd.read_csv(filename)
X_test1.drop(X_test1.columns[[0]], axis=1, inplace=True)


# Prediction

predictions = loaded_model.predict(X_test1)

predicted_class_probs = predictions[1]
predicted_class_index = np.argmax(predicted_class_probs, axis=1)
predicted_class_labels = le.inverse_transform(predicted_class_index)
percent = np.array(predictions[0])
percent *= 100
df_percent = pd.DataFrame(percent, columns=['Percentage_loss'])
df_class = pd.DataFrame(predicted_class_labels, columns=['Class'])
df_combined = pd.concat([df_percent, df_class], axis=1)

# Save the output
df_combined.to_csv('prediction_output.csv', index=False)
