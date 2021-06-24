
'''
unify and unify-var are courtesy of:

https://github.com/vsraptor/bi/blob/master/lib/bi_engine.py
'''







RULES = [
        # tastes:
        # tangy, sweet, earthy, bitter, nutty
        ('#1 Both ingredients have a tangy taste.',
            ['ingr ?ingr', 'sub ?sub', 'has-taste ?ingr tangy', 'has-taste ?sub tangy'], # if
            ['both-have-similar-taste ?ingr ?sub tangy 1.0'] # then
        ),
        ('#2 Both ingredients have a sweet taste.',
            ['ingr ?ingr', 'sub ?sub', 'has-taste ?ingr sweet', 'has-taste ?sub sweet'], # if
            ['both-have-similar-taste ?ingr ?sub sweet 1.0'] # then
        ),
        ('#3 Both ingredients have a earthy taste.',
            ['ingr ?ingr', 'sub ?sub', 'has-taste ?ingr earthy', 'has-taste ?sub earthy'], # if
            ['both-have-similar-taste ?ingr ?sub earthy 1.0'] # then
        ),
        ('#4 Both ingredients have a bitter taste.',
            ['ingr ?ingr', 'sub ?sub', 'has-taste ?ingr bitter', 'has-taste ?sub bitter'], # if
            ['both-have-similar-taste ?ingr ?sub bitter 1.0'] # then
        ),
        ('#5 Both ingredients have a nutty taste.',
            ['ingr ?ingr', 'sub ?sub', 'has-taste ?ingr nutty', 'has-taste ?sub nutty'], # if
            ['both-have-similar-taste ?ingr ?sub nutty 1.0'] # then
        ),


        # textures: has-texture
        # crunchy, gritty, chewy, tender
        ('#6 Both ingredients have a crunchy texture.',
            ['ingr ?ingr', 'sub ?sub', 'has-texture ?ingr crunchy', 'has-texture ?sub crunchy'], # if
            ['both-have-similar-texture ?ingr ?sub crunchy .8'] # then
        ),
        ('#7 Both ingredients have a gritty texture.',
            ['ingr ?ingr', 'sub ?sub', 'has-texture ?ingr gritty', 'has-texture ?sub gritty'], # if
            ['both-have-similar-texture ?ingr ?sub gritty .8'] # then
        ),
        ('#8 Both ingredients have a chewy texture.',
            ['ingr ?ingr', 'sub ?sub', 'has-texture ?ingr chewy', 'has-texture ?sub chewy'], # if
            ['both-have-similar-texture ?ingr ?sub chewy .8'] # then
        ),
        ('#9 Both ingredients have a tender texture.',
            ['ingr ?ingr', 'sub ?sub', 'has-texture ?ingr tender', 'has-texture ?sub tender'], # if
            ['both-have-similar-texture ?ingr ?sub tender .8'] # then
        ),


        # density: has-density
        # medium, dense, airy
        ('#10 Both ingredients have an airy density.',
            ['ingr ?ingr', 'sub ?sub', 'has-density ?ingr airy', 'has-density ?sub airy'], # if
            ['both-have-similar-density ?ingr ?sub airy .6'] # then
        ),
        ('#11 Both ingredients have a medium density.',
            ['ingr ?ingr', 'sub ?sub', 'has-density ?ingr medium', 'has-density ?sub medium'], # if
            ['both-have-similar-density ?ingr ?sub medium .6'] # then
        ),
        ('#12 Both ingredients are dense.',
            ['ingr ?ingr', 'sub ?sub', 'has-density ?ingr dense', 'has-density ?sub dense'], # if
            ['both-have-similar-density ?ingr ?sub dense .6'] # then
        ),


        # taste strenght:
        # subtle, medium, strong,
        ('#13 Both ingredients have a strong taste.',
            ['ingr ?ingr', 'sub ?sub', 'has-taste-strength ?ingr strong', 'has-taste-strength ?sub strong'], # if
            ['both-have-similar-taste-strength ?ingr ?sub strong .4'] # then
        ),
        ('#14 Both ingredients have a medium strength taste.',
            ['ingr ?ingr', 'sub ?sub', 'has-taste-strength ?ingr medium', 'has-taste-strength ?sub medium'], # if
            ['both-have-similar-taste-strength ?ingr ?sub medium .4'] # then
        ),
        ('#15 Both ingredients have a subtle taste.',
            ['ingr ?ingr', 'sub ?sub', 'has-taste-strength ?ingr subtle', 'has-taste-strength ?sub subtle'], # if
            ['both-have-similar-taste-strength ?ingr ?sub subtle .4'] # then
        ),


        # color: has-color
        # white, orange, purple, light-green, dark-green
        ('#16 Both ingredients are the color white.',
            ['ingr ?ingr', 'sub ?sub', 'has-color ?ingr white', 'has-color ?sub white'], # if
            ['both-have-similar-color ?ingr ?sub white .2'] # then
        ),
        ('#17 Both ingredients are the color orange.',
            ['ingr ?ingr', 'sub ?sub', 'has-color ?ingr orange', 'has-color ?sub orange'], # if
            ['both-have-similar-color ?ingr ?sub orange .2'] # then
        ),
        ('#18 Both ingredients are the color purple.',
            ['ingr ?ingr', 'sub ?sub', 'has-color ?ingr purple', 'has-color ?sub purple'], # if
            ['both-have-similar-color ?ingr ?sub purple .2'] # then
        ),
        ('#19 Both ingredients are the color light-green.',
            ['ingr ?ingr', 'sub ?sub', 'has-color ?ingr light-green', 'has-color ?sub light-green'], # if
            ['both-have-similar-color ?ingr ?sub light-green .2'] # then
        ),
        ('#20 Both ingredients are the color dark-green.',
            ['ingr ?ingr', 'sub ?sub', 'has-color ?ingr dark-green', 'has-color ?sub dark-green'], # if
            ['both-have-similar-color ?ingr ?sub dark-green .2'] # then
        )
]


