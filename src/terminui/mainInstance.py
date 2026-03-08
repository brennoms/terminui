class MainInstance:
    _instance = None

    @classmethod
    def setInstance(cls, instance):
        cls._instance = instance
        return cls._instance
    
    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            raise Exception("Main instance not set")
        return cls._instance
