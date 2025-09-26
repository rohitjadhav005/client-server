import socket

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 9999))

print("UDP Server ready to receive files...")

# Function to receive a file
def receive_file(filename):
    with open(filename, "wb") as f:
        while True:
            data, addr = server_socket.recvfrom(1024)
            if data == b"EOF":   # End of File signal
                break
            f.write(data)
    print(f"File received and saved as {filename}")

# Receive Script File
receive_file("received_script.py")

# Receive Text File
receive_file("received_text.txt")

# Receive Audio File
receive_file("received_audio.mp3")

# Receive Video File
receive_file("received_video.mp4")

server_socket.close()