# checks whether an element is a variable (as opposed to a constant)
# takes
# - elem: string
# returns
# - boolean
#
def is_var(elem):
    if (elem[0] == '?'):
        return True



# substitutes variables from the given pattern according to the substitution table given it
# takes
# - subs: substitution tabel (dictionary)
# - pat: pattern into which substitutions are to be made
# returns
# - pattern with newly substituted values
#
def substitute(subs, pat):
    for var in subs:
        pat = pat.replace(var, subs[var])
    return pat





# performs atomic unification
# takes
# - var: variable from a rules antecedent
# - val: corresponding value
# - subs: substitution table (of substitutions already discovered)
# returns:
# - updated substitution dictionary (possibly empty)
# - False if unification can't be performed
#
def unify_var(var, val, subs):
	if var in subs :
		return unify(subs[var], val, subs)
	elif isinstance(val, str) and val in subs :
		return unify(var, subs[val], subs)
	else :
		subs[var] = val ; return subs






# finds the substitutions that unify (or make equivalent) the given patterns
# takes
# - pat1: string (generally the antecedent of a rule)
# - pat2: string (generally a fact from working mem)
# returns
# - updated substitution table if the patterns can be unified
# - False otherwise
#
def unify(pat1, pat2, subs):

	if subs is False : return False
	#when both symbols match
	elif isinstance(pat1, str) and isinstance(pat2, str) and pat1 == pat2 :	return subs
	#variable cases
	elif isinstance(pat1, str) and is_var(pat1) : return unify_var(pat1, pat2, subs)
	elif isinstance(pat2, str) and is_var(pat2) : return unify_var(pat2, pat1, subs)
        # predicate case : Ex. (fun1, t11, t12, ... ) <=> (fun1, t21, t22, ... )
	elif isinstance(pat1, tuple) and isinstance(pat2, tuple) :
		if len(pat1) == 0 and len(pat2) == 0 : return subs
		#Functors of structures have to match.
		if isinstance(pat1[0], str) and  isinstance(pat2[0],str) and not ( is_var(pat1[0]) or is_var(pat2[0]) ) and pat1[0] != pat2[0] : return False
		return unify(pat1[1:],pat2[1:], unify(pat1[0], pat2[0], subs))
	#list case : Ex. [ s11, s12, ... ] <=> [ s21, s22, ... ]
	elif isinstance(pat1, list) and isinstance(pat2, list) :
		if len(pat1) == 0 and len(pat2) == 0 : return subs
		return unify(pat1[1:],pat2[1:], unify(pat1[0], pat2[0], subs))

	else: return False








