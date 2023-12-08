class Query:
    def __init__(self, db, cur):
        self.db = db
        self.cur = cur

    def insert(self, table, data):
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s)' % (table, keys, values)
        try:
            self.cur.execute(sql, tuple(data.values()))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
    
    def update(self, table, data, condition):
        keys = ', '.join(['%s=%s' % (k, '%s') for k in data.keys()])
        sql = 'update %s set %s where %s' % (table, keys, condition)
        try:
            self.cur.execute(sql, tuple(data.values()))
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
    
    def delete(self, table, condition):
        sql = 'delete from %s where %s' % (table, condition)
        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
    
    def select(self, table, condition='', fields='*', order='id desc'):
        sql = 'select %s from %s' % (fields, table)
        if condition:
            sql = '%s where %s' % (sql, condition)
        if order:
            sql = '%s order by %s' % (sql, order)
        try:
            self.cur.execute(sql)
            return self.cur.fetchall()
        except Exception as e:
            print(e)
            self.db.rollback()
        