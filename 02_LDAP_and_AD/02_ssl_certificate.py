from datetime import datetime, date
import OpenSSL
import ssl
cert=ssl.get_server_certificate(('google.com', 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
bytes=x509.get_notAfter()


expiration = datetime.strptime(bytes.decode('utf-8'), '%Y%m%d%H%M%S%z').date()

today = date.today()
print(type(expiration))
print(type(today))

till_expiration = (expiration-today).days;

print (expiration)
print (f'Time till expiration is {till_expiration} days')