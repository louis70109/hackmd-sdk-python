# HackMD Python SDK

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/louis70109/line-notify#contributing)
[![Python Version](https://img.shields.io/badge/Python-%3E%3D%203.5-blue.svg)](https://badge.fury.io/py/lotify)

It is a Type-safe Python SDK that can let HackMD development fastly.

# Usage

```shell
pip install hackmd

# or

python setup.py install
```

# Methods

> [Authentication](https://hackmd.io/@hackmd-api/developer-portal/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fapi-authorization): X-HackMD-API-Version: 1.0.0 
## [User](https://hackmd.io/@hackmd-api/developer-portal/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fuser-api)

- get_me()
    - return: Me()
  
## [User Note](https://hackmd.io/@hackmd-api/developer-portal/https%3A%2F%2Fhackmd.io%2F%40hackmd-api%2Fuser-notes-api)

- get_notes()
    - return: List[Notes]
- get_note(note_id=note_id)
    - return: Note()
- create_note(body=NoteCreate)
    - return: Note()
- update_note(note_id=note_id, body=NoteUpdate)
    - return: Note()
- delete_note(note_id=note_id)
    - return: ''
- get_read_notes_history()
    - return: List[Notes]

# Development

```shell
git clone
cd hackmd-sdk-python/
pythom -m pytest tests/
```

# License

[MIT](https://github.com/louis70109/hackmd-sdk-python/blob/master/LICENSE)
