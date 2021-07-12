from ivis import ivis
import requests

print(ivis.accessToken)
url = f"http://localhost:8444/{ivis.accessToken}/rest/files/job/file/56/"
test_file = open("job.py", "rb")
ivis.upload_file(test_file)