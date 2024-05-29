import os
import requests

def download_image_from_url(url, id):
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    img_bytes = requests.get(url).content
    name = f'image-{id}.jpg'
    full_path = f'session4\exercises\exercise-1\{output_dir}\{name}'
    # os.path.join('session4\exercises\exercise-1\',output_dir, name)
    with open(full_path, 'wb') as file:
        file.write(img_bytes)


def serial_download_image(filename):
    '''read file from file name, catch error
    parse filename
    download image
    rename image
    '''
    # try:
    with open(filename, 'r') as file:
        linecount = 0
        for line in file:
            linecount += 1
            line = line.strip()
            download_image_from_url(line, linecount)
    # except:
        # print('Error')
    return 0
if __name__ == '__main__':
    serial_download_image('session4\exercises\exercise-1\image_urls.txt')