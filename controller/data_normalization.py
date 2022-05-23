from controller.libraries import * 

def normalization(Dataset, outcomes):
    #normalize the Dataset 
    Dataset = np.array(Dataset)
    outcomes = np.array(outcomes)
    # print("Shape of Dataset:",Dataset.shape,outcomes.shape)
    Normalize_Dataset = Dataset/255.0
    return Normalize_Dataset, outcomes