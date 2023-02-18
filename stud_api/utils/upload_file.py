import os
import sys
import json
import requests


def upload(file):
    files = {"file": open(file, "rb")}
    headers = {"authorization": "r:764a3c255228b9ae3ac1aaa5f97d897c"}
    response = requests.post(
        "https://stud-api.sabir.pro/file/upload", files=files, headers=headers
    )

    return response.text


if __name__ == "__main__":
    if len(sys.argv) != 3:
        exit("Three arguments are required..")

    _, flag, file = sys.argv

    if flag == "-u":
        if not os.path.isfile(file):
            exit("It is not a file..")

        url = json.loads(upload(file))["url"]
        print(url)

    elif flag == "-d":
        os.popen(f"wget {file}")
    else:
        exit("Wrong flag, use -u or -d..")
