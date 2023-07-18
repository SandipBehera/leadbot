# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
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

import logging
import sys
from typing import Any, Dict, List, Text

# from database_pg import storeData
import psycopg2
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('actions.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(stdout_handler)
logger.addHandler(file_handler)


class ActionSubmitInfo(Action):
    def name(self) -> Text:
        return "action_submit_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("user_name")
        email = tracker.get_slot("email")
        phone_number = tracker.get_slot("phone")

        logger.info("Name slot value:", name)
        logger.info("Email slot value:", email)
        logger.info("Phone slot value:", phone_number)
        # Perform actions with the collected information
        # For example, you can store it in a database or perform further processing
        # storeData(name, email, phone_number)/
        try:
            conn = psycopg2.connect(
                host="localhost",
                port="5432",
                dbname="your_database",
                user="your_username",
                password="your_password"
            )

            # Create a cursor object to execute SQL queries
            cur = conn.cursor()

            # Execute an SQL INSERT statement to store the data
            insert_query = "INSERT INTO public.chat_bot_lead(name, email, phone) VALUES (%s, %s, %s)"
            # Provide the actual data for insertion
            data = (name, email, phone_number)
            cur.execute(insert_query, data)
            logger.info("Data inserted successfully", data)

            # Commit the transaction and close the connection
            conn.commit()
        except Exception as e:
            logger.error(e)
        dispatcher.utter_message(
            text=f"Thank you, {name} for providing your information!")

        return [SlotSet("user_name", None), SlotSet("email", None), SlotSet("phone", None)]

# class ActionDefaultResponse(Action):
#     def name(self) -> Text:
#         return "action_default_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(response="utter_default_response")
#         return []
