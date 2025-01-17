import os
import sys

# Use a raw string (r'') or escape backslashes (\\)
src_path = r'C:\ML Project Pw\DIAMOND PRICE PREDICTION\src'
sys.path.append(src_path)

from logger import logging
from exception import CustomException
from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransformation
from components.model_trainer import ModelTrainer

if __name__ == '__main__':
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    print(train_data_path, test_data_path)
    data_transformation=DataTransformation() 

    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    model_trainer=ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)

