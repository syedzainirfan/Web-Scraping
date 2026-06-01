# from bs4 import BeautifulSoup
# # import psycopg 
# # from psycopg.rows import dict_row
# import time

# # while True:
# #     try:
# #         connection=psycopg.connect(host="localhost",dbname="scrapy",user="postgres",password="1234",row_factory=dict_row)
# #         cursor=connection.cursor()
# #         print("Database connected sucessfully")
# #         break
# #     except Exception as error:
# #         print("Database is not connected")
# #         print('error', error)
# #         time.sleep(2)

# with open("file.html","r")as f:
#     html_doc=f.read()
# soup = BeautifulSoup(html_doc, 'html.parser')
# Data=soup.select("div.contentWrapper")
# with open("file1.html", "w", encoding="utf-8") as f:
#     for x in Data:
#        f.write(str(x))



# url0="https://www.thomsonlocal.com/search/barbers/manchester-lancashire"
# titles=soup.select("h2.businessName")
# prices=soup.select("div.address")
# images=soup.select("div.phoneIcon sprite")

# for title, price, image in zip(titles, prices, images):
#     title_text = title.text.strip()
#     price_text = price.text.strip()
#     image_url = image.text.strip()

#     # cursor.execute(
#     #     "INSERT INTO public.beautifulsoup (title, price, url) VALUES (%s, %s, %s)",
#     #     (title_text, price_text, image_url)
#     # )

# # --- Commit and Close ---
# # connection.commit()
# # cursor.close()
# # connection.close()
# # print("Data inserted successfully!")


#     print(title.get_text(strip=True), "<-->", price.get_text(strip=True),"<-->",image_url.get_text(strip=True))


# # title=soup.select("h4.p4.biggertext")
# # for x in title:
# #     # print(x.get_text(strip=False), "-->", x.get("href"))
# #     print(x.get_text(strip=True))
# # price=soup.select("span.PriceFont")
# # for x in price:
# #     # print(x.get_text(strip=False), "-->", x.get("href"))
# #     print(x.get_text(strip=True))


#     # print(x)

from bs4 import BeautifulSoup

# Open and read the HTML file
with open("file1.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# Extracting business names, addresses, and phone numbers
business_names = soup.select("h2.businessName")
addresses = soup.select("div.address")
phone_numbers = soup.select("div.phoneCont")  # Select the div containing phone numbers


# Loop through and print or store the extracted data
for name, address , phone in zip(business_names, addresses, phone_numbers):
    name_text = name.get_text(strip=True)  # Get the business name text
    address_text = address.get_text(strip=True)  # Get the address text
    phone_text = phone.get_text(strip=True)

    # Print the extracted data
    print(f"Business Name: {name_text} <---> Address: {address_text} <---> Phone: {phone_text}")