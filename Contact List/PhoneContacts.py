

def create_contact(contacts, first, last, email, age, phone):
    """
    Creates a contact.
    """
    # 1 create key(immutable, tuple)
    # 2 Put key into dictionary
    # 3 Assign a value to your key ( data structure)

    contacts[(first.lower(), last.lower())] = [email, age, phone]


def update_contact_number(contacts, first, last, phone):
    """
    Updates contact phone number.
    """
    update_phone = contacts[(first.lower(), last.lower())][2] = phone


def update_contact_email(contacts, first, last, email):
    """
    Updates contact email.
    """
    update_email = contacts[(first.lower(), last.lower())][0] = email


def update_contact_age(contacts, first, last, age):
    """
    Updates contact age.
    """
    update_age = contacts[(first.lower(), last.lower())][1] = age


def get_contact_email(contacts, first, last):
    """
    Gets contact email.
    """
    get_email = contacts[(first.lower(), last.lower())][0]
    return(get_email)


def get_contact_age(contacts, first, last):
    """
    Gets contact age.
    """
    get_age = contacts[(first.lower(), last.lower())][1]
    return(get_age)


def get_contact_number(contacts, first, last):
    """
    Gets contact phone number.
    """
    get_number = contacts[(first.lower(), last.lower())][2]
    return(get_number)


def contains_contact(contacts, first, last):
    """
    Checks to see if the dictionary contains  a contact.
    """
    return (first.lower(), last.lower()) in contacts


def display(contacts, first, last):
    """
    Displays a contact.
    """
    # Asks if the values are in the dictionary
    if (first.lower(), last.lower()) in contacts:
        print("")
        print("Name:", first, last)
        print("Email:", contacts[(first.lower(), last.lower())][0])
        print("Phone:", contacts[(first.lower(), last.lower())][2])
        print("Age:", contacts[(first.lower(), last.lower())][1])

    else:
        print("")
        print("No such contact for:", first, last)


def main():
    # The Dictionary
    contacts = {}
    # Provided Test Code
    create_contact(contacts, "Katie", "Katz", "katie.katz@nau.edu",
                   25, "857-294-2758")
    create_contact(contacts, "Jim", "Jones", "jim.jones@nau.edu", 19,
                   "525-866-2749")
    create_contact(contacts, "Sarah", "Sanders",
                   "sarah.sanders@nau.edu", 18, "593-026-2532")
    print("Creation of Jim Jones: {}".format(
        "Passed" if contains_contact(contacts, "jim", "Jones")
        else "Failed"))
    print("Creation of Katie Katz: {}".format(
        "Passed" if contains_contact(contacts, "Katie", "kaTz") else
        "Failed"))
    print("Creation of Sarah Sanders: {}".format(
        "Passed" if contains_contact(contacts, "Sarah", "Sanders") else
        "Failed"))
    update_contact_age(contacts, "Sarah", "Sanders", 19)
    print("Updating Sarah Sanders age to 19: {}".format(
        "Passed" if get_contact_age(contacts, "sarah", "sanDers") == 19
        else "Failed"))
    update_contact_email(contacts, "Jim", "Jones",
                         "jim.jones@gmail.com")
    print("Updating Jim Jones's email: {}".format(
        "Passed" if get_contact_email(contacts, "jim", "jones") ==
        "jim.jones@gmail.com" else "Failed"))
    update_contact_number(contacts, "Katie", "Katz", "907-536-2946")
    print("Updating Katie Katz's number: {}".format(
        "Passed" if get_contact_number(contacts, "Katie", "Katz") ==
        "907-536-2946" else "Failed"))

    (display(contacts, "Katie", "Katz"))
    (display(contacts, "George", "Shaw"))


# Calls Main
if __name__ == "__main__":
    main()
