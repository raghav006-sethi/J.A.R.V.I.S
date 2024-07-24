def reminder(query):
    query=query.partition('reminder')[2]
    print(query)
    file=open('reminders.txt','a+')
    file.write(query)

reminder('set reminder for cooking the eggs')