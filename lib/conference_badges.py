def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    new_list = []
    for name in names:
        new_list.append(f"Hello, my name is {name}.")
    return new_list

def assign_rooms(names):
    new_list = []
    for name in names:
        room_number = names.index(name)
        new_list.append(f"Hello, {name}! You'll be assigned to room {room_number+1}!")
    return new_list

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    
    for assignment in assign_rooms(names):
        print(assignment)
