import base64

def b64encode(s):
  sample_string = str(s)
  sample_string_bytes = sample_string.encode("ascii")
  
  base64_bytes = base64.b64encode(sample_string_bytes)
  base64_string = base64_bytes.decode("ascii")
  
  return base64_string

def b64decode(b64str):
  base64_message = str(b64str)
  base64_bytes = base64_message.encode('ascii')
  message_bytes = base64.b64decode(base64_bytes)
  message = message_bytes.decode('ascii')
  return message
