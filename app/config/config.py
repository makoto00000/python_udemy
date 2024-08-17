# コンフィグを書き出し
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {
  'debug': True
}

config['web_server'] = {
  'host': '127.0.0.1',
  'port': 80
}

config['db_server'] = {
  'host': '127.0.0.1',
  'port': 3306
}

with open('config/config.ini', 'w') as config_file:
    config.write(config_file)


# コンフィグを読み取り
config = configparser.ConfigParser()
config.read('config/config.ini')
print(config['web_server'])
print(config['web_server']['host'])
print(config['web_server']['port'])
print(config['DEFAULT']['debug'])

# <Section: web_server>
# 127.0.0.1
# 80
# True
