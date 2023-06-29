import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

  def exposed_remove(self, key, value):
    self.value = [i for i in self.value if i[key] != value]

  def exposed_search(self, key, value):
    return list(filter(lambda x: x[key] == value, self.value))

  def exposed_order(self, order_by):
    return self.value.sort(key=lambda x: x[order_by])

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

