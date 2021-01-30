def squirrel_play(temp, is_summer):
  return (is_summer and temp <= 100 and temp >= 60) or (not is_summer and temp <= 90 and temp >= 60)
