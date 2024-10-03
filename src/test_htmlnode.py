import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leafnode_values(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph of text.")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_basic_leafnode(self):
        node = LeafNode("p","This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

    def test_leafnode_with_props(self):
        node = LeafNode("a", "Click me!", {"href":"https://www.google.co.uk"})
        self.assertEqual(
            "<a href=\"https://www.google.co.uk\">Click me!</a>",
            node.to_html()
            )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!") 

    def test_standard_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )   
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())

    def test_nested_parent_node(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "ul", 
                    [
                        LeafNode("li", "Item 1"),
                        LeafNode("li", "Item 2")
                    ]
                )
            ]
        )
        self.assertEqual("<p><ul><li>Item 1</li><li>Item 2</li></ul></p>", node.to_html())

    def test_parent_with_empty_children(self):
        node = ParentNode(
            "p",
            None
        )
        self.assertRaises(ValueError, lambda: node.to_html())

    def test_parent_must_have_tag(self):
        node = ParentNode(None, [LeafNode("b","Bold text")])
        self.assertRaises(ValueError, lambda:  node.to_html())

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__=="__main__":
    unittest.main()