import requests

def create_bitly_link(long_url):
    access_token = "YOUR_BITLY_ACCESS_TOKEN"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    payload = {
        "long_url": long_url,
    }
    response = requests.post("https://api-ssl.bitly.com/v4/shorten", headers=headers, json=payload)
    if response.status_code == 201:
        return response.json()["link"]
    else:
        return None

if __name__ == "__main__":
    long_url = "http://<your_server_public_ip>:5000"  # Replace with your server's public URL
    short_url = create_bitly_link(long_url)
    print(f"Short URL: {short_url}")
