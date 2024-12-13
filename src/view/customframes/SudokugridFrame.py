import customtkinter as ctk


class SudokuFrame(ctk.CTkFrame):

    game_field = [[0 for _ in range(9)] for _ in range(9)]

    def __init__(self, master, game_gridsize):
        
        super().__init__(master)
        
        self.game_gridsize = game_gridsize
        self.gridsize = self.game_gridsize+(self.game_gridsize-1)
        
        self.configure_grid()
        self.initialize_fields()  # ideally should be dynamically scaled
        

        self.add_horizontal_separators()
        self.add_vertical_separators()



    def configure_grid(self):
        self.grid_columnconfigure([i for i in range(self.gridsize)], weight=1)
        self.grid_rowconfigure([i for i in range(self.gridsize)], weight=1)



    def initialize_fields(self):
        
        self.game_entry_dimension = int(self.master.master.window_height) // self.game_gridsize * 0.75

        self.sudoku_row = 0
        for row in range(self.gridsize):        
            if row % 2 == 0:
                self.sudoku_column = 0
                for column in range(self.gridsize):
                    if column % 2 == 0:
                        self.game_field[self.sudoku_row][self.sudoku_column] = SudokuEntryField(self, self.game_entry_dimension)
                        self.game_field[self.sudoku_row][self.sudoku_column].grid(row=row, column=column, sticky="nsew", padx=2, pady=2)
                        self.sudoku_column += 1
                self.sudoku_row += 1




    def add_horizontal_separators(self):
        for row in range(self.gridsize):
            if row % 2 != 0 and (row + 1) % 3 == 0:
                ctk.CTkFrame(self, height=4, fg_color="#505070", corner_radius=2).grid(row=row, column=0, columnspan=self.gridsize, sticky="ew", pady=3)



    def add_vertical_separators(self):
        for col in range(self.gridsize):
            if col % 2 != 0 and (col + 1) % 3 == 0:
                ctk.CTkFrame(self, width=4, fg_color="#505070", corner_radius=2).grid(row=0, column=col, rowspan=self.gridsize, sticky="ns", padx=3)
               
                
            


    


class SudokuEntryField(ctk.CTkEntry):

            def __init__(self, master, entry_dimensions):      

                self.entry_variable = ctk.StringVar()       

                super().__init__(master, 
                                 width= entry_dimensions, 
                                 height = entry_dimensions, 
                                 font = ("Arial", 34), 
                                 textvariable=self.entry_variable, 
                                 justify="center"
                                )

           
                self.entry_variable.trace_add("write", self.sudoku_callback)


            def sudoku_callback(self, *args):

                if len(self.entry_variable.get()) > 1:
                    self.entry_variable.set(self.entry_variable.get()[1:])
                    
                if (not self.entry_variable.get().isdigit() or self.entry_variable.get() == "0"):
                    self.entry_variable.set("")

            
