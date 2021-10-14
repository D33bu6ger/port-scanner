import socket

def scanin(host,port):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:

                s.connect((host,port))

                print("[+] Open port: "+ str(port))

                s.close()

        except:

                print("[-] Closed port: "+ str(port))

def start_program(url):

        print('''

======================= PORT SCANNER BY DY ======================================

||  This program accepts any url as a string from the user,                    ||

||  Also you can insert IP address,                                            ||

||  Finally, the result is printed to the User.                                ||

=================================================================================

''')

        for port in range(1024):

                scanin(url,port)

url = input("Enter url or IP Address: ")

start_program(url)
