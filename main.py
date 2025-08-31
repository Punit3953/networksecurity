from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionCofig
from networksecurity.entity.config_entity import TrainingPipelingConfig
import sys

if __name__ =="__main__":
    try:
        trainingpiplineconfig=TrainingPipelingConfig()
        dataingestionconfig=DataIngestionCofig(trainingpiplineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("initiate the data ingestion")
        dataingestionartrifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartrifact)
    
    except Exception as e :
        raise NetworkSecurityException(e,sys)

