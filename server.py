import socket, cv2, pickle, struct
import threading
import ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='./server-cert.pem', keyfile='./server-key.pem')
server_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_side=True)
host_name = socket.gethostname()
print(host_name)
host_ip = socket.gethostbyname(host_name)
port = 9999

socket_address = (host_ip, port)

server_socket.bind(socket_address)

server_socket.listen()
print("Listening at", socket_address)

def show_client(addr, client_socket):
    try:
        print('CLIENT {} CONNECTED!'.format(addr))
        if client_socket:
            vid = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
            print("capturing vid")
        
            while vid.isOpened():
                img, frame = vid.read()
                cv2.imshow('TRANSMITTING VIDEO', frame)
                a = pickle.dumps(frame)
                message = struct.pack("Q", len(a)) + a
                client_socket.sendall(message)

                #cv2.imshow('TRANSMITTING VIDEO', frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                     break
    except Exception as e:
        print(f"client {addr} disconnected")
        pass

while True:
    client_socket, addr = server_socket.accept()
    thread = threading.Thread(target=show_client, args=(addr, client_socket))
    thread.start()
    print("TOTAL CLIENTS ", threading.active_count() - 1)
