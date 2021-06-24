# hard coding the ingredient list as frames for the semantic net
# the nodes of the network will be frames



class Ingred:
    # rels contains tuples describing this object/concepts relationship to others in the net
    # the tuples are of the form (relation-to, object/concept)
    # possible relationships are: 'is-a' and 'instance-of'
    rels = list()
    # atts contains tuples describing attributes of the given object/concept
    # the tuples are of the form: (has-attr, value)
    atts = list()

    def __init__(self):
        self.name = 'ingredient'


class Veg(Ingred):
    rels = Ingred.rels.copy()
    rels.append(('is-a', 'ingredient'))

    atts = Ingred.atts.copy()

    def __init__(self):
        super(Ingred, self).__init__()
        self.name = 'veg'



class LeafyVeg(Veg):
    rels = Veg.rels.copy()
    rels.append(('is-a', 'veg'))

    atts = Veg.atts.copy()
    atts.append(('has-leaf', 'true'))

    def __init__(self):
        super(Veg, self).__init__()
        self.name = 'leafy-veg'



class RootVeg(Veg):
    rels = Veg.rels.copy()
    rels.append(('is-a', 'veg'))

    atts = Veg.atts.copy()
    atts.append(('has-leaf', 'false'))

    def __init__(self):
        super(Veg, self).__init__()
        self.name = 'root-veg'



# atts should be a list of tuples containing attributes
class LeafyVegItem(LeafyVeg):

    def __init__(self, name):
        self.name = name
        self.rels = LeafyVeg.rels.copy()
        self.build_rels()
        self.atts = LeafyVeg.atts.copy()
        self.build_atts()


    def build_rels(self):
        self.rels.append(('instance-of', 'leafy-veg'))


    def build_atts(self):
        desc = {
                'arugula': [('is-edible-raw', 'true'),
                            ('is-edible-cooked', 'true'),
                            ('has-taste-strength', 'strong'),
                            ('has-color', 'dark-green'),
                            ('has-texture', 'tender'),
                            ('has-taste', 'tangy'),
                            ('has-density', 'medium')],

                'lettuce': [('is-edible-raw', 'true'),
                            ('is-edible-cooked', 'true'),
                            ('has-taste-strength', 'mild'),
                            ('has-color', 'light-green'),
                            ('has-texture', 'crunchy'),
                            ('has-taste', 'sweet'),
                            ('has-density', 'medium')],

                'spinach': [('is-edible-raw', 'true'),
                            ('is-edible-cooked', 'true'),
                            ('has-taste-strength', 'medium'),
                            ('has-color', 'dark-green'),
                            ('has-texture', 'gritty'),
                            ('has-taste', 'tangy'),
                            ('has-taste', 'earthy'),
                            ('has-density', 'medium')],

                'kale': [('is-edible-raw', 'true'),
                        ('is-edible-cooked', 'true'),
                        ('has-taste-strength', 'strong'),
                        ('has-color', 'dark-green'),
                        ('has-texture', 'crunchy'),
                        ('has-texture', 'chewy'),
                        ('has-taste', 'bitter'),
                        ('has-density', 'medium')]
        }

        if self.name not in desc.keys():
            raise ValueError('Ingredient {} not in knowledge base. Try a different ingredient.'.format(self.name))

        self.atts.extend(desc[self.name])



class RootVegItem(LeafyVeg):

    def __init__(self, name):
        self.name = name
        self.rels = RootVeg.rels.copy()
        self.build_rels()
        self.atts = RootVeg.atts.copy()
        self.build_atts()


    def build_rels(self):
        self.rels.append(('instance-of', 'root-veg'))


    def build_atts(self):
        desc = {
                'carrot': [('is-edible-raw', 'true'),
                            ('is-edible-cooked', 'true'),
                            ('has-taste-strength', 'strong'),
                            ('has-color', 'orange'),
                            ('has-texture', 'crunchy'),
                            ('has-taste', 'sweet'),
                            ('has-taste', 'earthy'),
                            ('has-density', 'dense')],

                'parsnip': [('is-edible-raw', 'true'),
                            ('is-edible-cooked', 'true'),
                            ('has-taste-strength', 'mild'),
                            ('has-color', 'white'),
                            ('has-texture', 'starchy'),
                            ('has-taste', 'sweet'),
                            ('has-taste', 'nutty'),
                            ('has-density', 'dense'),
                            ('has-taste-strength', 'weak')],

                'beet-root': [('is-edible-raw', 'true'),
                              ('is-edible-cooked', 'true'),
                              ('has-taste-strength', 'medium'),
                              ('has-color', 'purple'),
                              ('has-texture', 'tender'),
                              ('has-taste', 'sweet'),
                              ('has-density', 'dense')],

                'sweet-potato': [('is-edible-raw', 'true'),
                                 ('is-edible-cooked', 'true'),
                                 ('has-taste-strength', 'medium'),
                                 ('has-color', 'orange'),
                                 ('has-texture', 'tender'),
                                 ('has-taste', 'sweet'),
                                 ('has-taste', 'earthy'),
                                 ('has-density', 'dense')]
        }

        if self.name not in desc.keys():
            raise ValueError('Ingredient {} not in knowledge base. Try a different ingredient.'.format(self.name))

        self.atts.extend(desc[self.name])




if __name__ == '__main__':

    # test frame instantiations
    '''
    leafy = LeafyVeg()
    print(leafy.name)
    for rel in LeafyVeg.rels:
        print(rel)

    print('----------------------------------------')
    for att in LeafyVeg.atts:
        print(att)



    print('========================================')
    veg = RootVeg()
    print(veg.name)
    for rel in RootVeg.rels:
        print(rel)


    print('----------------------------------------')
    for att in RootVeg.atts:
        print(att)
    '''


    spinach = LeafyVegItem('spinach')
    for rel in spinach.rels:
        print(rel)


    print('---------------------------------------------')
    for att in spinach.atts:
        print(att)

    print('=============================================')

    carrot = RootVegItem('carrot')
    for rel in carrot.rels:
        print(rel)

    print('---------------------------------------------')
    for att in carrot.atts:
        print(att)
