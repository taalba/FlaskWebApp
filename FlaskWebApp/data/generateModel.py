from py2neo import Graph

print("Building the model...")

graph = Graph("http://neo4j:7474/", password="Bluebee-123")


strCmd = "match (n) detach delete n"
graph.run(strCmd)

strCmd = """
create (WarehouseLocation: EntityModel {name: 'WarehouseLocation', description: 'WarehouseLocation', keyField: 'warehouseLocationID'})
create (Warehouse: EntityModel {name: 'Warehouse', description: 'Warehouse', keyField: 'warehouseID'})
create (Department: EntityModel {name: 'Department', description: 'Department', keyField: 'departmentID'})
create (Organization: EntityModel {name: 'Organization', description: 'Organization', keyField: 'organizationID'})
create (SalesOrder: EntityModel {name: 'SalesOrder', description: 'SalesOrder', keyField: 'salesOrderID'})
create (SalesOrderDetail: EntityModel {name: 'SalesOrderDetail', description: 'SalesOrderDetail', keyField: 'salesOrderDetailID'})
create (PurchaseOrder: EntityModel {name: 'PurchaseOrder', description: 'PurchaseOrder', keyField: 'purchaseOrderID'})
create (Product: EntityModel {name: 'Product', description: 'Product', keyField: 'productID'})
create (Customer: EntityModel {name: 'Customer', description: 'Customer', keyField: 'customerID'})
create (Supplier: EntityModel {name: 'Supplier', description: 'Supplier', keyField: 'supplierID'})
create (PurchaseOrderDetail: EntityModel {name: 'PurchaseOrderDetail', description: 'PurchaseOrderDetail', keyField: 'purchaseOrderDetailID'})
create (Shipment: EntityModel {name: 'Shipment', description: 'Shipment', keyField: 'shipmentID'})
create (ShipmentDetail: EntityModel {name: 'ShipmentDetail', description: 'ShipmentDetail', keyField: 'shipmentDetailID'})
create (Invoice: EntityModel {name: 'Invoice', description: 'Invoice', keyField: 'invoiceID'})
create (InvoiceDetail: EntityModel {name: 'InvoiceDetail', description: 'InvoiceDetail', keyField: 'invoiceDetailID'})
create (Receipt: EntityModel {name: 'Receipt', description: 'Receipt', keyField: 'receiptID'})
create (ReceiptDetail: EntityModel {name: 'ReceiptDetail', description: 'ReceiptDetail', keyField: 'receiptDetailID'})

create (Organization)-[:ONE_TO_MANY {name: 'USED_DEPARTMENT'}]->(Department)
create (Organization)-[:ONE_TO_MANY {name: 'USED_CUSTOMER'}]->(Customer)
create (Organization)-[:ONE_TO_MANY {name: 'USED_SUPPLIER'}]->(Supplier)
create (Department)-[:ONE_TO_MANY {name: 'USED_WAREHOUSE'}]->(Warehouse)
create (Customer)-[:ONE_TO_MANY {name: 'SENT_ORDER'}]->(SalesOrder)
create (Supplier)-[:ONE_TO_MANY {name: 'RECEIVED_PO'}]->(PurchaseOrder)
create (SalesOrder)-[:ONE_TO_MANY {name: 'ADDED_DETAIL'}]->(SalesOrderDetail)
create (SalesOrder)-[:ONE_TO_MANY {name: 'SHIPPED'}]->(Shipment)
create (PurchaseOrder)-[:ONE_TO_MANY {name: 'ADDED_DETAIL'}]->(PurchaseOrderDetail)
create (Warehouse)-[:ONE_TO_MANY {name: 'HAS_LOCATION'}]->(WarehouseLocation)
create (SalesOrderDetail)-[:ONE_TO_ONE {name: 'USED_PRODUCT'}]->(Product)
create (Shipment)-[:ONE_TO_MANY {name: 'ADDED_DETAIL'}]->(ShipmentDetail)
create (PurchaseOrderDetail)-[:ONE_TO_ONE {name: 'USED_PRODUCT'}]->(Product)
create (WarehouseLocation)-[:ONE_TO_MANY {name: 'USED_PRODUCT'}]->(Product)
create (SalesOrderDetail)-[:ONE_TO_MANY {name: 'SHIPPED'}]->(ShipmentDetail)
create (Invoice)-[:ONE_TO_MANY {name: 'ADDED_DETAIL'}]->(InvoiceDetail)
create (Shipment)-[:ONE_TO_ONE {name: 'INVOICED'}]->(Invoice)
create (ShipmentDetail)-[:ONE_TO_ONE {name: 'INVOICED'}]->(InvoiceDetail)
create (Receipt)-[:ONE_TO_MANY {name: 'ADDED_DETAIL'}]->(ReceiptDetail)
create (PurchaseOrder)-[:ONE_TO_MANY {name: 'RECEIVED'}]->(Receipt)
create (PurchaseOrderDetail)-[:ONE_TO_MANY {name: 'RECEIVED'}]->(ReceiptDetail)
"""

graph.run(strCmd)