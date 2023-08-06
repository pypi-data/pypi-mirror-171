import numpy as np
from gwu_nn.loss_functions import MSE, LogLoss, CrossEntropy

loss_functions = {'mse': MSE, 'log_loss': LogLoss, 'cross_entropy': CrossEntropy}

class GWUNetwork():
    """The GWUNetwork class is the core class of the library that provies a
    foundation to build a network by iteratively adding layers"""

    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_prime = None

    def add(self, layer):
        """A network is comprised of a series of layers connected together. The
        add method provides a means to add a layer to a network
        
        Args:
            Layer (Layer): A Layer object to add to the network
        """
        if len(self.layers) > 0:
            layer.init_weights(self.layers[-1].output_size)
        else:
            layer.init_weights(layer.input_size)
        self.layers.append(layer)

    def get_weights(self):
        """Get the weights for the model
        
        Returns:
            np.array: weights of the model
        """
        weights = []
        for layer in self.layers:
            weights.append(layer.weights)
        return np.array(weights)

    def compile(self, loss, lr):
        """Compile sets a model's loss function and learning rate, preparing the
        model for training
        
        Args:
            loss (LossFunction): The loss function used for the network
            lr (float): The learning rate for the network"""
        if isinstance(loss, str):
            layer_loss = loss_functions[loss]
        else:
            layer_loss = loss
        self.loss = layer_loss.loss
        self.loss_prime = layer_loss.loss_partial_derivative
        self.learning_rate = lr

    # predict output for given input
    def predict(self, input_data):
        """Predict produces predictions for the provided input data
        
        Args:
            input_data (np.array): Input data to inference
        
        Returns:
            np.array: the predictions for the given model
        """
        
        # Run through the layers
        output = input_data
        for layer in self.layers:
            output = layer.forward_propagation(output)

        return output

    def evaluate(self, x, y):
        preds = self.predict(x)
        loss = self.loss(y, preds)
        return loss

    # train the network
    def fit(self, x_train, y_train, epochs, batch_size=None):
        """Fit is the trianing loop for the model/network
        
        Args:
            x_train (np.array): Inputs for the network to train on
            y_train (np.array): Expected outputs for the network
            epochs (int): Number of training cycles to run through
            batch_size (int): Number of records to train on at a time"""
        # sample dimension first
        samples = len(x_train)

        # training loop
        for i in range(epochs):
            err = 0
            batch_count = 0
            for j in range(0, len(x_train), batch_size):
                # forward propagation
                output = x_train[j:j+batch_size]
                for layer in self.layers:
                    output = layer.forward_propagation(output)

                # compute loss (for display purpose only)
                y_true = y_train[j:j+batch_size]
                err += self.loss(y_true, output)
                batch_count += 1

                # backward propagation
                error = self.loss_prime(y_true, output)
                for layer in reversed(self.layers):
                    error = layer.backward_propagation(error, self.learning_rate)

            # calculate average error on all samples
            if i % 10 == 0 and i != 0:
                err /= batch_count
                print(f'epoch {i}/{epochs}   error={err}')
                
    def __repr__(self):
        rep = "Model:"

        if len(self.layers) < 1:
            return "Model: Empty"
        else:
            rep += "\n"

        for layer in self.layers:
            if layer.type == "Activation":
                rep += f'{layer.name} Activation'
            else:
                rep += f'{layer.name} - ({layer.input_size}, {layer.output_size})\n'

        return rep
