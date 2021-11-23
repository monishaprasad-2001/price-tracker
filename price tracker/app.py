from os import name
import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        "product_url":"https://www.amazon.in/OnePlus-Nord-Blue-128GB-Storage/dp/B097RD2JX8/ref=sr_1_1?dchild=1&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=be0a58aa-ab6d-41fe-9e58-bb43c31999f1&pf_rd_r=PH69T3S9ASCW706Z3WQ5&pf_rd_s=merchandised-search-3&qid=1631678775&refinements=p_89%3AOnePlus&rnid=3837712031&s=electronics&sr=1-1",
        "name":"OnePlus Nord 2 5G (Blue Haze, 8GB RAM, 128GB Storage)",
        "target_price":"29500"
        
    },
    {
        "product_url":"https://www.amazon.in/OnePlus-Nord-Charcoal-128GB-Storage/dp/B09576CYNP/ref=sr_1_3?dchild=1&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=be0a58aa-ab6d-41fe-9e58-bb43c31999f1&pf_rd_r=PH69T3S9ASCW706Z3WQ5&pf_rd_s=merchandised-search-3&qid=1631678775&refinements=p_89%3AOnePlus&rnid=3837712031&s=electronics&sr=1-3",
        "name":"OnePlus Nord CE 5G (Charcoal Ink, 8GB RAM, 128GB Storage)",
        "target_price":"24500"
    },
    {
        "product_url":"https://www.amazon.in/OnePlus-Nord-Blue-256GB-Storage/dp/B097RDF6NW/ref=sr_1_7?dchild=1&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=be0a58aa-ab6d-41fe-9e58-bb43c31999f1&pf_rd_r=PH69T3S9ASCW706Z3WQ5&pf_rd_s=merchandised-search-3&qid=1631678775&refinements=p_89%3AOnePlus&rnid=3837712031&s=electronics&sr=1-7",
        "name":"OnePlus Nord 2 5G (Blue Haze, 12GB RAM, 256GB Storage)" ,
        "target_price":"40500"   
    },
    {
        "product_url":"https://www.amazon.in/Test-Exclusive_2020_1181-Multi-3GB-Storage/dp/B089MSK447/ref=sr_1_11?dchild=1&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=be0a58aa-ab6d-41fe-9e58-bb43c31999f1&pf_rd_r=PH69T3S9ASCW706Z3WQ5&pf_rd_s=merchandised-search-3&qid=1631678775&refinements=p_89%3AOnePlus&rnid=3837712031&s=electronics&sr=1-11",
        "name":"OnePlus 9R 5G (Lake Blue, 12GB RAM, 256GB Storage)" ,
        "target_price":"49500"   
    },
    {
        "product_url":"https://www.amazon.in/Test-Exclusive_2020_1176-Multi-3GB-Storage/dp/B089MV1ZSM/ref=sr_1_13?dchild=1&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=be0a58aa-ab6d-41fe-9e58-bb43c31999f1&pf_rd_r=PH69T3S9ASCW706Z3WQ5&pf_rd_s=merchandised-search-3&qid=1631678775&refinements=p_89%3AOnePlus&rnid=3837712031&s=electronics&sr=1-13",
        "name":"OnePlus 9 5G (Arctic Sky, 8GB RAM, 128GB Storage)", 
        "target_price":"50000"   
    }
]

def give_product_price(product_url):
    headers = {
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }
    page = requests.get(product_url,headers = headers)
    soup = BeautifulSoup(page.content,'html.parser')

    product_price = soup.find(id="priceblock_dealprice")
    if(product_price == None):
        product_price = soup.find(id="priceblock_ourprice")

    return product_price.getText()

resultfile = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + "-" + every_product.get("name"))

        my_product_price = product_price_returned[1:]
        my_product_price = my_product_price.replace(',','')
        my_product_price = int(float(my_product_price))

        print(my_product_price)
        if my_product_price < float(every_product.get("target_price")):
            print("available at your price")
            resultfile.write(every_product.get("name") + ' - \t' + 'Availabke at target price ' + 'current price- '+ str(my_product_price) +'\n')
    
        else:
            print("still at the same price")

finally:
    resultfile.close()



