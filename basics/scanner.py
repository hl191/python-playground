import socket
import sys

# Argument 0 = scanner.py
# python3 scanner.py <ip>

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translate host name to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

print("-" * 50)
print("Scanning target " + target)
print("-" * 50)

try:
    for port in range(50, 85):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = soc.connect_ex((target, port))
        print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        soc.close()
except KeyboardInterrupt:
    print("\nExiting program.")

except socket.gaierror:
    print("\nHostname could not be resolved")

except socket.error:
    print("\nCouldn't connect to server")

finally:
    sys.exit()
