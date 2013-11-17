import xml.dom.minidom as dom


class Wsdl():
    def __init__(self, wsdl):
        self.tree = dom.parse(wsdl)
        self.file_name = wsdl
        self.operation = self.operation()
        #self.documentation = self.documentation()
        #self.all_tokens, self.service_tokens, self.operation_tokens, self.message_tokens, self.type_tokens, self.documentation_token = self.get_all_tokens()

    def operation(self):
        data = {}
        for portType in self.getElementsByTagName(self.tree, "portType"):
            port = dict()
            for operation in self.getElementsByTagName(portType, "operation"):
                port['operation'] = operation.getAttributeNode("name").nodeValue
                input_message = self.getElementsByTagName(operation, "input")[0].getAttributeNode("message").nodeValue.split(":")[-1]
                output_message = self.getElementsByTagName(operation, "output")[0].getAttributeNode("message").nodeValue.split(":")[-1]
                port['input'] = self.getElementsByMessage(input_message)
                port['output'] = self.getElementsByMessage(output_message)
            data['nodes']=port

        return data

    def documentation(self):
        data = []
        for document in self.getElementsByTagName(self.tree, "documentation"):
            try:
                data.append(document.firstChild.data)
            except:
                pass
        return data

    @staticmethod
    def getElementsByTagName(node, tag):
        return node.getElementsByTagName(tag) + node.getElementsByTagName("xsd:" + tag) + node.getElementsByTagName(
            "wsdl:" + tag)

        #this returns all the inputs/outputs corresponding to a message in WSDL

    def getElementsByMessage(self, message):
        data = []
        for message_element in self.getElementsByTagName(self.tree, "message"):
            if message_element.getAttributeNode("name").nodeValue == message:
                for part in self.getElementsByTagName(message_element, "part"):
                    part_data = dict()
                    part_data['name'] = part.getAttributeNode("name").nodeValue

                    type = part.getAttributeNode("type").nodeValue.split(":")[-1]
                    part_data['nodes'] = self.getComplexTypeNodes(type)
                    # part_data['type'] = part.getAttributeNode("type").nodeValue.split(":")[-1]
                    data.append(part_data)
        return data

    def getComplexTypeNodes(self,tag):
        data = []
        for complex_type in self.getElementsByTagName(self.tree, "complexType"):
            if complex_type.getAttributeNode('name').nodeValue == tag:
                for element in self.getElementsByTagName(complex_type,"element"):
                    data.append(element.getAttributeNode("name").nodeValue)
        return data