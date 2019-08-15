import socket
import xml.etree.ElementTree as ET

JULIUS_PORT = 10500
MAX_RECV_SIZE = 1024

# Connect Julius
def julius_connect(client):
    HOST = "localhost"
    PORT = JULIUS_PORT
    client.connect((HOST, PORT))

# Receive data from Julius
def julius_recv(callback, client):
    buf_tmp = bytes()
    while True:
        try:
            # Receive XML format
            buf_recv = client.recv(MAX_RECV_SIZE)
            buf_tmp += buf_recv

            # \n.\n is Julius section devider
            num_letters = buf_tmp.find(b"\n.\n")
            if num_letters < 0:
                continue

            line = buf_tmp[:num_letters].decode("utf-8")
            buf_tmp = buf_tmp[num_letters + 3:]
            
            # Received XML
            # Process devided data as XML
            root = ET.fromstring(line)
            if root.tag != "RECOGOUT":
                continue

            sentence_hypo = root[0]
            # Fetch recognized word
            words = []
            for word_hypo in sentence_hypo:
                words.append(word_hypo.attrib['WORD'])

            # Cut first of [s] and end of [/s]
            words = words[1:len(words) - 1]

            if callback(words) == False:
                break
        except KeyboardInterrupt:
            break
    return

# Test callback func
def test_callback(words):
    print("Word: ", words)
    return True

# main func
if __name__ == "__main__":
    julius_connect()
    julius_recv(test_callback)



