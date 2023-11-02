prefixes = 'JKLMNOPQ'
suffix = 'ack'
for p in prefixes:
    if p == prefixes[5]:
        print('**' +p + 'u' + suffix)
    elif p == prefixes[7]:
        print('**' + p + 'u' + suffix)
    else:
        print(p + suffix)
