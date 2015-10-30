import json


def script_to_json():
    full_script = []
    conversation = []
    message = ''
    with open('raw_script.txt') as f:
        for line in f.readlines():
            if line.startswith('                      '):
                # print message
                if message != '':
                    conversation.append(message)
                    message = ''  # start of new character talking
            elif line.startswith('          '):
                # print line.strip()
                message += ' ' + line.strip()
            elif len(line.strip()) > 0 and not line.startswith(' '):
                print conversation
                if len(conversation) > 0:
                    full_script.append(conversation)
                    conversation = []
                    message = ''
    with open('biglebowskiscript.json', 'w') as f:
        f.write(json.dumps({'conversations': full_script}))

if __name__ == '__main__':
    script_to_json()
