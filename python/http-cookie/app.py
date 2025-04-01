from flask import request, make_response, Flask

app = Flask(__name__)

click_counts = {}
last_session_id = 0

# Uses flask and proposes a statefull approach, which is different from main.py approach
@app.route('/')
def click_count():
    session_id = request.cookies.get('sessionId')
    if session_id :
        if session_id in click_counts:
            click_counts[session_id] += 1
            return str(click_counts.get(session_id))+ " click(s) for " + session_id
        else:
            click_counts[session_id] = 0
            return str(0) + " click(s) for " + session_id
    else:
        global last_session_id
        last_session_id += 1
        click_counts[str(last_session_id)] = 0
        resp = make_response(str(0) + " click(s) for " + str(last_session_id))
        resp.set_cookie('sessionId', str(last_session_id))
        return resp 