# from os import truncate
# from flask.scaffold import F
import requests
import json
import time
from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)


questions = [('1. When can we meet again?\n', 'A)When are you free?\nB)It was two days ago.\nC)Can you help me?'), ('2. My aunt is going to stay with me.\n', 'A)How do you do?\nB)How long for?\nC)How was it?'), ('3. When do you study?\n', 'A)at school\nB)in the evenings\nC)in the library'), ('4. Would you prefer lemonade or orange juice?\n', 'A)Have you got anything else?\nB)If you like.\nC)Are you sure about that?'), ('5. Let’s have dinner now.\n', "A)You aren't eating.\nB)There aren't any.\nC)Tom isn't here yet"), ('6. The snow was …… heavily when I left the house.\n', 'A)dropping\nB)landing\nC)falling\nD)descending'), ('7. I can’t find my keys anywhere – I …… have left them at work.\n', 'A)can\nB)must\nC)ought\nD)would'), ('8. When a car pulled out in front of her, Jane did well not to …… control of her bicycle.\n', 'A)miss\nB)lose\nC)fail\nD)drop'), ('9. According to Richard’s …… the train leaves at 7 o’clock.\n', 'A)opinion\nB)advice\nC)knowledge\nD)information'), ('10. When you stay in a country for some time you get used to the people’s …… of life.\n', 'A)habit\nB)custom\nC)way\nD)system'), ('11. The builders are …… good progress with the new house.\n', 'A)getting\nB)doing\nC)making\nD)taking'), ('12. She is now taking a more positive …… to her studies and should do well.\n', 'A)attitude\nB)behavior\nC)manner\nD)style'), ('13. My father …… his new car for two weeks now.\n', 'A)has had\nB)has\nC)is having\nD)had'), ('14. What differences are there …… the English spoken in the UK and the English spoken in the US?\n', 'A)among\nB)between\nC)beside\nD)with'), ('15. At 6 p.m. I started to get angry with him because he was late ……\n', 'A)as usual.\nB)in general.\nC)typically.\nD)usually.'), ('16. …… you get your father’s permission, I’ll take you skiing next weekend.\n', 'A)Although\nB)provided\nC)as\nD)unless'), ('17. A local company has agreed to …… the school team with football shirts.\n', 'A)contribute\nB)supply\nC)give\nD)produce'), ('18. I really enjoy stories that are …… in the distant future.\n', 'A)found\nB)set\nC)put\nD)placed'), ('19. That old saucepan will come in …… when we go camping.\n', 'A)convenient\nB)fitting\nC)handy\nD)suitable'), ('20. Anyone …… after the start of the play is not allowed in until the interval.\n', 'A)arrives\nB)has arrived\nC)arriving\nD)arrived'), ('21. I didn’t …… driving home in the storm so I stayed overnight in a hotel.\n', 'A)fancy\nB)desire\nC)prefer\nD)want'), ('22. The judge said that those prepared to…… in crime must be ready to suffer the consequences.\n', 'A)involve\nB)engage\nC)undertake\nD)enlist'), ('23. Marianne seemed to take …… at my comments on her work.\n', 'A)annoyance\nB)insult\nC)offense\nD)indignation'), ('24. You should not have a dog if you are not …… to look after it.\n', 'A)prepared\nB)adopted\nC)arranged\nD)decided'), ('25. The farmhouse was so isolated that they had to generate their own electricity ……\n', 'A)current.\nB)supply.\nC)grid.\nD)power.')]
answers =[1 , 2 , 2 , 1 , 3 , 3 , 2 , 2 , 4 , 3 , 3 , 1 , 1 , 2 , 1 , 2 , 2 , 2 , 3 , 3 , 1 , 2 , 3 , 1 , 2]
# questions = [('1. When can we meet again?\n', 'A)When are you free?\nB)It was two days ago.\nC)Can you help me?'), ('2. My aunt is going to stay with me.\n', 'A)How do you do?\nB)How long for?\nC)How was it?')]

