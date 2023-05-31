# Secure-Vpn
A safe VPN 

 Everything the code does:

1. Imports the necessary modules: `argparse`, `logging`, `socket`, `threading`, and `cryptography.fernet`.

2. Sets up the logging configuration to display log messages with the `INFO` level.

3. Defines the encryption key used for encrypting and decrypting data.

4. Defines two functions: `encrypt_data` and `decrypt_data`, which use the encryption key to encrypt and decrypt data using the Fernet symmetric encryption algorithm.

5. Defines a `ClientHandler` class that extends the `threading.Thread` class. This class represents a client handler thread that processes client requests.

6. The `ClientHandler` class's `run` method is overridden to implement the logic for receiving data from the client, decrypting it, forwarding it to the target server, receiving data from the target server, encrypting it, and sending it back to the client.

7. Defines a `start_vpn_server` function that sets up the VPN server, listens for incoming client connections, and spawns `ClientHandler` threads to handle client requests.

8. The `start_vpn_server` function uses a `socket` object to create a TCP server socket, binds it to the specified VPN server host and port, and starts listening for client connections.

9. Inside the main loop of the `start_vpn_server` function, when a new client connection is accepted, a `ClientHandler` thread is created to handle the client's requests. The client's socket, target host, and target port are passed to the `ClientHandler` constructor.

10. The `argparse` module is used to define command-line arguments for the VPN server host, VPN server port, target server host, and target server port.

11. The command-line arguments are parsed using `argparse.ArgumentParser`, and the values are extracted.

12. The `start_vpn_server` function is called with the extracted values from the command-line arguments to start the VPN server.

Overall, this code sets up a secure VPN server that listens for incoming client connections, encrypts and decrypts data using the Fernet encryption algorithm, and forwards the data between the clients and a target server. 

This code sets up a secure VPN server that accepts incoming client connections. It encrypts the data received from clients using the Fernet encryption algorithm and forwards it either directly to the target server or through a proxy server, based on the configuration.

The key components of the code include:

Encryption: The encrypt_data and decrypt_data functions use the Fernet encryption algorithm to encrypt and decrypt data using the specified encryption key.

ClientHandler Thread: This class represents a client connection handler. It receives data from the client, decrypts it, and forwards it either to the target server or through a proxy server.

Proxy Configuration: The code includes a proxy configuration that enables or disables proxy usage and specifies the proxy host and port.

VPN Server: The start_vpn_server function sets up the VPN server, binds it to the specified host and port, and listens for incoming client connections. For each client connection, it creates a ClientHandler thread to handle the communication with the client.

Command-Line Arguments: The code uses the argparse module to parse command-line arguments. It accepts arguments for the VPN server host and port, as well as the target server host and port. 
