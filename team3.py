+####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'CopyCat' # Only 10 chars displayed.
strategy_name = 'Whatever you can do, I can do better'
strategy_description = 'The strategy begins by always betraying the other prisoner, this minimizes the loss in the first round since you could either win big or lose a little compared to winning nothing or losing big if you started with a collude. For the rest of the responses, it will copy what the other user did last. This is geared to beat other programs aiming for a max score but it also sinks to the level of random programs or programs that always choose betray. '
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    if len(my_history) == 0: #Always betray first because I suspect that most people will betray first so by also betraying, I minimize losses
        return 'b'
    elif len(my_history) == 99: #Always betray on the last round
        return 'b'
    else:
        return their_history[-1] #For every other option copy whatever the other person said the last round

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
