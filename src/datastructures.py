
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members =  [{
            "id" : self._generateId(),
            "first_name" : 'John' ,
            "last_name" : self.last_name,
            "age" : 33,
            "lucky_numbers" : [ 7,13,22]
        },{
            "id" : self._generateId(),
            "first_name" : 'Jane' ,
            "last_name" : self.last_name,
            "age" : 35,
            "lucky_numbers" : [ 10,14,3]
        },{
            "id" : self._generateId(),
            "first_name" : 'Jimmy' ,
            "last_name" : self.last_name,
            "age" : 5,
            "lucky_numbers" : [1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if not member["id"]:
            member["id"] = self._generateId()
        self._members.append({
            "id" : member['id'],
            "first_name" : member["first_name"],
            "last_name" : self.last_name,
            "age" : member["age"],
            "lucky_numbers" : member["lucky_numbers"]
        })

    def delete_member(self, id):
        # fill this method and update the return
        for value in self._members:
            if str(id) == str(value["id"]):
                self._members.remove(value)
        print(self._members)

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the member with the given id
        for index in range(len(self._members)):
            if id == self._members[index]["id"]:
                return self._members.pop.append[index]

    def get_member(self, id):
        # fill this method and update the return
        print(self._members)
        print(id)
        for index in range(len(self._members)):
            if str(id) == str(self._members[index]["id"]):
                return self._members[index]

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

