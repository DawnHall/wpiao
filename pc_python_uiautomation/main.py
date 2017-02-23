# -*- coding: utf-8 -*-

import websocket
# import thread
import time
import json
import threading

import vote

def on_message(ws, message):
    print('on_message: ' + message)
    msg = json.loads(message)
    if msg['cmd'] == 'vote':
        # 投票 {"cmd":"vote", "url": "http://wxxxx", "votes": 100}
        vote.vote(msg['url'], msg['votes'])
    elif msg['cmd'] == 'train':
        vote.train()
    else:
        print('cmd('+msg['cmd']+') is invalid')
    # 其他动作：TODO

def on_error(ws, error):
    print('on_error: ', error)

def on_close(ws):
    print("on_close, will reconnect in 5 seconds... ")
    time.sleep(5)
    start_websocket()

def on_open(ws):
    print('on_open: ')
    # def run(*args):
    #     for i in range(3):
    #         time.sleep(1)
    #         ws.send("Hello %d" % i)
    #     time.sleep(1)
    #     ws.close()
    #     print "thread terminating..."
    # thread.start_new_thread(run, ())

def start_websocket():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:8080/api/ws/pc",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

print('start_websocket...')
t = threading.Thread(target=start_websocket, args=())
t.start()

# if __name__ == "__main__":
#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp("ws://127.0.0.1:8080/api/ws/pc",
#                               on_message = on_message,
#                               on_error = on_error,
#                               on_close = on_close)
#     ws.on_open = on_open
#     ws.run_forever()
