import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is also a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_type_not_equal(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_url_set_to_none(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_url_has_value(self):
        node = TextNode("This is a text node", "bold", "http://wwww.google.com")
        node2 = TextNode("This is a text node", "bold", "http://wwww.google.com")
        self.assertEqual(node, node2)
        

if __name__=="__main__":
    unittest.main()