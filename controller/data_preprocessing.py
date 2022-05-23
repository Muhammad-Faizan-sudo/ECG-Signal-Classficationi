from controller.libraries import *

def img_cropping(img,class_name):
  if class_name == 2:
    crop = img
  else:
    y,h,x,w = 300,1000,50,2100 
    crop = img[y:y+h, x:x+w]  
  return crop


def img_resizing(crop):
  dims = (500,500)
  resized = cv2.resize(crop, dims, interpolation = cv2.INTER_AREA)
  gray_scale = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
  # plt.figure()  
  # plt.imshow(gray_scale)
  # plt.show()
  resized_img = gray_scale.reshape(500,500,1)
  return resized_img


def load_images_from_folder(dataDir,images_dataset,output,categories):
  
  for folder in categories:  
    class_num = categories.index(folder)
    path = os.path.join(dataDir,folder)

    for filename in os.listdir(path):
      img = cv2.imread(os.path.join(path,filename)) 
      cropped_img = img_cropping(img, class_num)
      resized_img = img_resizing(cropped_img)

      try:
        images_dataset.append(resized_img)
        output.append(class_num)
      except Exception as e:        
        pass        

  return images_dataset,output




