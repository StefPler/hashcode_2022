class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level

class Contributor:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def findSkill(self, name):
        foundSkill = False
        for sk in self.skills:
            if(name == sk.name):
                foundSkill = True
        return foundSkill

    def findSkillLevel(self, name, level):
        foundSkill = False
        for sk in self.skills:
            if((name == sk.name) and (int(level) <= int(sk.level))):
                foundSkill = True
        return foundSkill

    def findSkillLevelMentor(self, name, level):
        foundSkill = False
        for sk in self.skills:
            if((name == sk.name) and (int(level) == int(sk.level-1))):
                foundSkill = True
        return foundSkill


class Project:
    def __init__(self, name, daysToComplete, score, bestBefore, roles, requirements):
        self.name = name
        self.daysToComplete = daysToComplete
        self.score = score
        self.bestBefore = bestBefore
        self.roles = roles
        self.requirements = requirements


class ProjectAssignment:
    def __init__(self, name, namesOfContributors):
        self.name = name
        self.namesOfContributors = namesOfContributors
