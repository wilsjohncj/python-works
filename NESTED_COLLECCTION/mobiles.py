# print all mobiles_names
# print all brands

mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":12500,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]

mobile_name=[st.get("title") for st in mobiles]
mobile_brand={mob.get("brand") for mob in mobiles}
# print(mobile_name)
# print(mobile_brand)

# print samsung mobile names

# samsung_mobiles=[mob.get("title") for mob in mobiles if mob.get("brand")=="samsung"]
# print(samsung_mobiles)

# print all mobile available in range of 23k to 40k

mobile_price=[mob.get("title") for mob in mobiles if mob.get("price" in range(23000,40001))]
print(mobile_price)

# costly mobile

max_price=0

for 