from abc import ABC, abstractmethod

class DatabaseAdapter(ABC):

    @abstractmethod
    def list_tables(self):
        pass

    @abstractmethod
    def get_schema(self, table):
        pass

    @abstractmethod
    def get_row_count(self, table):
        pass

    @abstractmethod
    def get_column_stats(self, table, column, sample_ratio):
        pass

    def get_null_count(self, table, column):
        return None

    def get_histogram(self, table, column, bins):
        return None
