import os
student_name =[]
student_no   =[]
natlang_score=[]
math_score   =[]
eng_score    =[]
total_score  =[]
avg_score    =[]
grade        =[]

i = 1
while True :
    ainput = input(str(i)+'번 학생이름, 학번, 국어점수, 수학점수, 영어점수를 입력해주세요. : ')
    asplit = ainput.split(',')
    if len(asplit) != 5 :
        print('정확하게 입력해주세요.')
    else :
        try :
            name = asplit[0]
            no   = int(asplit[1])
            natlang = int(asplit[2])
            math = int(asplit[3])
            eng  = int(asplit[4])
            
            student_name.append(name)
            student_no.append(no)
            natlang_score.append(natlang)
            math_score.append(math)
            eng_score.append(eng)
            total_score.append(natlang+math+eng)
            avg_score.append(int((natlang+math+eng)/3))
            
            i = i+1
        except Exception as ex:
            print(ex)
            print('입력값이 잘못되었습니다. 확인해주세요.\n')
            print(asplit)
            continue
    
    if i > 10:
        break


for i in range(0, len(total_score)):
    r = 1
    for j in range(0, len(total_score)):
        if total_score[i] < total_score[j]: r += 1
    grade.append(str(r))


rank = 1

while True :
    res_list = list(filter(lambda x: grade[x] == str(rank), range(len(grade))))
    
    for i in res_list :
        joinList = [str(student_name[i]), str(student_no[i]),  str(natlang_score[i]), str(math_score[i]), str(eng_score[i]), str(total_score[i]),str(avg_score[i]), str(grade[i])]
        print(",".join(joinList))
    
    rank = rank +1
    
    if rank > 10 :
        break

os.system("pause")    

    
    
    