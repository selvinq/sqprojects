#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Welcome message

yes_answers = ['yes', 'Yes', 'YES', 'Y', 'y', 'Yeah', 'yeah', 'Yea', 'yea', 'Yup', 'yup']
no_answers = ['no', 'No', 'NO', 'N', 'n', 'Naw', 'naw', 'Nope', 'nope']

print('Welcome to the SQ Insta-Beat Program!')

# Start the program
while True:
    start = input('\nEnter Start to begin: ')
    
    if start == 'Start':
        break
    else:
        print('Type Start')

# Ask user for their name
name = input("\nWhat's your name? ")

print('\nDope! Nice to meet you, '+ name + "! Let's get started!")

# Request user to open the digital audio workstation (DAW)
while True:
    openGB = input('\nGo ahead and open Garageband by typing Open.: ')
    
    if openGB == 'Open':
        break
    else:
        print('No problem, '+ name + '. Try again.')

# Provide the user with the program instructions
while True:
    letsgo = input("\nGreat, we have Garageband open. I'll walk you through making a beat.\nAll you have to do choose your instruments and I'll do the rest!\nSounds good?")
    
    if letsgo in yes_answers:
        break
    else:
        print('No problem. Try again.')
        
        
# Creates the DAW instrument library

# Drums
kicks = ['Kick 1', 'Kick 2','Kick 3','Kick 4','Kick 5',]
snares1 = ['Snare 1', 'Snare 2', 'Clap 1', 'Clap 2', 'Rimshot 1', 'Rimshot 2']
snares2 = ['Snare 3', 'Snare 4', 'Clap 3', 'Clap 4', 'Rimshot 3', 'Rimshot 4']
hihats = ['Hi-Hat 1', 'Hi-Hat 2', 'Shaker 1', 'Shaker 2']
drumpattern = ['Boom bap pattern', 'Simple pattern', 'Upbeat pattern', 'Lo-fi pattern']

# Chords
piano = ['Grand Piano', 'Electric Piano', 'Organ', 'Harpsichord']
chordprogression = ['Progression 1', 'Progression 2', 'Progression 3']

# Bassline
bass = ['Acoustic Bass', 'Electric Bass', 'Synth Bass']
bassline = ['Bassline 1', 'Bassline 2', 'Bassline 3']

# Melody
melodyinst = ['Flute', 'Violin', 'Guitar', 'Synth Lead', 'Saxophone', 'Clarinet']
melody = ['Melody 1', 'Melody 2', 'Melody 3', ]

print("\nFirst, we'll start off with the drums.\n")

# Request user to choose a kick.
while True:
    userkick = input('Choose a kick drum:\n\nKick 1\nKick 2\nKick 3\nKick 4\nKick 5\n\nYour choice: ')
    
    if userkick in kicks:
        print('\nNice!\n')
        break
    else:
        print('Make sure you choose one of the kicks above.')

# Request user to choose a snare.
while True:
    usersnare1 = input('Choose a snare drum:\n\nSnare 1\nSnare 2\nClap 1\nClap 2\nRimshot 1\nRimshot 2\n\nYour choice: ')
    
    if usersnare1 in snares1:
        print("\nPerfect!\n\nOkay " + name + ", let's make things interesting and choose another snare to layer on top of the first one\n")
        break
    else:
        print('Make sure you choose one of the snares above.')

# Request user to choose a 2nd snare.
while True:
    usersnare2 = input('Choose a second snare:\n\nSnare 3\nSnare 4\nClap 3\nClap 4\nRimshot 3\nRimshot 4\n\nYour choice: ')
    
    if usersnare2 in snares2:
        print('\nKick and snares are done! Time for the hi-hats.\n')
        break
    else:
        print('Make sure you choose one of the snares above.')      

