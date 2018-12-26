import io
import json

with io.open('C:\\a6ca2610-88e8-4698-a544-670b0c11c092.json', 'r', encoding='utf-8-sig') as f: 
    # ...
    for line in f: 
        tweet = json.loads(line)
        print(tweet)


https://github.com/kashifrazzaqui/json-streamer
https://stackoverflow.com/questions/46934135/jsondecodeerror-unexpected-utf-8-bom-display-problems-in-bash?rq=1
https://jsonlines.readthedocs.io/en/latest/
