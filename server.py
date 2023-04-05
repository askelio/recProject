import asyncio
import io
import os
import socket
from PIL import Image, ImageFont, ImageDraw
from predict import classify
from time import sleep

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))

server.listen()

BUFFER_SIZE = 4096
counter = 0


while True:
    try:
        print('Started')
        client_socket, _ = server.accept()

        file_stream = io.BytesIO()
        recv_data = client_socket.recv(BUFFER_SIZE)
        while recv_data:
            file_stream.write(recv_data)
            recv_data = client_socket.recv(BUFFER_SIZE)

            if recv_data == b"%IMAGE_COMPLETED%":
                print('Image recieved')
                break

        save_path = f'images/test{counter}.jpeg'
        image = Image.open(file_stream)
        image = image.convert("RGB")
        image.save(save_path, format='JPEG')
        text = classify(save_path)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 25)
        draw.text((15, 15), text, font=font, fill="#FF0000")
        image.save(save_path, format='JPEG')
        counter += 1
        print(str.encode(text))
        client_socket.send(str.encode(text))
        print('Ended')
        print(counter)
    except:
        client_socket.send(str.encode('No data'))





