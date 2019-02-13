from counter import Counter 
#create counter object
tally = Counter()
#reset values
tally.reset()
#limit clicks to two
tally.setlimit(2)
#click twice and print value
tally.click()
tally.click()
result = tally.getValue()
print("Value:", result)
#click and print value
tally.click()
result = tally.getValue()
print("Value:", result)

