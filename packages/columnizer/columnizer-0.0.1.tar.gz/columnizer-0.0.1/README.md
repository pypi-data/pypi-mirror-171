# columnizer
This is a simple package for which creates columnized text tables.  This is particularly useful where the text is of N length.  You can use the following example, to show a good set of uses. I find this code particularly useful in command line tools.

    from columnizer import *
    def test_columns(columnizer):
        test_text = "the quick brown fox jumped over the lazy dogs!"
        column_count = len(columnizer.columns)
        test_rows = []
        if columnizer.first_row_headers:
            header_titles=["A","B","C","D","E","F","G","H"]
            test_rows.append(header_titles[:column_count])
        test_rows.append([test_text for _ in range(0,column_count)])
        result = columnizer.apply(test_rows)
        print (result)

    c = Columnizer(
        columns=[ColumnClipped(width=25), ColumnLineWrap(width=17), ColumnWordWrap(width=17),
                 ColumnWordWrap(alignment=ColumnTextAlignment.RIGHT, width=17),
                 ColumnWordWrap(alignment=ColumnTextAlignment.CENTER, width=17)],
        style = ColumnTableStyleHeavy())

    print ("Heavy:")
    test_columns(c)

    c = Columnizer(
        columns=[ColumnClipped(width=25), ColumnLineWrap(width=17), ColumnWordWrap(width=17),
                 ColumnWordWrap(alignment=ColumnTextAlignment.RIGHT, width=17),
                 ColumnWordWrap(alignment=ColumnTextAlignment.CENTER, width=17)])

    print ("Default:")
    test_columns(c)

    print ("Default + Headers:")
    c.first_row_headers = True
    test_columns(c)


Columns are actual classes, and are used to describe the physical size and style of the columns. 
Rows are lists of lists, with each container list being used to store data for each column in the row.
