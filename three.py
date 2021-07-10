# from os import truncate
# from flask.scaffold import F
import requests
import json
from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)


English1 = [('1. When can we meet again?\n', 'A)When are you free?\nB)It was two days ago.\nC)Can you help me?'), ('2. My aunt is going to stay with me.\n', 'A)How do you do?\nB)How long for?\nC)How was it?'), ('3. When do you study?\n', 'A)at school\nB)in the evenings\nC)in the library'), ('4. Would you prefer lemonade or orange juice?\n', 'A)Have you got anything else?\nB)If you like.\nC)Are you sure about that?'), ('5. Let’s have dinner now.\n', "A)You aren't eating.\nB)There aren't any.\nC)Tom isn't here yet"), ('6. The snow was …… heavily when I left the house.\n', 'A)dropping\nB)landing\nC)falling\nD)descending'), ('7. I can’t find my keys anywhere – I …… have left them at work.\n', 'A)can\nB)must\nC)ought\nD)would'), ('8. When a car pulled out in front of her, Jane did well not to …… control of her bicycle.\n', 'A)miss\nB)lose\nC)fail\nD)drop'), ('9. According to Richard’s …… the train leaves at 7 o’clock.\n', 'A)opinion\nB)advice\nC)knowledge\nD)information'), ('10. When you stay in a country for some time you get used to the people’s …… of life.\n', 'A)habit\nB)custom\nC)way\nD)system'), ('11. The builders are …… good progress with the new house.\n', 'A)getting\nB)doing\nC)making\nD)taking'), ('12. She is now taking a more positive …… to her studies and should do well.\n', 'A)attitude\nB)behavior\nC)manner\nD)style'), ('13. My father …… his new car for two weeks now.\n', 'A)has had\nB)has\nC)is having\nD)had'), ('14. What differences are there …… the English spoken in the UK and the English spoken in the US?\n', 'A)among\nB)between\nC)beside\nD)with'), ('15. At 6 p.m. I started to get angry with him because he was late ……\n', 'A)as usual.\nB)in general.\nC)typically.\nD)usually.'), ('16. …… you get your father’s permission, I’ll take you skiing next weekend.\n', 'A)Although\nB)provided\nC)as\nD)unless'), ('17. A local company has agreed to …… the school team with football shirts.\n', 'A)contribute\nB)supply\nC)give\nD)produce'), ('18. I really enjoy stories that are …… in the distant future.\n', 'A)found\nB)set\nC)put\nD)placed'), ('19. That old saucepan will come in …… when we go camping.\n', 'A)convenient\nB)fitting\nC)handy\nD)suitable'), ('20. Anyone …… after the start of the play is not allowed in until the interval.\n', 'A)arrives\nB)has arrived\nC)arriving\nD)arrived'), ('21. I didn’t …… driving home in the storm so I stayed overnight in a hotel.\n', 'A)fancy\nB)desire\nC)prefer\nD)want'), ('22. The judge said that those prepared to…… in crime must be ready to suffer the consequences.\n', 'A)involve\nB)engage\nC)undertake\nD)enlist'), ('23. Marianne seemed to take …… at my comments on her work.\n', 'A)annoyance\nB)insult\nC)offense\nD)indignation'), ('24. You should not have a dog if you are not …… to look after it.\n', 'A)prepared\nB)adopted\nC)arranged\nD)decided'), ('25. The farmhouse was so isolated that they had to generate their own electricity ……\n', 'A)current.\nB)supply.\nC)grid.\nD)power.')]
# English1 = [('1. When can we meet again?\n', 'A)When are you free?\nB)It was two days ago.\nC)Can you help me?'), ('2. My aunt is going to stay with me.\n', 'A)How do you do?\nB)How long for?\nC)How was it?')]
answers_English1 =[1 , 2 , 2 , 1 , 3 , 3 , 2 , 2 , 4 , 3 , 3 , 1 , 1 , 2 , 1 , 2 , 2 , 2 , 3 , 3 , 1 , 2 , 3 , 1 , 2]
# answers_English1 =[1 , 2]
English2 = [('1.Are you German?\nYes, ....\n', 'A)you are German\nB)I am\nC)he is'), ('2. Are you and your friends German?....\n', 'A)Yes, we are\nB)Yes, I am\nC)Yes, they are'), ("3. Mary: How do you do?\nJohn: I am fine. ....\n", "A)How do you do?\nB)How are you?\nC)I'm a businessman."), ("4. ...\n-He's my father\n", "A)Who are they\nB)Where is he?\nC)Who is this?"), ("5. What's your name?\n... John.\n", "A)My name is\nB)My names are\nC)Your name is"), ('6.Hello Silvia, how are you?\n....\n', "A)I'm very good\nB)I'm fine\nC)Me is fine"), ('7.Are you from England?\n', "A)No, I don't\nB)Yes, you are\nC)No, I'm not"), ("8.There's John and ... wife.\n", "A)his\nB)he's\nC)its"), ('9.They are going to GB with ... son.\n', 'A)there\nB)her\nC)their'), ('10.Where is Susan going?\n... going to London.\n', "A)They're\nB)She's\nC)Susan does"), ('11.What are you doing?\n....\n', "A)I'm a manager\nB)I'm drinking coffee\nC)You're going to London"), ('12.Look! There are the Smiths.\nYes, ... for a house in this neighborhood.\n', "A)they are looking\nB)they look\nC)she's looking"), ('13.Do you speak English?\nYes, ....\n', 'A)I cannot\nB)I do\nC)I can'), ('14.Are you looking for a room?\n....\n', 'A)Yes, we can\nB)Yes, you are\nC)Yes, I am'), ("15.Where are you going?\nI'm going ... Piccadilly Circus\n", 'A)To\nB)Near\nC)In'), ("16.Where's Susan?\nShe's ... holiday.\n", 'A)in\nB)on\nC)by'), ("17.Look! There's Liza.\nShe's ... the street.\n", 'A)in\nB)at\nC)into'), ('18.Can I help you?\nYes, ... a cup of coffee, please.\n', "A)I'd like\nB)I will\nC)give me"), ("19.The postman always ... at 7 o'clock.\n", 'A)is coming\nB)comes\nC)come'), ('20.Cigarette?\nNo thanks, ...\n', "A)I don't smoke\nB)I'm not smoking\nC)I smoke not"), ('21.My suitcase is heavy but yours is ....\n', 'A)more heavy\nB)heavier\nC)heavyer'), ('22.Volkswagens are expensive, but Rolls Royces are ....\n', 'A)more expensive\nB)expensiver\nC)more expensiver'), ("23.It's ... expensive car.\n", 'A)one\nB)a\nC)an'), ("24.He's buying ... new house.\n", 'A)one\nB)a\nC)an'), ("25.Don't go near the river!\nYou can't ....\n", 'A)to swim\nB)swimming\nC)swim') ,('26.Next Monday Susan ... Eric.\n', 'A)visits\nB)is going to visit\nC)goes to visit'), ("27.... swimming because I haven't got the time today.\n", "A)I'm not going\nB)I don't go\nC)I go not"), ('28.... a newspaper?\n', 'A)Have you got\nB)You have\nC)You get'), ("29.She's got a big car.\nOh no, she ...\n", "A)doesn't!\nB)isn't!\nC)hasn't!"), ('30.What time ... to work every day?\n', "A)you go\nB)do you go\nC)are you going"), ('31.This is a hospital waiting-room.\n', "A)Don't smoke!\nB)Not smoking!\nC)Don't smoking!"), ('32.This is my husband.\nOh, where ...\n', 'A)do he works?\nB)does he work?\nC)works he?'), ("33.He's a bad singer but his brother is ....\n", 'A)more bad\nB)worst\nC)worse'), ("34.This car isn't ... that car.\n", 'A)as fast than\nB)as fast as\nC)so fast than'), ('35.Are ... your books over there?\n', 'A)those\nB)these\nC)that'), ('36.Will you be at my party?\n', "A)No, I won't\nB)No, I will\nC)No, I'm not"), ('37.My husband goes to work at 9 and ... home until 6.\n', "A)don't come\nB)doesn't come\nC)don't comes"), ('38.Mr. Clark smokes cigarettes.\nWhat ....\n', 'A)does he smoke?\nB)smokes he?\nC)he smokes?'), ("39.I'm looking ... my pen.\n", "A)after\nB)for\nC)about"), ("40.I'm waiting for someone.\n", "A)For who are you waiting?\nB)Who is waiting for you?\nC)Who are you waiting for?"), ('41.Do you have... apples?\n', 'A)some\nB)any\nC)a'), ("42.I don't have ... money on me.\n", 'A)some\nB)any\nC)the'), ('43.No letters yet?\nWhen ....\n', 'A)does come the postman?\nB)comes the postman?\nC)does the postman come?'), ("44.He's a very bad driver.\nHe drives very ....\n", 'A)dangerously\nB)dangerous\nC)bad'), ("45.And he's a fast driver.\nYes, he drives very ....\n", 'A)faster\nB)fastly\nC)fast'), ("46.He's from Italy, ....\n", "A)doesn't he?\nB)isn't he?\nC)hasn't he?"), ("47.That's nice and it isn't expensive.\n....\n", "A)Isn't it?\nB)Is it?\nC)Isn't that?"), ('48.I got it yesterday.\nOh really, ...\n', 'A)how did you get it?\nB)how do you get it?\nC)how you got it?'), ('49.Where did you find the money?\nI ... it in the street.\n', 'A)founded\nB)did find\nC)found'), ('50.When ... in Spain?\n', 'A)did you be\nB)was you\nC)were you') ,('51. ... Matcha Tea?\n', 'A)Have you ever tried\nB)Did you ever try\nC)Have you ever try'), ('52.My wife and I ... married since 1980.\n', 'A)were\nB)have been\nC)are'), ("53.I've had this car ....\n", 'A)for six years\nB)since six years\nC)six years ago'), ('54.When ... the film?\n', 'A)did you see\nB)have you seen\nC)you saw'), ("55.He's just arrived.\n... he?\n", "A)Is\nB)Has\nC)Does"), ('56.I really enjoy ....\n', 'A)swimming\nB)it to swim\nC)to swim'), ('57.He talks a lot about ... a new language.\n', 'A)to study\nB)studying\nC)study'), ('58.Would you mind if I ... the window?\n', 'A)opened\nB)would open\nC)open'), ("59.If it's sunny tomorrow ... for a picnic.\n", "A)I go\nB)I am planning to going\nC)I'm going"), ("60.That's the man ... lives next door to me.\n", 'A)that\nB)who\nC)which'), ('61. Is that the man ... wife is ill?\n', 'A)which\nB)who\nC)whose'), ("62.She's the secretary ... I told you about.\n", 'A)which\nB)what\nC)who'), ('63.When the doctor arrived the patient ... already died.\n', 'A)had\nB)has\nC)---'), ('64.I would buy a new car if I ... enough money.\n', 'A)had\nB)would have\nC)did have'), ('65.I would be happy if I ... rich.\n', 'A)would be\nB)am\nC)were'), ('66.If I ... her address I ... her a letter.\n', 'A)would knew / would send\nB)knew / would send\nC)did know / would send'), ('67.I wish my husband ... me with the housework.\n', 'A)would help\nB)helps\nC)did help'), ('68.They always repair their car ....\n', 'A)theirselves\nB)themselves\nC)themself'), ('69.I must wash ... hands.\n', 'A)the\nB)myself\nC)my'), ('70.I know Julie. She knows me.\nWe know ....\n', 'A)ourselves\nB)each other\nC)us')]
javab_english2 = [2,1,1,3,1,2,1,1,3,2,2,1,3,3,1,2,1,1,2,1,2,1,3,2,3,2,1,1,3,2,1,2,3,2,1,1,2,1,2,3,2,2,3,1,3,2,2,1,3,3,1,2,1,1,2,1,2,1,3,2,3,3,1,1,3,2,1,2,3,2]
france = [('1.Vous cherchez une chambre.\nVous allez ....\n', 'A)à l´hôtel\nB)au café\nC)au restaurant'), ('2.Il mange parce qu´il a ....\n', 'A)chaud\nB)faim\nC)soif'), ('3.Vous ... du sport?\n', 'A)aimez\nB)faites\nC)fais'), ('4.Quand monsieur Dubois a soif, ....\n', 'A)nous allons au bureau.\nB)il va au café.\nC)elle va à Paris.'), ('5.Demandez à l´employé la clé de la chambre.\n.... ?\n', "A)Pouvez-vous me montrer ma chambre ?\nB)Puis-je avoir la clé de la chambre S.V.P. ?\nC)Pouvez-vous prendre la clé de la chambre S.V.P. ?"), ('6.Cette maison est très ....\n', 'A)vieille\nB)grand\nC)vieux'), ('7.Où sont les livres de papa?\n... livres sont sur ... bureau.\n', 'A)son - sa\nB)leurs - son\nC)ses - son'), ('8.Vous allez souvent au théâtre?\nJe ne ....\n', 'A)pars pas\nB)le retiens pas\nC)sors jamais le soir'), ('9.Cette veste rouge est à vous madame?\n....\n', 'A)Oui, c´est moi.\nB)Oui, c´est à moi.\nC)Non, pas moi.'), ('10.J´ai besoin d´une voiture.\nC´est pourquoi ....\n', 'A)j´ai acheté une voiture.\nB)je vends ma voiture.\nC)je vais prendre le train.'), ('11.La moto coûte moins cher que la voiture.\n....\n', 'A)Il est aussi cher.\nB)Elle est meilleur marché.\nC)La voiture est meilleur marché.'), ('12.Madame Dupont va faire des courses parce qu´elle ....\n', 'A)a acheté un cheval.\nB)est très sportive.\nC)a besoin d´acheter de la nourriture.'), ('13.Pourquoi voulez-vous acheter cette machine à laver ?\n....\n', 'A)Il est pratique.\nB)Il est moins cher que les autres.\nC)C´est le dernier modèle.'), ('14.Quand êtes-vous arrivés?\n....\n', 'A)Je suis arrivé hier.\nB)Nous sommes arrivés hier.\nC)Il est arrivé à l´hôtel.'), ('15.Il a essayé de garer sa voiture, mais il n´a ....\n', 'A)pas réussi.\nB)pas voulu.\nC)pas demandé.'), ('16.Je vais mettre la robe ... j´ai achetée hier.\n', 'A)qui\nB)que\nC)qu´'), ('17.Demain matin, elle ... le train pour Paris.\n', 'A)prenais\nB)prendra\nC)prendras'), ('18.Un ami ... chez moi demain soir.\n', 'A)venir\nB)viendra\nC)viendrait'), ('19.... tu as invité à ton anniversaire?\n', 'A)Qu´est-ce qui\nB)Qui est-ce que\nC)Qui est-ce qui'), ('20.J´apprécie beaucoup cet endroit, ....\n', 'A)c´est tellement calme.\nB)c´est trop modeste.\nC)elle est sympathique.'), ('21.C´est l´anniversaire de ma mère.\nJe ... téléphone.\n', 'A)la\nB)leur\nC)lui'), ('22.Il y a beaucoup de clients qui attendent dans le magasin.\nLa vendeuse est débordée, elle ....\n', 'A)ne veut pas travailler.\nB)est très fatigué.\nC)a beaucoup de travail.'), ("23.Qui t'a attendu?\n....\n", "A)Je n'ai attendu personne.\nB)Personne ne m'a attendu.\nC)Je ne l'ai pas attendu."), ('24.Quelqu´un a envoyé ces fleurs à Sylvie.\n....\n', 'A)Qui est-ce qui les a envoyés?\nB)Qu´est-ce qu´il a envoyé?\nC)Qui est-ce qui les a envoyées?'), ("25.Si j'ai de l'argent, je ... cent euros.\n", 'A)te donnais\nB)te donnerai\nC)te donnerais') ,('26.Je lui ai téléphoné hier.\nIl m´a dit qu´il ... ce soir à huit heures.\n', 'A)arrivera\nB)arriverai\nC)arriverait'), ('27.Je suis invitée ce weekend.\n....\n', "A)J'ai été invité par Gisèle.\nB)Il l'a invitée.\nC)J'ai été invitée par Jean."), ('28.Si vous ... le temps la semaine prochaine, viendriez-vous à Paris avec moi?\n', 'A)auriez\nB)aviez\nC)avez'), ('29.Pourvu que le représentant ... à l´heure à la réunion de demain.\n', 'A)est\nB)serait\nC)soit'), ('30.Je suis désolé que vous ne ... pas venir à la soirée.\n', "A)pourrez\nB)pouviez\nC)puissiez")]
javab_france = [1,2,2,2,2,1,3,3,2,1,2,3,3,2,1,2,2,2,2,1,3,3,2,3,2,3,3,2,3,3]

