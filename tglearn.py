import numpy as np

class KNeighborsRegressor:
    def __init__(self, n_neighbors=5):  # default neighbor
        self.n_neighbors = n_neighbors

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for x_test in X_test:  # loop just one time in this example
            # d(P, Q) = sqrt((x2 - x1)^2 + (y2 - y1)^2)
            distances = np.sqrt(np.sum((x_test - self.X_train)**2, axis=1))
            # print(distances)
            indices = np.argsort(distances)[:self.n_neighbors]
            # print(indices)
            prediction = np.mean(self.y_train[indices])
            # prediction = (self.y_train[indices[0]]+self.y_train[indices[1]]+self.y_train[indices[2]]) / self.n_neighbors
            predictions.append(prediction)

            return np.array(prediction).reshape(-1, 1)


class LinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None


    def fit(self, X, y):
        """
        Learning function
        :param X: Independent variable (2d array format)
        :param y: dependent variable (2d array format)
        :return: void
        """
        X_mean = np.mean(X)
        y_mean = np.mean(y)

        denominator = np.sum(pow((X-X_mean), 2))
        numerator = np.sum((X-X_mean)*(y-y_mean))

        self.slope = numerator / denominator
        self.intercept = y_mean - (self.slope * X_mean)


    def predict(self, X) -> list:
        """
        predict value for input
        :param X: new independent variable
        :return: predict value for input (2d array format)
        """
        return self.slope * np.array(X) + self.intercept