import requests

def open_url():
    url = "https://www.google.com"
    
    response = requests.get(url)
    
    print("Status Code:", response.status_code)
    print("URL Opened Successfully")

if __name__ == "__main__":
    open_url()
