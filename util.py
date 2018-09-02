"""Util

Misc Useful stuff

"""

import json

def getLambdaRequest(event):
  """Gets JSON data out of lambda event

  If data or password are not given, return an error
  """

  body = None

  if 'body' not in event:
    body = event
  else:
    body = event['body']

  if 'data' not in body:
    raise ValueError('No data given')

  if 'password' not in body:
    raise ValueError('No password given')

  return json.loads(body)
