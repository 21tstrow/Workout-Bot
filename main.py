from random import randint
"""
Workouts:

Chest
-----
Barbell Bench (Upper Pec, Lower Pec, tricep, bicep, delts)
Dumbell Bench (Upper Pec, Lower Pec, tricep, bicep, delts)
Incline Barbell Bench (Upper Pec, tricep, bicep, delts)
Incline Dumbbell Bench (Upper Pec, tricep, bicep, delts)
Dumbbell Fly (Upper Pec, Lower Pec, bicep, delts)
Incline Dumbell Fly (Upper Pec, Lower Pec, bicep, delts)
(Pec Deck) Fly Machine (Upper Pec, Lower Pec)
Cable Crossover (Upper Pec, Lower Pec, tricep, bicep, delts)
Low Cable Crossover (Lower Pec, tricep, bicep, delts)
Chest Press Machine (Upper Pec, tricep, delts)
Landmine Press
Floor Press
Prone Fly
Plate Pressout
Diamond Pushups
Decline Pushups
Medicine ball pushups
Dip


Back
----
Deadlift
Dumbell Deadlift
Trap-Bar Deadlift
Chinup
Pullup
Underhand Grip Row (Yates Row)
Incline Dumbbell Row
Alternating Dumbell Row
Inverted Row
Landmine One-Arm Row
Cable Row
Seated Cable Row
Lying Lateral Raise
Bentover Reverse Fly
Hang clean
Lower Back Extensions


Arms
----
Hammer Curl
Close-Grip Curl
Barbell Curl
Suspension Trainer Biceps Curl
Cable Curl
Preacher Curl
Reverse Curl
Wide-Grip Curl
Chinup
Nuetral-Grip Tricep Extension (Skull Crushers)
Barbell Tricep extensions
Diamond Pushup
Close-Grip Pushup
Dip
Overhead Press
Close-Grip Bench Press
Face Pull
Underhand Kickback
Tate Press
High Pull
Lateral Cable raise
Seated Dumbbell Clean
Standing Dumbbell Fly
Curl & Press

Legs
----
Front Squat
Bulgarian Split Squat
Squat
Romanian Deadlift
Dumbbell Stepup
Deadlift
Single-Leg Romanian Deadlift
Leg Press
Calf Press
Calf Raises
Walking Lunge
Pause Squat
Reverse Lunge
Dumbell Squat
Single-Leg Glute Bridge
Leg Curl Machine
Leg Extension Machine
Overhead Lunge

Abs
---
Ab Wheel Rollout
Arms-High Partial Situp
Barbell Rollout
Barbell Russian Twist
Swiss Ball Crunch
Leg Raises
Flutter Kick
Horizontal Cable Woodchop
Medicine Ball Russian Twist
Mountain Climbers
Plank
Knees to Chest
Medicine Ball Knee Tuck
Side Plank
Straight-Leg Barbell Situp
Suitcase Deadlift
Medicine Ball V-Up
Weighted Situp
"""
chest = []
back = []
arms = []
legs = []
abds = []

class Exercise:
  def __init__(self, name1, style1, heavyReps1, lightReps1):
    self.name = name1
    self.genre = style1
    self.heavyReps = heavyReps1
    self.lightReps = lightReps1

def createExercise(name1, style1, heavyReps1, lightReps1):
  global Exercise, chest, back, arms, legs, abds
  excercise = Exercise(name1, style1, heavyReps1, lightReps1)
  if style1 == 'chest':
    chest.append(excercise)
  elif style1 == 'back':
    back.append(excercise)
  elif style1 == 'arms':
    arms.append(excercise)
  elif style1 == 'legs':
    legs.append(excercise)
  else:
    abds.append(excercise)

#CHEST#
createExercise('Barbell Bench', 'chest', '3 reps at 90% max barbell bench', '12 reps at 50% max barbell bench')
createExercise('Dumbell Bench', 'chest', '8 reps at 50% max barbell bench', '20 reps at 25% max barbell bench')
createExercise('Incline Barbell Bench', 'chest', '6 reps at 75% max barbell bench', '12 reps at 50% max barbell bench')
createExercise('Incline Dumbbell Bench', 'chest', '6 reps at 50% max barbell bench', '20 reps at 25% max barbell bench')
createExercise('Dumbbell Fly', 'chest', '8 reps', '20 reps')
createExercise('Incline Dumbell Fly', 'chest', '6 reps', '12 reps')
createExercise('Fly Machine (Pec Deck)', 'chest', '8 reps', '20 reps')
createExercise('Cable Crossover', 'chest', '8 reps', '12 reps')
createExercise('Low Cable Crossover', 'chest', '8 reps', '12 reps')
createExercise('Chest Press Machine', 'chest', '6 reps', '12 reps')
createExercise('Landmine Press', 'chest', '8 reps per arm', '12 reps per arm')
createExercise('Floor Press', 'chest', '8 reps at 50% max barbell bench', '20 reps at 25% max barbell bench')
createExercise('Prone Fly', 'chest', '6 reps', '12 reps')
createExercise('Plate Pressout', 'chest', '6 reps, hold at the bottom for 3 seconds per rep', '20 reps')
createExercise('Diamond Pushups', 'chest', '10 reps, descend in 3 seconds and explode up', '20 reps')
createExercise('Decline Pushups', 'chest', '10 reps, descend in 3 seconds and explode up', '20 reps')
createExercise('Medicine ball pushups', 'chest', '10 reps, descend in 3 seconds and explode up', '20 reps')
createExercise('Dip', 'chest', '8 reps', '20 reps')

