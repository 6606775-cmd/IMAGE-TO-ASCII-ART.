def generate_ascii_art():
    height =28
    width = 55
    
    for row in range(height):
        for column in range(width):
            char = ' '
            
            
            if row == 0:
                if column == 21:
                    char = "."
                elif column == 22:
                    char = "+"
                elif column == 23:
                    char = "#"
                elif 24 <= column <= 31:
                    char = "%"
                elif column == 32:
                    char = "#"
                elif column == 33:
                    char = "+"
                elif column == 34:
                    char = "-"
                    
            elif row == 1:
                if column == 19:
                    char = ":"
                elif column == 20:
                    char = "#"
                elif 21 <= column <= 34:
                    char = "%"
                elif column == 35:
                    char = "*"
                elif column == 36:
                    char = "."
                    
            elif row == 2:
                if column == 17:
                    char = "."
                elif column == 18:
                    char = "*"
                elif column == 19:
                    char = '#'
                elif column == 20:
                    char = '%'
                elif 21 <= column <= 23:
                    char = "#"
                elif column == 24:
                    char = "%"
                elif 25 <= column <= 30:
                    char = "#"
                elif 31 <= column <= 36:
                    char = "%"
                elif column == 37:
                    char = "#"
                elif column == 38:
                    char = "="
                    
            elif row == 3:
                if column == 16:
                    char = ":"
                elif 17 <= column <= 18:
                    char = '#'
                elif 19 <= column <= 20:
                    char = "*"
                elif 21 <= column <= 31:
                    char = "+"
                elif 32 <= column <= 36:
                    char = "*"
                elif column == 37:
                    char = "#"
                elif column == 38:
                    char = "*"
                elif column == 39:
                    char = "."
                    
            elif row == 4:
                if 16 <= column <= 18:
                    char = "*"
                elif 19 <= column <= 25:
                    char = "+"
                elif 26 <= column <= 28:
                    char = "="
                elif 29 <= column <= 32:
                    char = "+"
                elif 33 <= column <= 36:
                    char = "*"
                elif column == 37:
                    char = "+"
                elif 38 <= column <= 39:
                    char = "*"
                
            elif row == 5:
                if column == 15:
                    char = "="
                elif 16 <= column <= 17:
                    char = "*"
                elif 18 <= column <= 27:
                    char = "+"
                elif column == 28:
                    char = "="
                elif 29 <= column <= 31:
                    char = "+"
                elif 32 <= column <= 36:
                    char = "*"
                elif column == 37:
                    char = "+"
                elif column == 38:
                    char = "="
                elif column == 39:
                    char = "*"
                elif column == 40:
                    char = ":"
                    
            elif row == 6:
                if column == 15:
                    char = "+"
                elif column == 16:
                    char = "*"
                elif 17 <= column <= 22:
                    char = "+"
                elif 23 <= column <= 26:
                    char = "="
                elif 27 <= column <= 32:
                    char = "+"
                elif 33 <= column <= 36:
                    char = "*"
                elif column == 37:
                    char = "+"
                elif column == 38:
                    char = "-"
                elif column == 39:
                    char = "="
                elif column == 40:
                    char = ":"
                    
            elif row == 7:
                if 15 <= column <= 18:
                    char = "+"
                elif 19 <= column <= 22:
                    char = "*"
                elif 23 <= column <= 24:
                    char = "+"
                elif 25 <= column <= 26:
                    char = "="
                elif column == 27:
                    char = "-"
                elif 28 <= column <= 31:
                    char = "="
                elif column == 32:
                    char = "+"
                elif 33 <= column <= 34:
                    char = "*"
                elif 35 <= column <= 36:
                    char = "*"
                elif column == 37:
                    char = "+"
                elif column == 38:
                    char = "-"
                elif column == 39:
                    char = "="
                elif column == 40:
                    char = ":"
                    
            elif row == 8:
                if 15 <= column <= 18:
                    char = "+"
                elif column == 19:
                    char = "="
                elif 20 <= column <= 21:
                    char = "+"
                elif column == 22:
                    char = "="
                elif 23 <= column <= 25:
                    char = "+"
                elif 26 <= column <= 29:
                    char = "="
                elif 30 <= column <= 32:
                    char = "+"
                elif column == 33:
                    char = "="
                elif column == 34:
                    char = "+"
                elif 35 <= column <= 37:
                    char = "*"
                elif 38 <= column <= 39:
                    char = "="
                elif column == 40:
                    char = ":"
            
            elif row == 9:
                if column==14:
                    char = "."
                elif column==15:
                    char = "="
                elif column == 16:
                    char = "*"
                elif 17<= column<= 18:
                    char = "+"
                elif column == 19:
                    char = "*"
                elif column in (20,21,22):
                    char = "#"
                elif column == 23:
                    char = "*"
                elif 24<= column <=28:
                    char = "+"
                elif column in (29,30):
                    char = "*"
                elif column in (31,32):
                    char = "+"
                elif column ==33:
                    char = "*"
                elif 34<= column <= 36:
                    char = "#"
                elif column == 37:
                    char ="*"
                elif column == 38:
                    char = "+"
                elif column == 39:
                    char = "="
                elif column == 40:
                    char = "-" 
                
            elif row == 10: 
                if column in (14,15):
                    char = "="
                elif 16<= column<=24:
                    char = "+"
                elif column in (25,26):
                    char = "*"
                elif column in(27,28,29):
                    char ="+"
                elif column in(30,31):
                    char = "#"
                elif column in(32,33):
                    char = "+"
                elif 34<= column <= 38:
                    char = "*"
                elif column ==39:
                    char = '='
                elif column ==40:
                    char = "*"
                elif column == 41:
                    char = "-"
                    
            elif row == 11: 
                if column in (14,15):
                    char = "="
                elif 16<= column<=19:
                    char = "+"
                elif column == 20 :
                    char = "="
                elif column == 21 :
                    char = "+"
                elif 22<= column<=25:
                    char = "="
                elif 26<= column<=29:
                    char = "+"
                elif column ==30:
                    char = "*"
                elif column ==31:
                    char = "#"
                elif 32<= column <= 36:
                    char ="+"
                elif column == 37:
                    char ="*"
                elif column == 38:
                    char ="+"
                elif column == 39:
                    char ="="
                elif column == 40:
                    char ="#"
                elif column == 41:
                    char =":"
                
            elif row ==12:
                if column == 14:
                    char = ":"
                elif column in(15,16):
                    char ="+"
                elif 17<= column <= 20:
                    char = "="
                elif column == 21:
                    char ="-"
                elif column ==22:
                    char = "="
                elif column ==23:
                    char = "+"
                elif 24<= column <= 27:
                    char = "="
                elif column == 28:
                    char ="-"
                elif column ==29:
                    char = "="
                elif column ==30:
                    char = "+"
                elif column in(31,32):
                    char = "*"
                elif column ==33:
                    char = "+"
                elif column in(34,35):
                    char = "="
                elif column ==36:
                    char = "+" 
                elif column ==37:
                    char = "*" 
                elif column in(38,39):
                    char = "+"
                elif column == 40:
                    char = "*"
            
            elif row ==13:
                if column == 15:
                    char = "-"
                elif column ==16:
                    char ="="
                elif column ==17:
                    char ="+"
                elif  18<= column <=28:
                    char ="="
                elif column == 29:
                    char = "+"
                elif 30<= column <= 33:
                    char ="*"
                elif 34<= column <= 37:
                    char ="+" 
                elif column == 38:
                    char = "*"
                elif column == 39:
                    char = "+"   
                elif column == 40:
                    char = ":"
                                  
            elif row ==14 :
                if column == 16:
                    char = "."
                elif column in(17,18):
                    char = "="
                elif column == 19:       
                    char = "+"
                elif column ==20:
                    char = "="
                elif column in (21,22):
                    char = "+"
                elif 23<=column <=25:
                    char ="="
                elif column == 26:
                    char = "+"
                elif column ==27:
                    char = "="
                elif 28<= column <=30:
                    char ="+"
                elif 31<= column <=33:
                    char = "*"
                elif column in (34,35):
                    char = "+"
                elif 36<= column<=38:
                    char = "*"
                elif column == 39:
                    char = "-"
                 
            elif row ==15:                          
                if column ==17:
                    char ="-"
                elif 18<= column<=21:
                    char ="="
                elif 22<=column <=24:
                    char = "+"
                elif column ==25:
                    char = "="
                elif column ==26:
                    char ="-"
                elif column == 27:
                    char = ":"
                elif column in (28,29):
                    char = "-"
                elif column == 30:
                    char = "="
                elif column ==31:
                    char = "+"
                elif column in (32,33):
                    char = "#"
                elif column ==34:
                    char = "*"
                elif column in (35,36):
                    char = "+"
                elif column == 37:
                    char = "#"
                elif column == 38:
                    char ="+"
                elif column == 39:
                    char ="."
                              
            elif row == 16:
                if column == 17:
                    char = "-"
                elif 18<= column <=25:#+***+**.
                    char = "=" 
                elif column in (26,27):
                    char = "-"
                elif 28<= column <= 30:
                    char = "="
                elif column == 31:
                    char = "+"
                elif 32<= column <= 34:
                    char ="*"
                elif column == 35:
                    char= "+"
                elif column in (36,37):
                    char = "*"
                elif column ==38:
                    char = "."
            
            elif row == 17:
                if column == 17:
                    char ="-"
                elif 18<=column<=22:
                    char = "+"
                elif 23<=column <=30:
                    char  ="="
                elif column  in (31,32):
                    char = "+"
                elif column in (33,34):
                    char = "*"
                elif column == 35:
                    char = "#"
                elif column ==36:
                    char="*"
                elif column == 37:
                    char = "-"
            elif row == 18:
                if column == 17:
                    char ="="
                elif 18<=column<=22:
                    char = "+"
                elif 23<=column <=28:
                    char  ="="
                elif column  in (29,30):
                    char = "+"
                elif column in (31,32,33):
                    char = "*"
                elif 34<=column <= 36:
                    char = "#"
                elif column ==37:
                    char="+"
                elif column == 38:
                    char = ":"
            elif row == 19:
                if column ==16:
                    char = "-"
                elif 17<=column <= 22:
                    char ="+"
                elif column == 23:
                    char = "*"
                elif column ==24:
                    char = "+"
                elif 25<= column<=29:
                    char = "="
                elif column ==30:
                    char ="+"
                elif column in (31,32):
                    char = "*"
                elif column == 33:
                    char = "#"
                elif column in (34,35):
                    char = "%"
                elif column ==36:
                    char = "#"
                elif column ==37:
                    char = "*"
                elif column == 38:
                    char = "-"
                    
            elif row ==20:
                if column in(13,14,16):
                    char = "."
                elif 17<=column<=25:
                    char ="+"
                elif 26<=column <=28:
                    char = "*"
                elif  29<=column<= 36:
                    char ="#"
                elif column == 37:
                    char = "*"
                elif 38<=column<= 41:
                    char ="."
                elif column == 42:
                    char ="-"
                elif column == 43:
                    char = ":"
                elif column == 44:
                    char = "." 
                    
            elif row == 21:
                if column == 10:
                    char ="."
                elif column ==11:
                    char = ":"
                elif column ==12:
                    char = "="
                elif column ==13:
                    char = "+"
                elif column in(14,16,17):
                    char = "."
                elif 18<= column<=20:
                    char = "+"
                elif 21<= column <= 27:
                    char = "="
                elif column in(28,29):
                    char ="+"
                elif 30<= column <= 36:
                    char = "*" 
                elif column ==37:
                    char = "+"
                elif 38<= column <= 40:
                    char = "."
                elif column in(41,43):
                    char = ":"
                elif column == 42:
                    char = "-"
                elif column in (44,46):
                    char = "="
                elif column == 45:
                    char = "*"
                elif column in (47,48):
                    char = ":"
                elif column ==49:
                    char = "."
                    
            elif row == 22:
                if column ==5:
                    char ="."
                elif column in (6,8):
                    char = "="
                elif column == 7:
                    char = "*"
                elif column in(9,10):
                    char= ":"
                elif column == 11:
                    char = "="
                elif column == 12:
                    char = "."
                elif column  ==16:
                    char =":"
                elif column in (17,18):
                    char = "+"
                elif 19<= column <= 25:
                    char ="="
                elif 26<= column <= 31:
                    char = "+"
                elif 32<= column <= 34:
                    char = "*"
                elif column == 35:
                    char = ":"
                elif 36<= column <= 39:
                    char = "."
                elif column in (40,41):
                    char = ":"
                elif 42<= column <= 52:
                    char = "."
                
            elif row == 23:
                if column in (1,3):
                    char = ":"
                elif column ==2:
                    char ="="
                elif column ==4:
                    char = "."
                elif column in (5,6):
                    char = "*"
                elif column == 7:
                    char = "="
                elif column == 8:
                    char = ":"
                elif column in (9,10):
                    char = "."
                elif 13<=column<=17:
                    char = "."
                elif 18<= column <= 27:
                    char = "="
                elif 28<= column <= 34:
                    char = "+"
                elif column == 35:
                    char ="="
                elif 36<=column <=55:
                    char = "."
                
            elif row ==24:
                if column ==1:
                    char = "+"
                elif column == 2:
                    char ="#"
                elif column == 3:
                    char = "*"
                elif column == 4:
                    char = "="
                elif column == 5:
                    char = ":"
                elif 6<= column <= 8:
                    char = "."
                elif 11<= column <=16:
                    char = "."
                elif column  ==20:
                    char = ":"
                elif 21<= column <=30:
                    char = "="
                elif 31<= column <= 34:
                    char = "+"
                elif column == 35:
                    char = ":"
                elif 36<= column<=55:
                    char = "."
                
            elif row ==25:
                if 1<=column <=6:
                    char = "."
                elif 9<= column <= 18:
                    char ="."
                elif column == 23 :
                    char = ":"
                elif column == 24 :
                    char = "-"
                elif column == 25 :
                    char = "="
                elif column in (26,27):
                    char = "+"
                elif 28<= column <= 32:
                    char ="="
                elif column ==33:
                    char = "-"
                elif 34<=column <=55:
                    char = "."
            
            elif row ==26:
                if column == 1:
                    char = "."
                elif 6<= column <=27:
                    char = "."
                elif 31<= column <=55:
                    char = "."
                    
            elif row in(27,28):
                if 1<= column <=55:
                    char = "."
        
            print(char, end='')

            
        print()
        
generate_ascii_art()