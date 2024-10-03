from textnode import TextNode, text_type_bold
from htmlnode import HTMLNode
def main():
    text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(text_node.__repr__())

    html_node = HTMLNode("h1","This is the title",None,{"class":"active", "id":"Main header"})
    html_child_node = HTMLNode("li","Test",None, None)
    html_parent_node = HTMLNode("ul",None, html_child_node, None)
    # print(html_node.props_to_html())
    
    print(html_node.__repr__())
    print(html_parent_node.__repr__())

if __name__=="__main__":
    main()