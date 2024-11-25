# AWS_Deepracer


I trained several models for aws deepracer, relatively quickly. I based my reward function around the base version AWS provided, but rather than 3 road markers I used 5 to monitor the distance from the center line and prioritized fast speeds which worked well in the training environment but not in real life. After viewing the training data, I created a revised reward function to attempt to counteract the drop in performance after training iteration 8 that rewarded a completed lap and progress on the track. However I was unable to test this version, implemented at `Untested_RewardFunction.py` as I ran out of training model credits. 

It's also worth noting that the speed parameter interval I set was from 0.5 to 4, which performed very poorly on a physical track with a real car. Next time I would lower that to around 0.5 to 2, as the car was either going incredibly slow or fast with without the smaller speed interval.

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
