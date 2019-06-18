# import sqlite3
#
# conn = sqlite3.connect('sales.db')
# conn.execute('CREATE TABLE Sales (salesperson text, amt currency, year interger, model text, new boolean)')
# conn.execute('INSERT INTO Sales values ("Tim", 16000, 2010, "Honda Fit", "true")')
# conn.execute('INSERT INTO Sales values ("Tim", 9000, 2006, "Ford Focus", "false")')
# conn.execute('INSERT INTO Sales values ("Gayle", 8000, 2004, "Dodge Neon", "false")')
# conn.commit()
# conn.close()
#
import sqlite3


class QueryTemplate:
    def connect(self):
        self.conn = sqlite3.connect('sales.db')

    def construct_query(self):
        raise NotImplementedError()

    def do_query(self):
        results = self.conn.execute(self.query)

    def formate_results(self):
        output = []
        for row in self.results:
            row = [str(i) for i in row]
            output.append(", ".join(row))
        self.formatted_results = "\n".join(output)

    def output_results(self):
        raise NotImplementedError()

    def process_format(self):
        self.connect()
        self.construct_query()
        self.do_query()
        self.formate_results()
        self.output_results()


import datetime


class NewVehiclesQuery(QueryTemplate):
    def construct_query(self):
        self.query = "SELECT * FROM Sales WHERE new='true'"

    def output_results(self):
        print(self.formatted_results)


class UserGrossQuery(QueryTemplate):
    def construct_query(self):
        self.query = "SELECT salesperson, sum(amt) FROM Sales GROUP BY salesperson"

    def output_results(self):
        filename = "gross_sales_{0}".format(datetime.date.today().strftime("%Y%m%d"))
        with open(filename, 'w') as outfile:
            outfile.write(self.formatted_results)
