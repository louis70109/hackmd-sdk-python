import json
import os
from typing import List, Dict, Optional
from urllib.parse import urlencode

import requests

from models.notes import Note, Notes, NoteCreate, NoteUpdate
from models.users import Me


class Hackmd:
    TOKEN: str = os.environ.get('HACKMD_TOKEN')

    def __init__(self, token=None, uri=None, *args, **kwargs):
        super(Hackmd, self).__init__(*args, **kwargs)

        self.token: str = token or self.TOKEN
        self.uri: str = uri or "https://api.hackmd.io/v1"

    def __repr__(self):
        return f"<Hackmd token={self.token}, uri={self.uri}>"

    def get_me(self):
        # https://hackmd.io/@hackmd-api/developer-portal/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fuser-api
        response = self._get(url=f'{self.uri}/me')
        return Me(**response.json())

    def get_notes(self):
        # https://hackmd.io/@hackmd-api/developer-portal/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fuser-notes-api
        response = self._get(url=f"{self.uri}/notes")
        res: List[Dict[str, any]] = response.json()
        result: List[Notes] = [Notes(**note) for note in res]
        return result

    def get_note(self, note_id: str):
        # https://reurl.cc/oZ1YXQ
        response = self._get(url=f"{self.uri}/note/{note_id}")
        return Note(**response.json())

    def create_note(self, body: Optional[NoteCreate] = None):
        # https://reurl.cc/eW3kaM
        response = self._post(url=f"{self.uri}/notes", data=body.dict())
        return Note(**response.json())

    def update_note(self, note_id: str, body: Optional[NoteUpdate] = None):
        # https://reurl.cc/MX0zDW
        response = self._patch(url=f"{self.uri}/notes/{note_id}", data=body.dict())
        return Note(**response.json())

    def delete_note(self, note_id: str):
        # https://reurl.cc/VRDWeQ
        response = self._delete(url=f"{self.uri}/notes/{note_id}")
        return json.dumps(response.json())

    def get_read_notes_history(self):
        # https://reurl.cc/EXrQDv
        response = self._get(url=f"{self.uri}/history")
        res: List[Dict[str, any]] = response.json()
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

    def _post(self, url, data=None, headers=None, timeout=None):
        try:
            header = {'Authorization': f'Bearer {self.token}'}
            response = requests.post(
                url, headers=header, data=data, timeout=timeout)
            self.__check_http_response_status(response)
            return response
        except requests.exceptions.Timeout:
            raise RuntimeError(
                'Request time {timeout} timeout. Please check internet.'.format(timeout=timeout)
            )
        except requests.exceptions.TooManyRedirects:
            raise RuntimeError('URL {url} was bad, please try a different one.'.format(url=url))

    def _patch(self, url, data=None, headers=None, timeout=None):
        try:
            header = {'Authorization': f'Bearer {self.token}'}
            response = requests.patch(
                url, headers=header, data=data, timeout=timeout)
            self.__check_http_response_status(response)
            return response
        except requests.exceptions.Timeout:
            raise RuntimeError(
                'Request time {timeout} timeout. Please check internet.'.format(timeout=timeout)
            )
        except requests.exceptions.TooManyRedirects:
            raise RuntimeError('URL {url} was bad, please try a different one.'.format(url=url))

    def _delete(self, url, headers=None, timeout=None):
        try:
            header = {'Authorization': f'Bearer {self.token}'}
            response = requests.delete(
                url, headers=header, timeout=timeout)
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
        if 200 <= response.status_code < 300 and \
                response.headers['X-HackMD-API-Version'] == '1.0.0':
            pass
        else:
            raise ValueError(response.json())
