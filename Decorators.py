# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True
}

def authenticated(fn): # WE HAVE TO CALL fn IN THE WRAPPER, NOT message_friends
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
        # IF CALL message_friends HERE -> RECURSION
        return fn(*args, **kwargs) # WE HAVE TO CALL fn IN THE WRAPPER, NOT message_friends
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
