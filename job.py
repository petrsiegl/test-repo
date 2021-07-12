from ivis import ivis
import requests

with open("job.py", "rb") as f:
  ivis.upload_file(f)