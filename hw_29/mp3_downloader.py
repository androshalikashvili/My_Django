import requests
import threading


def download_and_save_mp3(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"File {filename} sucsesfuly dowloaded and saved.")
    else:
        print(f"Donwloaded error {filename}: {response.status_code}")


mp3_files = [
    {'url': 'https://download.samplelib.com/mp3/sample-6s.mp3', 'filename': 'music1.mp3'},
    {'url': 'https://download.samplelib.com/mp3/sample-15s.mp3', 'filename': 'music2.mp3'},
    {'url': 'https://file-examples.com/storage/fe0e2ce82f660c1579f31b4/2017/11/file_example_MP3_700KB.mp3', 'filename': 'music3.mp3'}
]


threads = []
for file_info in mp3_files:
    thread = threading.Thread(target=download_and_save_mp3, args=(file_info['url'], file_info['filename']))
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()

print("All files downloaded!.")
