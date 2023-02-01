numbers = [1,3,5]
# List comprehension  - creating a new list by doing iteration inside a new list
doubled = [num * 2 for num in numbers]
# This is same as we would have done externally
# for num in numbers:
    # doubled.append(num * 2)
print(doubled)

friends = ["Rolf", "Sam", "Samantha","Siim","Joonas"]
# start_s = [WHAT_YOU_ADD | LOOP | CONDITION]
starts_s = [friend for friend in friends if friend.startswith("S")]
# corresponds to
# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(starts_s)