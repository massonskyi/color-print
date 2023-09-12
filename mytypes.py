class uint8:

    def __init__(self, value) -> None:
        if not isinstance(value, int):
            raise ValueError("Value must be int or np.int8")
        self._value = value & 0xFF

    @property
    def ref(self):
        return self._value
    
    @ref.setter
    def ref(self, value):
        if not isinstance(value, int):
            raise ValueError("Value must be int or np.int8")
        self._value = value & 0xFF
    
    @property       
    def real(self):
        return uint8(self.ref)
    
    @property
    def imag(self):
        return uint8(0)
    
    @property
    def numerator(self):
        return uint8(self.ref)
    
    @property
    def denominator(self):
        return uint8(1)
    
    @property
    def to_int(self):
        return uint8(self.ref)

    @property
    def to_hex(self):
        return hex(self.ref)

    @property
    def to_binary(self):
        return bin(self.ref)[2:].zfill(8)

    def conjugate(self):
        return uint8(self.ref)
    
    def bit_length(self):
        return uint8(self.ref.bit_length())

    def __call__(self):
        return self.ref

    def __add__(self, other):
        if isinstance(other, uint8):
            return uint8(self.ref + other.ref)
        elif isinstance(other, int):
            return uint8(self.ref + other)
        elif isinstance(other, float):
            return uint8(self.ref + uint8(other))
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, uint8):
            return uint8(self.ref - other.ref)
        elif isinstance(other, int):
            return uint8(self.ref - other)
        elif isinstance(other, float):
            return uint8(self.ref - uint8(other))
        else:
            return NotImplemented
            
    def __mul__(self, other):
        if isinstance(other, uint8):
            return uint8(self.ref * other.ref)
        elif isinstance(other, int):
            return uint8(self.ref * other)
        elif isinstance(other, float):
            return uint8(self.ref * uint8(other).ref)
        else:
            return NotImplemented

    def __div__(self, other):
        if isinstance(other, uint8):
            return uint8(self.ref / other.ref)
        elif isinstance(other, int):
            return uint8(self.ref / other)
        elif isinstance(other, float):
            return uint8(self.ref / uint8(other).ref)
        else:
            return NotImplemented

    def __mod__(self, other):
        if isinstance(other, uint8):
            return uint8(self.ref % other.ref)
        elif isinstance(other, int):
            return uint8(self.ref % other)
        elif isinstance(other, float):
            return uint8(self.ref % uint8(other).ref)
        else:
            return NotImplemented
            
    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return f"{self.ref}"
    
    def __eq__(self, other):
        if isinstance(other, uint8):
            return self.ref == other.ref
        elif isinstance(other, int):
            return self.ref == other
        elif isinstance(other, float):
            return self.ref == uint8(other).ref
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, uint8):
            return self.ref != other.ref
        elif isinstance(other, int):
            return self.ref != other
        elif isinstance(other, float):
            return self.ref != uint8(other).ref
        else:
            return True

    def __lt__(self, other):
        if isinstance(other, uint8):
            return self.ref < other.ref
        elif isinstance(other, int):
            return self.ref < other
        elif isinstance(other, float):
            return self.ref < uint8(other).ref
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, uint8):
            return self.ref > other.ref
        elif isinstance(other, int):
            return self.ref > other
        elif isinstance(other, float):
            return self.ref > uint8(other).ref
        else:
            return False

    def __and__(self, other):
        if isinstance(other, uint8):
            return self.ref & other.ref
        elif isinstance(other, int):
            return self.ref & other
        elif isinstance(other, float):
            return self.ref & uint8(other).ref
        else:
            return None

    def __or__(self, other):
        if isinstance(other, uint8):
            return self.ref | other.ref
        elif isinstance(other, int):
            return self.ref | other
        elif isinstance(other, float):
            return self.ref | uint8(other).ref
        else:
            return None

    def __xor__(self, other):
        if isinstance(other, uint8):
            return self.ref ^ other.ref
        elif isinstance(other, int):
            return self.ref ^ other
        elif isinstance(other, float):
            return self.ref ^ uint8(other).ref
        else:
            return None
    
    def __lshift__(self, other):
        if isinstance(other, uint8):
            return uint8(self.ref << other.ref)
        else:
            return uint8(self.ref << other)
        
    def __rshift__(self, other):
        if isinstance(other, uint8):
            return uint8(self.ref >> other.ref)
        else:
            return uint8(self.ref >> other)

    def __invert__(self):
        return uint8(~self.ref)
    


    def __pow__(self, other):
        result = uint8(1)
        for i in range(other):
            result *= self
        return result
    
