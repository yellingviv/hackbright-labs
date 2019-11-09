############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""
        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = bool(is_seedless)
        self.is_bestseller = bool(is_bestseller)
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

    def __repr__(self):
        return self.name


def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []

    muskmelon = MelonType('musk', 1998, 'green', True, True, 'muskmelon')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellowwatermelon = MelonType('yw', 2013, 'yellow', True, True, 'yellow watermelon')
    yellowwatermelon.add_pairing('ice cream')
    all_melon_types.append(yellowwatermelon)

    return all_melon_types


def print_pairing_info(all_melon_types):
    """Prints information about each melon type's pairings."""

    for melon in all_melon_types:
        print(f'{melon.name} pairs with:')
        for pairing in melon.pairings:
            print(f'- {pairing}')
        print('')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melons_by_code = {}

    for melon in melon_types:
        melons_by_code[melon.code] = melon

    return melons_by_code

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, type, shape_rating, color_rating, field, harvester):
        """initialize a specific harvested melon"""
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        """checks for melon sellability based on quality and field of origin"""
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_code = make_melon_type_lookup(melon_types)
    melon_harvest = []

    melon_1 = Melon(melons_by_code['yw'], 8, 7, 2, 'Sheila')
    melon_harvest.append(melon_1)
    melon_2 = Melon(melons_by_code['yw'], 3, 4, 2, 'Sheila')
    melon_harvest.append(melon_2)
    melon_3 = Melon(melons_by_code['yw'], 9, 8, 3, 'Sheila')
    melon_harvest.append(melon_3)
    melon_4 = Melon(melons_by_code['cas'], 10, 6, 35, 'Sheila')
    melon_harvest.append(melon_4)
    melon_5 = Melon(melons_by_code['cren'], 8, 9, 35, 'Michael')
    melon_harvest.append(melon_5)
    melon_6 = Melon(melons_by_code['cren'], 8, 2, 35, 'Michael')
    melon_harvest.append(melon_6)
    melon_7 = Melon(melons_by_code['cren'], 2, 3, 4, 'Michael')
    melon_harvest.append(melon_7)
    melon_8 = Melon(melons_by_code['musk'], 6, 7, 4, 'Michael')
    melon_harvest.append(melon_8)
    melon_9 = Melon(melons_by_code['yw'], 7, 10, 3, 'Sheila')
    melon_harvest.append(melon_9)

    return melon_harvest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    sellable = "(CAN BE SOLD)"
    not_sellable = "(NOT SELLABLE)"

    for melon in melons:
        if melon.is_sellable():
            print(f'Harvested by {melon.harvester} from field {melon.field}. {sellable}')
        else:
            print(f'Harvested by {melon.harvester} from field {melon.field}. {not_sellable}')