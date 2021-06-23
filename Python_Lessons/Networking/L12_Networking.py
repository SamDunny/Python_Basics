# needed for sockets
import socket

def main():
    # makes a socket that connects to the internet (AF_INET) that streams characters (SOCK_STREAM)
    # makes a socket, does not 'associate' it
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # set timeout to 5 seconds to wait for connection
    mysock.settimeout(5)

    # connects socket to host (data.pr4e.org)(phone #) over port 80 (phone # ext)
    try:
        mysock.connect( ('data.pr4e.org', 80) )
    # catch socket-related errors
    except socket.error as msg:
        print ("Socket Error: ", msg)
    # catch type error-related errors
    except TypeError as msg:
        print ("Type Error: ", msg)

    # make a command to send to the web server (this program acts as a web browser), encodes to UTF-8
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    
    # while loop that runs, colecting returned data 512 characters at a time
    while True:
        data = mysock.recv(512)
        # exit loop if length of data is 0
        if (len(data) < 1):
            break
            # print decoded UTF-8 data with no print() function newline (end='')
        print(data.decode(),end='')

    # close socket when finished
    mysock.close()


if __name__ == '__main__':
    main()