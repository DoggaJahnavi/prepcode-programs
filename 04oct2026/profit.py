buyingprice=int(input("enter the buying price:"))
sellingprice=int(input("enter the selling price:"))
totalproduct=int(input("enter the amount of product:"))
storageprice=int(input("storageamount:"))
profit=((sellingprice-buyingprice)*totalproduct)-storageprice
print(f"totalprofit:{profit}")