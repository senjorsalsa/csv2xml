import csv
from pydoc import doc
import xml.etree.ElementTree as et
import os
from os import path

selected_delimiter = ';'
feed = {"Availability": False, "Price": False, "Product": False, "Media": True}
__location__ = path.realpath(path.join(os.getcwd(), path.dirname(__file__)))

def create_availability():
    with open(os.path.join(__location__, "availability.csv"), encoding = 'utf-8-sig') as availability:
        reader = csv.reader(availability, delimiter=selected_delimiter)
        values = list(reader)
        keys = values.pop(0)

    products = []
    avail_xsd = 'https://schemas.cdon.com/product/4.0/4.12.0/availability'
    
    for i in range(len(values)):
        products.append(dict(zip(keys, values[i])))

    marketplace = et.Element("marketplace",  xmlns=avail_xsd)

    for i in range(len(products)):
        product = et.SubElement(marketplace, "product")
        et.SubElement(product, "id").text = products[i]["id"]
        et.SubElement(product, "stock").text = products[i]["stock"]

        if "se status" in products[i]:
            se = et.SubElement(product, "se")
            et.SubElement(se, "status").text = products[i]["se status"]
            delivery_se = et.SubElement(se, "deliveryTime")
            et.SubElement(delivery_se, "min").text = products[i]["se min"]
            et.SubElement(delivery_se, "max").text = products[i]["se max"]

        if "dk status" in products[i]:
            dk = et.SubElement(product, "dk")
            et.SubElement(dk, "status").text = products[i]["dk status"]
            delivery_dk = et.SubElement(dk, "deliveryTime")
            et.SubElement(delivery_dk, "min").text = products[i]["dk min"]
            et.SubElement(delivery_dk, "max").text = products[i]["dk max"]

        if "no status" in products[i]:
            no = et.SubElement(product, "no")
            et.SubElement(no, "status").text = products[i]["no status"]
            delivery_no = et.SubElement(no, "deliveryTime")
            et.SubElement(delivery_no, "min").text = products[i]["no min"]
            et.SubElement(delivery_no, "max").text = products[i]["no max"]

        if "fi status" in products[i]:
            fi = et.SubElement(product, "fi")
            et.SubElement(fi, "status").text = products[i]["fi status"]
            delivery_fi = et.SubElement(fi, "deliveryTime")
            et.SubElement(delivery_fi, "min").text = products[i]["fi min"]
            et.SubElement(delivery_fi, "max").text = products[i]["fi max"]

    tree = et.ElementTree(marketplace)
    tree.write("availability.xml", encoding = "utf-8", xml_declaration = True)
    
def create_price():
    price_xsd = 'https://schemas.cdon.com/product/4.0/4.12.0/price'
    products = []
    
    with open(os.path.join(__location__, "price.csv"), encoding = 'utf-8-sig') as price:
        reader = csv.reader(price, delimiter=selected_delimiter)
        values = list(reader)
        keys = values.pop(0)

    for i in range(len(values)):
        products.append(dict(zip(keys, values[i])))

    marketplace = et.Element("marketplace",  xmlns=price_xsd)

    for i in range(len(products)):
        product = et.SubElement(marketplace, "product")
        et.SubElement(product, "id").text = products[i]["id"]

        if "SE saleprice" in products[i]:
            se = et.SubElement(product, "se")
            et.SubElement(se, "salePrice").text = products[i]["SE saleprice"]
            et.SubElement(se, "originalPrice").text = products[i]["SE originalprice"]
            if "SE shipped from EU" in products[i]:
                et.SubElement(se, "isShippedFromEU").text = products[i]["SE shipped from EU"]
            if "SE shipping cost" in products[i]:
                et.SubElement(se, "shippingCost").text = products[i]["SE shipping cost"]
            if "SE vat" in products[i]:
                et.SubElement(se, "vat").text = products[i]["SE vat"]

        if "DK saleprice" in products[i]:
            dk = et.SubElement(product, "dk")
            et.SubElement(dk, "salePrice").text = products[i]["DK saleprice"]
            et.SubElement(dk, "originalPrice").text = products[i]["DK originalprice"]
            if "DK shipped from EU" in products[i]:
                et.SubElement(dk, "isShippedFromEU").text = products[i]["DK shipped from EU"]
            if "DK shipping cost" in products[i]:
                et.SubElement(dk, "shippingCost").text = products[i]["DK shipping cost"]
            if "DK vat" in products[i]:
                et.SubElement(dk, "vat").text = products[i]["DK vat"]

        if "NO saleprice" in products[i]:
            no = et.SubElement(product, "no")
            et.SubElement(no, "salePrice").text = products[i]["NO saleprice"]
            et.SubElement(no, "originalPrice").text = products[i]["NO originalprice"]
            if "NO shipped from EU" in products[i]:
                et.SubElement(no, "isShippedFromEU").text = products[i]["NO shipped from EU"]
            if "NO shipping cost" in products[i]:
                et.SubElement(no, "shippingCost").text = products[i]["NO shipping cost"]
            if "NO vat" in products[i]:
                et.SubElement(no, "vat").text = products[i]["NO vat"]

        if "FI saleprice" in products[i]:
            fi = et.SubElement(product, "fi")
            et.SubElement(fi, "salePrice").text = products[i]["FI saleprice"]
            et.SubElement(fi, "originalPrice").text = products[i]["FI originalprice"]
            if "FI shipped from EU" in products[i]:
                et.SubElement(fi, "isShippedFromEU").text = products[i]["FI shipped from EU"]
            if "FI shipping cost" in products[i]:
                et.SubElement(fi, "shippingCost").text = products[i]["FI shipping cost"]
            if "FI vat" in products[i]:
                et.SubElement(fi, "vat").text = products[i]["FI vat"]

    tree = et.ElementTree(marketplace)
    tree.write("price.xml", encoding = "utf-8", xml_declaration = True)

def create_media():
    with open(os.path.join(__location__, "media.csv"), encoding = 'utf-8-sig') as media:
        reader = csv.reader(media, delimiter=selected_delimiter)
        values = list(reader)
        keys = values.pop(0)

    products = []
    media_xsd = "https://schemas.cdon.com/product/4.0/4.12.0/examples/media.xml"

    for i in range(len(values)):
        products.append(dict(zip(keys, values[i])))

    marketplace = et.Element("marketplace",  xmlns=media_xsd)
    for i in range(len(products)):
        product = et.SubElement(marketplace, "product")
        et.SubElement(product, "id").text = products[i]["id"]
        images = et.SubElement(product, "images")
        et.SubElement(images, "main").text = products[i]["main image"]

        extra_images_list = products[i]["extra images"].split(";")
        for image in extra_images_list:
            et.SubElement(images, "extra").text = image

    tree = et.ElementTree(marketplace)
    tree.write("media.xml", encoding = "utf-8", xml_declaration = True)

    with open("media.xml", 'r+') as media_xml:
        for line in media_xml:
            line = line.replace("'", "\"")

def create_product():
    with open(os.path.join(__location__, "product.csv"), encoding = 'utf-8-sig') as product:
        reader = csv.reader(product, delimiter=selected_delimiter)
        values = list(reader)
        keys = values.pop(0)


if feed["Availability"]:
    create_availability()
elif feed["Price"]:
    create_price()
elif feed["Media"]:
    create_media()
elif feed["Product"]:
    create_product()
