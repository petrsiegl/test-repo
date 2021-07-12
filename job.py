from ivis import ivis
import requests

print(ivis.accessToken)
url = f"/{ivis.accessToken}/"
test_file = open("job.py", "rb")
test_response = requests.post(url, files = {"files[]": test_file})