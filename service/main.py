import socket
import json
import io
from utils.crypto import decryptImage
from utils.socket import socketCatchMessaje, recvall
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(("localhost", 6791))

serversocket.listen(5)

while True:
    # accept connections from outside
    (clientsocket, address) = serversocket.accept()
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
    request = recvall(clientsocket)
    parsedReq = json.loads(request.decode())

    if parsedReq['option'] == 'processImage':
        response = json.dumps({
            "image": decryptImage(parsedReq['data']).decode(),
            "type": "result"
        })
        clientsocket.send(response.encode())
