from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.linear_model import SGDClassifier, RidgeClassifier
from sklearn.ensemble import AdaBoostClassifier, ExtraTreesClassifier, BaggingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

from src.data.preprocess_data import (
    DataCleaning
)

class BaseModelTrainer:
    def __init__(self):
        self.X_train = None
        self.X_val = None
        self.y_train = None
        self.y_val = None
        self.models = {}

    def split_data(self, data, target, test_size=0.2, random_state=42):
        X = data.drop(columns=[target])
        y = data[target]
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(X, y, test_size=test_size, random_state=random_state)
        return self.X_train, self.X_val, self.y_train, self.y_val 
        
    def train_models(self):
        """
        Train all classifiers on the training data.
        """
        self.models['RandomForest'] = RandomForestClassifier()
        self.models['RandomForest'].fit(self.X_train, self.y_train)

        self.models['GradientBoosting'] = GradientBoostingClassifier()
        self.models['GradientBoosting'].fit(self.X_train, self.y_train)

        # self.models['SVM'] = SVC()
        # self.models['SVM'].fit(self.X_train, self.y_train)

        # self.models['LogisticRegression'] = LogisticRegression()
        # self.models['LogisticRegression'].fit(self.X_train, self.y_train)

        # self.models['KNN'] = KNeighborsClassifier()
        # self.models['KNN'].fit(self.X_train, self.y_train)

        # self.models['DecisionTree'] = DecisionTreeClassifier()
        # self.models['DecisionTree'].fit(self.X_train, self.y_train)

        # # Add more classifiers
        # self.models['GaussianNB'] = GaussianNB()
        # self.models['GaussianNB'].fit(self.X_train, self.y_train)

        # self.models['MultinomialNB'] = MultinomialNB()
        # self.models['MultinomialNB'].fit(self.X_train, self.y_train)

        # self.models['SGDClassifier'] = SGDClassifier()
        # self.models['SGDClassifier'].fit(self.X_train, self.y_train)

        # self.models['RidgeClassifier'] = RidgeClassifier()
        # self.models['RidgeClassifier'].fit(self.X_train, self.y_train)

        # self.models['AdaBoost'] = AdaBoostClassifier()
        # self.models['AdaBoost'].fit(self.X_train, self.y_train)

        # self.models['ExtraTrees'] = ExtraTreesClassifier()
        # self.models['ExtraTrees'].fit(self.X_train, self.y_train)

        # self.models['Bagging'] = BaggingClassifier()
        # self.models['Bagging'].fit(self.X_train, self.y_train)

        # self.models['MLPClassifier'] = MLPClassifier()
        # self.models['MLPClassifier'].fit(self.X_train, self.y_train)

        # self.models['LinearSVC'] = LinearSVC()
        # self.models['LinearSVC'].fit(self.X_train, self.y_train)

        # self.models['RadiusNeighbors'] = RadiusNeighborsClassifier()
        # self.models['RadiusNeighbors'].fit(self.X_train, self.y_train)

        # self.models['QDA'] = QuadraticDiscriminantAnalysis()
        # self.models['QDA'].fit(self.X_train, self.y_train)

    def get_models(self):
        """
        Get trained models.

        Returns:
        - models: dict
            Dictionary containing trained model instances.
        """
        return self.models