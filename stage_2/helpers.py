from clvm import KEYWORD_TO_ATOM


CONS_KW = KEYWORD_TO_ATOM["c"]
QUOTE_KW = KEYWORD_TO_ATOM["q"]
ARGS_KW = KEYWORD_TO_ATOM["a"]


def eval_old(prog, args):
    EVAL_KW = KEYWORD_TO_ATOM["e"]
    return prog.to([EVAL_KW, prog, args])


def eval(prog, args):
    return prog.to([[CONS_KW, prog, args]])


def run(prog, macro_lookup):
    """
    PROG => (e (com (q PROG) (mac)) ARGS)

    The result can be evaluated with the stage_com eval_f
    function.
    """
    args = [ARGS_KW]
    mac = [QUOTE_KW, macro_lookup]
    return eval(prog.to([b"com", prog, mac]), args)


def brun(prog, args):
    return eval(prog.to([QUOTE_KW, prog]), [QUOTE_KW, args])
