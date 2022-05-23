import os
from tensorflow import keras
from controller.libraries import *
from sklearn.metrics import confusion_matrix


def img_cropping(img):
  y,h,x,w = 300,1000,50,2100 
  crop = img[y:y+h, x:x+w]  
  return crop


def img_resizing(crop):
  dims = (500,500)
  resized = cv2.resize(crop, dims, interpolation = cv2.INTER_AREA)
  gray_scale = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  
  resized_img = gray_scale.reshape(500,500,1)
  return resized_img

def preprocessing(img):
  dataset = []
  img = cv2.imread(img_path) 
  img = img_resizing(img)

  dataset.append(img)
  print(np.array(dataset).shape)
  Normalize_Dataset = np.array(dataset)/255.0
  return Normalize_Dataset

def ouput_processing(y_hat):
  y_hat = np.argmax(y_hat, axis=1)
  print("\n\nOutput")
  if y_hat[0] == 0:
    print(classes[0])
  elif y_hat[0] == 1:
    print(classes[1])
  elif y_hat[0] == 2:
    print(classes[2])
  else:
    print(classes[3])


img_path = "ECG_Updated-20220522T075145Z-001/ECG_Updated/"
dataset = []
classes = os.listdir(img_path)
print(classes)


print("\nModel loading ...\n\n")
ECG = keras.models.load_model('model/ECG_model_M1.h5')
img_path = "ECG_Updated-20220522T075145Z-001/ECG_Updated/COVID-19 Patients/Binder1_Page__0_15.jpg"
img = preprocessing(img_path)
y_hat = ECG.predict(img)
ouput_processing(y_hat)

