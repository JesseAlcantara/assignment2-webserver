# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)

  #Prepare a server socket
  serverSocket.bind(("", port))

  #Fill in start
  # I tell the server to begin listening for incoming TCP connections.
  # The argument '1' is the backlog size (how many waiting connections can queue up).
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection

    print('Ready to serve...')
    # This line blocks until a client connects.
    # connectionSocket = new socket created for this specific client connection
    # addr contains the client's IP address and port number
    connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end

    try:
      # This receives up to 4096 bytes from the client (HTTP request).
      # The request arrives as bytes, so I decode it into a string using UTF-8.
      message = connectionSocket.recv(4096).decode("utf-8", errors="replace") #Fill in start -a client is sending you a message   #Fill in end

      # HTTP request line example: "GET /helloworld.html HTTP/1.1"
      # Splitting by spaces gives: ["GET", "/helloworld.html", "HTTP/1.1"]
      # Index [1] is the requested file path.
      filename = message.split()[1]

      # filename[1:] removes the leading "/" from "/helloworld.html"
      # We open in "rb" mode (read binary) because sockets send bytes.
      f = open(filename[1:], "rb")     #fill in start              #fill in end   )



      #This variable can store the headers you want to send for any valid or invalid request.
      #Fill in start

      # I store the file contents (HTML) as bytes.
      body = b""

      # Content-Type tells the browser the response is HTML.
      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"

      #Fill in end

      for i in f: #for line in file
        #Fill in start - append your html file contents #Fill in end

        # Each i is already bytes because we opened the file in "rb".
        body += i

      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!

      # Fill in start

      # HTTP status line + headers for success (200 OK)
      header = (
          "HTTP/1.1 200 OK\r\n"
          "Server: SimplePythonWebServer/1.0\r\n"
          "Connection: close\r\n"
      ).encode("utf-8")

      # Add Content-Type
      header += outputdata

      # Content-Length tells the browser how many bytes are in the body.
      # "\r\n\r\n" ends the header section.
      header += f"Content-Length: {len(body)}\r\n\r\n".encode("utf-8")

      # Build full response (headers + body) and send ONCE
      response = header + body
      connectionSocket.send(response)

      # Fill in end

      connectionSocket.close() #closing the connection socket

    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start

      # If the file does not exist, send a 404 error page.
      body = b"<html><body><h1>404 Not Found</h1></body></html>"

      header = (
        "HTTP/1.1 404 Not Found\r\n"
        "Server: SimplePythonWebServer/1.0\r\n"
        "Connection: close\r\n"
        "Content-Type: text/html; charset=UTF-8\r\n"
        f"Content-Length: {len(body)}\r\n"
        "\r\n"
      ).encode("utf-8")

      connectionSocket.send(header + body)

      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

if __name__ == "__main__":
  webServer(13331)
