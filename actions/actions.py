# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import webbrowser
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionPlanDuration(Action):

    def name(self) -> Text:
        return "action_plan_duration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        type_of_plan = tracker.get_slot("duration")
        monthly_poss = ["monthly", "mnthly", "month", "mon", "MONTHLY", "MNTHLY", "MONTH", "MON", "Monthly", "Mon", "Month", "Mnthly"]
        yearly_poss = ["yearly", "yrly", "year", "yr", "YEARLY", "YRLY", "YEAR", "YR", "Yearly", "Yr", "Year", "Yer", "Yrly"]


        if type_of_plan in monthly_poss:

            test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                    "title": "Basic Plan",
                    "subtitle": "Best for collecting emails",
                    "image_url": "https://media.istockphoto.com/photos/two-bubble-talk-or-comment-sign-symbol-on-blue-background-picture-id1304849823?b=1&k=20&m=1304849823&s=170667a&w=0&h=WyxXj3Pj8gAD-9UP3bijhKuKFW2_1kCamAa-XbJrpxQ=",
                    "buttons": [
                        {
                            "title": "Collects Emails ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "Collects Queries ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "200 User messages per month",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                        "title": "$ 75 per month",
                        "url": "http://link.url",
                        "type": "web_url"
                        },
                        {
                            "title": "See All Features",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                    ]
                },
               {
                    "title": "Growth Plan",
                    "subtitle": "Best for collecting emails",
                    "image_url": "https://images.unsplash.com/photo-1543286386-2e659306cd6c?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fGdyb3d0aHxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
                    "buttons": [
                        {
                            "title": "Collects Emails ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "Ecommerce ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "3000 User messages per month",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                        "title": "$ 599 per month",
                        "url": "http://link.url",
                        "type": "web_url"
                        },
                        {
                            "title": "See All Features",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                    ]
                },
                {
                    "title": "Startup Plan",
                    "subtitle": "Best for collecting emails",
                    "image_url": "https://images.unsplash.com/photo-1512758017271-d7b84c2113f1?ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8c3RhcnR1cHxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
                    "buttons": [
                        {
                            "title": "Collects Emails ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "Ecommerce ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "12,000 User messages per month",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                        "title": "$ 1010 per month",
                        "url": "http://link.url",
                        "type": "web_url"
                        },
                        {
                            "title": "See All Features",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                    ]
                },
{
                    "title": "Scaling Plan",
                    "subtitle": "Best for collecting emails",
                    "image_url": "https://images.unsplash.com/photo-1612012060851-20f943c02d3d?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8c2NhbGV8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
                    "buttons": [
                        {
                            "title": "Collects Emails ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "Unlimited Ecommerce ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "25,000 User messages  User messages per month",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                        "title": "$ 1299 per month",
                        "url": "http://link.url",
                        "type": "web_url"
                        },
                        {
                            "title": "See All Features",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                    ]
                }, 
                 ]
                }
               }

            dispatcher.utter_message(text="Here are the features and prices of your selected choice!", attachment=test_carousel)
        
        elif type_of_plan in yearly_poss:
            
            buttons=[
                 {"payload":'/three_months_plan',"title":"Show me discounted plans 👀"},
                 {"payload":'/contact_us',"title":"Contact Us"},
            ]
            dispatcher.utter_message(text="We dont provide yearly plans 👀. But we have the 3 months combo with great discounts!", buttons=buttons)

        else:

            dispatcher.utter_message(text="Difficult to understand :( Are you looking for something that is mentioned below?")


        return []

class ActionThreeMonths(Action):

    def name(self) -> Text:
        return "action_three_months"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        three_months_courseal = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                    "title": "Basic Plan",
                    "subtitle": "Best for collecting emails",
                    "image_url": "https://media.istockphoto.com/photos/two-bubble-talk-or-comment-sign-symbol-on-blue-background-picture-id1304849823?b=1&k=20&m=1304849823&s=170667a&w=0&h=WyxXj3Pj8gAD-9UP3bijhKuKFW2_1kCamAa-XbJrpxQ=",
                    "buttons": [
                        {
                            "title": "Collects Emails ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "Collects Queries ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "200 User messages per month",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                        "title": "$ 65 per month",
                        "url": "http://link.url",
                        "type": "web_url"
                        },
                        {
                            "title": "See All Features",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                    ]
                },
               {
                    "title": "Growth Plan",
                    "subtitle": "Best for collecting emails",
                    "image_url": "https://images.unsplash.com/photo-1543286386-2e659306cd6c?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fGdyb3d0aHxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
                    "buttons": [
                        {
                            "title": "Collects Emails ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "Ecommerce ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "3000 User messages per month",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                        "title": "$ 570 per month",
                        "url": "http://link.url",
                        "type": "web_url"
                        },
                        {
                            "title": "See All Features",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                    ]
                },
                {
                    "title": "Startup Plan",
                    "subtitle": "Best for collecting emails",
                    "image_url": "https://images.unsplash.com/photo-1512758017271-d7b84c2113f1?ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8c3RhcnR1cHxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
                    "buttons": [
                        {
                            "title": "Collects Emails ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "Ecommerce ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "12,000 User messages per month",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                        "title": "$ 975 per month",
                        "url": "http://link.url",
                        "type": "web_url"
                        },
                        {
                            "title": "See All Features",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                    ]
                },
                {
                    "title": "Scaling Plan",
                    "subtitle": "Best for collecting emails",
                    "image_url": "https://images.unsplash.com/photo-1612012060851-20f943c02d3d?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8c2NhbGV8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
                    "buttons": [
                        {
                            "title": "Collects Emails ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "Unlimited Ecommerce ✅",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                            "title": "25,000 User messages  User messages per month",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                        {
                        "title": "$ 1259 per month",
                        "url": "http://link.url",
                        "type": "web_url"
                        },
                        {
                            "title": "See All Features",
                            "type": "web_url",
                            "url": "https://currsive.com"
                        },
                    ]
                }, 
                 ]
                }
               }

        dispatcher.utter_message(text="Discount open's for 3 months! Only for our lovely customers 😃", attachment=three_months_courseal)

        return []


class ActionCalendlyRedirect(Action):

    def name(self) -> Text:
        return "action_calendly"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email = tracker.get_slot("email")

        url = f"https://calendly.com/suyog_demo/discover-growth?email={email}"

        webbrowser.open(url)

        return []