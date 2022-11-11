import unittest
import responses
from hackmd.client import Hackmd


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
                    "logo": "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+PHN2ZyB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgaGVpZ2h0PSI5NiIgd2lkdGg9Ijk2IiB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCA5NiA5NiI+PGc+PHJlY3Qgd2lkdGg9Ijk2IiBoZWlnaHQ9Ijk2IiBmaWxsPSIjZDg0ZGUyIiAvPjx0ZXh0IGZvbnQtc2l6ZT0iNjRweCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmZmZmZmYiPjx0c3BhbiB4PSI0OCIgeT0iNzIiIHN0cm9rZS13aWR0aD0iLjI2NDU4cHgiIGZpbGw9IiNmZmZmZmYiPkM8L3RzcGFuPjwvdGV4dD48L2c+PC9zdmc+",
                    "description": "This is for testing client API",
                    "visibility": "public",
                    "created_at": 1644371278721
                }
            ]
        }

        responses.add(
            responses.GET,
            f'{self.uri}/me',
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
            responses.GET,
            f'{self.uri}/notes',
            json=expect_response,
            status=200
        )
        result = self.tested.get_notes()
        request = responses.calls[0]
        self.assertEqual('GET', request.request.method)
        self.assertEqual(result, expect_response)

    @responses.activate
    def test_get_note(self):
        expect_response = {
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
        }

        responses.add(
            responses.GET,
            f'{self.uri}/note/ehgwc6a8RXSmcSaRwIQ2jw',
            json=expect_response,
            status=200
        )
        result = self.tested.get_note(note_id="ehgwc6a8RXSmcSaRwIQ2jw")
        request = responses.calls[0]
        self.assertEqual('GET', request.request.method)
        self.assertEqual(result, expect_response)