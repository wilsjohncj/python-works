placement={"Django":35,"bigdata":45,"Java":65,"PBI":25,"C++":32}

def get_value(key):
    return placement.get(key)

srt=sorted(placement,key=get_value,reverse=True)

print(srt)