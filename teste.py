externalUrl=["https:","http:"]
aleratiro= "https://wikidocs.net/images/page/49159/png-2702691_1920_back.png"
listaurl2 = aleratiro.split("//")
if(listaurl2[0] not in externalUrl):
    print("interno")
else:
    print("externo")
print(listaurl2)