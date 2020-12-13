import requests
import os
import settings

# api-endpoint - credentials
kushki_card_url = 'https://api-uat.kushkipagos.com/card/v1/charges'
private_merchant_id = os.getenv("PRIVATE_MERCHANT_ID")
public_merchant_id = os.getenv("PUBLIC_MERCHANT_ID")

print(private_merchant_id, public_merchant_id)

def generate_request_info(token):
  # url - header - body
  body = {
    'token': token,
    'amount': {
      'subtotalIva': 0,
      'subtotalIva0': 10,
      'ice': 0,
      'iva': 0,
      'currency': 'USD'
    },
    'metadata': {
      'aditionalInfo': 'More Info'
    }
  }
  headers = {
    'Private-Merchant-Id': private_merchant_id,
    'Content-Type': 'application/json'
  }
  # charge to card
  return requests.post(kushki_card_url, json = body, headers = headers)
  

def charge(token):
  kushki_response = generate_request_info(token)
  data = kushki_response.json()

  print("data", data)

  if kushki_response.status_code == requests.codes.ok:
    ticket_number = data['ticketNumber']
    return kushki_response.status_code, ticket_number

  else:
    bad_response_code = data['code']
    bad_response_msg = data['message']
    return bad_response_code, bad_response_msg
