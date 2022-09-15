from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from bot import ask, append_interaction_to_chat_log
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fjkesjrelhg'

@app.route('/bot', methods=['POST'])
def huhu():
    incoming_msg = request.values['Body']
    '''
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, 
                                                         answer, chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    msg = MessagingResponse()
    msg.message(incoming_msg)
    return str(msg)
    '''
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)