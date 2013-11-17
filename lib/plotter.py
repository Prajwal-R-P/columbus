from lib.wsdl import Wsdl
import networkx as nx
import matplotlib.pyplot as plt
import basic
from lib.similarity import Similarity
import config

class Plot():
    def __init__(self):
        self.G = nx.DiGraph()
        self.operation_nodes=[]
        self.node_color=[]
        self.node_size=[]
        self.id=0

    def show(self):
        for v in self.G:
            self.node_size.append(1000)
            if v in self.operation_nodes:
                self.node_color.append(1.0)
            else:
                self.node_color.append(2.0)

        nx.draw(self.G,node_color=self.node_color,node_size=self.node_size,width=2,alpha=0.5,edge_color='b')
        plt.savefig("joker.png")

        plt.show()

    def __wsdl__(self,wsdl):
        wsdl=Wsdl(wsdl)
        data=wsdl.operation
        operation=data['nodes']['operation']
        input_nodes=data['nodes']['input']
        output_nodes=data['nodes']['output']

        operation_node=self.create_node(operation)
        self.operation_connect(operation_node,input_nodes,True)
        self.operation_connect(operation_node,output_nodes,False)
        self.operation_nodes.append(operation_node)

    def wsdl_connect(self,wsdl_input,wsdl_output):
        input_operation=Wsdl(wsdl_input).operation
        output_operation=Wsdl(wsdl_output).operation

        input_nodes=[]
        for __input__ in input_operation['nodes']['input']:
            input_nodes.append(__input__['name'])
            del(__input__['name'])
            basic.dict_to_list(__input__,input_nodes)

        output_nodes=[]
        for __output__ in output_operation['nodes']['output']:
            output_nodes.append(__output__['name'])
            del(__output__['name'])
            basic.dict_to_list(__output__,input_nodes)

        print input_nodes,output_nodes
        for input_node in input_nodes:
            for output_node in output_nodes:
                if Similarity.sentences(input_node,output_node) > config.threshold:
                    print "DRAW",input_node, output_node
                    self.G.add_edge(self.search_node(output_node),self.search_node(input_node))

        #todo connect wsdls

    def operation_connect(self,operation_node,nodes,isInward=True):
        #self.node_color.append(1.0)
        for node in nodes:
            data_node=self.create_node(node['name'])
            if isInward:
                self.G.add_edge(data_node,operation_node)
            else:
                self.G.add_edge(operation_node,data_node)
            self.data_node_connect(data_node,node,isInward)

    def data_node_connect(self,center,nodes, isInward=True):
        if nodes.has_key("name"):
            del(nodes['name'])
        for node in nodes.iterkeys():
            #self.node_color.append(2.0)
            if node != self.node_name(center):
                new_node=self.create_node(node)
                if not isInward:
                    self.G.add_edge(center,new_node)
                else:
                    self.G.add_edge(new_node,center)
                self.data_node_connect(new_node, nodes[node],isInward)

    def create_node(self,name):
        self.id+=1
        return name+" "+str(self.id)

    def search_node(self,node):
        for v in self.G.nodes():
            print v, node
            if node == self.node_name(str(v)):
                return v
        return None

    @staticmethod
    def node_name(node):
        return " ".join(node.split(" ")[:1])