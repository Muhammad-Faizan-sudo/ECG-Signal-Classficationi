#Classes
Model trained on four classes of ECG signal which are follow as
['COVID-19 Patients', 'Normal Person', 'Myocardial Infarction Patients', 'abnormal heart beats']

#Dataset
Dataset can be downloaded from [here](https://drive.google.com/drive/folders/1iIh7O2DpoYB1ZpDspgE3Boax8PV-RXuC?usp=sharing).

#Model Performance

model folder contains the trained model. It trained on the 1000 images per class. Due to less imbalance dataset, I apply the Data Augmentation on it.
##Model Metrics
Accuracy: 0.910000
Precision: 0.910000
Recall: 0.910000
F1 score: 0.910000
Confusion matrix:
 [[204   5   0   0]
 [  1 181   0  31]
 [  0   0 194   0]
 [  1  34   0 149]]


#How to Run the inference the model
1. create the virtual env
2. pip install -r requirements.txt
3. Change the path of img in inference.py
4. Run the command python3 run.py
