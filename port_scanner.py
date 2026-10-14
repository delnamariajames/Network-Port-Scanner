
import socket
import errno

def scan_port(ip, port, timeout):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    try:
        result = s.connect_ex((ip, port))

        if result == 0:
            status = "OPEN"
        elif result in (errno.ECONNREFUSED, 10061):
            status = "CLOSED"
        else:
            status = "FILTERED/UNKNOWN"

    except socket.timeout:
        status = "FILTERED/UNKNOWN"
    except OSError:
        status = "FILTERED/UNKNOWN"
    finally:
        s.close()

    return status


print("===== NETWORK PORT SCANNER =====")

ip = input("Enter target IP address: ")
start = int(input("Enter starting port: "))
end = int(input("Enter ending port: "))
timeout = float(input("Enter timeout (seconds): "))

if start < 1 or end > 65535 or start > end or timeout <= 0:
    print("Invalid port range or timeout!")
else:
    try:
        socket.inet_aton(ip)

        print("\nPORT       STATUS")
        print("----------------------------")

        for port in range(start, end + 1):
            status = scan_port(ip, port, timeout)
            print(f"{port:<10} {status}")

        print("\nScanning completed!")

    except OSError:
        print("Invalid IP address!")
