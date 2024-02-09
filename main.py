from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    # print(recv)
    #if recv[:3] != '220':
        # print('220 reply not received from server.')


   
    heloCommand = 'HELO localhost\r\n'  # Use the hostname of your machine
    clientSocket.send(heloCommand.encode())

    # print(recv1)
    #if recv1[:3] != '250':
        # print('250 reply not received from server.')


    
    fromCmd = 'MAIL FROM: <>\r\n'
    clientSocket.send(fromCmd.encode())
    recv2 = clientSocket.recv(1024).decode()
    # print(recv2)
    #if recv2[:3] != '250':
        # print('250 reply not received from server.')


  
    rcptToCmd = 'RCPT TO: <storage3454@gmail.com>\r\n'
    clientSocket.send(rcptToCmd.encode())
    recv3 = clientSocket.recv(1024).decode()
    # print(recv3)
    #if recv3[:3] != '250':
        # print('250 reply not received from server.')


    
    dataCmd = 'DATA\r\n'
    clientSocket.send(dataCmd.encode())
    recv4 = clientSocket.recv(1024).decode()
    # print(recv4)
    #if recv4[:3] != '354':
        #print('354 reply not received from server.')


    
    x = 1
    subject = 'Test Email'
    msgData = f'Subject: {subject}\r\n\r\n'
    while x <= 1:  # Adjust the number of emails to send per run
        message = f'{msgData}Testing out the server for the email {x}\r\n'
        clientSocket.send(message.encode())
        x += 3


    msgEnd = '\r\n.\r\n'
    clientSocket.send(msgEnd.encode())
    recv5 = clientSocket.recv(1024).decode()
    # print(recv5)
    #if recv5[:3] != '250':
        # print('250 reply not received from server.')


    
    quitCmd = 'QUIT\r\n'
    clientSocket.send(quitCmd.encode())
    recv6 = clientSocket.recv(1024).decode()
    # print(recv6)
    #if recv6[:3] != '221':
        # print('221 reply not received from server.')


    # Close the socket
    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
