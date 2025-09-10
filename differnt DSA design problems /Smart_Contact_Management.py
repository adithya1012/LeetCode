# Problem Statement
# Design a contact management system that handles messy real-world data. The system needs to:

# Automatically detect and merge duplicate contacts based on email, phone, name similarity
# Handle fuzzy matching (typos, different name formats)
# Maintain company hierarchies (employees belong to companies)
# Support fast search across multiple fields
# Track contact relationships and interaction history
# Validate and normalize contact information

# type contact_info = {
#     name: str | None
#     email: str | None
#     ...
# }

import collections
class Contact_Management:
    def __init__(self):
        self.contact = {} # contact_id -> {contact_info}
        self.name = {} # name -> contact_id
        self.email = {} # email -> contact_id
        self.duplicate = collections.defaultdict(list) # contact_id -> duplicat_contact_id
        self.company = collections.defaultdict(list)

    def add_contact(self, contact_id, name, email, phone, company):
        name = name.lower()
        email = email.lower()
        duplicate_id = self.is_duplicate(contact_id, name, email)
        if duplicate_id:
            self.duplicate[contact_id].append(duplicate_id)
            return duplicate_id
        self.contact[contact_id] = {
            "email": email,
            "name" : name,
            "phone": phone
        }
        self.email[email] = contact_id
        self.name[name] = contact_id
        self.company[company].append(contact_id)
        return contact_id

    def is_duplicate(self, contact_id, name, email):
        if contact_id in self.contact:
            return contact_id
        if name.lower() in self.name:
            return self.name[name]
        if email.lower() in self.email:
            return self.email[email]

    def similr_name(self, name, query):
        name_set = set(name.split())
        query_set = set(query.split())
        return len(name_set.intersection(query_set)) >= 2


    def search_contact(self, query):
        """
        Search the contact based on the query. Query can be anything, name, email
        :param query: string
        :return: int (contact_id)
        """

        if query in self.email:
            return self.email[query]

        if query in self.name:
            return self.name[query]

        for name in self.name:
            if self.similr_name(name, query):
                return self.name[name]
        return None




