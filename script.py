__version__ = "0.0.1"

def calcul_invest_classic(var_multiple, max_invest):
    ratio_classic = 1
    ratio_multiple = 9.72
    var_classic = (max_invest - var_multiple * ratio_multiple)
    return var_classic/ratio_classic


def calcul_invest_multiple(var_classic, max_invest):
    ratio_classic = 1
    ratio_multiple = 9.72
    var_multiple = (max_invest - var_classic * ratio_classic)
    return var_multiple/ratio_multiple


# go classic
## abondement
def abondement(var_classic):
    abondement = 0
    if var_classic <= 250:
        abondement = var_classic*1
    else:
        if var_classic <= 500:
            abondement = 250 + (var_classic - 250)*0.5
        else:
            abondement = 375
    return abondement

## resulat classic
def calcul_classic(var_classic, action_ref, action_final, target_year):
    if var_classic == 0:
        return {'result': 0, 'gain': 0, 'interet': 0, 'var': 0}
    res_abondement = abondement(var_classic)
    invest_classic = var_classic
    invest_classic += res_abondement * (1-0.097) # CSG / CRDS à 9.7%
    invest_classic *= action_ref
    res_classic = (invest_classic/action_ref)*action_final
    gain_classic = res_classic - var_classic
    interet_classic = (res_classic/var_classic)**(1/target_year)
    interet_classic -= 1
    interet_classic *= 100
    return {'result': res_classic, 'gain': gain_classic, 'interet': interet_classic, 'var': var_classic}


# go multiple
def calcul_multiple(var_multiple, action_ref, action_final, target_year):
    if var_multiple == 0:
        return {'result': 0, 'gain': 0, 'interet': 0, 'var': 0}
    gain_multiple = (var_multiple / action_ref) * action_final
    gain_multiple -= var_multiple
    gain_multiple *= 6
    res_multiple = var_multiple + gain_multiple
    interet_multiple = (res_multiple/var_multiple)**(1/target_year)
    interet_multiple -= 1
    interet_multiple *= 100
    return {'result': res_multiple, 'gain': gain_multiple, 'interet': interet_multiple, 'var': var_multiple}


def calcul_total(var_classic, var_multiple, action_ref, action_final, target_year):
    res_classic = calcul_classic(var_classic, action_ref, action_final, target_year)
    res_multiple = calcul_multiple(var_multiple, action_ref, action_final, target_year)
    res_total = res_classic['result'] + res_multiple['result']
    gain_total = res_classic['gain'] + res_multiple['gain']
    interet_total = (res_total/(var_classic+var_multiple))**(1/target_year)
    interet_total -= 1
    interet_total *= 100
    return {'result': res_total, 'gain': gain_total, 'interet': interet_total, 'classic': res_classic, 'multiple': res_multiple}


def ff(v):
    return v['gain']

if __name__ == '__main__':
    remuneration = 25000
    invest = 2000
    action_ref = 1.24
    action_final = 1.4

    import argparse
    parser = argparse.ArgumentParser(
        prog='Go Suez Optimizer 2025',
        description='''
            Become rich by being lazy! This program computes for you the best way to invest your money with Go Suez. It's basically like free financial consulting (well, not quite ^<^).
            ''',
        epilog='=== SUEZ 2025 ===',
        exit_on_error=True,
        add_help=False
    )
    # tools
    parser.add_argument('-h', '--help',
        action='help', 
        help="Display this message")
    parser.add_argument('-v', '--version', 
        action='version', 
        help="Script version",
        version=__version__)
    
    # optional
    parser.add_argument('-s', '--salary', 
        type=int, 
        help="This is your raw yearly income before tax (default: 25000)")
    parser.add_argument('-i', '--investment',
        type=int,
        help="Specify the amount of money you want to invest (default: 2000)")
    parser.add_argument('-p', '--price',
        type=float,
        help="Indicate the bond price estimated in 5 years (default: 1.4)")

    args = parser.parse_args()
    if args.salary:
        remuneration = int(args.salary)
    if args.investment:
        invest = int(args.investment)
    if args.price:
        action_final = float(args.price)

    target_year = 5
    max_invest = remuneration * 0.25

    vals_multiple = list(range(0, int(min(calcul_invest_multiple(0, max_invest), invest))))
    vals_classic = [min(calcul_invest_classic(i, max_invest), invest-i) for i in vals_multiple]

    res = []
    for i in range(len(vals_classic)):
        res.append(calcul_total(vals_classic[i], vals_multiple[i], action_ref, action_final, target_year))

    result = max(res, key=ff)
    print("~=< Suez Go Optimizer >=~")
    print("You should invest as follows:")
    print("- Classic: {:.2f}€".format(result['classic']['var']))
    print('\tresult: {:.2f}€ ({:.2f}%)'.format(result['classic']['result'], result['classic']['interet']))
    print("- Multiple: {:.2f}€".format(result['multiple']['var']))
    print('\tresult: {:.2f}€ ({:.2f}%)'.format(result['multiple']['result'], result['multiple']['interet']))
    print("- Total: {:.2f}€ (".format(result['result'])+('+' if result['gain']>=0 else '-')+'{:.2f}€ @ {:.2f}%)'.format(result['gain'], result['interet']))
