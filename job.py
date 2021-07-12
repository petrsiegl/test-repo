from ivis import ivis
import requests

print(ivis.accessToken)
url = f"http://localhost:8443/{ivis.accessToken}/rest/files/job/files/56/"
test_file = open("job.py", "rb")
test_response = requests.post(url, files = {"files[]": test_file})