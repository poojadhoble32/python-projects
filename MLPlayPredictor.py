import numpy as np
import pandas as pd
from sklearn import preprocessing                # use for func labelencoder= le obj in our code
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):

    #step 1 : load data
    data = pd.read_csv(data_path, index_col = 0)
    
    print("size of actual dataset", len(data))
    
    #step 2 : clean, prepare and manipulate data
    feature_names = ['whether', 'Temperature']
    
    print("names of features ", feature_names)
    
    whether = data.Whether
    Temperature = data.Temperature
    play = data.Play
    
    #creating labelEncoder
    le = preprocessing.LabelEncoder()
    
    #converting string labels into numbers
    weather_encoded = le.fit_transform(whether)    # encoding
    print(weather_encoded)
    
    #converting string labels into numbers
    temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(play)
    
    print(temp_encoded)
    
    #combining weather and temp into single listof tuples
    features = list(zip(weather_encoded,temp_encoded))
    
    #step 3: Train data
    model = KNeighborsClassifier(n_neighbors=3)            # 
    
    #Train the model using the training sets
    model.fit(features,label)
    
    #step 4 : Test data
    predicted = model.predict([[0,2]])  #0 : overcast, 2:Mild, 
    print(predicted)
    
def main():
    print("---Marvellous Infosystem---")
    
    print("Machine learning Application")
    
    print("Play predictor application using K Nearest Knighbor algorithm")
    
    MarvellousPlayPredictor("PlayPredictor.csv")
    
if __name__ == "__main__":
    main()
    