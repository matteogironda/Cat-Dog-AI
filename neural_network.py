import numpy as np
import load_data
from PIL import Image

x_train, y_train, x_test, y_test, dataset = load_data.data_load()

print(x_train.shape)
print(x_train.shape[0])

def show_image(pic):
    new_im = Image.fromarray(pic)
    new_im.save("numpy_altered_sample2.png")

def sigmoid(z):
    s = 1/(1+np.exp(z))
    return s

def init_as_zeros(dim):
    w = np.zeros((dim,1))
    b = 0

def propagate(w, b, X, Y):
    # number of examples
    m = X[1].shape
    print(Y.shape)
    # forward propagation
    A = sigmoid(np.dot(w.T,X)+b)
    print(A.shape)
    cost = -1/m*(np.sum((Y*np.log(A)+(1-Y)*np.log(1-A))))

    # backwards propagation
    dw = 1/m*np.dot(X,(A - Y).T)
    db = 1/m*np.sum(A - Y)

    #set gradiants as a dictionary
    grads = {'dw':dw,
             'db':db}

    return grads, cost

def optimize(w, b, X, Y, num_iterations = 100, learning_rate = 0.5):
    for i in range(num_iterations):
        grads, cost = propagate(w, b, X, Y)
        w = w - learning_rate*grads['dw']
        b = b - learning_rate*grads['db']

        params = {'w':w,
                  'b':b}

        grads = {'dw':dw,
                 'db':db}
                
    return params, grads

# predict the output of an image
def predict(w, b, X):
    # initialize size of prediction vector
    m = X[1].shape
    Y_prediction = np.zeros((1,m))
    w = w.reshape(X.shape[0], 1)
    # activation vector
    A = sigmoid(np.dot(w.T,X)+b)
    
    for i in range(A[1].shape):
        if A[0,i] > 0.5:
            Y_prediction = 1
        else:
            Y_prediction = 0
    return Y_prediction

def model(x_train, y_train, x_test, y_test, num_iterations = 100, learning_rate = 0.5):
    #w, b = init_as_zeros(3072)#x_train.shape[0])
    w = np.zeros((3072,1))
    b = 0
    parameters, grads, costs = optimize(w, b, x_test, y_test, num_iterations, learning_rate)
    
    w = parameters['w']
    b = parameters['b']
    
    Y_prediction_test = predict(w, b, x_test)
    Y_prediction_train =  predict(w, b, x_train)

model(x_train, y_train, x_test, y_test)