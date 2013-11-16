from lib.wsdl import Wsdl
import config
wsdl=Wsdl(config.res+"test.wsdl")
print wsdl.operation