url="https://api.telegram.org/bot1818253105:AAGz2CxtcaQabY7Bful3BolJkfXtjh4ymd4/"

guide_note= "This quiz has 25 questions and After each question you should submit your Answer by sending a NUMBER from 1-4 of choices.Send /En_short_quiz or /En_long_quiz or /Fn_quiz to begin. "

guide_note2 = "سلام"

def get_all_updates(): #برای گرفتن پیام ها
    response=requests.get(url + "getUpdates")
    return response.json()

def get_last_update(allupdates):  #برای گرفتن آخرین پیام که از طرف کاربر ارسال شده
    return allupdates["result"][-1]

def get_chat_id(update):
    try:   #برای گرفتن چت آی دی کاربری که پیام را ارسال کرده
        return update["message"]["chat"]["id"]
    except:
        pass
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
    if request.method == 'POST':
        try:
            msg = request.get_json()
            chat_id = get_chat_id(msg)
            try:
                text = msg['message'].get('text' , '')
            except:
                pass
            try:
                first_name = msg['message']['from']['first_name']
            except:
                first_name = 'کاربر'
            guide_note2 = "سلام"+first_name+"عزیز 👋\nبه ربات تعیین سطح زبان خوش آمدید\nاین ربات شامل:\nیک تست انگلیسی کوتاه که شامل 25 سوال سه و چهارگزینه ای: /English_quick_test\nیک تست انگلیسی کامل که شامل 70 سوال سه گزینه ای: /English_test\nو یک تست فرانسوی که شامل 30 تست سه گزینه ای است میباشد: /French_test\nبرای شروع آزمون تست مورد نظر را انتخاب کنید."
            # return Response('ok' , status=200)
            if text == '/start':
                sendMessage(chat_id , guide_note2)
            elif text == '/English_quick_test':
                users = read_json()
                type = read_json("type.json")
                user_id = msg['message']['from']['id']
                users[user_id] = []
                type[user_id] = "En_short_quiz"
                nokat = "آزمون آغاز شد!\nبرای پاسخ به گزینه ها لطفا به ترتیب یکی از اعداد 1 تا 3 یا 1 تا 4 را ارسال کنید"
                question = English1[0][0] + English1[0][1]
                sendMessage(chat_id , nokat)
                sendMessage(chat_id , question)
                write_json(users)
                write_json(type , "type.json")
            elif text == '/English_test':
                users = read_json()
                type = read_json("type.json")
                user_id = msg['message']['from']['id']
                users[user_id] = []
                type[user_id] = "/En_long_quiz"
                question = English2[0][0] + English2[0][1]
                nokat = "آزمون آغاز شد!\nبرای پاسخ به گزینه ها لطفا به ترتیب یکی از اعداد 1 تا 3 یا 1 تا 4 را ارسال کنید"
                sendMessage(chat_id , nokat)
                sendMessage(chat_id , question)
                write_json(users)
                write_json(type , "type.json")
            elif text == '/French_test':
                users = read_json()
                type = read_json("type.json")
                user_id = msg['message']['from']['id']
                users[user_id] = []
                type[user_id] = "/Fn_quiz"
                nokat = "آزمون آغاز شد!\nبرای پاسخ به گزینه ها لطفا به ترتیب یکی از اعداد 1 تا 3 یا 1 تا 4 را ارسال کنید"
                question = france[0][0] + france[0][1]
                sendMessage(chat_id , nokat)
                sendMessage(chat_id , question)
                write_json(users)
                write_json(type , "type.json")

            elif text.isdigit()==True:
                users = read_json()
                type = read_json("type.json")
                user_id = msg['message']['from']['id']
                # print(users , user_id)
                # print(len(users[str(user_id)]))
                if 'short' in type[str(user_id)]:
                    reference = English1
                    answers = answers_English1
                elif 'long' in type[str(user_id)]:
                    reference = English2
                    answers = javab_english2
                else:
                    reference = france
                    answers = javab_france
                # print(len(users[str(user_id)]))
                if int(text) == answers[len(users[str(user_id)])]:
                    users[str(user_id)].append((int(text) , True))
                else:
                    users[str(user_id)].append((int(text) , False))
                write_json(users)
                users = read_json()
                print(len(users[str(user_id)]))
                if len(users[str(user_id)]) != len(answers):
                    question = reference[len(users[str(user_id)])][0] + reference[len(users[str(user_id)])][1]
                    sendMessage(chat_id , question)
                else:
                    emtiaz = 0
                    for i in users[str(user_id)]:
                        if i[1]==True:
                            emtiaz += 1
                    if 'long' in type[str(user_id)]:
                        if emtiaz>=0 and emtiaz<=10:
                            level = 'Beginner'
                        elif emtiaz>10 and emtiaz<=20:
                            level = 'Beginner-Intermediate'
                        elif emtiaz>20 and emtiaz<=30:
                            level = 'Intermediate'
                        elif emtiaz>30 and emtiaz<=40:
                            level = 'Intermediate-Upper Intermediate'
                        elif emtiaz>50 and emtiaz<=60:
                            level = 'Upper Intermediate'
                        elif emtiaz>60 and emtiaz<=70:
                            level = 'Advanced'
                    elif 'Fn' in type[str(user_id)]:
                        if emtiaz>=0 and emtiaz<=10:
                            level = 'débutant'
                        elif emtiaz>10 and emtiaz<=12:
                            level = 'débutant-intermédiaire'
                        elif emtiaz>12 and emtiaz<=15:
                            level = 'intermédiaire'
                        elif emtiaz>15 and emtiaz<=17:
                            level = 'intermédiaire-intermédiaire supérieur'
                        elif emtiaz>17 and emtiaz<=19:
                            level = 'intermédiaire supérieur'
                        elif emtiaz>19 and emtiaz<=21:
                            level = 'intermédiaire supérieur-avancé'
                        elif emtiaz==22:
                            level = 'avancé-maître'
                        else:
                            level = 'maître'
                    else:
                        if emtiaz>=0 and emtiaz<=10:
                            level = 'Beginner'
                        elif emtiaz>10 and emtiaz<=12:
                            level = 'Beginner-Intermediate'
                        elif emtiaz>12 and emtiaz<=15:
                            level = 'Intermediate'
                        elif emtiaz>15 and emtiaz<=17:
                            level = 'Intermediate-Upper Intermediate'
                        elif emtiaz>17 and emtiaz<=19:
                            level = 'Upper Intermediate'
                        elif emtiaz>19 and emtiaz<=21:
                            level = 'UpperIntermediate-Advanced'
                        elif emtiaz==22:
                            level = 'Advanced-Master'
                        else:
                            level = 'Master'

                    karname = "خسته نباشید!\n" + "نمره شما در این آزمون : " + str(emtiaz) + "\nسطح شما : " + level + "\nبرای مشاهده تصحیح آزمونتان /result را بفرستید."
                    sendMessage(chat_id , karname)
            elif text=="/result":
                users = read_json()
                type = read_json("type.json")
                user_id = msg['message']['from']['id']
                if 'short' in type[str(user_id)]:
                    reference = English1
                    answers = answers_English1
                elif 'long' in type[str(user_id)]:
                    reference = English2
                    answers = javab_english2
                else:
                    reference = france
                    answers = javab_france
                if len(users[str(user_id)]) != len(answers):
                    sendMessage(chat_id , "برای مشاهده نتایج باید آزمون را به پایان برسانید!")
                else:
                    index = 0
                    results = ''
                    for j in users[str(user_id)]:
                        if j[1]==False:
                            results += str(index+1)+' : '+'❌'+' ----> Correct answer : '+str(answers[index])+'\n'
                        else:
                            results += str(index+1)+' : '+'✅'+'\n'
                        index += 1
                    sendMessage(chat_id , results)
            return Response('ok' , status=200)
        except:
            return Response('ok' , status = 200)
    else:
        return "<h1>Welcome</h1>"
write_json({} , "type.json")
write_json({})
app.run(debug=True)








