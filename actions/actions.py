# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import re
import requests
import json

from urllib import request
from cgitb import text
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


def get_details(pincode):
    try:
        request = requests.get(f"https://api.postalpincode.in/pincode/{pincode}")
        response = request.json()
    except:
        response = None

    return response


class ActionGetCity(Action):
    def name(self):
        return "action_get_city"

    def run(self, dispatcher, tracker, domain):
        pincode = tracker.get_slot("pincode")
        response = get_details(pincode)
        if response:
            city = response[0]["PostOffice"][0]["Block"]
            dispatcher.utter_message(template="utter_city", city=city)
        else:
            dispatcher.utter_message(text="Pincode is not valid.")

        return []


class ActionGetState(Action):
    def name(self):
        return "action_get_state"

    def run(self, dispatcher, tracker, domain):
        pincode = tracker.get_slot("pincode")
        response = get_details(pincode)
        if response:
            state = response[0]["PostOffice"][0]["State"]
            dispatcher.utter_message(template="utter_state", state=state)
        else:
            dispatcher.utter_message(text="Pincode is not valid.")

        return []


class ActionGetDistrict(Action):
    def name(self):
        return "action_get_district"

    def run(self, dispatcher, tracker, domain):
        pincode = tracker.get_slot("pincode")
        response = get_details(pincode)
        if response:
            district = response[0]["PostOffice"][0]["District"]
            dispatcher.utter_message(template="utter_district", district=district)
        else:
            dispatcher.utter_message(text="Pincode is not valid.")

        return []
