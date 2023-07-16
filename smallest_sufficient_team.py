"""
Leetcode: Smallest Sufficient Team

In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

It is guaranteed an answer exists.
"""

# Recursive Solution but the time complexity is too high

class Solution:
    def findSmallestTeam(self, count, persons, total_skills, tempList, finalAns, checkVal):
        if count == len(persons):
            if checkVal == '1' * total_skills:
                if len(finalAns[0]) == 0 or len(finalAns[0]) > len(tempList):
                    finalAns[0] = tempList.copy()

            return

        self.findSmallestTeam(count + 1, persons, total_skills, tempList, finalAns, checkVal)
        print(checkVal)

        tempList.append(count)
        t = bin(int(persons[count], 2) | int(checkVal, 2))[2:].zfill(max(len(persons[count]), len(checkVal)))
        self.findSmallestTeam(count + 1, persons, total_skills, tempList, finalAns, t)
        tempList.pop()

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        total_skills = len(req_skills)
        persons = []
        finalAns = [[]]
        temp = ['0'] * total_skills
        tempList = []
        checkVal = '0' * total_skills
        for p in people:
            for skill in p:
                ind = req_skills.index(skill)
                temp[ind] = '1'
            persons.append(''.join(temp))
            temp = ['0'] * total_skills

        print(persons)
        self.findSmallestTeam(0, persons, total_skills, tempList, finalAns, checkVal)

        return finalAns[0]








