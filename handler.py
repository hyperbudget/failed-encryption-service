"""Lambda handler

Encrypts and decrypts data

"""

import json

from crypto import encryptData, decryptData
from util import getLambdaRequest

def encrypt(event):
  """Encrypt a given string with the password, return lambda response with
  base64 encoded encrypted string"""

  request = None

  try:
    request = getLambdaRequest(event)
  except ValueError as error:
    return {
      "statusCode": 422,
      "body": json.dumps({
        "messaage": error
      })
    }

  result = encryptData(
    json.dumps(request['data']),
    request['password']
  )

  response = {
    "statusCode": 200,
    "body": json.dumps({
      "message": result
    })
  }

  return response

def decrypt(event):
  """Decrypt data"""

  request = None

  try:
    request = getLambdaRequest(event)
  except ValueError as error:
    return {
      "statusCode": 422,
      "body": json.dumps({
        "messaage": error
      })
    }

  result = decryptData(
    json.dumps(request['data']),
    request['password']
  )

  response = {
    "statusCode": 200,
    "body": json.dumps({
      "message": result
    })
  }

  return response
