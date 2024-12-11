import customtkinter as ctk

class CheckboxFrame(ctk.CTkFrame):

    def __init__(self, master, rows, columns, **kwargs):

        super().__init__(master, **kwargs)

        self.parent = master
        self.rows = rows
        self.columns = columns
    
        self.rowconfigure([i for i in range (0,rows)], weight=1)
        self.columnconfigure([i for i in range (0,columns)], weight=1)

        self.checkboxes = []

        self.index = 0
        for i in range(0, self.rows):

            for j in range(0, self.columns):

                self.checkboxes.append(ctk.CTkCheckBox(self, text=f"Checkbox {i}-{j}"))
                self.checkboxes[self.index].grid(row = i, column = j, padx=10, pady=10, sticky="ew")
                self.index += 1


class GridCheckBox(ctk.CTkCheckBox):

    def __init__(self, master, row, column, **kwargs):

        self.check_state = ctk.BooleanVar()

        super().__init__(master, variable = self.check_state, **kwargs)

        self.row = row
        self.column = column

        # self.grid(row = self.row, column = self.column, padx=10, pady=10, sticky="ew")