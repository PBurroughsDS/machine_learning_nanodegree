## Training the learning algorithmfrom sklearn.metrics import fbeta_score
from sklearn.metrics import fbeta_score
from sklearn.metrics import accuracy_score
import time

def train_predict(learner, sample_size, X_train, y_train, X_test, y_test): 
    '''
    inputs:
       - learner: the learning algorithm to be trained and predicted on
       - sample_size: the size of samples (number) to be drawn from training set
       - X_train: features training set
       - y_train: income training set
       - X_test: features testing set
       - y_test: income testing set
    '''
    
    results = {}
    
    # Fit the learner to the training data using slicing with 'sample_size' using .fit(training_features[:], training_labels[:])
    start = time.time() # Get start time
    learner = learner.fit(X_train[:sample_size] , y_train[:sample_size])
    end = time.time() # Get end time
    
    # Calculate the training time
    results['train_time'] = end - start 

    # Get the predictions on the test set(X_test),
    # then get predictions on the first 300 training samples(X_train) using .predict()
    start = time.time() # Get start time
    predictions_test = learner.predict(X_test[:])
    predictions_train = learner.predict(X_train[:300])
    end = time.time() # Get end time
    
    # Calculate the total prediction time
    results['pred_time'] = end - start 
            
    # Compute accuracy on the first 300 training samples which is y_train[:300]
    results['acc_train'] = accuracy_score(y_train[:300] , predictions_train)
        
    #  Compute accuracy on test set using accuracy_score()
    results['acc_test'] = accuracy_score(y_test , predictions_test)
    
    # Compute F-score on the the first 300 training samples using fbeta_score()
    
    # The F-score was noted earlier as 0.5  >> Lower this to 0.4
    
    results['f_train'] = fbeta_score(y_train[:300] , predictions_train , beta = 0.4 )
        
    # Compute F-score on the test set which is y_test
    results['f_test'] = fbeta_score(y_test , predictions_test , beta = 0.4)
       
    # Success
    print("{} trained on {} samples.".format(learner.__class__.__name__, sample_size))
        
    # Return the results
    return results