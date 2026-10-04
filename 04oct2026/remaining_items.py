products=int(input("enter no of products:"))
eachbox_products=12
completeboxes=products//eachbox_products
remainingproducts=products%eachbox_products
print(f"completeboxes:{completeboxes} and remainingproducts:{remainingproducts}")