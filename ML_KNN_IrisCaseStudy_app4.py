from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def MarvellousKNeighborsClassifier():
    Dataset = load_iris()       # 1 Load the data

    Data = Dataset.data          # data taken
    Target = Dataset.target      # label or target taken

    Data_train, Data_test, Target_train, Target_test = train_test_split(Data, Target, test_size = 0.5)      # test size means data splited 50% and also it will shufle before split.data splited 50 50 in train and test data

    Classifier = KNeighborsClassifier()

    Classifier.fit(Data_train, Target_train)

    Predictions = Classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test, Predictions)

    return Accuracy

def main():
    Ret = MarvellousKNeighborsClassifier()

    print("Acuracy of Iris dataset with KNN is ",Ret * 100)       #* 100 use for proper accuracy by 100

if __name__ == "__main__":
    main()