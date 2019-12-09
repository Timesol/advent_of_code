
from itertools import groupby

def get_range():
    range_input=[i for i in range(367479,893698)]

    
    return range_input
    
def has_doubles(n):
    has_double=len(set(str(n))) < len(str(n))
    if has_double:
        return n


def check_proof(with_double,no_smaller_end):
    start_range=[i for i in range(367479,893698)]
    print(len(start_range))
    print(len(with_double))
    print(len(no_smaller_end))


def remove_smaller_ends(number):
    if str(number)[0] <= str(number)[1]:
        if str(number)[1] <= str(number)[2]:
            if str(number)[2] <= str(number)[3]:
                if str(number)[3] <= str(number)[4]:
                    if str(number)[4] <= str(number)[5]:
                        number=get_grouping(number)
                        return number

def get_grouping(number):
    digits=[len(list(group)) for key, group in groupby(str(number))]
    
    if 6 in digits or 5 in digits:
        return None
    else:
        if 4 in digits and 2 not in digits:
            return None
        elif 3 in digits and 2 not in digits:
            return None
        else:
            return number
      

    




result=[i for i in list(map(has_doubles,get_range())) if i is not None]
result_end=[i for i in list(map(remove_smaller_ends,result)) if i is not None]
print(result_end)



check_proof(result,result_end)