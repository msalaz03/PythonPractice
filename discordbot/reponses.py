
import random

def handle_reponse(message) -> str:
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'Hey There!'
    
    if p_message == 'roll':
        return str(random.randint(1,6))
    
    if p_message == '!help':
        return "`These are of the follow commands available`\n/remind create \n/remind delete \n/remind info"


