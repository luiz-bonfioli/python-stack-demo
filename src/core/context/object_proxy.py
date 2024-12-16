class ObjectProxy:
    """
    ObjectProxy is a lazy initialization proxy that is used to instantiate an object only when
    it is actually needed. The proxy holds a reference to an object generator (usually a
    callable that creates the object), and it will only create the object when one of its
    attributes or methods is accessed.

    This class is useful when you want to delay the creation of an object to improve
    performance, or if the object creation is expensive and you want to create it only
    when required.
    """

    def __init__(self, object_generator):
        self.object_generator = object_generator
        self.object = None

    def __generate_object(self):
        if self.object is None:
            self.object = self.object_generator()

    def __getattr__(self, name):
        self.__generate_object()
        return getattr(self.object, name)

