import requests

if __name__ == "__main__":
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    json_response = response.json()
    url_image: str = json_response[0]["url"]
    data = requests.get(url_image)
    file_name = url_image.split("/")[4]
    with open("cats/"+file_name, "wb") as local_file:
        local_file.write(data.content)