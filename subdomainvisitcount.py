cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

result = cpdomains

for ind, item in enumerate(cpdomains):
    c_split = item.split(' ')
    init_count = int(c_split[0])
    words = c_split[1].split('.')

    for i2 in cpdomains[ind+1:]:


