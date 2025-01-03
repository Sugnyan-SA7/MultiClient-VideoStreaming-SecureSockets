import socket, cv2, pickle, struct
import ssl

host_ip = input("Enter the server IP: ")
host_address=(host_ip,9999)
#client_socket = None
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations(cafile="./ca-cert.pem")  # Load the CA certificate file for verification
context.check_hostname = False  # Disable hostname check
client_socket = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
client_socket.connect(host_address)

data = b""
payload_size = struct.calcsize("Q")
while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4 * 1024)  # 4K
        if not packet: break
        data += packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(4 * 1024)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    cv2.imshow("RECEIVING VIDEO", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

client_socket.close()