# sudoku
calculate 9*9 sudoku

there are two files in the source dictionary
        sudoku.py
        generator.py

about sudoku.py :
        1. purpose: it is used to solve sudoku problems
        2. It include 10 function:
               (1) receiver(n): receive a sudoku, and return this 'grid' in the form of nested list 
               (2) input_order() : receive a number 'n', which is the order of the sudoku, and return 'n^2'
                            all the n below means  len(grid)
               (3) S_reverse(n) : is the inverse process of S
               (4) S(n) : is a fomular to ouput a number;
               (5) initial_state(n) : return 'clause' in the form of nested list
               (6) R_1(n) : the first rule of solving a sudoku; it means every row contains every number in the range of (1,n+1)
               (7) R_2(n) : the second rule of solving a sudoku; it means every colunm contains every number in the range of (1,n+1)
               (8) R_3(n) : the third rule of solving a sudoku; it means every n^2 square contains every number in the range of (1,n+1)
               (9) R_4(n) : the fourth rule of solving a sudoku; it means every cell can only contain one number
               (10) final_sudoku(n, model, grid) : return the final sudoku of every case; return -1 if it is insoluble 
        3. usage: first input a number 'n', which is the order of your sudoku;
                        then input your sudoku.

about generator.py :
       1. purpose : it is used to generate a n^2*n^2 sudoku, which can not guarantee the exsitence of the solution.
       2. it include 1 main function:
              (1) generator(n,p) : 'n' means the order of your sudoku; p means the proportion of a cell to be filled with a nonzero number;
                                               it will return a sudoku in random in numpy array
              
                        
