
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
        self._nex_id = 1
        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        # member["first_name"] = self.first_name --> porque no es colocado?
        member["last_name"] = self.last_name
        member["id"] = self._generateId()
        member["lucky_numbers"] = list(member.get("lucky_numbers", set()))
        self._members.append(member)
        return member

    def delete_member(self, id):
        # fill this method and update the return
        for position in range(len(self._members)):
            if self._members[position][id] == id:
                self._members.pop(position)
            return None
          

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member['id'] == int(id):
                return member 
    
    
    def get_all_members(self):
        return self._members
