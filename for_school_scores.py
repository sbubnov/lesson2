school_data=[
    {'school_class':'4a','scores':[3,4,4,5,2]},
    {'school_class':'5a','scores':[5,4,5,2,3]},
    {'school_class':'6a','scores':[2,5,5,4,4]}]

average_overall=0
count=0

for x in school_data:
    record=x['scores']
    for y in record:
        average_overall=y+average_overall
        count+=1

print('Общий бал по всей школе: '+ str(average_overall/count))