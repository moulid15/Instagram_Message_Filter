import json
import sys

if len(sys.argv) < 4:
    print(f'python filename.py {messages.json file} {user} {message}')

filename = sys.argv[1]

with open(filename, 'r') as jsonFile:
    d = jsonFile.read()

d2 =json.loads(d)
truth = False
print('\n---------------------------messages-------------------------')
for i in d2:
    list = i['conversation']
    message = ' '.join(word for word in sys.argv[3:])
    if str(sys.argv[2]) in i['participants']:
        for j in list:
            send = j['sender']
            for values in j.values():
                if str(values).lower().find(message.lower()) != -1:
                    truth = True
                    print(f'\n-----------------[ {send} sent ]-------------------\n\n{send}: {values} ')
if not truth:
    print(f'This message does not exist with {sys.argv[2]}......try agian')

print('\n----------------messages ends--------------------------------')

# if you want to make the json file neat uncomment the below code.

# with open('messages2.json', 'w') as f:
#     print('Working......')
#     json.dump(d2,f, indent=4)
