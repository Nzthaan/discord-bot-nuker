# Nukezinho Bot - Discord Channel Control

This is an **amateurish and poorly made** project, created by me to have **control over my Discord server**. The main objective of the bot is to **delete text and voice channels periodically**, ensuring that the server does not "crash" with too many unnecessary channels, keeping everything organized.

### **Objective**

I created this bot to manage my server more efficiently. It is basically to ensure that **text and voice channels are recreated automatically** at each time interval, without losing permissions and settings. The idea is to delete and recreate channels periodically, so that the server does not accumulate obsolete or useless channels.

### **Functionality (limited)**

- **Delete and recreate channels**: The bot can delete and recreate text and voice channels automatically at each configured interval (in seconds). The recreation tries to maintain the channels' settings and permissions. - **Changing the avatar**: You can set a custom avatar for the bot.
- **Connecting to a voice channel**: The bot automatically connects to a specific voice channel when started.

### **Important**

- **This project is not professional and has poorly structured code**. It was made as a quick and simple solution to a problem I faced on my server.
- **Do not use it in production** or on large servers unless you understand what you are doing. The idea is that it is useful for personal purposes and for simple channel control.

### **Installation**

1. **Clone or download** this repository.

2. Install the necessary dependencies with the command:
```
pip install discord.py
```

3. Create a config.json file with the bot settings (example below).

### Example config.json

```
{
"token": "YOUR_TOKEN_HERE",
"guild_id": "YOUR_SERVER_ID_HERE",
"channels": [
{
"name": "text-1",
"type": "text",
"category": "Text-Category",
"permissions": true
},
{
"name": "text-2",
"type": "text",
"category": "Text-Category",
"permissions": true
},
{
"name": "text-3",
"type": "text",
"category": "Text-Category",
"permissions": true
},
{
"name": "voice-1",
"type": "voice",
"category": "Voice-Category", "permissions": true
},
{
"name": "voice-2",
"type": "voice",
"category": "Voice-Category",
"permissions": true
},
{
"name": "voice-3",
"type": "voice",
"category": "Voice-Category",
"permissions": true
}
],
"interval": 3600,
"voice_channel_id": "1345647660954157118",
"avatar_path": "avatar.png",
"status": "online",
"bot_name": "Meu Bot Legal"
}
```

### How to run the bot?

1 Open the terminal or command prompt in the folder where the nukezinho.py script is located.

2. Run the command:

```
python nukezinho.py
```
3. The bot will start and start recreating the channels as configured in config.json.

## Warning
This project was made with little care and is not scalable or reliable for larger environments. Use it only if you need something simple and functional to control your own server. It is not recommended for large servers or for production.
