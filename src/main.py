from textnode import TextNode, text_type_bold
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # print(text_node.__repr__())

    html_node = HTMLNode("h1","This is the title",None,{"class":"active", "id":"Main header"})
    html_child_node = HTMLNode("li","Test",None, None)
    html_parent_node = HTMLNode("ul",None, html_child_node, None)
    # print(html_node.props_to_html())
    
    # print(html_node.__repr__())
    # print(html_parent_node.__repr__())

    # html_leaf_node = LeafNode("p", "Paragraph text")
    # print(html_leaf_node.to_html())
    # html_leaf_node = LeafNode(None, "Test")
    # print(html_leaf_node.to_html())

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())

if __name__=="__main__":
    main()