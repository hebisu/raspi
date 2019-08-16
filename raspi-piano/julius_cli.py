"""
julius_cli.py
Written by Hiro Ebisu
"""

import socket

import xml.etree.ElementTree as ET

JULIUS_PORT = 10500
MAX_RECV_SIZE = 1024

def julius_connect(client_socket):
    """
    julius_connect is to connect Julius with IP socket
    """
    julius_host = "localhost"
    julius_port = JULIUS_PORT
    client_socket.connect((julius_host, julius_port))

def julius_recv(callback, client_socket):
    """
    julius_recv is to receive data from Julius,
    recognize words and return the string
    """
    buf_tmp = bytes()
    while True:
        try:
            # Receive XML format
            buf_recv = client_socket.recv(MAX_RECV_SIZE)
            buf_tmp += buf_recv

            # \n.\n is Julius section devider
            # Check the number of letters before \n.\n
            num_letters = buf_tmp.find(b"\n.\n")
            if num_letters < 0:
                continue

            # Fetch a word and progress pointer after \n.\n
            line = buf_tmp[:num_letters].decode("utf-8")
            buf_tmp = buf_tmp[num_letters + 3:]

            # Process devided data as XML
            root = ET.fromstring(line)
            if root.tag != "RECOGOUT":
                continue

            sentence_hypo = root[0]
            # Fetch recognized word
            words = []
            for word_hypo in sentence_hypo:
                words.append(word_hypo.attrib['WORD'])

            # Cut first letter [s] and end letter [/s]
            words = words[1:len(words) - 1]

            if callback(words) is False:
                break
        except KeyboardInterrupt:
            print("Keyboard Interrupt. Closing process.")
            break
    return


# Test callback func
def test_callback(words):
    """
    test_callback is test callback function for Julius
    """
    print("Word: ", words)
    return True


# main func
if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        julius_connect(client)
        julius_recv(test_callback, client)
    print("Socket closed.")
