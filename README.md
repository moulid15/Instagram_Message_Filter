# Instagram_Message_Filter
This script will filter every instagram message containing the message string you give it. 

# Clone

```
git clone https://github.com/moulid15/Instagram_Message_Filter.git
```

# How to use

1. You need to request your instagram data by going to `settings` and then `security` , tap download data. On the app.<br />

2. After recieving a link from instagram download the zip. These downloads should include `messages.json`. <br />

3. Put `messages.json` in the side Instagram_Message_Filter folder. <br />

# Running
#### in the terminal
```
python finder.py {messages.json} {user} {message}
```
`{user}` == the person you sent the direct message to <br />
`{message}` == the message you are looking for 

# Example

    python finder.py messages.json blink_182_intern this is a message




