from abc import ABC, abstractmethod
from abstractions.observer import Observer


class Observable(ABC):
    @abstractmethod
    def subscribe(self, observer: Observer):
        """Attach an observer to observable instance"""
    
    
    @abstractmethod
    def unsubscribe(self, observer: Observer):
        """Detaches an observer from observable instance"""

        
    @abstractmethod
    def notify(self):
        """Notifies all observers about changes"""