import re
import prakhar as long
import wikipedia
import streamlit as st



def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True



    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hi there! my name is Saahay. Welcome to Ministry of Home Affairs.Please enter your Amateur Techies Unique ID and password', ['hi', 'hey', 'heyo'], single_response=True)
    response('I am good', ['sup', 'How are you?'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('What type of help are you looking for? Centralized or Departmental.', ['trouble', 'issues', 'troubleshoot', 'troubleshooting'], single_response=True)
    response('Run an SFC scan', ['crashed'], single_response=True)
    response('Reason for ticket?', ['raise', 'ticket', 'queies'], single_response=True)
    response('What type of requirement', ['software','hardware', 'require'], single_response=True)
    response('You can try reaching our toll-free number 1800-123-123-123 or email us at support@MHA.com', ['other', 'problem'], single_response=True)
    response('What is the name of department', ['departmental'], single_response=True)
    response('What type of help can be done for you?', ['foreign', 'border management', 'centre state', 'coordination & international', 'administration', 'disaster management', 'cyber and information security', 'counter terrorism and counter radicalization', 'finance', 'police'], single_response=True)
    #response('Run an SFC scan', ['software', 'crashed'], single_response=True)


    
    # Prakhar
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_ACCESS, ['how', 'get', 'access'], required_words=['get', 'access'])
    #response(long.R_HELP_TYPE, ['centralized', 'departmental'], single_response=True)
   
    response(long.R_UNABLETOLOGIN, ['unable', 'to', 'login'], required_words=['unable', 'login'])
    response(long.R_SOFTWARECRASH, ['software', 'crashed'], required_words=['crashed', 'keeps'])
   
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))

if __name__ == "__main__":
    chatbot_app()