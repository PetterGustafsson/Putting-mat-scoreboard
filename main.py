from ws_connection import ClientClosedError
from ws_server import WebSocketServer, WebSocketClient
import time
from collections import OrderedDict 

scorebaord = {}
holes = 0

def make_scoreboard(message_list):
    scoreboard = OrderedDict()
    for player in message_list:
        if player !='':
            scoreboard[player] = []           
    return scoreboard  
        
        
def make_html(scoreboard, holes, active=None):
    string = '''
    <style>
    table, th, td {
      border: 1px solid black;
    }
    </style>
    </head>
    <body>
    <table style="width:100%">
     
     <tr><th>  </th>
     '''
    for hole in range(holes):
        string += '<th>' + str(hole+1) + '</th>'
    string += '<th>Total</th></tr>'
    for player in scoreboard:
        if player == active:
            string+='<tr bgcolor="yellow">'
        string += '<th>' + player + '</th>'
        holes_add = holes - len(scoreboard[player])
        for hole in scoreboard[player]:
            string += '<th>'
            string += str(hole)
            string += '</th>'
        for hole in range(holes_add):
            string += '<th>  </th>'
        string += '<th>'+ str(sum(scoreboard[player])) +'</th>'
        string += '</tr>'
    string += '</table>'
    string += '<button type ="button"  onclick="sendCorrection()">Correct last ruling</button>'  #Fix appearance     
    string += '<button type ="button"  onclick="sendPlay()">Next player</button>'
    
#     string +='</body></html>'

    return string 

def blink(led, n, t):
    for _ in range(n):
        led.value(1)
        time.sleep(t)
        led.value(0)
        time.sleep(t)
    return

def ball():
    calibration = pot.read()
#     cals = []
#     for _ in range(10):
#         cals.append(sensor.distance_cm())
#         time.sleep(0.1)
#     cal = sum(cals)/len(cals)

    while True:

        green.value(1)
        red.value(0)
        var = pot.read()
        if var < 0.5* calibration:
            green.value(0)
            t = time.time()
            while time.time() - t < 3:
                if switch.value() == 0:
                    blink(green, 3, 0.5)
                    return 1
            blink(red
                  , 3, 0.5)
            return 0                      
        time.sleep(0.001)

    
    
    
class TestClient(WebSocketClient):
    def __init__(self, conn):
        super().__init__(conn)

    def process(self):
        global holes
        global scoreboard
        try:
            msg = self.connection.read()
            if not msg:
                return
            msg = msg.decode('utf-8')
            msg = msg.split(',')    
            scoreboard = make_scoreboard(msg[1:])
            holes = int(msg[0])
            self.connection.write(make_html(scoreboard, holes))
            
            for _ in range(holes):
                for player in scoreboard:
                    scoreboard[player].append(0)
                    self.connection.write(make_html(scoreboard, holes, player))
                    
                    score = 0
                    while True:
                        pass
                        result = ball()
                        
                        if result == 1:
                            score+= 1
                            scoreboard[player][-1] = score
                            self.connection.write(make_html(scoreboard, holes, player))
                            break
                        else:
                            score+= 1
                            scoreboard[player][-1] = score
                            self.connection.write(make_html(scoreboard, holes, player))
                            pass
            #Winner
            highscore = 1000
            winner = ''
            for player in scoreboard:
                if sum(scoreboard[player]) < highscore:
                    highscore = sum(scoreboard[player])
                    winner = player
            winner = 'The winner is {} with {} shots'.format(str(winner), str(highscore))
            self.connection.write(winner)               
             
        except ClientClosedError:
            pass
            #self.connection.close()


class TestServer(WebSocketServer):
    def __init__(self):
        super().__init__("test.html", 2)

    def _make_client(self, conn):
        return TestClient(conn)


server = TestServer()
server.start()
try:
    while True:
        server.process_all()
except KeyboardInterrupt:
    pass
server.stop()


