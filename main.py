'''
This is the chef's assistant program
It creatively offers substitutes for an ingredient of you choice

How to run:
python main.py <ingredient> <creativity-level>

Available ingredients can be found in: frames.py

'''

# imports
import sys
from reasoner import *
from frames import *
from semnet import Semnet




def read_ingreds(ingred_file):
    with open(ingred_file, 'r') as f:
        lines = f.readlines()

    return [str(line).strip() for line in lines]




def get_replacements(ingred, creative_level):

    semnet = Semnet()
    path = semnet.get_path(semnet.head, ingred)
    search_start = path[-creative_level]
    return semnet.get_subs(search_start, ingred)




def gen_wm(ingred, sub):

    def to_lisp(ingr):

        rels_list = list()
        for rel, val in ingr.rels:
            rels_list.append(' '.join([rel, ingr.name, val]))

        atts_list = list()
        for att, val in ingr.atts:
            atts_list.append(' '.join([att, ingr.name, val]))

        return rels_list + atts_list

    return ['ingr {}'.format(ingred.name)] + to_lisp(ingred) + ['sub {}'.format(sub.name)] + to_lisp(sub)






def chefs_assistant():

    try:
        ingred_name = sys.argv[1]
        creativity_level = int(sys.argv[2])
    except IndexError:
        print('Wrong number of args. Setting ingredients and creativity level to defaults.\n\n')
        ingred_name = 'arugula'
        creativity_level = 1


    semnet = Semnet()
    ingred = semnet.get_ingred(ingred_name)
    potential_reps = get_replacements(ingred.name, creativity_level)
    working_mems = [gen_wm(ingred, pr) for pr in potential_reps]
    # pass working mems to reasoner, collect results
    rules_matches = [match_rules(wm, RULES) for wm in working_mems]

    # pick between results and print explanation
    final_choices = list()
    for i, matches in enumerate(rules_matches):
        score = 0
        explanation = list()
        for match in matches:
            cons = match[0].split()
            explanation.append(' '.join(cons[:-1]))
            score += float(cons[-1])

        final_choices.append((potential_reps[i].name, score, explanation))



    best_choice = max(final_choices, key=lambda x: x[1])
    name, score, explanation = best_choice

    print('Recommended Substitution: ', name)
    print('Because: ')
    for line in explanation:
        print('\t' + line)

    print('\n\n')







if __name__ == '__main__':


    chefs_assistant()
