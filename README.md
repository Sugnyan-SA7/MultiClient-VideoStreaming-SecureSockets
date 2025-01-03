# Secure Multi-Client Video Streaming Using Python, Sockets, OpenCV, and SSL

This project is an advanced implementation of **Socket Programming** designed for real-time video streaming between a server and multiple clients. It incorporates **SSL/TLS (Secure Sockets Layer)** to establish encrypted communication, ensuring secure data transfer over the network. The server can efficiently manage and stream video to multiple clients simultaneously using multi-threading, making it robust and scalable.

---

## 🔑 Key Features

1. **Socket Programming**: 
   - Utilizes TCP sockets for stable and reliable communication between the server and clients.

2. **Multi-Client Support**:
   - The server can handle multiple clients simultaneously by assigning a dedicated thread to each client.
   - Real-time video streaming is maintained for all active clients.

3. **SSL Encryption**:
   - Protects data transmission by encrypting the communication channel.
   - Ensures secure authentication between the server and clients.

4. **Real-Time Video Streaming**:
   - The server streams live video captured from its webcam using OpenCV.
   - Clients receive and display the video feed in real-time.

---

## 🛠️ Technology Stack

- **Python**: Programming language for both server and client-side implementation.
- **OpenCV**: For video capture and display functionalities.
- **Socket Module**: To establish and manage network connections.
- **SSL Module**: To secure communication with certificates.

---

## 📚 How It Works

### Server
1. The server initializes an SSL-secured socket using a self-signed or CA-signed certificate.
2. It binds to a specific IP address and port, then listens for incoming client connections.
3. Upon receiving a connection, the server starts a new thread to handle communication with the client.
4. The server captures video from its webcam using OpenCV.
5. The video frames are serialized using Python's `pickle` module and sent over the socket to connected clients.

### Client
1. The client establishes an SSL-secured connection to the server using the server's certificate.
2. It receives serialized video frames from the server, deserializes them, and displays the video feed in real-time using OpenCV.

---

## 🔧 Setup Instructions

### Prerequisites
1. **Python Installation**: Install Python 3.6 or later.
2. **Install Dependencies**:
    ```bash
    pip install opencv-python
    ```
3. **Generate SSL Certificates**:
   - **For the Server**:
     - Generate a server certificate (`server-cert.pem`) and private key (`server-key.pem`).
   - **For the Client**:
     - Use a CA certificate (`ca-cert.pem`) to verify the server's authenticity.
   - Example commands for self-signed certificates (make sure to install and setup openssl):
     ```bash
     openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server-key.pem -out server-cert.pem
     openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ca-cert.pem -out ca-cert.pem
     ```

---

### Running the Project

1. **Start the Server**:
   - Run the server script:
     ```bash
     python server.py
     ```
   - The server will start listening on its hostname and port (default: 9999).
   - Example output:
     ```
     Listening at ('192.168.1.100', 9999)
     ```

2. **Start the Client(s)**:
   - Run the client script:
     ```bash
     python client.py
     ```
   - Enter the server's IP address when prompted. (Enter the address that is displayed in the terminal running the server.)
   - Example input:
     ```
     Enter the server IP: 192.168.1.100
     ```

3. **Streaming Video**:
   - The server will begin streaming video to all connected clients in real-time.
   - Clients will display the received video feed in a window.

---

## 📂 Code Overview

### Server Code Highlights
- **Video Capture**: Captures frames from the webcam using OpenCV.
- **SSL Configuration**: Uses `ssl.wrap_socket()` to secure communication.
- **Multi-Client Handling**: Each client connection is handled on a separate thread using Python's `threading` module.
- **Video Streaming**: Frames are serialized with `pickle` and sent to clients.

### Client Code Highlights
- **SSL Connection**: Establishes a secure connection to the server using the CA certificate.
- **Frame Deserialization**: Receives and decodes video frames using `pickle`.
- **Video Display**: Displays the video feed in real-time using OpenCV.

---

## ⚠️ Exiting the Application
- **Server**: Press `q` in the video display window to stop capturing and streaming.
- **Clients**: Press `q` in the video display window to disconnect from the server.

---

## 💡 Example Use Cases
1. **Remote Monitoring**:
   - Stream video feeds from a centralized server to multiple clients for surveillance or monitoring.
2. **Online Learning**:
   - Securely broadcast video streams to multiple students in real-time.
3. **Collaborative Workspaces**:
   - Share video streams in secure environments.

---

## 🌟 Future Enhancements
1. **Client Authentication**:
   - Implement user-based authentication for added security.
2. **Support for Low-Bandwidth Networks**:
   - Optimize video compression to improve performance on slower connections.
3. **Dynamic Video Source Selection**:
   - Allow the server to switch between multiple video sources.

---

## 📝 License
This project is licensed under the MIT License. See the LICENSE file for more details.
