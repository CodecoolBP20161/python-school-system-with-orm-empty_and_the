from model_applicant import *


class Table:

    def __init__(self, table, title_list):
        self.table = Table.change_table_data_to_str(table)
        self.title_list = title_list

    # printing tables
    def __str__(self):
        self.table.insert(0, self.title_list)

        self.table = [[str("| " + cell) for cell in row] for row in self.table]
        lenghts = [max(map(len, col)) for col in zip(*self.table)]
        width_format = ''.join('{{:<{}}}'.format(x) for x in lenghts)
        self.table = [width_format.format(*row) for row in self.table]

        self.table[:] = [x for i in self.table for x in [i + ' |', '-'*(2+len(self.table[0]))]]
        self.table.insert(0, "-"*(len(self.table[0])))

        row_list = list(self.table[1])
        for i in range(len(self.table[1])):
            if row_list[i] == "|":
                for k in range(1, len(self.table)-1):
                    row_list2 = list(self.table[k])
                    row_list2[i] = "|"
                    self.table[k] = "".join(row_list2)

        return '\n'.join(self.table)

    # get's a lists in list table and returns the same table but with all of data converted to string
    @staticmethod
    def change_table_data_to_str(table):
        for index, item in enumerate(table):
            table[index] = list(item)
            for i, j in enumerate(table[index]):
                table[index][i] = str(j)
        return table
