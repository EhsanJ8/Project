questions = list()
# questions.append({'A: Excuse me, where is my bag?\nB:' : "A) It's yellow and green.\nB) It's over there on the chair.\nC) It's not very big.\nD)It's thirty dollors."})
questions.append(("A: Excuse me, where is my bag?\nB:\n" , "A) It's yellow and green.\nB) It's over there on the chair.\nC) It's not very big.\nD)It's thirty dollors."))

# print(questions[0][0] , questions[0][1])
a = "I have two ------- and one brother\n"
b = "A) sisters\nB) girls\nC) women\nD) mothers"
questions.append((a , b))
# print(questions)
a = "The office is ------ Hall Street.\n"
b = "A) by\nB) at\nC)in\nD) on"
questions.append((a , b))
# print(questions)
a = "Sara is ------ red shoes.\n"
b = "A) playing\nB) wearing\nC) reading\nD) making"
questions.append((a , b))
# print(questions)
a = "This car is ------. It costs $500,00.\n"
b = "A) safe\nB) empty\nC) expensive\nD) difficult"
questions.append((a , b))
a = "A: I can't play tennis very well.\nB: I can't ------.\n"
b = "A) too\nB) either\nC) neither\nD) so"
questions.append((a , b))
a = "Cats, dogs, and horses are ------.\n"
b = "A) animals\nB) places\nC) numbers\nD) holidays"
questions.append((a , b))
a = "A: Can I help you with your suitcase?\nB: -------\n"
b = "A) Sure, here you are.\nB) All right, let's go.\nC) No thanks. Ihave to go now.\nD) No,it's OK. Thanks."
questions.append((a , b))
a = "Those flowers are -------.\n"
b = "A) empty\nB) busy\nC) beautiful\nD) safe"
questions.append((a , b))
a = "The woman is ------- the bag she lost.\n"
b = "A) opnening\nB) breaking\nC) describing\nD) visiting"
questions.append((a , b))
a = "Canadian Daniel Smith ------- the gold medal.\n"
b = "A) looked\nB) pushed\nC) won\nD) spent"
questions.append((a , b))
a = "The movie was really ------.\n"
b = "A) bored\nB) boredom\nC) bore\nD) boring"
questions.append((a , b))
# print(len(questions))
a = "A: What are your plans for this weekend?\nB: -----\n"
b = "A) Let me see. I remember going to a friend's house\nB) Idon't know. I'll probably stay at home.\nC) Ican't believe it. The weekend goes so quickly.\nD) I'm not sure if my parents would agree."
questions.append((a , b))
a = "It is -------- to drive a car in crowded cities.\n"
b = "A) intelligent\nB) friendly\nC) generous\nD) dangerous"
questions.append((a , b))
a = "I am really looking ------- to seeing you this weekend.\n"
b = "A) after\nB) around\nC) through\nD) forward"
questions.append((a , b))
# print(len(questions))
a = "Terry ----- to the good news by happily jumping up and down.\n"
b = "A) reacted\nB) earned\nC) applied\nD) invested"
questions.append((a , b))
a = "A: Dave, I'm really sad about failing the entrance exam.\nB: Cheer up! ------\n"
b = "A) It lived up to all our expectations.\nB) Keep up the good work.\nC) It's not the end of the world.\nD) You made a right mess of that."
questions.append((a , b))
a = "The sooner you take care of a problem,-------- it is to solve it.\n"
b = "A) the easiest\nB) easy\nC) the easier\nD) the easy"
questions.append((a , b))
a = "Who is in ---------- of the office while the boss is away?\n"
b = "A) check\nB) channel\nC) chance\nD) charge"
questions.append((a , b))
a = "It is ------- to have to wait so long for the next step.\n"
b = "A) impatient\nB) frustrating\nC) sensitive\nD) similar"
questions.append((a , b))
a = "Prof. Jones suggested that Kelly ---------- working on a new project.\n"
b = "A) starting\nB) is started\nC) has started\nD) start"
questions.append((a , b))
a = "The witness helped the police by giving them a(n) --------- description of the thieves.\n"
b ="A) accurate\nB) guilty\nC) irritated\nD) conscious"
questions.append((a , b))
# print(questions)
a = "A: Can you give me a hand with this?\nB: Sorry, ------\n"
b = "A) I've had a change of heart\nB) I'm a bit tied up right now.\nC) I can't work up any enthusuasm for it.\nD) I'd rather not talk about it."
questions.append((a , b))
a = "The company makes huge ------- on the cars it sells every year.\n"
b = "A) profits\nB) costs\nC) taxes\nD) credits"
questions.append((a , b))
a = "Paul has tried hard to --------- everyone with his knowledge and skills.\n"
b = "A) succeed\nB) retire\nC) impress\nD) expect"
questions.append((a , b))
a = "The speaker's -------- voice began to put me to sleep during the meeting.\n"
b = "A) eccentric\nB) monotonous\nC) hilarious\nD) haunting"
questions.append((a , b))
a = "The soldiers were forced to-------- due to the bad weather conditions.\n"
b = "A) survive\nB) withdraw\nC) outlaw\nD) celebrate"
questions.append((a , b))
a = "A: What is your attitude to the idea of living in the countryside?\nB: -------\n"
b = "A) I'm afraid it does not appeal to me.\nB) That's one way of putting it.\nC) That's a weight off my mind.\nD) I'd stake my life on it."
questions.append((a , b))
a = "Fred has formed a ------- with his brother-in-law as part of a family business.\n"
b = "A) treatment\nB) estimation\nC) partnership\nD) demonstration"
questions.append((a , b))
a = "The children are used -------- swimming on weekends.\n"
b = "A) go\nB) to going\nC) going\nD) to go"
questions.append((a , b))

f = open("questions.txt" , 'w')
f.write(str(questions))
f.close()
# print(*questions[0])

# for i in questions:
#     print(*i[0] , *i[1])