"""
Python Dunder (Double Underscore) Methods

Dunder methods are special methods in Python with double underscores at the beginning and end
of their names. They allow you to emulate built-in behavior and implement operator overloading.
"""

# Object Initialization and Lifecycle
__new__ = "Class method that creates and returns a new instance"
__init__ = "Initialize a new instance (constructor)"
__del__ = "Called when an object is garbage collected (destructor)"

# Object Representation
__str__ = "String representation for end-users (str())"
__repr__ = "String representation for developers (repr())"
__bytes__ = "Bytes representation (bytes())"
__format__ = "Formatted string representation (format())"

# Attribute Access
__getattr__ = "Called when attribute lookup fails"
__getattribute__ = "Called for all attribute lookups"
__setattr__ = "Called when setting an attribute"
__delattr__ = "Called when deleting an attribute"
__dir__ = "List of attributes (dir())"

# Container/Sequence Methods
__len__ = "Length of container (len())"
__getitem__ = "Access item by index/key (obj[key])"
__setitem__ = "Set item by index/key (obj[key] = value)"
__delitem__ = "Delete item by index/key (del obj[key])"
__contains__ = "Membership test (in operator)"
__iter__ = "Return iterator for container"
__next__ = "Return next item from iterator"
__reversed__ = "Return reversed iterator (reversed())"

# Callable Objects
__call__ = "Make an object callable like a function"

# Comparison Operators
__lt__ = "Less than (<)"
__le__ = "Less than or equal (<=)"
__eq__ = "Equal (==)"
__ne__ = "Not equal (!=)"
__gt__ = "Greater than (>)"
__ge__ = "Greater than or equal (>=)"
__hash__ = "Hash value for dictionary keys (hash())"

# Numeric Operations (Arithmetic)
__add__ = "Addition (+)"
__sub__ = "Subtraction (-)"
__mul__ = "Multiplication (*)"
__matmul__ = "Matrix multiplication (@)"
__truediv__ = "Division (/)"
__floordiv__ = "Floor division (//)"
__mod__ = "Modulo (%)"
__divmod__ = "Division and modulo (divmod())"
__pow__ = "Exponentiation (**)"
__lshift__ = "Left shift (<<)"
__rshift__ = "Right shift (>>)"
__and__ = "Bitwise AND (&)"
__xor__ = "Bitwise XOR (^)"
__or__ = "Bitwise OR (|)"

# Reflected/Reversed Arithmetic Operations (when left operand doesn't support the operation)
__radd__ = "Reflected addition"
__rsub__ = "Reflected subtraction"
__rmul__ = "Reflected multiplication"
__rmatmul__ = "Reflected matrix multiplication"
__rtruediv__ = "Reflected division"
__rfloordiv__ = "Reflected floor division"
__rmod__ = "Reflected modulo"
__rdivmod__ = "Reflected divmod"
__rpow__ = "Reflected power"
__rlshift__ = "Reflected left shift"
__rrshift__ = "Reflected right shift"
__rand__ = "Reflected bitwise AND"
__rxor__ = "Reflected bitwise XOR"
__ror__ = "Reflected bitwise OR"

# In-place Operations
__iadd__ = "In-place addition (+=)"
__isub__ = "In-place subtraction (-=)"
__imul__ = "In-place multiplication (*=)"
__imatmul__ = "In-place matrix multiplication (@=)"
__itruediv__ = "In-place division (/=)"
__ifloordiv__ = "In-place floor division (//=)"
__imod__ = "In-place modulo (%=)"
__ipow__ = "In-place power (**=)"
__ilshift__ = "In-place left shift (<<=)"
__irshift__ = "In-place right shift (>>=)"
__iand__ = "In-place bitwise AND (&=)"
__ixor__ = "In-place bitwise XOR (^=)"
__ior__ = "In-place bitwise OR (|=)"

# Unary Operations
__neg__ = "Unary negation (-)"
__pos__ = "Unary positive (+)"
__abs__ = "Absolute value (abs())"
__invert__ = "Bitwise inversion (~)"
__complex__ = "Complex conversion (complex())"
__int__ = "Integer conversion (int())"
__float__ = "Float conversion (float())"
__round__ = "Round to nearest integer (round())"
__trunc__ = "Truncation to integer (math.trunc())"
__floor__ = "Floor (math.floor())"
__ceil__ = "Ceiling (math.ceil())"

# Context Management
__enter__ = "Enter a context (with statement)"
__exit__ = "Exit a context (with statement)"

# Descriptor Protocol
__get__ = "Get descriptor value"
__set__ = "Set descriptor value"
__delete__ = "Delete descriptor value"
__set_name__ = "Set descriptor name"

# Pickle Protocol
__reduce__ = "Helper for pickle"
__reduce_ex__ = "Helper for pickle with protocol version"
__getnewargs__ = "Arguments for __new__ when unpickling"
__getnewargs_ex__ = "Arguments for __new__ when unpickling with protocol 4+"
__getstate__ = "State for pickle"
__setstate__ = "Restore state during unpickling"

# Class Customization
__init_subclass__ = "Called when a class is subclassed"
__class_getitem__ = "Support for class[...]"
__mro_entries__ = "Modify method resolution order"

# Other
__copy__ = "Create a shallow copy"
__deepcopy__ = "Create a deep copy"
__sizeof__ = "Size in memory (sys.getsizeof())"
__instancecheck__ = "isinstance() implementation"
__subclasscheck__ = "issubclass() implementation"
__prepare__ = "Namespace preparation for class definition"

# Example implementation of some common dunder methods
class Example:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"Example({self.value})"
    
    def __repr__(self):
        return f"Example({self.value!r})"
    
    def __eq__(self, other):
        if isinstance(other, Example):
            return self.value == other.value
        return False
    
    def __add__(self, other):
        if isinstance(other, Example):
            return Example(self.value + other.value)
        return Example(self.value + other)
    
    def __len__(self):
        return len(str(self.value))
    
    def __call__(self, x):
        return self.value * x