from ivis import ivis
import requests

with open("README.md", "rb") as f:
  ivis.upload_file(f)