class IconFactory:
    def __init__(self, icon_set):
        self.icon_set = icon_set

    def getIcon(self, type):
        icons = {
            'set1': {'node': '♦', 'leaf': '♠'},
            'set2': {'node': '○', 'leaf': '☆'}
        }
        return icons[self.icon_set].get(type, '')
