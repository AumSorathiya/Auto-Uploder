# Telegram Bulk Photo Uploader with Unique Captions

This project lets you upload a large number of photos to a Telegram **channel**, where each photo has its **own unique caption**, using a single Python script.

It is designed for creators, marketers, and channel owners who need to post media in bulk without doing everything manually.

---

## Features

- Upload unlimited photos automatically
- Unique caption for every photo
- CSV-based caption mapping
- Works with public and private Telegram channels
- Safe posting with delay to avoid flood limits
- Simple, clean Python script

---

## Requirements

- Python 3.8 or higher
- Telegram bot token
- Telegram channel where the bot is an admin
- Internet connection

---

## Project Structure

```

telegram_uploader/
│
├── upload.py
├── captions.csv
└── images/
├── 1.jpg
├── 2.jpg
├── 3.jpg
└── ...

````

---

## Step 1: Create a Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Send `/start`
3. Send `/newbot`
4. Choose a name and username
5. Copy the **API Token**

Keep the token private.

---

## Step 2: Add Bot to Your Channel

1. Open your Telegram channel
2. Go to **Settings → Administrators**
3. Add your bot
4. Enable **Post Messages** permission
5. Save changes

---

## Step 3: Get Channel ID or Username

You can use either:

### Option A: Channel ID
- Forward a message from your channel to **@userinfobot**
- Copy the ID (starts with `-100`)

### Option B: Channel Username (recommended)
- Use the public username directly  
  Example: `@mychannelname`

---

## Step 4: Install Dependencies

Make sure Python is installed, then run:

```bash
python -m pip install requests
````

---

## Step 5: Prepare Captions File

Create `captions.csv` in this format:

```csv
filename,caption
1.jpg,This is caption for image 1
2.jpg,This is caption for image 2
3.jpg,This is caption for image 3
```

Notes:

* `filename` must match image names exactly
* Maximum caption length is 1024 characters
* Emojis, hashtags, and links are supported

---

## Step 6: Configure the Script

Open `upload.py` and edit:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHANNEL_ID = "@yourchannelusername"
```

You can also use the numeric channel ID instead of username.

---

## Step 7: Run the Script

From the project folder, run:

```bash
python upload.py
```

The script will upload each image with its caption automatically.

---

## Usage Notes

* A delay is added between uploads to prevent Telegram flood limits
* Missing images are skipped automatically
* Errors are printed in the terminal for easy debugging
* Works on Windows, macOS, and Linux

---

## Common Errors

### 404 Not Found

* Invalid or incorrect bot token

### 401 Unauthorized

* Bot is not admin in the channel
* Missing “Post Messages” permission
* Wrong channel ID or username

---

## Customization Ideas

* Add scheduling support
* Read captions from TXT instead of CSV
* Auto-generate captions using AI
* Resume uploads if script stops
* Upload albums instead of single photos

---

## Disclaimer

This project uses the official Telegram Bot API.
Use responsibly and follow Telegram’s terms of service.

---

## License

MIT License

```

---

If you want, I can:
- Optimize this README for **GitHub stars**
- Add screenshots section
- Add a **one-click setup** section
- Write a short project description for your GitHub profile

Just tell me what you want next.
```
