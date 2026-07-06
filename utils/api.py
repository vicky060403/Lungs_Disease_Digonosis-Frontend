import requests

API_URL = "http://13.201.23.111/predict"


def predict_image(image_file):

    try:

        response = requests.post(
            API_URL,
            headers={
                "Content-Type": "image/jpeg"
            },
            data=image_file.getvalue(),
            timeout=60
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }