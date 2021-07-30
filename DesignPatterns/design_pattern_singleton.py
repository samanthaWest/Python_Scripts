# Singleton - Single class resp. for creating an object

class SingleObject:
    _singleObject = SingleObject()
    
    def SingleObject(self):
        pass

    def getInstance(self) -> SingleObject:
        return self._singleObject


if __name__ == "__main__":
    singleObj = SingleObject()
    singleObj.getInstance()