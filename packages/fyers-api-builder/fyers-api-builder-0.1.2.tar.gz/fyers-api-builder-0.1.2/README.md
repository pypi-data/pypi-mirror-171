## Fyers Token Generator

```
from fyers_api_builder import FyersApiBuilder
```

```
config = {
  "username": "<USERNAME>",
  "password": "<PASSWORD>",
  "pin": "<PIN>",
  "client_id": "<CLIENT_ID>",
  "secret_key": "<SECRET_KEY>",
  "redirect_uri": <REDIRECT_URL>
}
```

#### Initialization

- fyersApiBuilder = FyersApiBuilder(config=config)

#### HTTP Client

- fyersApiBuilder.client.get_profile()

#### WebSocket Client

- fyersApiBuilder.ws_client.subscribe()
