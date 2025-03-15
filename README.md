# Discord-BOT-for-automatic-message

# **Step 1: Create a Discord Bot**
💡 The bot will send messages to student channels based on the list you enter in a Google Sheet or CSV file.

1.1. Create a bot on the Discord Developer Portal
Go to the Discord Developer Portal.
Click "New Application" → Name the bot (e.g., AttendanceBot).
Select the "Bot" tab (on the left) → Click "Add Bot" → Confirm with "Yes, do it!".
Enable MESSAGE CONTENT INTENT (required for the bot to send messages):
In the Bot tab, scroll down to "Privileged Gateway Intents".
Enable "MESSAGE CONTENT INTENT".
Copy the TOKEN for later use.

1.2. Invite the bot to your Discord server
Go to OAuth2 > URL Generator.
Select the Bot scope.
In Bot Permissions, check:
✅ Send Messages
✅ Read Messages
Copy the generated link → Open it in a browser and invite the bot to your server.
Verify the bot has joined by checking the member list in Discord.

**Step 2: Get Channel IDs**
💡 The bot needs each channel's ID to send messages to the correct place.

Update the list in your file

**Step 3: Install Software to Run the Bot**
📌 You need to install Python to run the bot, but only once.

**3.1 Install Python**
You need to install Python to run it as it is Python-powered

**3.2 Install required libraries**
discord: Connects the bot to Discord.
pandas: Reads data from CSV or Google Sheets.
gspread, oauth2client: Accesses Google Sheets data.

**Step 4: Run the Bot to Send Bulk Messages**
Save the bot’s code as bot.py and run it
