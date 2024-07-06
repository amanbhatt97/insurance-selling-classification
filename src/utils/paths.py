import os

class ProjectPaths:
    def __init__(self, PROJECT_PATH):
        """
        Initialize the ProjectPaths class and load environment variables from the specified file.

        Parameters:
        env_file (str): Path to the .env file. Default is '.env'.
        """
        self.BASE_PATH = PROJECT_PATH
        print(f'Project Path: {self.BASE_PATH}')
        self.RAW_DATA_PATH = os.path.join(self.BASE_PATH, "data", "raw_data")
        self.PROCESSED_DATA_PATH = os.path.join(self.BASE_PATH, "data", "processed_data")
        self.NOTEBOOKS_PATH = os.path.join(self.BASE_PATH, "notebooks")
        self.DEPLOY_PATH = os.path.join(self.BASE_PATH, "deploy")
        self.SRC_PATH = os.path.join(self.BASE_PATH, "src")
        self.CONFIG_PATH = os.path.join(self.BASE_PATH, "config")
        self.MODELS_PATH = os.path.join(self.BASE_PATH, "models")
        self.LOGS_PATH = os.path.join(self.BASE_PATH, "logs")
        self.DOCS_PATH = os.path.join(self.BASE_PATH, "docs")
        