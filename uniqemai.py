emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]

temp_result = []

for email in emails:
    local_name = email.split('@')[0]
    print(local_name)

    filter_plus = local_name.split('+')[0]

    email_to_send = filter_plus.replace('.', '') + '@' + email.split('@')[1]

    if email_to_send not in temp_result:
        temp_result.append(email_to_send)

    print(temp_result)

print(len(set(temp_result)))


