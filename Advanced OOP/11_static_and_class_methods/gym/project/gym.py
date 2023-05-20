from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        result = ''
        customer_id = ''
        trainer_id = ''
        exercise_id = ''
        for subs in self.subscriptions:
            if subs.id == subscription_id:
                result = f"{subs.__repr__()}\n"
                customer_id = subs.customer_id
                trainer_id = subs.trainer_id
                exercise_id = subs.exercise_id
                for customer in self.customers:
                    if customer.id == customer_id:
                        result += customer.__repr__() + '\n'
                for trainer in self.trainers:
                    if trainer.id == trainer_id:
                        result += trainer.__repr__() + '\n'
                for exercise in self.plans:
                    if exercise.id == exercise_id:
                        equipment_id = exercise.equipment_id
                        for equipment in self.equipment:
                            if equipment.id == equipment_id:
                                result += equipment.__repr__() + '\n'
                        result += exercise.__repr__()
        return result
