# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from datetime import date, datetime
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet, EventType, UserUtteranceReverted
from . import (
    EMAIL,
    FIRST_NAME,
    BIRTH_DT,
    PHONE,
    LINKEDIN,
    WORK,
    WORK_AREA,
    LOCATION,
)


class ActionGreetUser(Action):
    """Greets the user with/without privacy policy"""

    def name(self) -> Text:
        return "action_greet_user"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        intent = tracker.latest_message["intent"].get("name")
        name_entity = next(tracker.get_latest_entity_values("name"), None)

        if intent == "greet" or (intent == "enter_data" and name_entity):
            nm = tracker.get_slot("name") or None
            if name_entity:
                if nm and nm == name_entity:
                    dispatcher.utter_message(
                        response="utter_already_knew",
                    )
                else:
                    dispatcher.utter_message(
                        response="utter_greet_name",
                        name=name_entity,
                    )
                return [SlotSet(key="name", value=name_entity)]
            elif nm:
                dispatcher.utter_message(
                    response="utter_greet_name",
                    name=nm,
                )
            else:
                dispatcher.utter_message(response="utter_greet")
            return []


class ActionBye(Action):
    """Greets the user with/without privacy policy"""

    def name(self) -> Text:
        return "action_bye"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        user_name = tracker.get_slot("name") or None
        if user_name:
            dispatcher.utter_message(
                response="utter_bye_name", name=user_name
            )
        else:
            dispatcher.utter_message(response="utter_bye")
        return []


class ActionGetName(Action):
    def name(self) -> Text:
        return "action_get_name"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        dispatcher.utter_message(
            response="utter_faq_name",
            name=str(FIRST_NAME),
        )
        return []


class ActionGetEmail(Action):
    def name(self) -> Text:
        return "action_get_email"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        # intent = tracker.latest_message["intent"].get("name")
        dispatcher.utter_message(
            response="utter_faq_email",
            name=str(FIRST_NAME),
            email=str(EMAIL),
        )
        return []


class ActionGetWork(Action):
    def name(self) -> Text:
        return "action_get_work"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        # intent = tracker.latest_message["intent"].get("name")
        dispatcher.utter_message(
            response="utter_faq_work",
            work_area=str(WORK_AREA),
            work=str(WORK),
        )
        return []


class ActionGetAge(Action):
    def name(self) -> Text:
        return "action_get_age"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        # intent = tracker.latest_message["intent"].get("name")

        birth_dt = datetime.strptime(BIRTH_DT, "%d/%m/%Y").date()
        today = date.today()
        one_or_zero = (today.month, today.day) < (
            birth_dt.month,
            birth_dt.day,
        )
        year_difference = today.year - birth_dt.year
        age = year_difference - one_or_zero

        # age = 1
        dispatcher.utter_message(response="utter_faq_age", age=str(age))
        return []


class ActionGetPhone(Action):
    def name(self) -> Text:
        return "action_get_phone"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        # intent = tracker.latest_message["intent"].get("name")
        dispatcher.utter_message(
            response="utter_faq_phone", phone=str(PHONE)
        )
        return []


class ActionGetLinks(Action):
    def name(self) -> Text:
        return "action_get_linkedin"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        # intent = tracker.latest_message["intent"].get("name")
        dispatcher.utter_message(
            response="utter_faq_linkedin", links=str(LINKEDIN)
        )
        return []


class ActionGetLocation(Action):
    def name(self) -> Text:
        return "action_get_location"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        # intent = tracker.latest_message["intent"].get("name")
        dispatcher.utter_message(
            response="utter_faq_location", location=str(LOCATION)
        )
        return []


class ActionGetTime(Action):
    def name(self) -> Text:
        return "action_get_time"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        # intent = tracker.latest_message["intent"].get("name")
        now = datetime.now().time()
        dispatcher.utter_message(
            response="utter_chitchat_time", time=str(now)
        )
        return []


class ActionWhatIsMyName(Action):
    def name(self) -> Text:
        return "action_whatismyname"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        nm = tracker.get_slot("name") or None
        if nm:
            dispatcher.utter_message(
                response="utter_chitchat_whatismyname_name",
                name=nm,
            )
        else:
            dispatcher.utter_message(
                response="utter_chitchat_whatismyname_noname"
            )
        return []


class ActionWhoAmI(Action):
    def name(self) -> Text:
        return "action_whoami"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        nm = tracker.get_slot("name") or None
        if nm:
            dispatcher.utter_message(
                response="utter_chitchat_whoami_name",
                name=nm,
            )
        else:
            dispatcher.utter_message(
                response="utter_chitchat_whoami_noname"
            )
        return []


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:

        dispatcher.utter_message(template="utter_default")
        return [UserUtteranceReverted()]
