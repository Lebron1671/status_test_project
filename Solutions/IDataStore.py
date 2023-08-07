from abc import abstractmethod, ABC


class IDataStore(ABC):
    @abstractmethod
    def __init__(self, data):
        self.data = None

    @abstractmethod
    def getAll(self) -> list:
        pass

    @abstractmethod
    def getItem(self, id: int) -> list:
        pass

    @abstractmethod
    def getChildren(self, id: int) -> list:
        pass

    @abstractmethod
    def getAllParents(self, id: int) -> list:
        pass
