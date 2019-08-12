import json
import sys

if len(sys.argv) < 4:
    print('python filename.py {messages.json file} {user} {message}')

filename = sys.argv[0]

with open('messages.json', 'r') as jsonFile:
    d = jsonFile.read()

d2 =json.loads(d)

for i in d2:
    list = i['conversation']
    message = ' '.join(word for word in sys.argv[3:])
    if str(sys.argv[2]) in i['participants']:
        for j in list:
            send = j['sender']
            for values in j.values():
                if str(values).lower().find(message.lower()) != -1:
                    print(f'{send}: {values}')

#if you want to make the json file neat uncomment the below code.

# with open('messages2.json', 'w') as f:
#     print('Working......')
#     json.dump(d2,f, indent=4)
