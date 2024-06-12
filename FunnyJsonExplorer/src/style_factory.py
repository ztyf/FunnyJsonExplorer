from container import TreeContainer, RectangleContainer

class StyleFactory:
    def createContainer(self, name, level, icon):
        raise NotImplementedError

class TreeStyleFactory(StyleFactory):
    def createContainer(self, name, level, icon):
        return TreeContainer(name, level, icon)

class RectangleStyleFactory(StyleFactory):
    def createContainer(self, name, level, icon):
        return RectangleContainer(name, level, icon)
