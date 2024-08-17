# yamlファイルに書き出し

# pip install pyyamlが必要
import yaml
with open('config/config.yml', 'w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, yaml_file)  # default_flow_style=Falseは不要になった？


# yamlファイルを読み込む
with open('config/config.yml', 'r') as yaml_file:
    data = yaml.load(yaml_file, Loader=yaml.Loader)  # pyyaml6.0ではLoaderが必要
    print(data, type(data))
    print(data['web_server'][('host')])
    print(data['web_server'][('port')])
    print(data['db_server'][('host')])
    print(data['db_server'][('port')])

# {'db_server': {'host': '127.0.0.1', 'port': 3306},
# 'web_server': {'host': '127.0.0.1', 'port': 80}} <class 'dict'>
# 127.0.0.1
# 80
# 127.0.0.1
# 3306
