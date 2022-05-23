Model trained on four classes of ECG signal which are follow as
['COVID-19 Patients', 'Normal Person', 'Myocardial Infarction Patients', 'abnormal heart beats']

model folder contains the trained model. It trained on the 1000 images per class. Due to less imbalance dataset, I apply the Data Augmentation on it.

#How to Run the inference the model
1. create the virtual env
2. pip install -r requirements.txt
3. Change the path of img in inference.py
4. Run the command python3 run.py
