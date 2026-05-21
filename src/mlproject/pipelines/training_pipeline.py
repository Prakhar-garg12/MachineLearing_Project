# src/mlproject/pipelines/training_pipeline.py

import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging

from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_trainer import ModelTrainer


class TrainPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        try:
            # Step 1: Data Ingestion
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion()
            train_path, test_path = data_ingestion.initiate_data_ingestion()

            # Step 2: Data Transformation
            logging.info("Starting data transformation")
            data_transformation = DataTransformation()
            train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
                train_path, test_path
            )

            # Step 3: Model Training
            logging.info("Starting model training")
            model_trainer = ModelTrainer()
            r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)

            logging.info(f"Training complete. R2 Score: {r2_score}")
            print(f"Model trained successfully! R2 Score: {r2_score}")

            return r2_score

        except Exception as e:
            raise CustomException(e, sys)


# Direct run karne ke liye
if __name__ == "__main__":
    pipeline = TrainPipeline()
    pipeline.run_pipeline()