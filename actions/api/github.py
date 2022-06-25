import requests


class Github:
    def __init__(self) -> None:
        self.base_url = "https://api.github.com"
        self.session = requests.Session()

    def get_languages_list(self, repositores: dict) -> dict:
        resp = set([x.get("language") for x in repositores if x.get("language")])
        return resp

    def get_all_repositores(self, user) -> list:
        url = self.base_url + f"/users/{user}/repos"
        resp = self.session.get(url=url)

        if resp.status_code != 200:
            raise f"Erro ao buscar dados do github :( {resp}"

        resp = resp.json()

        return resp
