from numpy import random
import numpy as np
import time

def MontyHallSimulation (N):
    ChoiceUnchanged=[]
    ChoiceChanged=[]
    NN=1
    for i in range(0,N):
        
        # 1) The car is placed behind a random door.
        WinningDoor=random.choice(['1번 문', '2번 문', '3번 문'])

        # 2) The contestant selects a random door.
        FirstSelection=random.choice(['1번 문', '2번 문', '3번 문'])
        
        # 3) The host opens a door that is different than the contestants choice 
        #    and not the door with the car.
        HostOpens=list(set(['1번 문', '2번 문', '3번 문'])-set([FirstSelection,WinningDoor]))[0]
        
        # 4) The other door is not the participant's selected door and not the opened door. 
        OtherDoor=list(set(['1번 문', '2번 문', '3번 문'])-set([FirstSelection,HostOpens]))[0]
        
        # 5) Add "True" to a list where the participant DOES NOT change their selection AND thier 
        #    selection identified the door with the car. 
        ChoiceUnchanged.append(FirstSelection==WinningDoor)
        
        # 6) Add "True" to a list where the participant DOES change their selection and thier 
        #    new selected door has the car behind it.
        ChoiceChanged.append(OtherDoor==WinningDoor)
        
    # NOTE: The boolean object "TRUE" is equal to 1 and "False" is equal to 0.
    #       As such, we can use the "sum" function to get the total number of wins
    #       for each strategy.
    print(f'\n\
    {N:,} 게임이 진행되었습니다. \n\
    다음 전략에 따라 자동차로 이길 확률 :\n\
    초기 선택으로 남아있는 것 : {"{:.1%}".format(sum(ChoiceUnchanged)/N)}\n\
    바뀐 문들 : {"{:.1%}".format(sum(ChoiceChanged)/N)}')
            
###############################            
###### Run the Simulation######
###############################
Start_time = time.time()
MontyHallSimulation(N=100000)         
print(f'\nSimulation Completed in: {round(time.time()-Start_time,2)} Seconds')
