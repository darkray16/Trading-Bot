import CommandFactory
"""
Determines and returns the correct command
according to the type of command passed to this
instance.  if none then determines it.
"""
def get_command(request):
    if not request:
        cmd = determine_client_state()
    else:
        cmd = request
    new_cmd = CommandFactory.make_command(cmd)
    
    return new_cmd

def determine_client_state():
    """
    do some stuff to determine at what point in the client
    we are, e.g. logging in, buying, selling, etc.
    """
    for state, img in ImageHelper.client_states():
        if ViewHelper.find(img):
            client_state = state
    if not client_state:
        CommandError("CommandResolve could not determine client state")
    else:
        return client_state