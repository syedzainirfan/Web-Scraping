from bs4 import BeautifulSoup

# Open and read the HTML file
with open("file1.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# Extracting business names, addresses, and phone numbers using the right tags.
business_names = soup.select("h2.businessName")
addresses = soup.select("div.address")
phone_numbers = soup.select("div.phoneCont")  # Select the div containing phone numbers


# Loop through and print or store the extracted data
for name, address, phone in zip(business_names, addresses, phone_numbers):
    name_text = name.get_text(strip=True)  # Get the business name text
    address_text = address.get_text(strip=True)  # Get the address text
    phone_text = phone.get_text(strip=True)

    # Print the extracted data
    print(f"Business Name: {name_text} <---> Address: {address_text} <---> Phone: {phone_text}")
