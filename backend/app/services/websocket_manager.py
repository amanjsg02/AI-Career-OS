from fastapi import WebSocket

class ConnectionManager:

    def __init__(self):
        self.connections = {}

    async def connect(self, task_id, websocket: WebSocket):
        await websocket.accept()
        print("CONNECTED:", task_id)
        self.connections[task_id] = websocket
        print(self.connections)
        self.connections[task_id] = websocket

    def disconnect(self, task_id):
        self.connections.pop(task_id, None)

    async def send_progress(self, task_id, data):
        print("TASK ID =", task_id)

        websocket = self.connections.get(task_id)

        print("WEBSOCKET =", websocket)

        if websocket:

          print("SENDING", data)

          await websocket.send_json(data)

manager = ConnectionManager()