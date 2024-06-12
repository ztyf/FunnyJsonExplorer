class Container:
    def __init__(self, name, level=0, icon=None):
        self.name = name
        self.level = level
        self.icon = icon
        self.children = []

    def add(self, child):
        self.children.append(child)

    def draw(self):
        raise NotImplementedError

class TreeContainer(Container):
    def draw(self):
        icon_str = f"{self.icon} " if self.icon else ""
        result = f"{' ' * self.level * 2}├─{icon_str}{self.name}\n"
        for child in self.children:
            result += child.draw()
        return result



class RectangleContainer(Container):
    def draw(self):
        icon_str = f"{self.icon} " if self.icon else ""
        result = f"{' ' * self.level * 2}┌─{icon_str}{self.name}\n"
        for child in self.children:
            result += child.draw()
        result += f"{' ' * self.level * 2}└\n"
        return result
