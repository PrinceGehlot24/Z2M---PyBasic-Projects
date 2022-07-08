from prettytable import PrettyTable
""""creating an object from Class"""
table = PrettyTable()

"""calling a method situated in the class."""
table.add_column("Classes", ["Class 1", "Class 2", "Class 3"])
table.add_column("Students", ["25", "30", "28"])

"""calling an attribute situated in the class."""
table.align = "r"

print(table)
