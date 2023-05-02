### VisualStudioCode ###
feat: Add .gitignore
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  touch .gitignore
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  vi .gitignore
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  git status
현재 브랜치 main
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.

추적하지 않는 파일:
  (커밋할 사항에 포함하려면 "git add <파일>..."을 사용하십시오)
	.gitignore

커밋할 사항을 추가하지 않았지만 추적하지 않는 파일이 있습니다 (추적하려면 "git
add"를 사용하십시오)
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  git add .gitignore
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main ✚  git commit
[main 1a79e2d] feat: Add .gitignore
 1 file changed, 77 insertions(+)
 create mode 100644 .gitignore
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall  ↱ main  git status
현재 브랜치 main
#Play the game
  win_no_switch_cnt = 0
  doors = [0,1,2] #Get the doors
  num_doors = len(doors) #Get the number of doors

    door_with_prize = random.randint(0, num_doors-1) #Randomly choose the door with the wanted prize
    host = door_with_prize #The host knows which door has the prize
    #The player chooses initially a random door that s/he believes has the prize
    player_choice = random.randint(0, num_doors-1)
    original_player_choice = player_choice
      player_choice = switch_function(shown_door,num_doors, player_choice)

      win_no_switch_cnt = win_no_switch_cnt + 1
브랜치가 'origin/main'보다 1개 커밋만큼 앞에 있습니다.
  (로컬에 있는 커밋을 제출하려면 "git push"를 사용하십시오)

커밋할 사항 없음, 작업 폴더 깨끗함
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall  ↱ main  git push origin main
오브젝트 나열하는 중: 4, 완료.
오브젝트 개수 세는 중: 100% (4/4), 완료.
Delta compression using up to 8 threads
오브젝트 압축하는 중: 100% (3/3), 완료.
오브젝트 쓰는 중: 100% (3/3), 974 bytes | 974.00 KiB/s, 완료.
feat: Add monty_hall.py
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/yd3-team-parrots/monty-hall.git
   5674efc..1a79e2d  main -> main
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  git status
현재 브랜치 main
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.

커밋할 사항 없음, 작업 폴더 깨끗함
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  touch monty_hall.py
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  vi monty_hall.py
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  git add monty_hall.py
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main ✚  git status
현재 브랜치 main
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.

커밋할 변경 사항:
#Play the game
def monty_hall_game(switch, num_tests):
  win_switch_cnt = 0
  win_no_switch_cnt = 0
  lose_switch_cnt = 0
  lose_no_switch_cnt = 0
  doors = [0,1,2] #Get the doors
  num_doors = len(doors) #Get the number of doors


  for i in range(0,num_tests):
    door_with_prize = random.randint(0, num_doors-1) #Randomly choose the door with the wanted prize
    host = door_with_prize #The host knows which door has the prize
    #The player chooses initially a random door that s/he believes has the prize
    player_choice = random.randint(0, num_doors-1)
    original_player_choice = player_choice
    shown_door = get_non_prize_door(host, num_doors, player_choice)
    if switch == True:
      player_choice = switch_function(shown_door,num_doors, player_choice)

"monty_hall.py" 40L, 2243B#Play the game 
def monty_hall_game(switch, num_tests):
  win_switch_cnt = 0
  win_no_switch_cnt = 0
  lose_switch_cnt = 0
  lose_no_switch_cnt = 0
  doors = [0,1,2] #Get the doors
  num_doors = len(doors) #Get the number of doors
  
  
  for i in range(0,num_tests):
    door_with_prize = random.randint(0, num_doors-1) #Randomly choose the door with the wanted prize
    host = door_with_prize #The host knows which door has the prize
    #The player chooses initially a random door that s/he believes has the prize
    player_choice = random.randint(0, num_doors-1) 
    original_player_choice = player_choice
    shown_door = get_non_prize_door(host, num_doors, player_choice)
    if switch == True:
      player_choice = switch_function(shown_door,num_doors, player_choice)
    
    if player_choice == host and switch == False:
      #Then the player wins from not switching
      print('Player Wins (No switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice ,', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      win_no_switch_cnt = win_no_switch_cnt + 1
    elif player_choice == host and switch == True:
      #Then the player wins from switching
      print('Player Wins (switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice , ', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      win_switch_cnt = win_switch_cnt +1
    elif player_choice != host and switch == False:
      #The player lost from not switching
      print('Player Lost ### VisualStudioCode ###
feat: Add .gitignore
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  touch .gitignore
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  vi .gitignore
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  git status
현재 브랜치 main
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.

추적하지 않는 파일:
  (커밋할 사항에 포함하려면 "git add <파일>..."을 사용하십시오)
	.gitignore

커밋할 사항을 추가하지 않았지만 추적하지 않는 파일이 있습니다 (추적하려면 "git
add"를 사용하십시오)
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  git add .gitignore
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main ✚  git commit
[main 1a79e2d] feat: Add .gitignore
 1 file changed, 77 insertions(+)
 create mode 100644 .gitignore
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall  ↱ main  git status
현재 브랜치 main
#Play the game
  win_no_switch_cnt = 0
  doors = [0,1,2] #Get the doors
  num_doors = len(doors) #Get the number of doors

    door_with_prize = random.randint(0, num_doors-1) #Randomly choose the door with the wanted prize
    host = door_with_prize #The host knows which door has the prize
    #The player chooses initially a random door that s/he believes has the prize
    player_choice = random.randint(0, num_doors-1)
    original_player_choice = player_choice
      player_choice = switch_function(shown_door,num_doors, player_choice)

      win_no_switch_cnt = win_no_switch_cnt + 1
브랜치가 'origin/main'보다 1개 커밋만큼 앞에 있습니다.
  (로컬에 있는 커밋을 제출하려면 "git push"를 사용하십시오)

커밋할 사항 없음, 작업 폴더 깨끗함
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall  ↱ main  git push origin main
오브젝트 나열하는 중: 4, 완료.
오브젝트 개수 세는 중: 100% (4/4), 완료.
Delta compression using up to 8 threads
오브젝트 압축하는 중: 100% (3/3), 완료.
오브젝트 쓰는 중: 100% (3/3), 974 bytes | 974.00 KiB/s, 완료.
feat: Add monty_hall.py
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/yd3-team-parrots/monty-hall.git
   5674efc..1a79e2d  main -> main
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  git status
현재 브랜치 main
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.

커밋할 사항 없음, 작업 폴더 깨끗함
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  touch monty_hall.py
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  vi monty_hall.py
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  git add monty_hall.py
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main ✚  git status
현재 브랜치 main
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.

커밋할 변경 사항:

추적하지 않는 파일:
  (커밋할 사항에 포함하려면 "git add <파일>..."을 사용하십시오)
        .gitignore

(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  git add .gitignore
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main ✚  git commit
 create mode 100644 .gitignore
#Play the game
  win_no_switch_cnt = 0
  doors = [0,1,2] #Get the doors
    door_with_prize = random.randint(0, num_doors-1) #Randomly choose the door with the wanted prize
      win_no_switch_cnt = win_no_switch_cnt + 1
브랜치가 'origin/main'보다 1개 커밋만큼 앞에 있습니다.
  (로컬에 있는 커밋을 제출하려면 "git push"를 사용하십시오)

(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  git status
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  touch monty_hall.py
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  vi monty_hall.py
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main  git add monty_hall.py
(yeardream)  b10@b10ui-iMac  ~/Documents/dev/monty-hall   main ✚  git status
현재 브랜치 main
def monty_hall_game(switch, num_tests):
  win_switch_cnt = 0
  win_no_switch_cnt = 0
  lose_switch_cnt = 0
  lose_no_switch_cnt = 0
  doors = [0,1,2] #Get the doors
  num_doors = len(doors) #Get the number of doors


  for i in range(0,num_tests):
    door_with_prize = random.randint(0, num_doors-1) #Randomly choose the door with the wanted prize
    host = door_with_prize #The host knows which door has the prize
    #The player chooses initially a random door that s/he believes has the prize
    player_choice = random.randint(0, num_doors-1)
    original_player_choice = player_choice
    shown_door = get_non_prize_door(host, num_doors, player_choice)
    if switch == True:
      player_choice = switch_function(shown_door,num_doors, player_choice)

"monty_hall.py" 40L, 2243B#Play the game
def monty_hall_game(switch, num_tests):
  lose_switch_cnt = 0
  lose_no_switch_cnt = 0
  doors = [0,1,2] #Get the doors

  for i in range(0,num_tests):
    door_with_prize = random.randint(0, num_doors-1) #Randomly choose the door with the wanted prize
    player_choice = random.randint(0, num_doors-1)
    original_player_choice = player_choice
    shown_door = get_non_prize_door(host, num_doors, player_choice)
    if switch == True:
      player_choice = switch_function(shown_door,num_doors, player_choice)

    if player_choice == host and switch == False:
      #Then the player wins from not switching
      print('Player Wins (No switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice ,', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      win_no_switch_cnt = win_no_switch_cnt + 1
    elif player_choice == host and switch == True:
      #Then the player wins from switching
      print('Player Wins (switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice , ', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      win_switch_cnt = win_switch_cnt +1
    elif player_choice != host and switch == False:
      #The player lost from not switching
      print('Player Lost (No switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice , ', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
-- INSERT --(No switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice , ', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      lose_no_switch_cnt = lose_no_switch_cnt + 1
    elif player_choice != host and switch == True:
      #The player lost from switching
      print('Player Lost (switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice , ', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      lose_switch_cnt = lose_switch_cnt + 1
    else:
      print('SOMETHING IS WRONG')

  return win_no_switch_cnt,win_switch_cnt,lose_no_switch_cnt,lose_switch_cnt, num_tests
