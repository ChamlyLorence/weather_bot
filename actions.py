# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from sqlalchemy.types import Text

class ActionHelp(Action):

    def name(self):
        return "action_help"

    def run(self, dispatcher,tracker,domain):
        name = tracker.get_slot('name')
        dispatcher.utter_message(text="What can i do for you {}".format(name))

        return []

class ActionSendWeather(Action):

    def name(self):
        return "action_send_weather"

    def run(self, dispatcher,tracker,domain):
        locaton = tracker.get_slot('location')
        dispatcher.utter_message(text="weather in  {} good".format(locaton))

        return []
