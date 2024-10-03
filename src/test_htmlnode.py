import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_tag_props(self):
        node = HTMLNode("A",None, None, {"href":"https://www.google.co.uk", "target":"_blank"})
        self.assertEqual(" href=\"https://www.google.co.uk\" target=\"_blank\"", node.props_to_html())

    def test_basic_node(self):
        node = HTMLNode("h1","This is the title",None,{"class":"active", "id":"Main header"})
        self.assertEqual("HTMLNode(h1, This is the title, children: None, {'class': 'active', 'id': 'Main header'})", node.__repr__())

    def test_child_node(self):
        child = HTMLNode("li", "Test", None, None)
        parent = HTMLNode("ul",None, child, None)
        self.assertEqual("HTMLNode(ul, None, children: HTMLNode(li, Test, children: None, None), None)", parent.__repr__())
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )
if __name__=="__main__":
    unittest.main()