# expands rule states performing dfs to find bindings for a rule's antecedents
# takes
# - antecs: a rule's list of antecedents
# - wm: the working mem of facts that the function is to make matches of
# - subs: dictionary of previously found substitutions for the rule
# returns
# - list of possible states that can be achived given a rule and wm
#
def match_antecedent(antecs, wm, subs):
    antec = antecs[0]
    def match_helper(states, wm_left):
        # if no working mem -> return discovered states
        if not wm_left:
            return states

        # otherwise -> unify antecedent with next fact in wm
        subs_new = unify(antec.split(), wm_left[0].split(), subs.copy())
        # if unification fails -> move to next fact in wm
        if not subs_new:
            return match_helper(states, wm_left[1:])

        # build new state and add to states if not already there
        ns = (antecs[1:], subs_new)
        if ns not in states:
            states.append(ns)

        return match_helper(states, wm_left[1:])

    return match_helper([], wm)





# performs a substitution for a given consequent given a list of substitutions
# takes
# - subs: dict of substitutions/bindings
# - rhs: the consequent of a rule
# - wm: a list of facts/assertions to check the resulting substitution against
# returns
# - a consequent with values subbed in for its variables
#
def execute(subs, rhs, wm):
    # apply substitutions to each consequent in rhs
    pats = list()
    for cons in rhs:
        pat = substitute(subs, cons)
        if pat and pat not in wm:
            pats.append(pat)

    return pats








# matches a rule to facts in the reasoner's working memory
# takes
# - name: string, name of the rule
# - lhs: list, the antecedents/conditions of the rule
# - rhs: list, the consequent(s) of said rule
# returns
# - list of newly matched rule consequent(s)
#
def match_rule(name, lhs, rhs, wm):
    # useful messages

    def mr_helper(queue, new_wm):
        # each state in queue is of form:  (remaining_lhs, subs)
        if not queue:
            return new_wm
        # else -> examine first item in queue
        else:
            antecs, subs = queue[0]
            if not antecs: # goal state (rule matched)
                # get list of consequences not in wm
                cons = execute(subs, rhs, wm)
                # append assertions returned from exec to new_wm
                new_wm.extend(cons)
                # call helper on rest of queue/states and new_wm
                return mr_helper(queue[1:], new_wm)

            else: # state has anteceds
                matched = match_antecedent(antecs, wm, subs)

                # if returns no new states, move to next state in the queue
                if not matched:
                    return mr_helper(queue[1:], new_wm)

                # else return mr_helper on the updated queue
                    # ie. the old one with the new states found by match_antecedent() replacing staet1
                matched.extend(queue[1:])
                return mr_helper(matched, new_wm)

    return mr_helper(match_antecedent(lhs, wm, dict()), list())




#
#
def match_rules(wm, rules=RULES):
    matched_cons = list()
    for name, antecs, cons in rules:
        matched = match_rule(name, antecs, cons, wm)
        if matched:
            matched_cons.append(matched)
        #matched_cons.append(match_rule(name, antecs, cons, wm))
    return matched_cons








