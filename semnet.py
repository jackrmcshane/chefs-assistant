from frames import *
import copy




class Semnet:

    def __init__(self):

        # the net will be accessible as the instance attribute 'net'
        # the structure of nodes in the network is : {key: [concept-frame, adjacency-list]}
        self.build_net()



    # the
    def build_net(self):

        # the key for accessing the first/head node in the semantic net
        self.head = 'ingredient'
        self.net = dict()
        self.net['ingredient'] = [Ingred(), ['veg']]
        # vegetables
        self.net['veg'] = [Veg(), ['leafy-veg', 'root-veg']]
        # leafy
        self.net['leafy-veg'] = [LeafyVeg(), ['arugula', 'lettuce', 'spinach', 'kale']]
        self.net['arugula'] = [LeafyVegItem('arugula'), list()]
        self.net['lettuce'] = [LeafyVegItem('lettuce'), list()]
        self.net['spinach'] = [LeafyVegItem('spinach'), list()]
        self.net['kale'] = [LeafyVegItem('kale'), list()]
        # root
        self.net['root-veg'] = [RootVeg(), ['carrot', 'parsnip', 'beet-root', 'sweet-potato']]
        self.net['carrot'] = [RootVegItem('carrot'), list()]
        self.net['parsnip'] = [RootVegItem('parsnip'), list()]
        self.net['beet-root'] = [RootVegItem('beet-root'), list()]
        self.net['sweet-potato'] = [RootVegItem('sweet-potato'), list()]




    def get_ingred(self, name):
        if name not in self.net:
            raise ValueError('Ingredient {} not found in semantic network. Try a different ingredient.'.format(goal))

        return copy.deepcopy(self.net[name][0])




    def get_path(self, start, goal):
        curr_depth = 0
        visited = list()
        fringe = [(start, 0, [])]

        while fringe:
            successors = list()
            # while fringe not empty and node depth equals curr depth
            while fringe and (curr_depth - fringe[-1][1]) == 0:
                curr_node, curr_dist, path = fringe.pop()
                path = path.copy()
                path.append(curr_node)
                visited.append(curr_node)
                # for successor in curr_node's adjacency list
                for succ in self.net[curr_node][1]:
                    # check if goal
                    if succ == goal:
                        return path

                    if succ not in visited:
                        successors.append((succ, curr_dist+1, path))

            [fringe.append(succ) for succ in successors]
            curr_depth += 1

        # ingredient not found in network
        raise ValueError('Ingredient {} not found in semantic network. Try a different ingredient.'.format(goal))




    # orig is the original ingredient that was to be substituted
    def get_subs(self, start, orig):
        fringe = [start]
        visited = list()
        subs = list()

        while fringe:
            curr_node = fringe.pop(0)
            visited.append(curr_node)
            for succ in self.net[curr_node][1]:
                # check if usable ingredient
                # three conditions:
                # - successor contains an 'instance-of' relation, and is therefore a physically usable ingredient
                # - successor is not the original ingredient that is to be replaced
                # - successor is not already in the possible subs list
                if (self.net[succ][0].rels[-1][0] == 'instance-of') and (succ != orig) and (succ not in subs):
                    subs.append(succ)

                else:
                    if succ not in visited:
                        fringe.append(succ)

        return [copy.deepcopy(self.net[sub][0]) for sub in subs]









if __name__ == '__main__':

    # test net instantiation
    semnet = Semnet()
    '''
    print('ingredient ------------------------------------------')
    print('adj-list: {}'.format(semnet.net['ingredient'][1]))
    print('rels: {}'.format(semnet.net['ingredient'][0].rels))
    print('atts: {}'.format(semnet.net['ingredient'][0].atts))
    print('veg ------------------------------------------')
    print('adj-list: {}'.format(semnet.net['veg'][1]))
    print('rels: {}'.format(semnet.net['veg'][0].rels))
    print('atts: {}'.format(semnet.net['veg'][0].atts))
    print('leafy-veg ------------------------------------------')
    print('leafy-veg: {}'.format(semnet.net['leafy-veg'][1]))
    print('rels: {}'.format(semnet.net['leafy-veg'][0].rels))
    print('atts: {}'.format(semnet.net['leafy-veg'][0].atts))
    print('root-veg ------------------------------------------')
    print('adj-list: {}'.format(semnet.net['root-veg'][1]))
    print('rels: {}'.format(semnet.net['root-veg'][0].rels))
    print('atts: {}'.format(semnet.net['root-veg'][0].atts))
    '''






    # implemented search tests

    # path retrieval
    ingreds = ['spinach', 'lettuce', 'arugula', 'kale', 'sweet-potato', 'beet-root', 'parsnip', 'carrot']
    for ing in ingreds:
        path = semnet.get_path('ingredient', ing)
        print(ing, ': ', path)


    # subs retrieval
    '''
    print('ingred ============================')
    subs = semnet.get_subs('ingredient', '')
    print(len(subs))
    print([sub.name for sub in subs])

    print('veg ============================')
    subs = semnet.get_subs('veg', '')
    print(len(subs))
    print([sub.name for sub in subs])

    print('leafy-veg ============================')
    subs = semnet.get_subs('leafy-veg', '')
    print(len(subs))
    print([sub.name for sub in subs])

    print('root-veg ============================')
    subs = semnet.get_subs('root-veg', '')
    print(len(subs))
    print([sub.name for sub in subs])

    print('ingred ============================')
    subs = semnet.get_subs('ingredient', 'spinach')
    print(len(subs))
    print([sub.name for sub in subs])
    '''
