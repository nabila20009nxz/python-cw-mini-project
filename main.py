def padel_court_cost(court_type):
  if court_type == "indoor":
    return 30 
  if court_type == "outdoor":
    return 20  
  
def rackets_cost (racket_brand):
    if racket_brand == "Bullpadel":
      return 100
    elif racket_brand == "Nox": 
      return 140
    elif racket_brand == "Siux": 
      return 200
    
def padel_balls_cost (ball_boxes): 
  if ball_boxes== "one box":
    return 2
  elif ball_boxes== "two boxes":
    return 3.5
  elif ball_boxes=="three boxes":
    return 5  
  else: 
    return False
  
def padel_game_cost ():

     court_type = input("enter the court_type: ") 
     racket_brand = input("enter the racket brand: ")
     ball_boxes = int(input("enter the number of ball boxes: "))
     return padel_court_cost(court_type) + rackets_cost(racket_brand)+ padel_balls_cost(ball_boxes)

print(f"Results is {padel_game_cost()}")
