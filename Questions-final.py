questions = list()
a = "1. When can we meet again?\n"
b = "A)When are you free?\nB)It was two days ago.\nC)Can you help me?"
questions.append((a , b))
# print(questions)
a = "2. My aunt is going to stay with me.\n"
b = "A)How do you do?\nB)How long for?\nC)How was it?"
questions.append((a , b))
a = "3. When do you study?\n"
b = "A)at school\nB)in the evenings\nC)in the library"
questions.append((a , b))
a = "4. Would you prefer lemonade or orange juice?\n"
b = "A)Have you got anything else?\nB)If you like.\nC)Are you sure about that?"
questions.append((a , b))
# print(len(questions))
a = "5. Let’s have dinner now.\n"
b = "A)You aren't eating.\nB)There aren't any.\nC)Tom isn't here yet"
questions.append((a , b))
a = "6. The snow was …… heavily when I left the house.\n"
b = "A)dropping\nB)landing\nC)falling\nD)descending"
questions.append((a , b))
a = "7. I can’t find my keys anywhere – I …… have left them at work.\n"
b = "A)can\nB)must\nC)ought\nD)would"
questions.append((a , b))
a = "8. When a car pulled out in front of her, Jane did well not to …… control of her bicycle.\n"
b = "A)miss\nB)lose\nC)fail\nD)drop"
questions.append((a , b))
a = "9. According to Richard’s …… the train leaves at 7 o’clock.\n"
b = "A)opinion\nB)advice\nC)knowledge\nD)information"
questions.append((a , b))
a = "10. When you stay in a country for some time you get used to the people’s …… of life.\n"
b = "A)habit\nB)custom\nC)way\nD)system"
questions.append((a , b))
a = "11. The builders are …… good progress with the new house.\n"
b = "A)getting\nB)doing\nC)making\nD)taking"
questions.append((a , b))
a = "12. She is now taking a more positive …… to her studies and should do well.\n"
b = "A)attitude\nB)behavior\nC)manner\nD)style"
questions.append((a , b))
a = "13. My father …… his new car for two weeks now.\n"
b = "A)has had\nB)has\nC)is having\nD)had"
questions.append((a , b))
a = "14. What differences are there …… the English spoken in the UK and the English spoken in the US?\n"
b = "A)among\nB)between\nC)beside\nD)with"
questions.append((a , b))
a = "15. At 6 p.m. I started to get angry with him because he was late ……\n"
b = "A)as usual.\nB)in general.\nC)typically.\nD)usually."
questions.append((a , b))
a = "16. …… you get your father’s permission, I’ll take you skiing next weekend.\n"
b = "A)Although\nB)provided\nC)as\nD)unless"
questions.append((a , b))
a = "17. A local company has agreed to …… the school team with football shirts.\n"
b = "A)contribute\nB)supply\nC)give\nD)produce"
questions.append((a , b))
a = "18. I really enjoy stories that are …… in the distant future.\n"
b = "A)found\nB)set\nC)put\nD)placed"
questions.append((a , b))
a = "19. That old saucepan will come in …… when we go camping.\n"
b = "A)convenient\nB)fitting\nC)handy\nD)suitable"
questions.append((a , b))
a = "20. Anyone …… after the start of the play is not allowed in until the interval.\n"
b = "A)arrives\nB)has arrived\nC)arriving\nD)arrived"
questions.append((a , b))
a = "21. I didn’t …… driving home in the storm so I stayed overnight in a hotel.\n"
b = "A)fancy\nB)desire\nC)prefer\nD)want"
questions.append((a , b))
a = "22. The judge said that those prepared to…… in crime must be ready to suffer the consequences.\n"
b = "A)involve\nB)engage\nC)undertake\nD)enlist"
questions.append((a , b))
a = "23. Marianne seemed to take …… at my comments on her work.\n"
b = "A)annoyance\nB)insult\nC)offense\nD)indignation"
questions.append((a , b))
a = "24. You should not have a dog if you are not …… to look after it.\n"
b = "A)prepared\nB)adopted\nC)arranged\nD)decided"
questions.append((a , b))
a = "25. The farmhouse was so isolated that they had to generate their own electricity ……\n"
b = "A)current.\nB)supply.\nC)grid.\nD)power."
questions.append((a , b))

# print(questions)

answers = [1 , 2 , 2 , 1 , 3 , 3 , 2 , 2 , 4 , 3 , 3 , 1 , 1 , 2 , 1 , 2 , 2 , 2 , 3 , 3 , 1 , 2 , 3 , 1 , 2]
print(len(questions))

f = open("final_questions.txt" , 'w')
f.write(str(questions))
f.close()