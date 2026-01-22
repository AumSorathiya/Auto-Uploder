import csv
import time
import requests
import os

BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"
CHANNEL_ID = "-100XXXXXXXXXX"
IMAGES_FOLDER = "images"

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

with open("captions.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        image_path = os.path.join(IMAGES_FOLDER, row["filename"])
        caption = row["caption"]

        if not os.path.exists(image_path):
            print(f"❌ Missing file: {row['filename']}")
            continue

        with open(image_path, "rb") as img:
            response = requests.post(
                API_URL,
                data={
                    "chat_id": CHANNEL_ID,
                    "caption": caption,
                    "parse_mode": "HTML"
                },
                files={
                    "photo": img
                }
            )

        if response.status_code == 200:
            print(f"✅ Uploaded: {row['filename']}")
        else:
            print(f"❌ Failed: {row['filename']} → {response.text}")


        time.sleep(1.2)  # IMPORTANT: avoid flood limits
