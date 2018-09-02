"""Crypto

Wraps GPG methods

"""

import time
import gnupg

GPG = gnupg.GPG()

def encryptData(data, password):
  """Encrypt a string with the given password,
  returns base64 encrypted string
  """

  print('d=' + data)

  start = int(round(time.time() * 1000))

  crypt = GPG.encrypt(
    data,
    symmetric='AES256',
    passphrase=password,
    encrypt=False,
    armor=True
  )

  end = int(round(time.time() * 1000))

  return {
    "encryptedB64": str(crypt),
    "timeMs": end - start,
  }

def decryptData(data, password):
  """Decrypts an GPG encrypted string with the given password."""

  start = int(round(time.time() * 1000))

  decrypted = GPG.decrypt(
    data,
    passphrase=password,
  )

  end = int(round(time.time() * 1000))

  return {
    "decrypted": str(decrypted),
    "timeMs": end - start,
  }
