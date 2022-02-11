# Basic Chat Bot Using RASA (v2.8) [Pincode Bot]

This is a chat bot created using [RASA Open Source](https://rasa.com/docs/rasa/2.x/), version 2. Current versioning for RASA is [version 3](https://rasa.com/docs/rasa/). This bot has the functionality to determine the `city`,`state` & `district` using `pincode` that would be entered by the user. 

This bot uses the [Postal Pincode API](http://www.postalpincode.in/Api-Details) to get the required data & hence output the details.

To try out this bot, do the following steps:
1. Clone this repository, 
    `git clone https://github.com/DhruvSondhi/rasa-basic-chat-bot.git`
2. Create a virtual environment for `Python` (majorly using v 3.7 or 3.8).
3. Use the given `requirements.txt` to install the required dependencies, after activating your virtual env,
    `python3 -m pip install -r requirements.txt`
4. Use `rasa shell` to interact with the bot

For further details about working of the chat bot & other functionality, please checkout the [RASA Documentation](https://rasa.com/docs/rasa/).
