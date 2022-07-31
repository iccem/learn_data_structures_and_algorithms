from abc import ABC, abstractmethod

class Rectangle:
    default_color = 'green'
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    '''
    магические методы
    начинаются с двух символов '_'
    __init = конструктор
    __del = не совсем деструктор, но закрытие объекта
    '''
    
    '''
    статические методы @staticmethod
    def staticmethod():
        return 'static method called'
    
    экземплярные методы
    def instancemethod(self):
    return 'instance method called', self
    
    
    классовые методы @classmethod
    def classmethod(cls):
        return 'class method called', cls
    '''
    
    
class ChessPiece(ABC):
    def draw(self):
        print('Drew a chess piece')
        
    @abstractmethod
    def passmove(self):
        pass