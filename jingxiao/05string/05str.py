s = ''
for n in range(0, 10):
    s += str(n)

print(s)

l = []
for n in range(0, 10):
    l.append(str(n))
l = ' '.join(l)

print(l)


def query_data(namespace, table):
    """
    given namespace and table, query database to get corresponding
    data
    """

path = 'hive://ads/training_table'
namespace = path.split('//')[1].split('/')[0] # 返回'ads'
table = path.split('//')[1].split('/')[1] # 返回 'training_table'
data = query_data(namespace, table)

print(table)

id = 123456
name = 'liu'
print('no data available for person with id: {}, name: {}'.format(id, name))

print('no data available for person with id: %s, name: %s' % (id, name))





