from ivis import ivis
import requests

fileId = ivis.params['file']

print(ivis.get_job_file(fileId).content)