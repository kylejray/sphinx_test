import sys
import os

sys.path.append(os.path.expanduser('~/source'))

def the_funk(x, **kwargs):
    '''
    gives up the funk
    Parameters
    ---------
    x: str
        input string, 

    Returns
    -------
    returns desire of the funk unless the input is actually, indeed the funk

    '''
    if x=='the funk':
        print('thanks')
    else:
        print('we want the funk')
    return

