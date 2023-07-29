from xgboost import XGBClassifier


class XGBoost:

    def __init__(self):
        self.__model = XGBClassifier()

    def fit(self, X_train, y_train):
        self.__model.fit(X_train, y_train - 1)
        # n.b: XGBoost necessita che le classi siano [0 1 2 3], quindi temporaneamente riduco di 1 ciascun valore di y_train

    def predict(self, X_test):
        y_prediction = self.__model.predict(X_test)

        return y_prediction + 1  # raggiungo UNO al risultato di tutte le predizioni
