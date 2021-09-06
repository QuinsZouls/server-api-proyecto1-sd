import socket
import json
import sys
from cryptography.fernet import InvalidToken
from utils.crypto import decryptImage
from utils.socket import recvall
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(("localhost", 6791))

serversocket.listen(5)

while True:
    try:
        # accept connections from outside
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a threaded server
        request = recvall(clientsocket)
        parsedReq = json.loads(request.decode())
        print('Se ha recibido un mensaje')
        if parsedReq['option'] == 'processImage':
            print('Decodificando mensaje...')
            response = json.dumps({
                "image": decryptImage(parsedReq['data']).decode(),
                "type": "result"
            })
            clientsocket.send(response.encode())
            print('Se ha enviado el mensaje')
    except InvalidToken:
        print("El token es invalido")
    except KeyboardInterrupt:
        sys.exit()
    except:
        print('Error desconocido')