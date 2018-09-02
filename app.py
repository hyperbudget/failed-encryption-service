"""Encrypts or decrypts data"""
import json
import falcon

from crypto import encryptData, decryptData

class EncryptResource:
  """handles encryption"""
  def on_post(self, req, resp):
    """Encrypts data"""
    data = json.dumps(req.media['data'])
    password = req.media['password']

    result = encryptData(data, password)

    resp.media = {
      "OK": "true",
      "result": result
    }

  def on_get(self, req, resp):
    """NOOP"""
    pass

class DecryptResource:
  """handles decryption"""
  def on_post(self, req, resp):
    """Decrypts data"""
    data = req.media['data']
    password = req.media['password']

    result = decryptData(data, password)

    resp.media = {
      "OK": "true",
      "result": {
        "decrypted": json.loads(result['decrypted']),
        "timeMs": result['timeMs']
      }
    }

  def on_get(self, req, resp):
    """NOOP"""
    pass


API = falcon.API()
API.add_route('/encrypt', EncryptResource())
API.add_route('/decrypt', DecryptResource())
