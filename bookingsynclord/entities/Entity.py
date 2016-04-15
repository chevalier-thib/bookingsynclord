from abc import ABCMeta
class Entity:
    """Abstract class with common properties for all entities."""
    __metaclass__ = ABCMeta

    def __init__(self, id = None):
        # String Unique identifier (at this moment values are integers; may be replaced by GUIDs in future)
        self.id = id
