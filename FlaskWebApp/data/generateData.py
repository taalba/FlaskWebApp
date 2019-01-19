from objects import EntityModel


print("Filling with data...")

org  = EntityModel("Organization")
org.set("organizationID", "1")
org.set("name", "Organization 1")
org.update()

org.find("1") 
dept = EntityModel("Department")
sup = EntityModel("Supplier")
cust = EntityModel("Customer")
whs = EntityModel("Warehouse")
whsloc = EntityModel("WarehouseLocation")
prod = EntityModel("Product")

ord = EntityModel("SalesOrder")
po = EntityModel("PurchaseOrder")

whscount = 0
whsloccount = 0
prodcount = 0
ordcount = 0
pocount = 0
ordlinecount = 0
polinecount = 0

for i in range(1, 4):
    dept.set("departmentID", "%s" %(i))
    dept.set("name", "Department %s" %(i)) 
    dept.set("description", "Department %s" %(i))
    dept.update()

    rel = org.getRelationTo(dept)
    rel.set("description", "Department used")
    rel.update(org, dept)

    for j in range(1, 4):
        whscount = whscount + 1
        whs.set("warehouseID", "%s" %(whscount))
        whs.set("name", "Warehouse %s" %(whscount)) 
        whs.set("description", "Warehouse %s" %(whscount))
        whs.update()

        rel = dept.getRelationTo(whs)
        rel.set("description", "Warehouse used")
        rel.update(dept, whs)

        for k in range(1, 4):
            whsloccount = whsloccount + 1
            whsloc.set("warehouseLocationID", "%s" %(whsloccount))
            whsloc.set("name", "Location %s" %(whsloccount)) 
            whsloc.set("description", "Location %s" %(whsloccount))
            whsloc.update()

            rel = whs.getRelationTo(whsloc)
            rel.set("description", "Location used")
            rel.update(whs, whsloc)

            for l in range(1, 6):
                prodcount = prodcount + 1
                prod.set("productID", "%s" %(prodcount))
                prod.set("name", "Product %s" %(prodcount)) 
                prod.set("description", "Product %s" %(prodcount))
                prod.update()

                rel = whsloc.getRelationTo(prod)
                rel.set("description", "Product used used")
                rel.update(whsloc, prod)

for i in range(1, 11):
    sup.set("supplierID", "%s" %(i))
    sup.set("name", "supplier %s" %(i)) 
    sup.set("description", "supplier %s" %(i))
    sup.update()

    rel = org.getRelationTo(sup)
    rel.set("description", "Supplier used")
    rel.update(org, sup)

for i in range(1, 6):
    cust.set("customerID", "%s" %(i))
    cust.set("name", "customer %s" %(i)) 
    cust.set("description", "customer %s" %(i))
    cust.update()

    rel = org.getRelationTo(cust)
    rel.set("description", "customer used")
    rel.update(org, cust)


def generateSalesOrder(custID):
    global ordcount
    cust = EntityModel("Customer")
    ord = EntityModel("SalesOrder")
    cust.find(custID)
    ordcount = ordcount + 1
    ord.set("salesOrderID", "%s" %(ordcount))
    ord.set("name", "salesOrder %s" %(ordcount)) 
    ord.set("description", "salesOrder %s" %(ordcount))
    ord.update()
    rel = cust.getRelationTo(ord)
    rel.set("description", "salesOrder used")
    rel.update(cust, ord)

    generateSalesOrderDetail("%s" %(ordcount), '1')
    generateSalesOrderDetail("%s" %(ordcount), '2')
    generateSalesOrderDetail("%s" %(ordcount), '3')

def generateSalesOrderDetail(salesOrderId, productID):
    global ordlinecount
    ord = EntityModel("SalesOrder")
    ordline = EntityModel("SalesOrderDetail")
    prod = EntityModel("Product")
    ord.find(salesOrderId)
    prod.find(productID)

    ordlinecount = ordlinecount + 1
    ordline.set("salesOrderDetailID", "%s" %(ordlinecount))
    ordline.set("name", "salesOrderDetail %s" %(ordlinecount)) 
    ordline.set("description", "salesOrderDetail %s" %(ordlinecount))
    ordline.update()

    rel = ord.getRelationTo(ordline)
    rel.set("description", "salesOrderDetail used")
    rel.update(ord, ordline)

    rel = ordline.getRelationTo(prod)
    rel.set("description", "Product used")
    rel.update(ordline, prod)

def generatePurchaseOrder(supplierID):
    global pocount
    sup = EntityModel("Supplier")
    po = EntityModel("PurchaseOrder")
    sup.find(supplierID)
    pocount = pocount + 1
    po.set("purchaseOrderID", "%s" %(pocount))
    po.set("name", "purchaseOrder %s" %(pocount)) 
    po.set("description", "purchaseOrder %s" %(pocount))
    po.update()
    rel = sup.getRelationTo(po)
    rel.set("description", "purchaseOrder used")
    rel.update(sup, po)

    generatePurchaseOrderDetail("%s" %(pocount), '1')
    generatePurchaseOrderDetail("%s" %(pocount), '2')
    generatePurchaseOrderDetail("%s" %(pocount), '3')

def generatePurchaseOrderDetail(purchaseOrderId, productID):
    global polinecount
    po = EntityModel("PurchaseOrder")
    poline = EntityModel("PurchaseOrderDetail")
    prod = EntityModel("Product")
    po.find(purchaseOrderId)
    prod.find(productID)

    polinecount = polinecount + 1
    poline.set("purchaseOrderDetailID", "%s" %(polinecount))
    poline.set("name", "PurchaseOrderDetail %s" %(polinecount)) 
    poline.set("description", "PurchaseOrderDetail %s" %(polinecount))
    poline.update()

    rel = po.getRelationTo(poline)
    rel.set("description", "PurchaseOrderDetail used")
    rel.update(po, poline)

    rel = poline.getRelationTo(prod)
    rel.set("description", "Product used")
    rel.update(poline, prod)

generateSalesOrder('1')
generatePurchaseOrder('1')
