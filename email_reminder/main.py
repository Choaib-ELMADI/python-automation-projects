from datetime import date, datetime, timedelta
from utils import send_email, create_server

tasks = [
    {
        "email": "choaib1996elmadi@gmail.com",
        "name": "Choaib 01",
        "task": "Start NodeJs Course",
        "date": "2023-05-05",
        "isDone": False,
    },
    {
        "email": "choaib1996elmadi@gmail.com",
        "name": "Choaib 02",
        "task": "Start Machine Learning Course",
        "date": "2023-05-25",
        "isDone": False,
    },
    {
        "email": "choaib1996elmadi@gmail.com",
        "name": "Choaib 03",
        "task": "Complete The RC Controller",
        "date": "2023-05-23",
        "isDone": False,
    },
    {
        "email": "choaib1996elmadi@gmail.com",
        "name": "Choaib 04",
        "task": "Finish React Docs",
        "date": "2023-05-22",
        "isDone": False,
    },
    {
        "email": "choaib1996elmadi@gmail.com",
        "name": "Choaib 05",
        "task": "Buy The 3d Printer",
        "date": "2023-05-22",
        "isDone": False,
    },
]

server = create_server()
present_plus_one = date.today() + timedelta(1)

for task in tasks:
    format_date = datetime.strptime(task["date"], '%Y-%m-%d').date()

    if (format_date == present_plus_one and not task['isDone']):
        try:
            send_email(server, task['email'], task['name'], datetime.strftime(format_date, "%d, %b %Y"), task['task'])
            print('done')

        except Exception as exp:
            print(f"ERROR, Failed to send the email { exp }")