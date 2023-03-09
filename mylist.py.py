class MyList:
    def __init__(self):
        self.elements = []
        
    def append(self, n):
        self.elements.append(n)
        
    def pop(self):
        self.elements.pop()
        
    def max(self):
        return max(self.elements)
        
    def min(self):
        return min(self.elements)
        
    def __str__(self):
        return str(self.elements)
        
    def __add__(self, other):
        result = MyList()
        for i in range(max(len(self.elements), len(other.elements))):
            if i < len(self.elements) and i < len(other.elements):
                result.append(self.elements[i] + other.elements[i])
            elif i < len(self.elements):
                result.append(self.elements[i])
            elif i < len(other.elements):
                result.append(other.elements[i])
        return result
        
    def __sub__(self, other):
        result = MyList()
        for i in range(max(len(self.elements), len(other.elements))):
            if i < len(self.elements) and i < len(other.elements):
                result.append(self.elements[i] - other.elements[i])
            elif i < len(self.elements):
                result.append(self.elements[i])
            elif i < len(other.elements):
                result.append(-other.elements[i])
        return result
        
    def __len__(self):
        return len(self.elements)
        
    def __lt__(self, other):
        return len(self.elements) < len(other.elements)
        
    def __le__(self, other):
        return len(self.elements) <= len(other.elements)
        
    def __gt__(self, other):
        return len(self.elements) > len(other.elements)
        
    def __ge__(self, other):
        return len(self.elements) >= len(other.elements)