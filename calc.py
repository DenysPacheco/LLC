def calc(string, debug=True):

    method = string.split(' ')[0]
    args = string.split(' ')[1:]

    console = lambda *msg: print(*msg) if debug else None
    '''
    def log(*msg):
        if debug:
            print(*msg)
    '''

    _funcs = {
        'sum': '+',
        'div': '//',
        'mult': '*',
        'sub': '-',
        'pow': '**',
        'rem': '%',
    }

    console('-'*15)
    console(string)
    func = _funcs[method].join(args)
    console(func)
    result = eval(func)
    console(result)
    console('-'*15)
    console()

    return result


calc('sum 1 2 3')
calc('div 10 2 3')
calc('mult 3 3 2')
calc('sub 4 11 +3')
calc('pow 2 3 2')
calc('rem 10 4 1')
