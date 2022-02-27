from dataStructures import Skill, Contributor, Project, ProjectAssignment

def produceOutput(projects):
    f = open("out.txt", "w")
    f.write(str(len(projects)) + "\n")
    for project in projects:
        f.write(f'{project.name}\n')
        for name in project.namesOfContributors:
            f.write(f'{name} ')
        f.write("\n")
    f.close()

fileA = 'a_an_example.in.txt'
fileB = 'b_better_start_small.in.txt'
fileC = 'c_collaboration.in.txt'
fileD = 'd_dense_schedule.in.txt'
fileE = 'e_exceptional_skills.in.txt'
fileF = 'f_find_great_mentors.in.txt'

with open(f'./tests/{fileB}', 'r') as f:
    lines = f.readlines()
line0 = lines[0].split(" ")
numberOfContributors = int(line0[0])
projects = int(line0[1])
print("Number of contributors is :", numberOfContributors,
      " and number of projects is: ", projects)

i = 0
linecount = 1
projlist = []
contributors = []
while (i < numberOfContributors):
    temp = lines[linecount].split()

    j = int(temp[1])
    linecount += 1
    skills = []
    for k in range(0, j):
        temp2 = lines[linecount].split()
        linecount += 1
        skill = Skill(temp2[0], temp2[1])
        skills.append(skill)
    i = i+1
    contributors.append(Contributor(temp[0], skills))

i = 0
while (i < projects):
    temp = lines[linecount].split()
    linecount += 1
    numberOfRequirements = temp[4]
    skills = []
    for j in range(0, int(numberOfRequirements)):
        temp2 = lines[linecount].split()
        skills.append(Skill(temp2[0], temp2[1]))
        linecount += 1
    projlist.append(
        Project(temp[0], temp[1], temp[2], temp[3], temp[4], skills))
    i += 1

for con in contributors:
    for sk in con.skills:
        print(
            f"contributor name: {con.name} skill name: {sk.name} skill level: {sk.level}")

for proj in projlist:
    print(f"Project name: {proj.name} days to complete: {proj.daysToComplete} score: {proj.score} Best Before: {proj.bestBefore} number of requirements {len(proj.requirements)}")
    for sk in proj.requirements:
        print(f"skill name: {sk.name} skill level: {sk.level}")

projectAssignments = []
contributorAvailability = list(contributors)
for proj in projlist:
    names = []
    projectBound = []
    for sk in proj.requirements:
        for con in contributors:
            if(con.findSkillLevel(sk.name, sk.level) and (con in contributorAvailability) and (con not in projectBound)):
                projectBound.append(con)
                names.append(con.name)
                break
    if(len(names) == len(proj.requirements)):
        projectAssignments.append(ProjectAssignment(proj.name, list(names)))
        for contributor in projectBound:
            try:
                contributorAvailability.remove(contributor)
            except ValueError:
                print(f'contributor {contributor.name} not available')
    projectBound.clear()
    names.clear()

print("----------------------------------------------------")

# for project in projectAssignments:
#     print(f"\n* {project.name} *")
#     for name in project.namesOfContributors:
#         print(f"- {name}")

produceOutput(projectAssignments)
