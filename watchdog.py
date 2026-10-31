import random
battery = 100.0
for i in range (10):
  battery = battery - random.uniform(1.5, 3.5)
  if battery < 75:
      print ("EMERGENCY RETURN TRIGGERED")
      break
  elif battery < 80:
      print("Bro , watch out") 