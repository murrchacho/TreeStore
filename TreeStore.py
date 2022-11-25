class TreeStore:
    def __init__(self, items):
        self.items = {item['id']: item for item in items}

    def getAll(self):
        '''Возвращает изначальный массив элементов'''
        return list(self.items.values())
    
    def getItem(self, id):
        '''Принимает id элемента и возвращает сам объект элемента'''
        return self.items.get(id)

    def getChildren(self, id):
        '''Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента,
        чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив'''
        return [item for item in list(self.items.values()) if item['parent'] == id]

    def getAllParents(self, id):
        '''Принимает id элемента и возвращает массив из цепочки родительских элементов,
        начиная от самого элемента, чей id был передан в аргументе и до корневого элемента,
        т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок элементов важен!'''
        item = self.getItem(id).get('parent')
        if item and not item == 'root':
            return [self.getItem(item)] + self.getAllParents(item)
        return []

def main():
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]
    ts = TreeStore(items)

    print(ts.getAll())
    print(ts.getItem(7))
    print(ts.getChildren(1))
    print(ts.getAllParents(7))

if __name__ == '__main__':
    main()