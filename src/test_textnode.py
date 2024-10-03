import unittest

from textnode import TextNode, text_type_bold, text_type_code, text_type_image,text_type_italic,text_type_link,text_type_text, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is also a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_type_not_equal(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_italic)
        self.assertNotEqual(node, node2)

    def test_url_set_to_none(self):
        node = TextNode("This is a text node", text_type_bold, None)
        node2 = TextNode("This is a text node", text_type_bold, None)
        self.assertEqual(node, node2)

    def test_url_has_value(self):
        node = TextNode("This is a text node", text_type_bold, "http://wwww.google.com")
        node2 = TextNode("This is a text node", text_type_bold, "http://wwww.google.com")
        self.assertEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("This is a text node", text_type_bold, "http://www.google.com")
        self.assertEqual("TextNode(This is a text node, bold, http://www.google.com)", repr(node))

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", text_type_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", text_type_image,"http://www.images.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"http://www.images.com/image.jpg", "alt":"This is an image"})
    
    def test_link(self):
        node = TextNode("Click Me!", text_type_link, "http://www.google.co.uk")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click Me!")
        self.assertEqual(html_node.props, {"href":"http://www.google.co.uk"})


if __name__=="__main__":
    unittest.main()