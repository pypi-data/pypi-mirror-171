# Qotto Auth Client

The python package `qotto-auth-client` is a client for the API `qotto-auth` which will soon be open sourced.

It allows to manage a scoped permission and authentication system.

More information coming soon...

## Quickstart

The `QottoAuthApi` class allows to interact with a `qotto-auth` GraphQL server.

```python
from qottoauth import QottoAuthApi

# qotto-auth server running
api = QottoAuthApi('http://localhost:3000')
```

You can the use (and extends if necessary) the `QottoAuthService` class.

```python
from qottoauth import QottoAuthService

service = QottoAuthService(api)
```

### Testing

To allow offline testing, you can plug a `QottoAuthTestApi` instance to same service.

```python
from qottoauth import QottoAuthTestApi, QottoAuthService

test_api = QottoAuthTestApi()
service = QottoAuthService(test_api)
```

You can then test your application, as if a `qotto-auth` server was running.

```python
# create a user
user = service.create_user(name='John Doe', is_superuser=True)

# ...
``` 