#Back#
createExercise('Deadlift', 'back', '6 reps', '12 reps')
createExercise('Dumbell Deadlift', 'back', '8 reps', '16 reps')
createExercise('Trap-Bar Deadlift', 'back', '8 reps', '20 reps')
createExercise('Chinup', 'back', 'Max reps', 'Max reps')
createExercise('Pullup', 'back', 'Max reps', 'Max reps')
createExercise('Underhand Grip Row (Yates Row)', 'back', '', '')
createExercise('Incline Dumbbell Row', 'back', '8 reps', '16 reps')
createExercise('Alternating Dumbell Row', 'back', '8 reps per arm', '12 reps per arm')
createExercise('Inverted Row', 'back', '8 reps', '16 reps')
createExercise('Landmine One-Arm Row', 'back', '6 reps per arm', '12 reps per arm')
createExercise('Cable Row', 'back', '8 reps', '16 reps')
createExercise('Seated Cable Row', 'back', '8 reps', '20 reps')
createExercise('Lying Lateral Raise', 'back', '12 reps', '20 reps')
createExercise('Bentover Reverse Fly', 'back', '12 reps', '20 reps')
createExercise('Hang clean', 'back', '6 reps', '12 reps')
createExercise('Lower Back Extensions', 'back', '8 reps', '20 reps')

#Arms#
createExercise('Hammer Curl', 'arms', '8 reps per arm', '12 reps per arm')
createExercise('Close-Grip Curl', 'arms', '6 reps per arm', '20 reps per arm')
createExercise('Barbell Curl', 'arms', '8 reps per arm', '20 reps per arm')
createExercise('Suspension Trainer Biceps Curl', 'arms', '6 reps', '20 reps')
createExercise('Cable Curl', 'arms', '6 reps', '12 reps')
createExercise('Preacher Curl', 'arms', '6 reps', '20 reps')
createExercise('Reverse Curl', 'arms', '6 reps', '20 reps')
createExercise('Wide-Grip Curl', 'arms', '8 reps', '16 reps')
createExercise('Chinup', 'arms', 'Max reps', 'Max reps')
createExercise('Nuetral-Grip Tricep Extension', 'arms', '6 reps', '20 reps')
createExercise('Barbell Tricep extensions', 'arms', '6 reps', '12 reps')
createExercise('Diamond Pushup', 'arms', '10 reps', 'max reps')
createExercise('Close-Grip Pushup', 'arms', '10 reps, descend in 3 seconds and explode up', 'max reps')
createExercise('Dip', 'arms', '6 reps', '20 reps')
createExercise('Overhead Press', 'arms', '8 reps', '16 reps')
createExercise('Close-Grip Bench Press', 'arms', '8 reps', '20 reps')
createExercise('Face Pull', 'arms', '8 reps', '20 reps')
createExercise('Underhand Kickback', 'arms', '8 reps per arm', '16 reps per arm')
createExercise('Tate Press', 'arms', '6 reps', '12 reps')
createExercise('High Pull', 'arms', '6 reps', '12 reps')
createExercise('Lateral Cable raise', 'arms', '6 reps', '16 reps')
createExercise('Seated Dumbbell Clean', 'arms', '6 reps', '16 reps')
createExercise('Standing Dumbbell Fly', 'arms', '8 reps', '24 reps')
createExercise('Curl & Press', 'arms', '6 reps per arm', '12 reps per arm')

#Legs#
createExercise('Front Squat', 'legs', '6 reps', '12 reps')
createExercise('Bulgarian Split Squat', 'legs', '6 reps per leg', '12 reps per leg')
createExercise('Squat', 'legs', '8 reps', '20 reps')
createExercise('Romanian Deadlift', 'legs', '6 reps', '12 reps')
createExercise('Dumbbell Stepup', 'legs', '6 reps per leg', '12 reps per leg')
createExercise('Deadlift', 'legs', '8 reps', '12 reps')
createExercise('Leg Press', 'legs', '8 reps', '20 reps')
createExercise('Calf Press', 'legs', '8 reps', '20 reps')
createExercise('Calf Raises', 'legs', '8 reps', '16 reps')
createExercise('Walking Lunge', 'legs', '6 reps per leg', '12 reps per leg')
createExercise('Pause Squat', 'legs', '6 reps, pausing 3 seconds at the bottom', '12 reps, pausing 3 seconds at the bottom')
createExercise('Reverse Lunge', 'legs', '6 reps per leg', '10 reps per leg')
createExercise('Dumbell Squat', 'legs', '8 reps', '16 reps')
createExercise('Glute Bridge', 'legs', '8 reps per leg', '12 reps per leg')
createExercise('Leg Curl', 'legs', '6 reps', '16 reps')
createExercise('Leg Extension', 'legs', '6 reps', '16 reps')
createExercise('Overhead Lunge', 'legs', '6 reps per leg', '10 reps per leg')

