import unittest
import responses
from hackmd.client import Hackmd
from models.notes import NoteCreate, Note, NoteUpdate


class TestClient(unittest.TestCase):
    def setUp(self):
        self.tested = Hackmd(token='123456789abcdefghidhFeXkIQVjmuI6Oz123456789')
        self.token = '123456789abcdefghidhFeXkIQVjmuI6Oz123456789'
        self.uri = "https://api.hackmd.io/v1"

    @responses.activate
    def test_get_me(self):
        expect_response = {
            "id": "00c437e8-9d79-4200-997f-8e9384415a76",
            "name": "James",
            "email": None,
            "user_path": "AMQ36J15QgCZf46ThEFadg",
            "photo": "https://avatars.githubusercontent.com/u/26138990?s=96",
            "teams": [
                {
                    "id": "e9ed1dcd-830f-435c-9fe2-d53d5f191666",
                    "owner_id": "00c437e8-9d79-4200-997f-8e9384415a76",
                    "path": "CAT",
                    "name": "API client testing team",
                    "logo": "data:image/svg+xml;base64,PD94bWwgdmVyc2lv...dmc+",
                    "description": "This is for testing client API",
                    "visibility": "public",
                    "created_at": 1644371278721
                }
            ]
        }

        responses.add(
            method=responses.GET,
            url=f'{self.uri}/me',
            headers={'X-HackMD-API-Version': '1.0.0'},
            json=expect_response,
            status=200
        )
        result = self.tested.get_me()
        request = responses.calls[0]

        self.assertEqual('GET', request.request.method)
        self.assertEqual(result.dict(), expect_response)

    @responses.activate
    def test_get_notes(self):
        expect_response = [{
            "id": "ehgwc6a8RXSmcSaRwIQ2jw",
            "title": "Personal note title",
            "tags": ["personal", "test"],
            "created_at": 1643270371245,
            "publish_type": "view",
            "published_at": None,
            "permalink": None,
            "short_id": "SysJb0yAY",
            "last_changed_at": 1643270452413,
            "last_change_user": {
                "name": "James",
                "photo": "https://avatars.githubusercontent.com/u/26138990?s=96",
                "biography": None,
                "user_path": "AMQ36J15QgCZf46ThEFadg"
            },
            "user_path": "AMQ36J15QgCZf46ThEFadg",
            "team_path": None,
            "read_permission": "guest",
            "write_permission": "signed_in",
            "publish_link": "https://hackmd.io/@username/permalink"
        }]

        responses.add(
            method=responses.GET,
            url=f'{self.uri}/notes',
            headers={'X-HackMD-API-Version': '1.0.0'},
            json=expect_response,
            status=200
        )
        result = self.tested.get_notes()
        request = responses.calls[0]
        self.assertEqual('GET', request.request.method)
        self.assertEqual(result, expect_response)

    @responses.activate
    def test_get_note(self):
        expect_response = Note(**{
            "id": "ehgwc6a8RXSmcSaRwIQ2jw",
            "title": "Personal note title",
            "tags": [
                "Personal",
                "test"
            ],
            "created_at": 1643270371245,
            "publish_type": "view",
            "published_at": None,
            "permalink": None,
            "short_id": "SysJb0yAY",
            "content": "# Personal note title\n###### tags: `Personal` `test`",
            "last_changed_at": 1644461594806,
            "last_change_user": {
                "name": "James",
                "photo": "https://avatars.githubusercontent.com/u/26138990?s=96",
                "biography": None,
                "user_path": "AMQ36J15QgCZf46ThEFadg"
            },
            "user_path": "AMQ36J15QgCZf46ThEFadg",
            "team_path": None,
            "read_permission": "guest",
            "write_permission": "signed_in",
            "publish_link": "https://hackmd.io/@username/permalink"
        }).dict()

        responses.add(
            method=responses.GET,
            url=f'{self.uri}/note/ehgwc6a8RXSmcSaRwIQ2jw',
            headers={'X-HackMD-API-Version': '1.0.0'},
            json=expect_response,
            status=200
        )
        result = self.tested.get_note(note_id="ehgwc6a8RXSmcSaRwIQ2jw")
        request = responses.calls[0]
        self.assertEqual('GET', request.request.method)
        self.assertEqual(result, expect_response)

    @responses.activate
    def test_create_note(self):
        body = {
            "title": "New note",
            "content": "",
            "read_permission": "owner",
            "write_permission": "owner",
            "comment_permission": "everyone"
        }
        expect_response = Note(**{
            "id": "ehgwc6a8RXSmcSaRwIQ2jw",
            "title": "New note",
            "tags": [
                "Personal",
                "test"
            ],
            "created_at": 1643270371245,
            "publish_type": "view",
            "published_at": None,
            "permalink": None,
            "short_id": "SysJb0yAY",
            "content": "# `test`",
            "last_changed_at": 1644461594806,
            "last_change_user": {
                "name": "James",
                "photo": "https://avatars.githubusercontent.com/u/26138990?s=96",
                "biography": None,
                "user_path": "AMQ36J15QgCZf46ThEFadg"
            },
            "user_path": "AMQ36J15QgCZf46ThEFadg",
            "team_path": None,
            "read_permission": "owner",
            "write_permission": "owner",
            "comment_permission": "everyone",
            "publish_link": "https://hackmd.io/@username/permalink"
        }).dict()

        responses.add(
            method=responses.POST,
            url=f'{self.uri}/notes',
            json=expect_response,
            headers={'X-HackMD-API-Version': '1.0.0'},
            status=201
        )
        result = self.tested.create_note(body=NoteCreate(**body))
        request = responses.calls[0]
        self.assertEqual('POST', request.request.method)
        self.assertEqual(result, expect_response)

    @responses.activate
    def test_update_note(self):
        body = {
            "content": "# Updated personal note",
            "read_permission": "signed_in",
            "write_permission": "owner",
            "permalink": "note-permalink"
        }
        expect_response = Note(**{
            "id": "ehgwc6a8RXSmcSaRwIQ2jw",
            "title": "New note",
            "tags": [],
            "created_at": 1643270371245,
            "publish_type": "view",
            "published_at": None,
            "permalink": "note-permalink",
            "short_id": "SysJb0yAY",
            "content": "# Updated personal note",
            "last_changed_at": 1644461594806,
            "last_change_user": {
                "name": "James",
                "photo": "https://avatars.githubusercontent.com/u/26138990?s=96",
                "biography": None,
                "user_path": "AMQ36J15QgCZf46ThEFadg"
            },
            "user_path": "AMQ36J15QgCZf46ThEFadg",
            "team_path": None,
            "read_permission": "signed_in",
            "write_permission": "owner",
            "comment_permission": "everyone",
            "publish_link": "https://hackmd.io/@username/permalink"
        }).dict()

        responses.add(
            method=responses.PATCH,
            url=f'{self.uri}/notes/ehgwc6a8RXSmcSaRwIQ2jw',
            headers={'X-HackMD-API-Version': '1.0.0'},
            json=expect_response,
            status=202
        )
        result = self.tested.update_note(note_id="ehgwc6a8RXSmcSaRwIQ2jw", body=NoteUpdate(**body))
        request = responses.calls[0]
        self.assertEqual('PATCH', request.request.method)
        self.assertEqual(result, expect_response)
