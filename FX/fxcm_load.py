import posixpath
import requests
import pandas as pd

BASE_DIR = '/Temp/FXData'


def run():
    symbol = 'GBPUSD'
    year = 2018
    week = 1
    directory = posixpath.join(BASE_DIR, symbol)
    url = f"https://tickdata.fxcorporate.com/{symbol}/{year}/{week}.csv.gz"
    r = requests.get(url, stream=True)

    filename = f"{directory}/{symbol}_{year}_w{week}.csv.gz"

    with open(filename, 'wb') as file:
        for chunk in r.iter_content(chunk_size=1024):
            file.write(chunk)

    csv_filename =f"{directory}/{symbol}_{year}_w{week}.csv"

    df = pd.read_csv(
        csv_filename,
        header=0,
        sep=',',
        quotechar='"',
        error_bad_lines=False
    )

    temp = 1


if __name__ == "__main__":
    run()
