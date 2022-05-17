from abc import ABC, abstractmethod


class IObservable(ABC):

    @staticmethod
    @abstractmethod
    def subscribe(observer): ...

    @staticmethod
    @abstractmethod
    def unsubscribe(observer): ...

    @staticmethod
    @abstractmethod
    def notify(observer): ...


class Subject(IObservable):

    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, *args):
        for observer in self._observers:
            observer.notify(*args)