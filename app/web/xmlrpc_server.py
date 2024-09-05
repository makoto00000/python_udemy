from xmlrpc.server import SimpleXMLRPCServer

with SimpleXMLRPCServer(('127.0.0.1', 8001)) as server:
    def add_num(x, y):
        return x + y

    server.register_function(add_num, "add_num")
    server.serve_forever()

# clientからは関数を呼び出すだけ。serverで実行する。
