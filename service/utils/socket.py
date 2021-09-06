import os
MSGLEN = os.getenv('SERVER_URL', 10)
def socketMessage(s, msg):
  totalsent = 0
  while totalsent < MSGLEN:
      sent = s.send(msg[totalsent:])
      if sent == 0:
          raise RuntimeError("socket connection broken")
      totalsent = totalsent + sent
def socketCatchMessaje(s):
  chunks = []
  index = 0
  while index <= 157:
      chunk = s.recv(4096).decode()
      print(len(chunk), index)
      if not chunk or chunk == '' or not chunk:
          print('End', len(chunks))
          return b''.join(chunks)
      chunks.append(chunk)
      index += 1
  return b''.join(chunks)

def recvall(sock):
    BUFF_SIZE = 8192 # 4 KiB
    data = b''
    index = 0
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE - BUFF_SIZE * 0.1:

            # either 0 or end of data
            break
        index += 1
    return data