# Request user to choose a hi-hat.
while True:
    userhihats = input('Choose a hi-hat:\n\nHi-Hat 1\nHi-Hat 2\nShaker 1\nShaker 2\n\nYour choice: ')
      
    if userhihats in hihats:
        print("\nNow we'll put all of those sounds into a pattern.")
        break
    else:
        print('Make sure you choose one of the hi-hats above.')      

# Request user to choose a drum pattern.
while True:
    userdrumpattern = input('\nChoose a drum pattern:\n\nBoom bap pattern\nSimple pattern\nUpbeat pattern\nLo-fi pattern\n\nYour choice: ')
      
    if userdrumpattern in drumpattern:
        print('\nDope! Give me a sec while I put your drum pattern in a loop...\n...\n...\n...\nDone!\n')
        break
    else:
        print('Make sure you choose one of the hi-hats above.')        

print('Good job, ' + name + '! I like the drums you picked for this one. On to the instruments.\nWe will start with a layer of chords.\n')

# Request user to choose a piano and chord progression
while True:
    userpiano = input('Choose a piano:\n\nGrand Piano\nElectric Piano\nOrgan\nHarpsichord\n\nYour choice: ')
      
    if userpiano in piano:
        break
    else:
        print('Make sure you choose one of the pianos above.')

while True:
    userprogression = input('\nChoose a chord progression:\n\nProgression 1\nProgression 2\nProgression 3\n\nYour choice: ')
    
    if userprogression in chordprogression:
        print('\nThanks! Time for the bass!\n')
        break
    else:
        print('Make sure you choose one of the progressions above.')

# Request user to choose a bass and bassline
while True:
    userbass = input('Choose a bass:\n\nAcoustic Bass\nElectric Bass\nSynth Bass\n\nYour choice: ')
      
    if userbass in bass:
        break
    else:
        print('Make sure you choose one of the basses above.')

while True:
    userbassline = input('\nChoose a bassline:\nBassline 1\nBassline 2\nBassline 3\n\nYour choice: ')
    
    if userbassline in bassline:
        print('\nFinally, choosing a melody for your beat.\n')
        break
    else:
        print('Make sure you choose one of the basslines above.')
        
# Request user to choose an instrument for the melody and the melody itself
while True:
    usermelodyinst = input('Choose an instrument for the melody:\n\nFlute\nViolin\nGuitar\nSynth Lead\nSaxophone\nClarinet\n\nYour choice: ')
      
    if usermelodyinst in melodyinst:
        break
    else:
        print('Make sure you choose one of the instruments above.')

while True:
    usermelody = input('\nChoose a melody:\n\nMelody 1\nMelody 2\nMelody 3\n\nYour choice: ')
    
    if usermelody in melody:
        print('\nDope! Almost done here, ' + name + '!\n')
        break
    else:
        print('Make sure you choose one of the melodies above.')

# Compile user's choices into sounds and patterns
usersounds = [userkick, usersnare1, usersnare2, userhihats, userpiano, userbass, usermelodyinst]
userpatterns = [userdrumpattern, userprogression, userbassline, usermelody]

# Show user their choices
print('\nHere is a list of your sounds:\n\nSOUNDS\n')

for n in usersounds:
    print(n)
              
moveon = input('\nEnter any key to see a list of your patterns: ')
    
print('\nHere is a list of your patterns:\n\nPATTERNS\n')

for n in userpatterns:
    print(n)

moveon = input('Enter any key to finish up: ')

print('\nEverything looks great!\nI will put your sounds and patterns together and mix them together.\n')

# Check if user is ready to finish the beat
while True:
    mix = input('Ready to mix and finish your beat?: ')
    
    if mix in yes_answers:
        print('\nBoom! Your beat is mixed, finalized, and sounds fire!!!\n')
        break
    elif mix in no_answers:
        print("No worries, I'll give you some time to vibe to it a little :) \n")
    else:
        print('Hmm, not sure I understood that. Try again\n')

# Ending message
print('Thanks for using the SQ Insta-Beat Program, ' + name + '! Hope to make some more music with you again soon!')

