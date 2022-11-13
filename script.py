#Importing libaries
from Libaries import *
sc = StandardScaler()

def create_dataset():
    dataset = open("Dataset.csv", "w", newline="")
    for i in range(2000):    
        x = np.random.randint(11, size=1)
        if( x != 10):
            noise_probability = np.random.randint(5, size=1)
            if(noise_probability == 4):
                noise = round(random.uniform(0, 0.5), 2)
                temp_arr = numbers[int(x)].copy()
                for i in range(len(temp_arr)):
                    if(temp_arr[i] == 1):
                        temp_arr[i] = 1 - noise
                line = line = (temp_arr, numbers_result[int(x)], int(x))
            else:
                line = (numbers[int(x)], numbers_result[int(x)], int(x))
        else:
            matrix = np.random.randint(2, size=28)
            for data in range(len(numbers)):
                comparison = matrix == numbers[data]
                if (comparison.all()):
                    line = (numbers[int(data)], numbers_result[int(data)], int(data))
                else:
                    line = (list(matrix), numbers_result[10], 10)
                            
        writer = csv.writer(dataset)
        writer.writerow(line)
    dataset.close()
    initialization()
    
def initialization():
    dataset = pd.read_csv("Dataset.csv")
    
    X = list(dataset.iloc[:, 0].values)
    y = (dataset.iloc[:, 1].values)
        
    X_result = []
    y_result = []
    
    for i in range(len(X)):
        str_out = list(map(float, X[i][1:len(X[i])-1].split(', ')))
        X_result.append(str_out)
        
    for i in range(len(y)):
        str_out = list(map(int, y[i][1:len(y[i])-1].split(', ')))
        y_result.append(str_out)
  
    X = np.array(sc.fit_transform(X_result))
    
    #Splitting dataset into the Training set and Test set
    X_train, X_test, y_train, y_test = train_test_split(X, np.array(y_result), test_size = 0.22, random_state = 0)
    
    #Initializing Artificial Neural Network ( ANN )
    ann = tf.keras.models.Sequential()
    
    add_layers(ann, X_train, X_test, y_train, y_test) 
    

    
def add_layers(ann, X_train, X_test, y_train, y_test):
    
    #Input layer and first hidden layer
    ann.add(tf.keras.layers.Dense(units = 16, activation = "sigmoid", input_dim = 28))
    
    #Other hidden layers
    ann.add(tf.keras.layers.Dense(units = 36, activation = "relu"))
    ann.add(tf.keras.layers.Dense(units = 28, activation = "relu"))
    ann.add(tf.keras.layers.Dense(units = 18, activation = "relu"))
    
    #Output layer
    ann.add(tf.keras.layers.Dense(units = 10, activation = "softmax"))
    
    fit(ann, X_train, X_test, y_train, y_test)
    
    
def fit(ann, X_train, X_test, y_train, y_test):
    
    #Compiling the ANN
    ann.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ['accuracy'])
    
    #Fitting the ANN to the Training set
    ann_fit = ann.fit(X_train, y_train, validation_data = (X_test, y_test), batch_size = 32, epochs = 200)
    
    create_graphs(ann_fit, ann)
    
def create_graphs(ann_fit, ann):
    
        #Accurancy graph
        plt.plot(ann_fit.history['accuracy'])
        plt.plot(ann_fit.history['val_accuracy'])
        plt.title("Model accurancy")
        plt.xlabel("Epoch")
        plt.ylabel("Accurancy")
        plt.legend(["Train", "Test"], loc = "upper left")
        plt.show()
        
        #Loss graph
        plt.plot(ann_fit.history['loss'])
        plt.plot(ann_fit.history['val_loss'])
        plt.title("Model loss")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.legend(["Train", "Test"], loc = "upper left")
        plt.show()
        
        prediction(ann)
        
def prediction(ann):
    
    print("-------------------- Wihout noise --------------------")
    
    for i in range(10):
        test = ann.predict(sc.transform([numbers[i]]))
        print(str(i) + ": " + str(max(max(test))) + " for number: " + str((np.argmax(max(test), axis=0) + 1) % 10))
        
    print("------------------ With noise : " + str(round(1 - noised_data, 2)) + " ------------------")
        
    for i in range(10):
        test = ann.predict(sc.transform([noised_numbers[i]]))
        print(str(i) + ": " + str(max(max(test))) + " for number: " + str((np.argmax(max(test), axis=0) + 1) % 10))
        
    


def __main__():
    create_dataset()
    
    
__main__()