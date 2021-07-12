## Posting signal data

```
curl --header "Content-Type: application/json" --request POST --header 'access-token: 8e3f7bf6bed944b40a0ec08ab0dc0c11d0d18fdd' https://api.fivis.smartarch.cz/api/signals --data '
{
  "partnerId": "cuni",
  "signalSetId": "test",
  "schema": {
    "ts": "datetime",
    "sig1": "integer",
    "sig2": "double",
    "sig3": "boolean"
  },
  "data": [
    {
      "id": "0001", "ts" : "2019-02-20T18:25:43.511Z",
      "sig1": 12, "sig2": 34.2, "sig3": true
    },
    {
      "id": "0002", "ts" : "2019-02-20T18:25:44.000Z",
      "sig1": 12, "sig2": 34.2, "sig3": true
    }
  ]
}
'
```