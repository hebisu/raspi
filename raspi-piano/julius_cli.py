import socket
import xml.etree.ElementTree as ET

JULIUS_PORT = 10500
MAX_RECV = 1024

# Connect Julius
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def julius_connect():
    HOST = "localhost"
    PORT = JULIUS_PORT
    client.connect((HOST, PORT))

# Receive data from Julius
def julius_recv(callback):
    tmp = bytes()
    while True:
        try:
            # Receive XML format
            buf = client.recv(MAX_RECV)
            tmp += buf
            # \n.\n is Julius section devider
            n = tmp.find(b"\n.\n")
            if n < 0: continue
            line = tmp[:n].decode("utf-8")
            tmp = tmp[n+3:]
            # Received XML
            # Process devided data as XML
            root = ET.fromstring(line)
            if root.tag != "RECOGOUT": continue
            shypo = root[0]
            # Fetch recognized word
            words = []
            for whypo in shypo:
                words.append(whypo.attrib['WORD'])
            # Cut first of [s] and end of [/s]
            words = words[1:len(words)-1]
            if callback(words) == False:
                break
        except KeyboardInterrupt:
            break
    client.close()
    return

# Test callback func
def test_callback(words):
    print("Word: ", words)
    return True

# main func
if __name__ == "__main__":
    julius_connect()
    julius_recv(test_callback)



