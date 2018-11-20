# dict of responses for each type of intent
intent_response_dict = {
    'greet': ['Hello Mrs!', 'Hello!', 'Hello back!'],
    'goodbye': ['Goodbye!', 'See you later!', 'Have a good day!', 'Take care! Have a nice day!'],
    'thanks': ['You are welcome!', 'Glad you enjoyed it!', 'My pleasure!'],
    'chat': ['I am fine. How about you?', 'I am great!'],
    'affirm': ['Perfect!', 'Great!', 'Ok!'],
    'name': ['My name is ArmyBot. I am your chatbot for today!', 'My name is ArmyBot.'],
    'info': ['I can give info on today\'s medical checkup and some secret videos about military training.'],
    'medical': ['There are 7 stations in total. Aproximative waiting time is currently 2 minutes at station 1-6 and 5 minutes at station 7.',
                'You will undergo a medical check-up at 7 differnt stations. The visit during pick hours can last up to 3 hours but usually is takes less than 1.5h hours.'],
    'military': ['Here you can watch videos about Air Force, Navy and Police military training.'],
}