from flask_socketio import SocketIO

from backends.services.wth.app.init import init

app = init.create_app()
socketio=SocketIO(app)




if __name__ == '__main__':
    # 初始化数据库（创建表）

    """ 实时聊天：客户端通过emit方法发送聊天消息给服务器，服务器再将消息广播给所有连接的客户端，实现实时聊天功能。
多人协作：在多人协作的应用中，emit方法可以用于发送协作事件和数据，如文档编辑、游戏状态更新等。
实时数据更新：服务器可以通过emit方法将实时数据更新发送给客户端，如股票价格、天气预报等。 """
        #socketio.run(app, debug=True, host="127.0.0.1", port=8889)
    app.run(debug=True, host="127.0.0.1", port=8889, threaded=True)#多线程

    #app.run(debug=True,threading=True,host="127.0.0.1",port=8889,)
    # app.run(debug=True, threaded=True)
