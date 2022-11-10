import os
from typing import List

import requests

from models.notes import Note, Notes
from models.users import Me


class Hackmd:
    TOKEN = os.environ.get('HACKMD_TOKEN')
    
    def __init__(self,
                 token=None,
                 uri=None,
                 *args, **kwargs):
        super(Hackmd, self).__init__(*args, **kwargs)
        
        self.token: str = token or self.TOKEN
        self.uri: str = uri or "https://api.hackmd.io/v1"

    def __repr__(self):
        return f"<Lotify token={self.token}, uri={self.uri}>"

    def get_me(self):
        # https://hackmd.io/@hackmd-api/developer-portal/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fuser-api
        response = self._get(url=f'{self.uri}/me')
        return Me(**response.json()).dict()

    def get_notes(self):
        # https://hackmd.io/@hackmd-api/developer-portal/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fuser-notes-api
        response = self._get(url=f"{self.uri}/notes")
        res = response.json()
        result: List[Notes] = [Notes(**note) for note in res]
        return result

    def _get(self, url, headers=None, timeout=1):
        try:
            header = {'Authorization': f'Bearer {self.token}'}
            response = requests.get(url, headers=header, timeout=timeout)
            self.__check_http_response_status(response)
            return response
        except requests.exceptions.Timeout:
            raise RuntimeError(
                'Request time {timeout} timeout. Please check internet.'.format(timeout=timeout)
            )
        except requests.exceptions.TooManyRedirects:
            raise RuntimeError('URL {url} was bad, please try a different one.'.format(url=url))

    def _post(self, url, data=None, headers=None, files=None, timeout=None):
        try:
            header = {'Authorization': f'Bearer {self.token}', **headers}
            response = requests.post(
                url, headers=header, data=data, files=files, timeout=timeout)
            self.__check_http_response_status(response)
            return response
        except requests.exceptions.Timeout:
            raise RuntimeError(
                'Request time {timeout} timeout. Please check internet.'.format(timeout=timeout)
            )
        except requests.exceptions.TooManyRedirects:
            raise RuntimeError('URL {url} was bad, please try a different one.'.format(url=url))

    @staticmethod
    def __check_http_response_status(response):
        if 200 <= response.status_code < 300:
            pass
        else:
            raise ValueError(response.json())
