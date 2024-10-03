class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        output_string = ""
        for prop in self.props:
            output_string += f" {prop}=\"{self.props[prop]}\""
        return output_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("must have a value")
        if self.tag:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return self.value
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if self.children is None:
            raise ValueError("parents must have children or they can't be parents!")
        output_string = ""
        output_string = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            output_string += child.to_html()
        output_string += f"</{self.tag}>"
        return output_string
    
    def __repr__(self):
        return f"ParentNode({self.tag}. children: {self.children}, {self.props})"