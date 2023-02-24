class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        # if customer not in self.customer:
        #     self.customer.append(customer)

        self.__add_entity(self.customers, customer)

    def __add_entity(self, collection, entity):
        if entity not in collection:
            collection.append(entity)

    def add_trainer(self, trainer):
        self.__add_entity(self.trainers, trainer)

    def add_equipment(self, equipment):
        self.__add_entity(self.equipment, equipment)

    def add_plan(self, plan):
        self.__add_entity(self.plans, plan)

    def add_subscription(self, subscription):
        self.__add_entity(self.subscriptions, subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_ent_by_id(self.subscriptions, subscription_id)
        customer = self.__find_ent_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_ent_by_id(self.trainers, subscription.trainer_id)
        plan = self.__find_ent_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_ent_by_id(self.equipment, plan.equipment_id)

        return repr(subscription) + "\n" + \
               repr(customer) + "\n" + repr(trainer) + "\n" + repr(equipment) + "\n" + repr(plan)

    def __find_ent_by_id(self, collection, ent_id):
        for ent in collection:
            if ent.id == ent_id:
                return ent


