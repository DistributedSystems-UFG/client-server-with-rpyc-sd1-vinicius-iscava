import rpyc
import sys
from constRPYC import * #-
from typing import List


def print_line(char="=", line_size=50):
    print(char*line_size)
    

class Client(object):

    def __init__(self):
        self.conn = rpyc.connect(SERVER, PORT) # Connect to the server

    def print_value(self, line_size=50) -> None:
        print_line()
        print("current value:")
        print(self.conn.root.exposed_value())   # Print the result

    def append_values(self, values: List[dict], line_size=50) -> None:
        print_line()
        print(f"appending {len(values)} dicts")
        for value in values:
            self.conn.root.exposed_append(value)

    def remove_values(self, key, value, line_size=50) -> None:
        print_line()
        print(f"removing dict with value {value} for key {key}")
        self.conn.root.exposed_remove(key, value)

    def sort_by(self, key):
        print_line()
        print(f"ordering list with the value of the key {key}")
        self.conn.root.exposed_order(key)

    def search(self, key, value):
        print_line()
        print(f"finding data with {value} on key {key}")
        result = self.conn.root.exposed_search(key, value)
        print(f"result: {result}")



def main(args):
    client = Client()
    client.print_value()
    client.append_values([{"name": "bob", "age": 40}, {"name": "paul", "age": 20}])
    client.print_value()

    client.sort_by("age")
    client.print_value()

    client.search("name", "bob")

    client.remove_values("name", "bob")
    client.print_value()


if __name__ == "__main__":
    main(sys.argv[1:])

