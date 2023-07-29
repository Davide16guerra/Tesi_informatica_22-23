from sklearn.ensemble import RandomForestClassifier


class RandomForest:

    def __init__(self):
        self.__model = RandomForestClassifier()

    def fit(self, X_train, y_train):
                self.__model.fit(X_train, y_train)

    def predict(self, X_test):
        y_predictions = self.__model.predict(X_test)

        return y_predictions
