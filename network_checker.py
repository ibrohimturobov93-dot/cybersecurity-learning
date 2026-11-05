import socket
import subprocess

print("================================")
print("       NETWORK CHECKER")
print("================================")

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

gateway = "192.168.1.1"

print("Kompyuter nomi:", hostname)
print("Lokal IP manzil:", local_ip)
print("Router manzili:", gateway)

print("--------------------------------")
print("Router bilan aloqa tekshirilmoqda...")

result = subprocess.run(
    ["ping", "-n", "1", gateway],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("Natija: Router bilan aloqa mavjud!")
else:
    print("Natija: Router bilan aloqa yo'q!")
print("--------------------------------")
print("Internet aloqasi tekshirilmoqda...")

internet = subprocess.run(
    ["ping", "-n", "1", "8.8.8.8"],
    capture_output=True,
    text=True
)

if internet.returncode == 0:
    print("Natija: Internet aloqasi mavjud!")
else:
    print("Natija: Internet aloqasi mavjud emas!")
print("================================")