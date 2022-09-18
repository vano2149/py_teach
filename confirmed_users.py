"""
confirmed_users.py file!
"""

uncunfirmed_users = ["alice", "brian", "candace"]

cunfirmed_users = []

while uncunfirmed_users:
    current_user = uncunfirmed_users.pop()

    print(f"Verifying user : {current_user.title()}")
    cunfirmed_users.append(current_user)

print("\n The following users have been confirmed:")
for cunfirmed_user in cunfirmed_users:
    print(cunfirmed_user.title())
