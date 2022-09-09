from dataclasses import dataclass

@dataclass
class vector:
    
    x: float()
    y: float()
    z: float()
    
    def __add__(self, other):
        """
        Perform vector sum between two three dimensional vectors (c = a + b).
        

        Parameters
        ----------
        other : vector
            The second term in the sum

        Returns
        -------
        vector
            The result of the sum between two vector

        """
        return vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):
        if (isinstance(other, vector)):
            return (self.x * other.x + self.y * other.y + self.z * other.z)
        if (isinstance(other, float) or isinstance(other, int)):
            return vector(other * self.x, other * self.y, other * self.z)
    
    def __neg__(self):
        return self * -1
        
    def __sub__(self, other):
        return self + -other
        

def translate(pos, delta):
    return pos + delta