class int8:
    """This code snippet defines a class called `uint8` that represents an 8-bit unsigned integer. It includes methods for arithmetic operations, bitwise operations, and comparison operations. The class also provides methods to convert the value to integer, hexadecimal, and binary representations.

    Example Usage:
    - Create a `uint8` object with a value of 10: `x = uint8(10)`
    - Get the value of `x`: `print(x)` (Output: 10)
    - Perform addition with another `uint8` object: `y = uint8(20)`, `z = x + y` (Output: 30)
    - Perform multiplication with an integer: `w = x * 3` (Output: 30)
    - Perform bitwise AND operation with another `uint8` object: `a = uint8(15)`, `b = uint8(7)`, `c = a & b` (Output: 7)
    - Convert the `uint8` value to integer, hexadecimal, and binary representations: `print(x.to_int())`, `print(x.to_hex())`, `print(x.to_binary())`

    Note: The code snippet also includes various magic methods for arithmetic, bitwise, and comparison operations, as well as in-place operations.

    Inputs:
    - The `__init__` method takes an initial value for the `ref` attribute, which can be an integer or an `np.int8` object.

    Outputs:
    - The code snippet does not have any explicit outputs. It defines the behavior of the `uint8` class for various operations and provides methods to convert the `ref` value to different representations.
    """
    
    def __init__(self, value) -> None:
        if not isinstance(value, int):        
            raise ValueError("Value must be int or byte")    
        if value < -128 or value > 127:        
            raise ValueError("Value must be between -128 and 127") 
        if value < 0:        
            value = -(abs(value) & 0x7F)    
        self._value = value   

    @property
    def ref(self):
        return self._value
    
    @ref.setter
    def ref(self, value):
        if not isinstance(value, int):        
            raise ValueError("Value must be int or byte")    
        if value < -128 or value > 127:        
            raise ValueError("Value must be between -128 and 127") 
        if value < 0:        
            value = -(abs(value) & 0x7F)    
        self.ref = value   

    
    @property       
    def real(self):
        return int8(self.ref)
    
    @property
    def imag(self):
        return int8(0)
    
    @property
    def numerator(self):
        return int8(self.ref)
    
    @property
    def denominator(self):
        return int8(1)
    
    @property
    def to_int(self):
        return int8(self.ref)

    @property
    def to_hex(self):
        return hex(self.ref)

    @property
    def to_binary(self):
        return bin(self.ref)[2:].zfill(8)

    def conjugate(self):
        return int8(self.ref)
    
    def bit_length(self):
        return int8(self.ref.bit_length())

    def __add__(self, other):
        if isinstance(other, int8):
            return int8(self.ref + other.ref)
        elif isinstance(other, int):
            return int8(self.ref + other)
        elif isinstance(other, float):
            return int8(self.ref + int8(other).ref)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, int8):
            return int8(self.ref - other.ref)
        elif isinstance(other, int):
            return int8(self.ref - other)
        elif isinstance(other, float):
            return int8(self.ref - int8(other).ref)
        else:
            return NotImplemented
            
    def __mul__(self, other):
        if isinstance(other, int8):
            return int8(self.ref * other.ref)
        elif isinstance(other, int):
            return int8(self.ref * other)
        elif isinstance(other, float):
            return int8(self.ref * int8(other).ref)
        else:
            return NotImplemented

    def __div__(self, other):
        if isinstance(other, int8):
            return int8(self.ref / other.ref)
        elif isinstance(other, int):
            return int8(self.ref / other)
        elif isinstance(other, float):
            return int8(self.ref / int8(other).ref)
        else:
            return NotImplemented

    def __mod__(self, other):
        if isinstance(other, int8):
            return int8(self.ref % other.ref)
        elif isinstance(other, int):
            return int8(self.ref % other)
        elif isinstance(other, float):
            return int8(self.ref % int8(other).ref)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return f"{self.ref}"
    
    def __eq__(self, other):
        if isinstance(other, int8):
            return self.ref == other.ref
        elif isinstance(other, int):
            return self.ref == other
        elif isinstance(other, float):
            return self.ref == int8(other).ref
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, int8):
            return self.ref != other.ref
        elif isinstance(other, int):
            return self.ref != other
        elif isinstance(other, float):
            return self.ref != int8(other).ref
        else:
            return True

    def __lt__(self, other):
        if isinstance(other, int8):
            return self.ref < other.ref
        elif isinstance(other, int):
            return self.ref < other
        elif isinstance(other, float):
            return self.ref < int8(other).ref
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, int8):
            return self.ref > other.ref
        elif isinstance(other, int):
            return self.ref > other
        elif isinstance(other, float):
            return self.ref > int8(other).ref
        else:
            return False

    def __and__(self, other):
        if isinstance(other, int8):
            return self.ref & other.ref
        elif isinstance(other, int):
            return self.ref & other
        elif isinstance(other, float):
            return self.ref & int8(other).ref
        else:
            return None

    def __or__(self, other):
        if isinstance(other, int8):
            return self.ref | other.ref
        elif isinstance(other, int):
            return self.ref | other
        elif isinstance(other, float):
            return self.ref | int8(other).ref
        else:
            return None

    def __xor__(self, other):
        if isinstance(other, int8):
            return self.ref ^ other.ref
        elif isinstance(other, int):
            return self.ref ^ other
        elif isinstance(other, float):
            return self.ref ^ int8(other).ref
        else:
            return None
    
    def __lshift__(self, other):
        if isinstance(other, int8):
            return int8(self.ref << other.ref)
        else:
            return int8(self.ref << other)
        
    def __rshift__(self, other):
        if isinstance(other, int8):
            return int8(self.ref >> other.ref)
        else:
            return int8(self.ref >> other)

    def __invert__(self):
        return uint8(~self.ref)
    
    def __pow__(self, other):
        result = int8(1)
        for i in range(other):
            result *= self
        return result
    


    """
    def inverse(self):
        for i in range(256):
            if (self.ref * i) % 256 == 1:
                return uint8(i)
        return None
    def factorial(self):
        result = uint8(1)
        for i in range(1, self.ref + 1):
            result *= uint8(i)
        return result

    def gcd(self, other):
        while other != uint8(0):
            self, other = other, self % other
        return self

    def lcm(self, other):
        return (self * other) // self.gcd(other)

    def sqrt(self):
        for i in range(256):
            if uint8(i) * uint8(i) == self:
                return uint8(i)
        return None
    """