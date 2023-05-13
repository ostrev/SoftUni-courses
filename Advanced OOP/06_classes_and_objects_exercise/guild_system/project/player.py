class Player:
    DEF_CONSTANT = 'Unaffiliated'

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self. skills = {}
        self.guild = Player.DEF_CONSTANT

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        for k, v in self.skills.items():

            result += f'==={k} - {v}'
            result += '\n'
        return result
