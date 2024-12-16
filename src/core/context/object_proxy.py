class ObjectProxy:

    def __init__(self, object_generator):
        self.object_generator = object_generator
        self.object = None

    def __generate_object(self):
        if self.object is None:
            self.object = self.object_generator()

    def __getattr__(self, name):
        self.__generate_object()
        return getattr(self.object, name)

    def get_proxy_object(self):
        self.__generate_object()
        return self.object
