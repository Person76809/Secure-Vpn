import argparse

import logging

import socket

import threading

from cryptography.fernet import Fernet

logging.basicConfig(level=logging.INFO)

# Set the encryption key (replace with your own key)

ENCRYPTION_KEY = b'YourSecretKey1234567890'

# Proxy configuration

PROXY_ENABLED = True

PROXY_HOST = 'proxy.example.com'

PROXY_PORT = 8080

def encrypt_data(data):

    cipher = Fernet(ENCRYPTION_KEY)

    return cipher.encrypt(data)

def decrypt_data(data):

    cipher = Fernet(ENCRYPTION_KEY)

    return cipher.decrypt(data)

class ClientHandler(threading.Thread):

    def __init__(self, client_socket, target_host, target_port):

        super().__init__()

        self.client_socket = client_socket

        self.target_host = target_host

        self.target_port = target_port

    def run(self):

        while True:

            try:

                # Receive data from the client

                encrypted_client_data = self.client_socket.recv(4096)

                if len(encrypted_client_data) == 0:

                    break

                # Decrypt the received data

                client_data = decrypt_data(encrypted_client_data)

                if PROXY_ENABLED:

                    # Connect to the proxy server

                    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                    proxy_socket.connect((PROXY_HOST, PROXY_PORT))

                    proxy_socket.sendall(client_data)

                    # Receive data from the proxy server

                    proxy_data = proxy_socket.recv(4096)

                    # Encrypt the received data

                    encrypted_proxy_data = encrypt_data(proxy_data)

                    # Send the encrypted data back to the client

                    self.client_socket.sendall(encrypted_proxy_data)

                    # Close the proxy socket

                    proxy_socket.close()

                else:

                    # Forward the decrypted data to the target server

                    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                    target_socket.connect((self.target_host, self.target_port))

                    target_socket.sendall(client_data)

                    # Receive data from the target server

                    target_data = target_socket.recv(4096)

                    # Encrypt the received data

                    encrypted_target_data = encrypt_data(target_data)

                    # Send the encrypted data back to the client

                    self.client_socket.sendall(encrypted_target_data)

                    # Close the target socket

                    target_socket.close()

            except Exception as e:

                logging.error(f'Error: {e}')

                break

        # Close the client socket

        self.client_socket.close()

def start_vpn_server(vpn_server_host, vpn_server_port, target_host, target_port):

    vpn_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    vpn_server.bind((vpn_server_host, vpn_server_port))

    vpn_server.listen(5)

    logging.info(f'VPN server is running on {vpn_server_host}:{vpn_server_port}')

    while True:

        try:

            client_socket, client_address = vpn_server.accept()

            logging.info(f'New client connected: {client_address[0]}:{client_address[1]}')

            client_handler = ClientHandler(client_socket, target_host, target_port)

            client_handler.start()

        except KeyboardInterrupt:

            logging.info('VPN server stopped.')

            break

        except Exception as e:

            logging.error(f'Error: {e}')

            break

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Secure VPN Server')

    parser.add_argument('--vpn-host', default='0.0.0.0', help='VPN server host (default: 0.0.0.0)')

    parser.add_argument('--vpn-port', type=int, default=123 
                        
    parser.add_argument('--vpn-port', type=int, default=12345, help='VPN server port (default: 12345)')

    parser.add_argument('--target-host', required=True, help='Target server host')

    parser.add_argument('--target-port', type=int, required=True, help='Target server port')

    args = parser.parse_args()

    start_vpn_server(args.vpn_host, args.vpn_port, args.target_host, args.target_port)

 

 

