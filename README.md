# AWS_Deepracer


I trained several models for aws deepracer, unfortunately I didn't have a ton of time but I'm hoping to experiment after the UVic hackathon. The more successful model I trained did well before losing that performance. As you can see in the reward graph, because I didn't reward completing the track or the number of steps taken to do so, the model began to drop drastically in performance. I wrote up another reward function that took advantage of the steps and reward parameters, unfortunately I don't have any model credits left so I was unable to train the model with the new reward function.

The race is on the 2018 re:invent track with the physical DeepRacer car, fastest lap of 3 tries is taken and fastest time wins. 

## Tested Model Online
### Here is the video simulation of 5 time trials on the re:invent 2018 track after an hour of training

https://github.com/user-attachments/assets/915c8610-91e7-47e9-a4d6-0e5058c535be


### Hyperparameters and Reward Function
![image](https://github.com/user-attachments/assets/bb6d5c10-c877-41af-beb8-7e8dc1de2fbc)

<img src="https://github.com/user-attachments/assets/16201c07-b9de-4bc4-91d7-aef3bfaf6290" alt="image">


#### Reward function used
![image](https://github.com/user-attachments/assets/d5b5337f-a65a-4883-b6d4-75ff72411e9b)

#### Updated reward function
My take on a better reward function can be found in 'Untested_RewardFunction.py' which uses the step and progress parameters to attempt to avoid the reward function declining after lots of training.

## Testing model in person

This model performed extremely poorly on an actual racetrack and could barely get over the starting line. This was due to a large spectrum of speeds it had the choice of going, from 0.5 to 4. When the model did start moving, it quickly ran into a wall on the circuit. 
