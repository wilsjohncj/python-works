from json import load

f=open("C:\\Users\\wils_\\OneDrive\\Desktop\\PythonJuneWorks\\JSONworks\\products.json","r",encoding="UTF-8")

products = load(f)

# print(len(products))

# product_titles=[p.get("title") for p in products]

# print(product_titles)

def get_rating_count(dic): # creates a function

    return dic.get("rating").get("count")

top_selling_prod=max(products,key=get_rating_count)

print(top_selling_prod.get("title"),top_selling_prod.get("rating").get("count"))





# jewelery_products=[i.get("title") for i in products if i.get("category")=="jewelery"]

# print(jewelery_products)

# product_price=[i.get("title") for i in products if i.get("price")>100]

# print(product_price)

# products in range of 100 to 150

# product_range=[i.get("title") for i in products if i.get("price")>=100 and i.get("price") <=150]

# print(product_range)

# most number of ratings

product_rating=[ for i in products ]







