#!/usr/bin/python3                                                  
                                                                    
def square_matrix_simple(matrix=[]):                                
                                                                    
        new_matrix = []                                             
        tmp = []                                                    
        for row in matrix:                                          
                for element in row:                                 
                        tmp.append(element**2)                      
                new_matrix.append(tmp)                              
                tmp = []                                            
                                                                    
        return (new_matrix)                                         
                               
