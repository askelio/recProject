import socket
from time import sleep


BUFFER_SIZE = 4096

client_path = 'client_image.jpeg'

def send_img_to_process(img):
    print('Start')
    print('Sending started')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    with open(img, 'rb') as file:
        file_data = file.read(BUFFER_SIZE)

        while file_data:
            client.send(file_data)
            file_data = file.read(BUFFER_SIZE)
    client.send(b"%IMAGE_COMPLETED%")
    print('Sending completed')
    recv_data = client.recv(BUFFER_SIZE)
    print(recv_data)
    print('Close')
    client.close()
    print('End')
    sleep(2)




send_img_to_process('Test/00000.png')

send_img_to_process('Test/00001.png')
send_img_to_process('Test/00002.png')

send_img_to_process('Test/00003.png')
send_img_to_process('Test/00004.png')

send_img_to_process('Test/00005.png')
send_img_to_process('Test/00006.png')

send_img_to_process('Test/00007.png')
send_img_to_process('Test/00008.png')

send_img_to_process('Test/00009.png')
send_img_to_process('Test/00010.png')

send_img_to_process('Test/00001.png')





