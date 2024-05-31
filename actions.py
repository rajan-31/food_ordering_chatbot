# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class DisplayMenuItems(Action):

    def name(self) -> Text:
        return "display_menu_items"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conn = sqlite3.connect('food.db')
        user_message = str((tracker.latest_message)['text'])

        print("User message : ", user_message)
        if "7 plates" in user_message:
            exe_str = "Select food, price from food_items where restaurant_name is '{0}'".format('7 plates')
        elif 'Anugraha veg' in user_message:
            exe_str = "Select food, price from food_items where restaurant_name is '{0}'".format('Anugraha Veg')
        elif 'Leon Grill' in user_message:
            exe_str = "Select food, price from food_items where restaurant_name is '{0}'".format('Leon Grill')
        elif 'Brahmins Thatte Idli' in user_message:
            exe_str = "Select food, price from food_items where restaurant_name is '{0}'".format('Brahmins Thatte Idli')
        elif 'Delhi Xpress' in user_message:
            exe_str = "Select food, price from food_items where restaurant_name is '{0}'".format(
                'Delhi Xpress')
        elif 'KFC' in user_message:
            exe_str = "Select food, price from food_items where restaurant_name is '{0}'".format('KFC')

        content = conn.execute(exe_str)
        content_text = ''
        for index, value in enumerate(content):
            content_text += str(index + 1) + ") " + str(value[0]) + "  ----  " + str(value[1]) + "/-\n"

        content_text += "Enter item numbers (eg : 1,2,4)"
        dispatcher.utter_message(text=content_text)

        return []


class UserOrderReceived(Action):

    def name(self) -> Text:
        return "user_order_received"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = sqlite3.connect('food.db')
        user_message = str((tracker.latest_message)['text'])

        messages = []

        for event in (list(tracker.events))[:15]:
            if event.get("event") == "user":
                messages.append(event.get("text"))

        user_message = messages[-1]
        print("Messages : ", messages)
        if "7 plates" in user_message:
            exe_str = "Select food, price from food_items where restaurant_name is '{0}'".format('7 plates')
        elif 'Anugraha veg' in user_message:
            exe_str = "Select food, price from food_items where restaurant_name is '{0}'".format('Anugraha Veg')
        elif 'Leon Grill' in user_message:
            exe_str = "Select food, price from food_items where restaurant_name is '{0}'".format('Leon Grill')
        elif 'Brahmins Thatte Idli' in user_message:
            exe_str = "Select food, price from food_items where restaurant_name is '{0}'".format('Brahmins Thatte Idli')
        elif 'Delhi Xpress' in user_message:
            exe_str = "Select food, price from food_items where restaurant_name is '{0}'".format(
                'Delhi Xpress')
        elif 'KFC' in user_message:
            exe_str = "Select food, price from food_items where restaurant_name is '{0}'".format('KFC')

        content = conn.execute(exe_str)

        user_input = str((tracker.latest_message)['text'])
        user_input = user_input.replace(" ", "")
        # user_input = user_input.split(',')
        user_input = [int(n) for n in user_input.split(',')]
        print("user_input : ", user_input)

        total = 0
        content_text = ''
        for index, value in enumerate(content):
            if index + 1 in user_input:
                total += value[1]

        content_text = "Your order has been received and your total order is " + str(total)
        dispatcher.utter_message(text=content_text)

        return []


class RestaurantNotified(Action):

    def name(self) -> Text:
        return "restaurant_notified"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        content = "The order has been taken and the respective restaurent will be notified"
        dispatcher.utter_message(text=content)

        return []
