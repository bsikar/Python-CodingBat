def caught_speeding(speed, is_birthday):
  x = 5 if is_birthday else 0
  if speed <= 60 + x:
    return 0
  elif speed >= 61 + x and speed <= 80 + x:
    return 1
  else:
    return 2
