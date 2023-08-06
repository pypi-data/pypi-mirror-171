# apiruns-swagger

Swagger documentation for Apiruns projects

Install

```bash
pip install apiruns-swagger
```

Using
```python
from apiruns_swagger import json_to_swagger

apiruns_schema = {
    "path": "/users",
    "schema": {
        "name": "anybody",
        "last_name": "anybody",
    }
}

servers = [{"url": "https://api.cloud.apiruns.com"}]

swagger_schema = json_to_swagger(apiruns_schema, servers=servers)
```
