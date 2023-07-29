from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

class ClassifierValidator:

    def __init__(self):
        pass

    def validation(self, y_test, y_predictions):
        return classification_report(y_test.flatten(), y_predictions.flatten(), output_dict=True)

    def confusion_matrix(self, y_test, y_predictions):
        return confusion_matrix(y_test.flatten(), y_predictions.flatten())