url="https://api.telegram.org/bot1848540350:AAG5JclNyx3863mB19cvYGlx5K8Adlcvge4/"  #BOT ELT_IUST

guide_note= "This quiz has 25 questions and After each question you should submit your Answer by sending a NUMBER from 1-4 of choices.Send /start_quiz to begin. "

def get_all_updates(): #برای گرفتن پیام ها
    response=requests.get(url + "getUpdates")
    return response.json()

def get_last_update(allupdates):  #برای گرفتن آخرین پیام که از طرف کاربر ارسال شده
    return allupdates["result"][-1]

def get_chat_id(update):   #برای گرفتن چت آی دی کاربری که پیام را ارسال کرده
    return update["message"]["chat"]["id"]

def sendMessage(chat_id , text):   #برای ارسال پیام به کاربر
    sendData={
        "chat_id" : chat_id,
        "text" : text
    }

    response = requests.post(url + "sendMessage",sendData)
    return response

def write_json(data , filename="questions.json"):
    with open(filename , 'w') as target:
        json.dump(data , target , indent=4 , ensure_ascii=False)

def read_json(filename = 'questions.json'):
    with open(filename , 'r') as target:
        data = json.load(target)
    return data



@app.route('/' , methods = ['POST' , 'GET'])
def index():
    # emtiaz = 0
    # soal=0
    # javab = []
    if request.method == 'POST':
        msg = request.get_json()
        chat_id = get_chat_id(msg)
        text = msg['message'].get('text' , '')
        #return Response('ok' , status=200)
        if text == '/start':
            sendMessage(chat_id , guide_note)
        elif text == '/start_quiz':
            users = read_json()
            user_id = msg['message']['from']['id']
            users[user_id] = []
            question = questions[0][0] + questions[0][1]
            sendMessage(chat_id , question)
            write_json(users)
        elif text.isdigit()==True:
            users = read_json()
            user_id = msg['message']['from']['id']
            print(users , user_id)
            print(len(users[str(user_id)]))
            if int(text) == answers[len(users[str(user_id)])]:
                users[str(user_id)].append((int(text) , True))
            else:
                users[str(user_id)].append((int(text) , False))
            write_json(users)
            users = read_json()
            if len(users[str(user_id)]) != 25:
                question = questions[len(users[str(user_id)])][0] + questions[len(users[str(user_id)])][1]
                sendMessage(chat_id , question)
            else:
                emtiaz = 0
                for i in users[str(user_id)]:
                    if i[1]==True:
                        emtiaz += 1
                if emtiaz>=0 and emtiaz<=10:
                    sendMessage(chat_id , "WORK HARDER !!!")
                    sendMessage(chat_id , f'Your score is : {emtiaz} >> BEGINNER <<')
                elif emtiaz>10 and emtiaz<=12 :
                    sendMessage(chat_id , f'Your score is : {emtiaz} >> BEGINNER-INTERMEDIATE <<')
                elif emtiaz>12 and emtiaz<=15:
                    sendMessage(chat_id , f'Your score is : {emtiaz} >> INTERMEDIATE <<')
                elif emtiaz>15 and emtiaz<=17:
                    sendMessage(chat_id , f'Your score is : {emtiaz} >> INTERMEDIATE-UpperINTERMEDIATE <<')
                elif emtiaz>17 and emtiaz<=19:
                    sendMessage(chat_id , f'Your score is : {emtiaz} >> UpperINTERMEDIATE <<')
                elif emtiaz>19 and emtiaz<=21:
                    sendMessage(chat_id , f'Your score is : {emtiaz} >> UpperINTERMEDIATE-ADVANCED <<')
                elif emtiaz==22 :
                    sendMessage(chat_id , f'Your score is : {emtiaz} >> ADVANCED-UpperADVANCED <<')
                else:
                    sendMessage(chat_id , "WELL-DONE")
                    sendMessage(chat_id , f'Your score is : {emtiaz} >> UpperADVANCED <<')

        return Response('ok' , status=200)
    else:
        return "<h1>Welcome</h1>"

write_json({})
app.run(debug=True)