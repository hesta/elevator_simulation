import random 

incall = range(0, 6) #Incall: 0, 1, 2 ,3, 4, 5 
up = range(6, 11)   #Up call: 6, 7, 8, 9, 10, False
up.append(False)
down = [False]
down.extend(range(11,16)) #Down call: False, 11, 12, 13, 14, 15
 

#call = [11, 15, 13, 12, 15, 12, 2, 5, 15, 8, 10, 13, 6, 9, 0, 4, 15, 10, 8, 15]
option = range(0, 16)
option.append(None)
call = [random.choice(option) for i in range(0,1000)]

def elevator_control(call, initial):
    current = initial
    message = []
    j = 0
    status = 0 #down: -1, stop: 0 , up = 1  
    goal = -1 
    
    while(end(message, j)):

      if j < len(call):
          if call[j] != None:
              message.append(call[j])             
          j = j+1
     
      goal, status = choose_goal(status, goal, message, current)
      output(message, current)
     
      if current == goal_val(goal):
         message = update(current, status, message)
         
      elif status == -1:
          if goal in down or goal in incall:
              message = update(current, status, message)
          current = current - 1
      
      elif status == 1:
          if goal in up or goal in incall:
              message = update(current, status, message)
          current = current + 1

      else:
          pass
    
      
                            
def update(current, status, message):
    if status == -1:
         mssg = [x for x in message if x != current and x != down[current]]
    elif status == 1:
         mssg = [x for x in message if x != current and x != up[current]]
    else:
         mssg = [x for x in message if x != current]

    return mssg
    

def output(message, current):
    
    print "--------------------------------"
    print "Floor Location Incall  Up   Down"
    ls = range(0, 6)
    ls.reverse() 
 
    for i in ls:
      a, b, c, d = " ", " ", " ", " "
      if i in message: 
         a = "x"
      if up[i] in message:
         b = "x"
      if down[i] in message:
         c = "x"
      if current == i:
         d = "x"

      print " " + str(i)+ "        " + d + "       " + a + "     " + b + "     " + c
          
    
def goal_val(goal):
    if goal in down:
       return down.index(goal)
    elif goal in up:
       return up.index(goal)
    else:
       return goal
        

def choose_goal(status, goal, message, current):
    
    if status == 1 and message:
       if goal not in down:
           new_goal = largest(message)
           if goal_val(new_goal) < goal_val(goal):
              if current >= goal_val(highest(message)):
                  if smallest(message) == 20:
                     goal = message[0]
                  else:
                     goal = smallest(message)
                  status = -1
              else:
                  goal = message[0]
                  if current > goal_val(goal):
                      status = -1
                  else:
                      status = 1
           else:
              goal = new_goal
       else:
          if current == goal_val(goal):
             if smallest(message) == 20:
                 goal = message[0]
                 if current > goal_val(goal):
                      status = -1
                 else:
                      status = 1

             else:
                 goal = smallest(message)
                 if goal_val(goal) > current:
                    goal = message[0]
                    if current > goal_val(goal):
                      status = -1
                    else:
                      status = 1
                 else:
                     status = -1

    
    elif status == -1 and message:
        if goal not in up:
           new_goal = smallest(message)   
           if goal_val(new_goal) > goal_val(goal):
               if current <= goal_val(lowest(message)):
                  if largest(message) == -1:
                     goal = message[0]
                  else:
                     goal = largest(message)
                  status = 1
               else:
                  goal = message[0]
                  if current > goal_val(goal):
                      status = -1
                  else:
                      status = 1
            
           else:
              goal = new_goal
        else:
           if current == goal_val(goal):
              if largest(message) == -1:
                  goal = message[0]
                  if current > goal_val(goal):
                      status = -1
                  else:
                      status = 1

              else:
                 goal = largest(message) 
                 if goal_val(goal) > current:
                    goal = message[0]
                    if current > goal_val(goal):
                      status = -1
                    else:
                      status = 1
                 else:
                     status = 1
         
    else:
        if message:
           goal = message[0] 
        if goal_val(goal) > current:
           status = 1
        elif goal_val(goal) < current:
           status = -1
        else:
           if goal in up:
              status = 1
           elif goal in down:
              status = -1 
           else:
              status = 0
        
    return (goal, status)

def largest(message):
    
    def f(ls):
        if not ls:
           return -1
        elif ls[0] in down:
           return f(ls[1:])
        else:
           result = f(ls[1:])
           if goal_val(ls[0]) > goal_val(result):
              return ls[0]
           else:
              return result

    return f(message)
           
    
def smallest(message):
    
    def f(ls):
        if not ls:
           return 20
        elif ls[0] in up:
           return f(ls[1:])
        else:
           result = f(ls[1:])
           if goal_val(ls[0]) < goal_val(result):
              return ls[0]
           else:
              return result

    return f(message)


def highest(message):
    
    def f(ls):
        if not ls:
           return -1
        else:
           result = f(ls[1:])
           if goal_val(ls[0]) > goal_val(result):
              return ls[0]
           else:
              return result

    return f(message)

def lowest(message):

    def f(ls):
        if not ls:
           return 20
        else:
           result = f(ls[1:])
           if goal_val(ls[0]) < goal_val(result):
              return ls[0]
           else:
              return result

    return f(message)
   
   
def end(message, counter):
    return message or counter < len(call)

    


if __name__ == "__main__":
   print "******************************************************************"
   print "Output shows the process of the elevator handles different requests:"
   print "******************************************************************"
   elevator_control(call,  0)
 
  
    
