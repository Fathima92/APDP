# Strategy Pettern : Data ingection
import json
from abc import ABC, abstractmethod


# interface

class DataIngestionStrategy(ABC):
    @abstractmethod

    def ingest_data(self, file_path):
        pass

# concrete class

class JSONDataIngestion(DataIngestionStrategy):
    def ingest_data(self, file_path):
        with open(file_path, 'r') as file:
            data = json.loads(file)
        return data

#Context

class DataIngestionContext:
    def __init__(self):
        pass

    def set_strategy(self, strategy):
        self.strategy = strategy

    def ingest_data(self, file_path):
        return self.strategy.ingest_data(file_path)



