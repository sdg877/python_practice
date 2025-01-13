from dotenv import load_dotenv
import os
from requests import get
from pprint import PrettyPrinter

load_dotenv()

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")

printer = PrettyPrinter()

def get_currencies():
   
    endpoint = "/api/v/currencies"
    url = f"{base_url}{endpoint}?apiKey={api_key}"
    print(f"Request URL: {url}")  

    try:
        response = get(url)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")
        response.raise_for_status() 

        data = response.json()
        printer.pprint(data)
    except Exception as e:
        print(f"An error occurred: {e}")

get_currencies()
