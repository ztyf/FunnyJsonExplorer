from container import Container

class Leaf(Container):
    def draw(self):
        icon_str = f"{self.icon} " if self.icon else ""
        return f"{' ' * self.level * 2}{icon_str}{self.name}\n"
