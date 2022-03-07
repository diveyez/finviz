def create_table_string(table_list):
    """ Used to create a readable representation of a table. """

    col_size = [max(map(len, col)) for col in zip(*table_list)]
    format_str = " | ".join([f"{{:<{i}}}" for i in col_size])
    table_list.insert(1, ["-" * i for i in col_size])

    return "".join(format_str.format(*item) + "\n" for item in table_list)
