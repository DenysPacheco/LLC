# Output for 'Hourglass'
#
# H o u r g l a s s
# H               s
#   o           s
#     u       a
#       r   l
#         g
#       r   l
#     u       a
#   o           s
# H               s
# H o u r g l a s s


########## Hourglass v2 ##########

# l = 9
# p = ''
p = 'Hourglass'
l = len(p)

for x in reversed(range(0, l+2)):
    for y in range(1, l+1):
        if x == 0 or x == l+1 or y == x or y+x == l+1:
            print(y if p == '' else p[y-1], end=' ')
        else:
            print('  ', end='')
    print()


########## Hourglass v1 ##########

# # r = [1, 2, 3, 4, 5, 6, 7]
# r = 'Abelhas'

# for x in r:
#     print(x, end=' ')

# print()

# l = r[::-1]

# for x, c in enumerate(l):
#     for y, cr in enumerate(r):
#         if y == x or (y+x+1)/2 == len(r)/2:
#             print(cr, end=' ')
#         else:
#             print('  ', end='')
#     print()

# for x in r:
#     print(x, end=' ')

# print()
