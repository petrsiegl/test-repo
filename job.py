from ivis import ivis
import requests

print(ivis.accessToken)
test_file = open("job.py", "rb")
ivis.upload_file(test_file)