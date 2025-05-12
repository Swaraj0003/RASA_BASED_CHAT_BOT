from typing import Dict, Text, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionSaveEnquiry(Action):
    def name(self) -> Text:
        return "action_save_enquiry"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        email = tracker.get_slot("email")
        enquiry = tracker.get_slot("enquiry")

        payload = {
            "name": name,
            "email": email,
            "enquiry": enquiry
        }

        # Call Flask API to save enquiry
        try:
            requests.post("http://localhost:5000/save-user", json=payload)
        except:
            dispatcher.utter_message("Error saving your enquiry.")

        return []
