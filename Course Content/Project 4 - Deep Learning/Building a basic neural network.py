Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
	import numpy as np
    from keras.models import Sequential
    from keras.layers.core import Dense, Activation

    # X has shape (num_rows, num_cols), where the training data are stored
    # as row vectors
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)

    # y must have an output vector for each input vector
    y = np.array([[0], [0], [0], [1]], dtype=np.float32)

    # Create the Sequential model
    model = Sequential()

    # 1st Layer - Add an input layer of 32 nodes with the same input shape as
    # the training samples in X
    model.add(Dense(32, input_dim=X.shape[1]))

    # Add a softmax activation layer
    model.add(Activation('softmax'))

    # 2nd Layer - Add a fully connected output layer
    model.add(Dense(1))

    # Add a sigmoid activation layer
    model.add(Activation('sigmoid'))

    # Need to compile the model with loss function , optimiser and
    # How to judge the model
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics = ["accuracy"])

    # View the models architecture
    model.summary()

    # Fit the model
    model.fit(X, y, nb_epoch=1000, verbose=0)

    # Evaluate the model
    model.evaluate()



    
