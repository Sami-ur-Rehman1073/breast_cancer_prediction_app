import os

# MySQL Configuration

MYSQL_USERNAME = "root"
MYSQL_PASSWORD = "sami1073"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DATABASE = "breast_cancer_db"

# SQLAlchemy Database URL

DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
)

# Trained Model Path

MODEL_PATH = os.path.join(
    "trained-model",
    "logistic_regression.pkl"
)