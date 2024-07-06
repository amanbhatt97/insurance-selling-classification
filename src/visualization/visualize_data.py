import matplotlib.pyplot as plt
import seaborn as sns

from src.data.preprocess_data import EDA
eda = EDA()

class UnivariateAnalysis:
    def __init__(self):
        """
        Initialize the UnivariateAnalysis class.
        """
        pass

    def hist_plot(self, data, columns, bins=20):
        """
        Plots histograms for the specified columns in the dataframe.

        Parameters:
        data (DataFrame): The pandas DataFrame containing the data.
        columns (list): A list of column names to plot.
        bins (int): The number of bins for the histograms. Default is 20.
        """
        num_columns = len(columns)
        num_rows = (num_columns + 2) // 3  # Calculate the number of rows needed for subplots
        fig, axes = plt.subplots(num_rows, 3, figsize=(15, num_rows * 5))  # Adjusting figure size
        axes = axes.flatten()  # Flatten the axes array for easy iteration

        for i, column in enumerate(columns):
            ax = axes[i]
            data[column].hist(bins=bins, ax=ax)
            ax.set_title(column)
            ax.set_xlabel(column)
            ax.set_ylabel('Frequency')

        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])  # Remove any empty subplots

        plt.tight_layout()
        plt.show()

    def count_plot(self, data, columns):
        """
        Plots count plots for specified categorical columns in the dataframe.

        Parameters:
        data (DataFrame): The pandas DataFrame containing the data.
        columns (list): A list of column names to plot (categorical).
        """
        for column in columns:
            plt.figure(figsize=(10, 6))
            sns.countplot(data[column])
            plt.title(f'Count plot of {column}')
            plt.xlabel(column)
            plt.ylabel('Count')
            plt.show()
    

class AnalysisWithTarget:
    def __init__(self):
        pass

    def plot_numerical_relationships(self, data, numerical_features, target_feature):
        """
        Plot relationships between numerical features and the target variable.

        Parameters:
        data (DataFrame): The pandas DataFrame containing the data.
        numerical_features (list): A list of numerical column names to analyze.
        target_feature (str): The name of the target variable column.
        """
        for feature in numerical_features:
            plt.figure(figsize=(8, 6))
            sns.boxplot(x=data[target_feature], y=data[feature])
            plt.title(f'Relationship between {feature} and {target_feature}')
            plt.xlabel(target_feature)
            plt.ylabel(feature)
            plt.show()

    def plot_categorical_relationships(self, data, categorical_features, target_feature):
        """
        Plot relationships between categorical features and the target variable.

        Parameters:
        data (DataFrame): The pandas DataFrame containing the data.
        categorical_features (list): A list of categorical column names to analyze.
        target_feature (str): The name of the target variable column.
        """
        for feature in categorical_features:
            plt.figure(figsize=(10, 6))
            sns.countplot(x=data[feature], hue=data[target_feature])
            plt.title(f'Relationship between {feature} and {target_feature}')
            plt.xlabel(feature)
            plt.ylabel('Count')
            plt.legend(title=target_feature)
            plt.show()
            
            
class MultivariateAnalysis:
    def __init__(self):
        """
        Initialize the MultivariateAnalysis class with the provided DataFrame.

        Parameters:
        data (DataFrame): The pandas DataFrame containing the data.
        """
        pass
        
    def heatmap(self, data, annot=True):
        """
        Plots a heatmap to visualize the correlation matrix of numerical features.

        Parameters:
        annot (bool, optional): Whether to annotate each cell with the correlation value. Default is True.
        """
        plt.figure(figsize=(10, 8))
        numerical_features = eda.numerical_features(data)
        sns.heatmap(data[numerical_features].corr(), annot=annot, cmap='coolwarm', fmt='.2f', linewidths=.5)
        plt.title('Correlation Heatmap')
        plt.show()