import sys
import math
import json


with open('temp.json') as json_file:
    json_data = json.load(json_file)


MAX_NUMBER = 16000


my_position = [] 
your_position = [] 

for key in json_data["my_position"].keys():
    my_position.append(json_data["my_position"][key]) 

for key in json_data["your_position"].keys():
    your_position.append(json_data["your_position"][key]) 


current_stone_number = 0 
index = 0
min_length = MAX_NUMBER #16000
x_length = MAX_NUMBER
y_length = MAX_NUMBER


two_stone = MAX_NUMBER
your_dist = MAX_NUMBER
a = 0 #상대방 돌의 index 번호
b = 0 #상대방 돌의 index 번호2
two_stone_index1 = 0
two_stone_index2 = 0

#상대방 돌이 얼마나 뭉쳐있는지 확인
while a <= (len(your_position)-2):
    b = a+1
    while b <= (len(your_position)-1):
        your_dist = math.sqrt((your_position[a][0]-your_position[b][0])*(your_position[a][0]-your_position[b][0])+(your_position[a][1]-your_position[b][1])*(your_position[a][1]-your_position[b][1]))
        if two_stone > your_dist:
            two_stone_index1 = a #뭉친돌1
            two_stone_index2 = b #뭉친돌2
            two_stone = your_dist
        b += 1
    a += 1

#두 돌 사이 공격
avg_x = (your_position[two_stone_index1][0]+your_position[two_stone_index2][0])/2
avg_y = (your_position[two_stone_index1][1]+your_position[two_stone_index2][1])/2

#충분히 뭉쳐있다면 뭉친 돌들을 공격, 아니라면 그냥 가장 가까운 돌 공격
if your_dist <= 150:
    for my in my_position:
        x_distance = abs(my[0]-avg_x)
        y_distance = abs(my[1]-avg_y)

        current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance) 
        if min_length > current_distance: 
            current_stone_number = index 
            min_length = current_distance 
            x_length = avg_x - my[0] 
            y_length = avg_y - my[1] 
            stone_x_strength = x_length * 10 
            stone_y_strength = y_length * 10
    index = index + 1

else: #뭉쳐있는 곳이 없는 경우
    for my in my_position:
        for your in your_position:
            x_distance = abs(my[0] - your[0]) #내 돌과 상대 돌과의 x축거리
            y_distance = abs(my[1] - your[1]) #내 돌과 상대 돌과의 y축거리
            current_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance) #내 돌과 상대 돌 사이의 현재 거리
            if min_length > current_distance: #현재거리가 최소거리보다 작다면
                current_stone_number = index 
                min_length = current_distance #현재거리를 최소거리로 삼는다.
                x_length = your[0] - my[0] #최소거리에서의 x축거리
                y_length = your[1] - my[1] #최소거리에서의 y축거리
                stone_x_strength = x_length * 7 
                stone_y_strength = y_length * 7
        index = index + 1


#Return values
message = ""
stone_number = current_stone_number #최종 도출된 최소거리에 있는 상대방의 돌을 스톤 넘버에 넣어준다.



result = [stone_number, stone_x_strength, stone_y_strength, message, two_stone_index1, two_stone_index2]
print(str(result)[1:-1].replace("'", ""))
