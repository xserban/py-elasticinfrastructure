from abc import abstractmethod


class BaseMetric:
    def __init__(self):
        pass

    @abstractmethod
    def measure(self):
        raise NotImplementedError
