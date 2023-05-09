from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization
import keras

class DNN_Text:
    def __init__(self, shape, nClasses, model_number, dropout=0.5):
        """
        DNN_Text(shape, nClasses, model_number, dropout)
        Initialize a deep neural network model for text classification.
        Parameters:
            shape: int, the size of the input feature space
            nClasses: int, the number of classes for classification
            model_number: int, the model number to use for determining the number of nodes and hidden layers
            dropout: float, the dropout rate to use for regularization (default=0.5)
        """
        self.shape = shape
        self.nClasses = nClasses
        self.model_number = model_number
        self.dropout = dropout
    
    def Build_Model_DNN_Text(self):
        """
        Build a deep neural network model for text classification.
        Returns:
            model: a compiled Keras model object
        """
        # define the number of nodes for each hidden layer
        nodes = [128, 192, 256]
        
        # define the number of hidden layers
        layers = [1, 2, 3]
        
        # create a Sequential model object
        model = Sequential()
        
        # determine the number of nodes and hidden layers based on the specified model number
        node = nodes[int(self.model_number % 3)]
        nLayers = layers[int(self.model_number / 3)]
        
        # add the first hidden layer to the model, with the specified number of nodes and input shape
        model.add(Dense(node, input_dim=self.shape, activation='relu'))
        model.add(Dropout(self.dropout))
        
        # add additional hidden layers, if specified
        for i in range(0, nLayers):
            model.add(Dense(node, input_dim=node, activation='relu'))
            model.add(BatchNormalization())
            model.add(Dropout(self.dropout))
        
        # add output layer with softmax activation for multi-class classification
        model.add(Dense(self.nClasses, activation='softmax'))
        
        # compile the model with categorical crossentropy loss and Adam optimizer with specified learning rate
        model.compile(loss='sparse_categorical_crossentropy', 
                      optimizer=keras.optimizers.Adam(learning_rate=0.00001), 
                      metrics=['accuracy'])
        
        # return the compiled model
        return model
