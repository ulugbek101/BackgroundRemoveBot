import requests
import logging


url = "https://background-removal.p.rapidapi.com/remove"

headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "61c70485b7msh59d85911958a368p1d646djsn4eaeaef4ef3d",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}


async def remove_background(img_url):
    payload = f"image_url={img_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    logging.info(response.json()["response"]["image_url"])
    return response.json()["response"]["image_url"]