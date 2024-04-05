#### magic method
class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self): ## magic method __str__
        return (f"Flower name: {self.name}, Flower color: {self.color}")

    def __ne__(self, other):  ## mm __not equal__
         return self.name != other.name and self.color != other.color


flower1 = Flower("Rose", "white")
flower2 = Flower("baily", "white")
print(flower1 != flower2)
