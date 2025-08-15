import joblib
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

def predict_unseen_data(model_path, label_encoder_path, unseen_data_path):
    # Load unseen data
    df_unseen = pd.read_csv(unseen_data_path)
    X_unseen_np = df_unseen.values.astype(np.float32)

    # Load label encoder for decoding class indices
    le = joblib.load(label_encoder_path)

    # Load the saved model (normalizer included inside)
    model = keras.models.load_model(model_path)

    # Predict: get both regression and classification outputs
    preds = model.predict(X_unseen_np)
    plant_performance_preds = preds[0].flatten()
    class_preds_indices = np.argmax(preds[1], axis=1)
    class_preds_labels = le.inverse_transform(class_preds_indices)

    # Append predictions to dataframe
    df_unseen['Predicted_Plant_Performance'] = plant_performance_preds
    df_unseen['Predicted_Parameter'] = class_preds_labels

    # Save predictions to CSV
    output_path = "unseen_data_predictions.csv"
    df_unseen.to_csv(output_path, index=False)
    print(f"Predictions saved to '{output_path}'.")

    return df_unseen

if __name__ == "__main__":
    model_path = "tanh_best_model.keras" #Model Input file path
    label_encoder_path = "label_encoder.pkl" #Encoder file path
    unseen_data_path = "d:\\Prediction_model\\Manuscript\\Prediction_model-main\\unseen_yield.csv" #OUTPUT File path

    predictions = predict_unseen_data(model_path, label_encoder_path, unseen_data_path)
    print(predictions.head())
