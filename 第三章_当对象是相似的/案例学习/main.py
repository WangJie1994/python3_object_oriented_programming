class Property:
    def __init__(self, square_feet="", beds="", baths="", **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))

    def prompt_init():
        return dict(square_feet=input("enter the square feet"),
                    beds=input("enter the number of bedrooms"),
                    baths=input("enter the number of baths"))

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    input_string += " ({}) ".format(",".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony="", laundry="", **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("apartment details")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        parent_init = Property.prompt_init()
        # laundry = ""
        # while laundry.lower() not in Apartment.valid_laundries:
        #     laundry = input(
        #         "what laundry facilities does the property have? ({})".format(",".join(Apartment.valid_laundries)))

        # balcony = ""
        # while balcony.lower() not in Apartment.valid_balconies:
        #     balcony = input("does the property have a balcony? ({})".format(",".join(Apartment.valid_balconies)))

        laundry = get_valid_input("what laundry facilities does the property have?", Apartment.valid_laundries)
        balcony = get_valid_input("does the property have a balcony?", Apartment.valid_balconies)

        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories="", garage="", fenced="", **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print("house details")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("is the yard fenced?", House.valid_fenced)
        garage = get_valid_input("is there a garage?", House.valid_garage)
        num_stories = input("how many stroies?")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })

        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    def __init__(self, price="", taxes="", **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("purchase details")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        return dict(price=input("what is the selling price?"),
                    taxes=input("what are the estimated taxes?"))

    prompt_init = staticmethod(prompt_init)


class Rental:
    def __init__(self, furnished="", utilities="", rent="", **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super().display()
        print("rental details")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        return dict(
            rent=input("what is the monthly rent? "),
            utilities=input("what are the estimated utilities? "),
            furnished=get_valid_input("is the property furnished? ", ("yes", "no"))
        )

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        property_type = get_valid_input("what type of property? ", ("house", "apartment")).lower()
        payment_type = get_valid_input("what payment type? ", ("rental", "purchase")).lower()

        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))


if __name__ == '__main__':
    # init = HouseRental.prompt_init()
    # house = HouseRental(**init)
    # house.display()
    agent = Agent()
    agent.add_property()
    agent.display_properties()