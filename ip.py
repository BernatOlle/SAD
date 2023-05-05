import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
    except:
        ip_address = "No se pudo determinar la dirección IP"
    finally:
        s.close()
    return ip_address

print("La dirección IP local es:", get_local_ip())
