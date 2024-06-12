# 主程序

from style_factory import TreeStyleFactory, RectangleStyleFactory
from icon_factory import IconFactory
from container import Container
from leaf import Leaf

class FunnyJsonExplorer:
    def __init__(self, style_factory, icon_factory):
        self.style_factory = style_factory
        self.icon_factory = icon_factory
        self.root = None

    def load(self, json_data):
        self.root = self.parse_json(json_data)

    def parse_json(self, data, level=0):
        if isinstance(data, dict):
            container = self.style_factory.createContainer(list(data.keys())[0], level, self.icon_factory.getIcon('node'))
            for k, v in data.items():
                container.add(self.parse_json(v, level + 1))
            return container
        elif isinstance(data, list):
            container = self.style_factory.createContainer("list", level, self.icon_factory.getIcon('node'))
            for item in data:
                container.add(self.parse_json(item, level + 1))
            return container
        else:
            return Leaf(data, level, self.icon_factory.getIcon('leaf'))

    def show(self):
            print(self.root.draw())

if __name__ == "__main__":
    import json

    json_data = '''
    {
        "technology": {
            "work": {
                "day": "8h",
                "eve": "5h"
            },
            "employee Number": 100,
            "employer": {
                "boss":{
                    "boss A": null,
                    "boss B": null
                },
                "vice boss":{
                    "vice boss 1": null,
                    "vice boss 2": null,
                    "vice boss 3": "bxx"
                }
            }
        },
        "chemical": {
            "figures": 400,
            "boxes":{
                "this value is": false,
                "that value is": true
            },
            "sodu": "homework"
        }
    }
    '''

    # Initialize factories for four different combinations
    tree_style_factory = TreeStyleFactory()
    rectangle_style_factory = RectangleStyleFactory()

    icon_factory_set1 = IconFactory('set1')
    icon_factory_set2 = IconFactory('set2')

    fje_tree_set1 = FunnyJsonExplorer(tree_style_factory, icon_factory_set1)
    fje_tree_set2 = FunnyJsonExplorer(tree_style_factory, icon_factory_set2)
    fje_rectangle_set1 = FunnyJsonExplorer(rectangle_style_factory, icon_factory_set1)
    fje_rectangle_set2 = FunnyJsonExplorer(rectangle_style_factory, icon_factory_set2)

    # Load data
    data = json.loads(json_data)
    fje_tree_set1.load(data)
    fje_tree_set2.load(data)
    fje_rectangle_set1.load(data)
    fje_rectangle_set2.load(data)

    # Show data in different styles and icon sets
    print("Tree Style with Icon Set 1:")
    fje_tree_set1.show()
    print("\nTree Style with Icon Set 2:")
    fje_tree_set2.show()
    print("\nRectangle Style with Icon Set 1:")
    fje_rectangle_set1.show()
    print("\nRectangle Style with Icon Set 2:")
    fje_rectangle_set2.show()