if __name__ == '__main__':

    #sub = [('?y', 'mary'), ('?x', 'john')]
    #pat = '?x gave (son-of ?y) ?z'
    #out = substitute(sub, pat)


    '''
    sub = [('?t', '?z'), ('?z', '?x')]
    for item in sub:
        print(item)
    pat = 'drop arnold (class ?y 563)'
    expected = 'drop arnold (class ?x 563)'
    out = substitute(sub, pat)
    print('orig: ', pat)
    print('out: ', out)
    '''


    # unify tests
    '''
    pat1 = 'has-taste-strength ?ingr strong'
    pat2 = 'has-taste-strength spinach strong'

    sub = unify(pat1, pat2, list())
    print(sub)


    pat1 = 'has-taste-strength ?ingr strong'
    pat2 = 'has-taste ?sub metallic'
    sub = unify(pat1, pat2, list())
    print(sub)


    pat1 = 'has-taste-strength ?ingr weak'
    pat2 = 'has-taste-strength ?sub weak'
    sub = unify(pat1, pat2, list())
    print(sub)
    '''



    # match_antecedant tests
    '''
    anteceds = RULES[0][1]
    wm = ['ingr kale', 'sub arugula', 'sub spinach', 'has-taste-strength kale strong', 'has-taste kale strong', 'has-color kale green', 'has-taste-strength spinach medium', 'has-color spinach green', 'has-taste spinach metallic', 'has-taste-strength arugula strong']
    res = match_antecedent(anteceds, wm, list())
    for state in res:
        print(state)
        print('---------------------------')
    '''



    # execute tests
    '''
    cons = ['have-similar-strength ?ingr ?sub strong', 'has-strong-taste ?sub']
    subs = [('?ingr', 'kale'), ('?sub', 'spinach')]
    wm = ['is-gross spinach']
    assertion = execute(subs, cons, wm)
    print(assertion)
    '''


    # match_rule tests
    #name, lhs, rhs = RULES[0]
    #wm = ['ingr kale', 'sub arugula', 'sub spinach', 'has-taste-strength kale strong', 'has-taste kale strong', 'has-color kale green', 'has-taste-strength spinach medium', 'has-color spinach green', 'has-taste spinach metallic', 'has-taste-strength arugula strong']
    #res = match_rule(name, lhs, rhs, wm)
    #for r in res:
        #print(r)



    '''
    pats = rhs
    subs = [('?ingr', 'kale'), ('?sub', 'arugula')]
    cons = [substitute(subs, pat) for pat in pats]
    ex = execute(subs, pats, list())
    #print(type(cons))
    #print(len(cons))
    #print(cons)
#
    #print(type(ex))
    #print(len(ex))
    #print(ex)


    wm = ['ingr arugula', 'sub kale', 'has-taste-strength kale strong', 'has-taste-strength arugula strong']
    print('--------------------starting conditions-----------------------')
    print('wm: ', wm)
    print('name: ', name)
    print('lhs: ', lhs)
    print('rhs: ', rhs)
    new_wm = match_rule(name, lhs, rhs, wm)
    print(new_wm)
    '''


    '''
    #name = 'doesnt matter'
    #lhs = ['ingr ?ingr', 'sub ?sub']
    #rhs = ['?sub is the proper substitution for ?ingr']
    #wm = ['ingr kale', 'sub arugula']
    #new_wm = match_rule(name, lhs, rhs, wm)
    #for item in new_wm:
        #print(item)

    # new unify tests

    res = unify(lhs[1], wm[1], [('?ingr', 'kale')])
    #print(res)
    res = unify('car-model ?car toyota', 'car-model mycar toyota', res)
    #print(res)
    '''

    name, antecs, cons = RULES[0]
    wm = ['ingr lettuce', 'sub radish', 'has-taste-strength radish strong', 'ingr arugula', 'ingr sweet-potato', 'sub kale', 'has-taste-strength kale strong', 'has-taste-strength arugula strong']
    print('name: ', name)
    print('--------------antecedents----------------')
    for item in antecs:
        print(item)
    print('--------------consequents----------------')
    for item in cons:
        print(item)

    print('--------------working mem----------------')
    for item in wm:
        print(item)
    print('=========================================\n\n')


    pstates = match_antecedent(antecs, wm, dict())
    print('possible states from matching first antecedent: ')
    for ps in pstates:
        print(ps)

    # def unify(antec, pat, subs):
    # def match_antecedent(antecs, wm, subs):
    #antecs = antecs[1:]
    #subs = [('?ingr', 'arugula')]


    new_wm = match_rule(name, antecs, cons, wm)
    print('\n\nresult of match_rule')
    print(new_wm)
