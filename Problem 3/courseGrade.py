def courseGrade():

    with open('./Problem 3/report.txt', 'w') as report:

        report_line_num = 0

        midterm1_total = 0
        midterm2_total = 0
        finals_total = 0

        with open(input(), 'r') as file:

            line = file.readline()

            while line:
            
                tokens = line.split('\t')
                
                for i in range(len(tokens)):
                    tokens[i] = tokens[i].strip()

                average_exam_score = ( int(tokens[2]) + int(tokens[3]) + int(tokens[4]) ) / 3
                
                if average_exam_score >= 90:
                    average_exam_score = 'A'
                elif 80 <= average_exam_score < 90:
                    average_exam_score = 'B'
                elif 70 <= average_exam_score < 80:
                    average_exam_score = 'C'
                elif 60 <= average_exam_score < 70:
                    average_exam_score = 'D'
                elif average_exam_score < 60:
                    average_exam_score = 'F'
                
                file_new_line = tokens.copy()
                file_new_line.append(average_exam_score)
                file_new_line = '\t'.join(file_new_line)

                if report_line_num == 0:
                    report.write(f'{file_new_line}')
                else:
                    report.write(f'\n{file_new_line}')
                
                report_line_num += 1
                    

                midterm1_total += int(tokens[2])
                midterm2_total += int(tokens[3])
                finals_total += int(tokens [4])

                line = file.readline()
            
            midterm1_average = f'{midterm1_total / report_line_num:.2f}'
            midterm2_average = f'{midterm2_total / report_line_num:.2f}'
            finals_average = f'{finals_total / report_line_num:.2f}'
            
            report.write(f'\n\nAverages: midterm1 {midterm1_average}, midterm2 {midterm2_average}, final {finals_average}')


    # TODO: Declare any necessary variables here. 
      
      
    # TODO: Read a file name from the user and read the tsv file here. 
   
   
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    return

if __name__ == "__main__":
    courseGrade()
    
    