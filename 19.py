months = [
            31, #jan  
            28, #feb
            31, #march
            30, #april
            31, #may
            30, #june
            31, #july
            31, #august
            30, #september
            31, #oct
            30, #nov
            31  #dec
          ]

num_sundays = 0
day = 0
sunday = 6
for year in range(101):
  for month in months:
    day = (day + month) % 7
    if year > 0 and day == sunday:
      num_sundays += 1

print num_sundays
