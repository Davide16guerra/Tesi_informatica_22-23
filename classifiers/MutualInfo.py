from sklearn import feature_selection


class MutualInfo:

    def __init__(self, flattenLabel):
        self.flattenLabel = flattenLabel

    def compute(self, band):
        return feature_selection.mutual_info_classif(band, self.flattenLabel, random_state=42)

