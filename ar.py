def arithmetic_arranger(problems, solutions = False) :
    if len(problems) > 5 : 
        return('Error: Too many problems.')
    
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    arranged_problems = ''
    
    for problem in problems: 
        num1 = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        num2 = problem.split(" ")[2]
        
        if not ((operator == "+") or (operator == "-")):
            return("Error: Operator must be '+' or '-'.")
        if num1.isnumeric() == False :
            return('Error: Numbers must only contain digits.')
        if num2.isnumeric() == False:
            return ('Error: Numbers must only contain digits.')
        if (len(num1) > 4) or (len(num2) > 4) : 
            return ('Error: Numbers cannot be more than four digits.')
        
        solution = ""
        if (operator == "+") : 
            solution = str(int(num1) + int(num2))
        elif (operator == "-") : 
            solution = str(int(num1) - int(num2))
    
        width = max(len(num1), len(num2)) + 2
        top = str(num1).rjust(width)
        bottom = operator + str(num2).rjust(width - 1)
        line = ""
        answer = str(solution).rjust(width)
        for x in range(width) : 
            line += "-"
        
        
        line1 += top + '    '
        line2 += bottom + '    '
        line3 += line + '    '
        line4 += answer + '    '
        
    if solutions == True : 
        arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip() + "\n" + line4.rstrip()
    else : 
        arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
        
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))