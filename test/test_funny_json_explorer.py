# 测试程序

import sys
import os
import unittest
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from funny_json_explorer import FunnyJsonExplorer
from style_factory import TreeStyleFactory, RectangleStyleFactory
from icon_factory import IconFactory

class TestFunnyJsonExplorer(unittest.TestCase):
    def setUp(self):
        self.json_data = '''
        {
          "oranges": {
            "mandarin": {
              "clementine": null,
              "tangerine": "cheap & juicy!"
            }
          },
          "apples": {
            "gala": null,
            "pink lady": null
          }
        }
        '''
        self.data = json.loads(self.json_data)
        self.tree_style_factory = TreeStyleFactory()
        self.rectangle_style_factory = RectangleStyleFactory()

        self.icon_factory_set1 = IconFactory('set1')
        self.icon_factory_set2 = IconFactory('set2')

    def test_tree_style_set1(self):
        fje_tree_set1 = FunnyJsonExplorer(self.tree_style_factory, self.icon_factory_set1)
        fje_tree_set1.load(self.data)
        fje_tree_set1.show()

    def test_tree_style_set2(self):
        fje_tree_set2 = FunnyJsonExplorer(self.tree_style_factory, self.icon_factory_set2)
        fje_tree_set2.load(self.data)
        fje_tree_set2.show()

    def test_rectangle_style_set1(self):
        fje_rectangle_set1 = FunnyJsonExplorer(self.rectangle_style_factory, self.icon_factory_set1)
        fje_rectangle_set1.load(self.data)
        fje_rectangle_set1.show()

    def test_rectangle_style_set2(self):
        fje_rectangle_set2 = FunnyJsonExplorer(self.rectangle_style_factory, self.icon_factory_set2)
        fje_rectangle_set2.load(self.data)
        fje_rectangle_set2.show()

if __name__ == "__main__":
    unittest.main()
