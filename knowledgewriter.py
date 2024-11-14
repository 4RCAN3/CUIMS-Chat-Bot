import json

with open('Data/info.json') as f:
    data = json.load(f)
    for key in data.keys():
        with open(f'Data/{key}.txt', 'w', encoding="utf-8") as fp:
            page = str()
            for heading, text in data[key].items():
                page += f'{heading}:\n{text}\n\n'
            
            fp.write(page)