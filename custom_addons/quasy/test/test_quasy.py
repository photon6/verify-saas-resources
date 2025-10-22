import requests

url = "https://photon6-propensic-main-24768631.dev.odoo.com/odoo/quasy/anonymize"
payload = {"query": "John Smith from New York wants to transfer $10,000 to his account."}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
#print(response.json())