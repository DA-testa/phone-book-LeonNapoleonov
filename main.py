#python
#Leons Dolgopolovs 221RDB432

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for _ in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    # Keep dictionary of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    result = []

    def process_add(query):
        contacts[query.number] = query.name

    def process_del(query):
        if query.number in contacts:
            del contacts[query.number]

    def process_find(query):
        result.append(contacts.get(query.number, 'not found'))

    process_query = {
        'add': process_add,
        'del': process_del,
        'find': process_find
    }

    for query in queries:
        process_query[query.type](query)

    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