#abs#
createExercise('Ab Wheel Rollout','abs','0','10 reps')
createExercise('Arms-High Partial Situp','abs','0','20 reps')
createExercise('Barbell Rollout','abs','0','8 reps')
createExercise('Landmine Russian Twist','abs','0','10 reps per side')
createExercise('Swiss Ball Crunch','abs','0','20 reps')
createExercise('Leg Raises','abs','0','12 reps')
createExercise('Flutter Kick','abs','0','10 reps per leg')
createExercise('Horizontal Cable Woodchop','abs','0','8 reps per side')
createExercise('Medicine Ball Russian Twist','abs','0','20 reps per side')
createExercise('Mountain Climbers','abs','0','15 reps per leg')
createExercise('Plank','abs','0','30 secs')
createExercise('Knees to Chest','abs','0','20 reps')
createExercise('Medicine Ball Knee Tuck','abs','0','15 reps')
createExercise('Side Plank','abs','0','30 secs per side')
createExercise('Straight-Leg Barbell Situp','abs','0','12 reps')
createExercise('Suitcase Deadlift','abs','0','12 reps')
createExercise('Medicine Ball V-Up','abs','0','20 reps')
createExercise('Weighted Situp','abs','0','12 reps')

#Generate Workout#
#5 * 4 rounds or 5 * 3 rounds
workout = []
workoutType = 'chest'
for i in range(5):
  if workoutType == 'chest':
    temp1 = chest[randint(0, len(chest) - 1)]
    choice = randint(1,2)
    if choice == 1:
      temp2 = arms[randint(0, len(arms) - 1)]
    else:
      temp2 = back[randint(0, len(back) - 1)]
  workout.append([temp1, temp2, i + 1])
print(workout)

abWork = []
randints = []

def isInRandInts(inte):
  flag = False
  for i in randints:
    if i == inte:
      flag = True
  return flag


for i in range(7):
  randomInt = randint(0, len(abds) - 1)
  while isInRandInts(randomInt):
    randomInt = randint(0, len(abds) - 1)
  abWork.append(abds[randomInt])
  randints.append(randomInt)


def getReps(reps):
  repsRaw = reps[:8]
  try:
    if repsRaw[6] == ' ' or repsRaw[6] == ',':
      repsRaw = repsRaw[:6]
    if repsRaw[7] == ',':
      repsRaw = repsRaw[:7]
  except:
    ''
  return repsRaw


#Create Image#

from PIL import Image,ImageFont, ImageDraw
import sys

for i in range(2): 
  font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 50)
  if i == 0:
    text = "Strength & Size"
    text2 = "4 rounds per set"
  else:
    text = "Endurance"
    text2 = "3 rounds per set"
  img = Image.open('WeightsImage.png')
  draw = ImageDraw.Draw(img)
  draw.text((200, 80), text, (0, 0, 0), font=font)
  font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 30)
  draw.text((200, 145), text2, (0, 0, 0), font=font)
  print('start')
  x,y = (200, 200)
  for ic in range(5):
    y = 200 + 150 * ic
    for inn in range(3):
      weight = 0
      if inn == 0:
        text = "Set " + str(workout[ic][2])
        weight = 15
      elif inn == 1:
        text = workout[ic][0].name
        if i == 0:
          reps = getReps(workout[ic][0].heavyReps)
        else:
          reps = getReps(workout[ic][0].lightReps)
        y += 45
        text += " - " + reps
      else:
        text = workout[ic][1].name
        if i == 0:
          reps = getReps(workout[ic][1].heavyReps)
          print('yay')
        else:
          reps = getReps(workout[ic][1].lightReps)
        text += " - " + reps
        y += 45
      font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 27 + weight)
      draw.text((x, y), text, (0, 0, 0), font=font)

  img.save('ImageOut' + str(i + 1) + '.png')

img = Image.open('WeightsImage.png')
font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf',50)
draw = ImageDraw.Draw(img)
draw.text((200, 80), 'Abs', (0, 0, 0), font=font)
font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf',35)
draw.text((200, 145), '3 rounds', (0, 0, 0), font=font)
font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 30)
print('start')
x,y = (200, 250)
for ic in range(7):
  y = 250 + 60 * ic
  text = abWork[ic].name
  reps = getReps(abWork[ic].lightReps)
  text += " - " + reps
  font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 27 + weight)
  draw.text((x, y), text, (0, 0, 0), font=font)
img.save('ImageOut3.png')