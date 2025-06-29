import os
from kidney_disease_classification import logger
from kidney_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from kidney_disease_classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from kidney_disease_classification.pipeline.stage_03_model_training import ModelTrainingPipeline
from kidney_disease_classification.pipeline.stage_04_model_evaluation import EvaluationPipeline



STAGE_NAME = "Data Ingestion"
try:
   logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e





STAGE_NAME = "Prepare base model"
if __name__ == "__main__":
    os.makedirs("artifacts/prepare_base_model", exist_ok=True)  # ✅ Add this if nothing else works


try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Training"

try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
      

STAGE_NAME = "Model Evaluation"


try:
   logger.info(f"*******************")
   logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e 