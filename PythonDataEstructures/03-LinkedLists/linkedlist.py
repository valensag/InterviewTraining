head = {"value": 11,
         "next": {"value": 3,
                "next": {"value": 23,
                        "next": {"value": 7,
                                "next": {"value": 4,
                                        "next": None
                                        }
                                }
                        }
                }
        }

print(head['next']['next']['value'])

#print(my_linked_list.head.next.next.value)