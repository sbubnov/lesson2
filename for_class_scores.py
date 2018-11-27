school_data=[
            {'school_class':'4a','scores':[3,4,4,5,2]},
            {'school_class':'5a','scores':[5,4,5,2,3,3,2,5,4]},
            {'school_class':'6a','scores':[2,5,5,4,4,5,2,5]}]



for x in school_data:
    count=0
    count_score=0
    record=x['scores']
    class_name=x['school_class']
    for y in record:
        count_score=y+count_score
        count+=1
    print('Средняя оценка класса '+class_name+' равна '+str(count_score/count))
    
