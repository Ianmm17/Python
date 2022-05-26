import sys
import clipboard
import json

SAVED_DATA = 'clipboard.json'

def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save':
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print('Data Saved!\n')
    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print('data copied to clipboard\n')
        else:
            print('Key does not exist\n')
    elif command == 'list':
        print(f"{data}\n")
    elif command == 'delete':
        key = input('Enter key to delete: ')
        if key in data:
            del data[key]
            save_data(SAVED_DATA, data)
            print("Key has been deleted from data\n")
        else:
            print('Key does not exist\n')
    else:
        print('Unknown Command\n')
else:
    print('Please pass exactly one command.\n')