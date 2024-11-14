import csv
import os

def csv_scraper(filepath: str) -> str:
    with open('Data/Structured/' + filepath) as f:
        csv_data = list(csv.reader(f))
        cols, rows = csv_data[0], csv_data[1:]
        res = f"{filepath.replace('.csv', '')}\n"

        for count, row in enumerate(rows):
            res += f'{count + 1}:\n'
            for count, val in enumerate(row):
                res += f'{cols[count]}: {val}\n'

        return res
    


directory = 'Data/Structured'
for path in os.listdir(directory):
    if not path.endswith('.csv'):
        continue
    else:
        data = csv_scraper(path)
        with open(f"{directory}/{path.replace('.csv', '.txt')}", 'w', encoding='utf-8') as f:
            f.write(data)
