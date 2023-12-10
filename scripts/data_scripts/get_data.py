import kaggle
import os

os.environ['KAGGLE_USERNAME'] = "dtrubki22"
os.environ['KAGGLE_KEY'] = "99980df7d0447b859d3cfdde8856ba4c"

kaggle.api.authenticate()

kaggle.api.dataset_download_files('spaceship-titanic', path='data/raw', unzip=True)