from py2neo import Graph
graph = graph = Graph("http://localhost:7474/", password="Bluebee-123")

def deleteNode(nodeName):
    strCmd = 'match (n:%s) detach delete n' %(nodeName)
    graph.run(strCmd)

deleteNode("Organization")
deleteNode("Organization")
deleteNode("Department")
deleteNode("Supplier")
deleteNode("Customer")
deleteNode("Warehouse")
deleteNode("WarehouseLocation")
deleteNode("Product")
deleteNode("PurchaseOrder")
deleteNode("SalesOrder")
deleteNode("PurchaseOrderDetail")
deleteNode("SalesOrderDetail")