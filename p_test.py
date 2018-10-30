import csv
import requests
from urllib import parse

def normLine(data):
    data["Currency"]= "GBP"
    url = parse.parse_qs(parse.urlsplit(data["Url"]).query)
    for value in url:
        url[value] = url[value][0]
    data.update(url)
    return data

def post(data):
    url = "https://webhook.site/2daa4e3b-c691-4190-977d-d9b7eb1d72d7"
    requests.post(url,data=data)


def main():
    with open("users.csv", mode='r') as file:
        reader = csv.DictReader(file)
        for line in reader:
            normalisedLine = normLine(line)
            post(normalisedLine)

if __name__ == '__main__':
    main()