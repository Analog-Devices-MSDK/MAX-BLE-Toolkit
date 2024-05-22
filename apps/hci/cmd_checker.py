
cmd_sets = {
    'NOP' : set(()),
    'LINK_CONTROL' : set(()),
    'CONTROLLER' : set(()),
    'INFORMATIONAL' : set(()),
    'STATUS' : set(()),
    'LE_CONTROLLER' : set(()),
    'VENDOR_SPEC' : set(())
}

key = None

with open('cmds.txt', 'r') as cfile:
    lines = cfile.readlines()

for line in lines:
    line = line.strip()
    if line.startswith('#'):
        key = line.split(' ')[1]
        continue
    
    if line == '':
        continue

    cmd_sets[key].add(line)

print(cmd_sets['LE_CONTROLLER'].intersection(cmd_sets['VENDOR_SPEC']))

# for key, val in cmd_sets.items():
#     print(key)
#     print('='*15)

#     for v in val:
#         print(f'\t{v}')

#     print('\n')

