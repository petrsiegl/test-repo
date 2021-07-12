from ivis import ivis
import requests

test_file = open("job.py", "rb")
ivis.upload_file(test_file)