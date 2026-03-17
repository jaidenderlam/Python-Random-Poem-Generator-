import random 

print ("--- Welcome to the poem Generator ---")
adjectives = input("Enter an adjective: ")
nouns = input("Enter a noun: ")
verbs = random.randint(0,4)
if verbs == 0:
    verbs = "runs"
elif verbs == 1:
    verbs = "jumps"
elif verbs == 2:
    verbs = "swims"
elif verbs == 3:
    verbs = "eats"
else:
    verbs = "sleeps"
adverbs = random.randint(0,5)
if adverbs == 0:
    adverbs = "quickly"
elif adverbs == 1:
    adverbs = "slowly"
elif adverbs == 2:
    adverbs = "softly"
elif adverbs == 3:
    adverbs = "creepy"
elif adverbs == 4:
    adverbs = "drowsy"
else:
    adverbs = "sleepy"
  
for i in range(5):
 print("The " + adjectives + " "+ nouns + " "+ verbs + " all day long!!!" ) 
print("\n")

for i in range(2):
   y = (f"""A brain of {nouns}, not flesh and bone,
A mind that's grown, but all alone.
It learns and {verbs}, in circuits deep,
While we're awake, and while we sleep.

It paints and writes, composes songs,
Where did it get, where did it belong?
A {adverbs} tool we built, a {adjectives} thing,
What wonders will tomorrow bring?""")
   d = y.upper()
   print(d + "\n")
    
print( "--- Thank U for using the poem Generator ---" )
