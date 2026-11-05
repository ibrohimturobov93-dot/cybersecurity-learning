import socket

print("================================")
print("          DNS CHECKER")
print("================================")

domain = input("Domen nomini kiriting: ")

try:
    ip_address = socket.gethostbyname(domain)

    print("--------------------------------")
    print("Domen nomi:", domain)
    print("IP manzili:", ip_address)
    print("DNS tekshiruvi muvaffaqiyatli!")

except socket.gaierror:
    print("Xatolik: Domen topilmadi!")

print("================================")