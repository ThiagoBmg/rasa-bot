# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from services.github import Github

from config import GITHUB_USERNAME, FIRST_NAME


class ActionGitHub(Action):

    def name(self) -> Text:
        return "action_github"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # buscando os dados no github
        github = Github()
        repositores = github.get_all_repositores(user=GITHUB_USERNAME)

        # criando texto de resposta
        text = f'O {FIRST_NAME} tem um total de {len(repositores)} repositórios... '

        # enviando resposta para o bot
        dispatcher.utter_message(text=text)

        return []
