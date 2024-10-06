#pyinstaller --onefile --icon=app_
#wap to download file using python request library
import requests
def download_file(url,file_name):
    response=requests.get(url)
    if response.status_code == 200:
        with open(file_name,'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file. status code: {response.status_code}")
if __name__ =="__main__":
    url=r"https://github.com/upessocs/B1B2/blob/main/fileOrganizerGui/Organizer.zip"
    file_name='organizer.zip'
    download_file(url,file_name)