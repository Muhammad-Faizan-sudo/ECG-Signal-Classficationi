from controller.libraries import * 

def run():
    dataset_path = "ECG_Updated-20220522T075145Z-001/ECG_Updated/"
    classes = os.listdir(dataset_path)
    print(classes)
    images_dataset,output,dataDir = [],[],dataset_path
    Dataset,outcomes = load_images_from_folder(dataDir,images_dataset,output,classes)
    print("Dataset shape: ", np.array(Dataset).shape)


    Normalize_Dataset, outcomes = normalization(Dataset, outcomes)        
    X_train, X_test, y_train, y_test = train_test_split(Normalize_Dataset, outcomes, test_size = 0.2, random_state = 42)

    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
    # print("Shape of the training and testing dataset", X_train.shape,X_test.shape, y_train.shape, y_test.shape)
    optimizer, loss_fun, classes, epochs, batch_size = 'adam', 'sparse_categorical_crossentropy', len(classes), 24, 32


    ECG = model(optimizer, loss_fun, classes, X_train, y_train, epochs, batch_size)
    ECG.evaluate(X_test, y_test)
    ECG.save('model/ECG_model_2.h5')

    


