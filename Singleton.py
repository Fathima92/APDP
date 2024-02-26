class singleton(type):  #songlton inherit type which makes singlton as meta class
    _instances ={}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances: #if any instance of class is not exist
            cls._instances[cls] = super(singleton,cls).__call__(*args, **kwargs) # create an instance for a singlton class
            return cls._instances[cls] #return a new instance



class Logger(metaclass= singleton):
        def log(self,msg):
            print(msg)
