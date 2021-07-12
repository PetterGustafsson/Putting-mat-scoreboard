# Putting-mat-scoreboard
Makes your simple putting mat smart

Make your putting mat smart by connecting sensors to a esp32.

First sensor is a photo resistor and a laser that detects the ball the shot. The second sensor is a preassure plate with a limit switch that is placed in the hole. If more than 3 seconds pass between the ball is detected and the pressure plate, it is registered as a miss and the player get another shot. I the limit switch is closed before 3 seconds has passed, the players score is logged and it's the next players turn. Maximum number of players is 4, and maimum shots per "hole" is 7.

The game is played and monitored with a web browser on iPad or laptop

<img width="1237" alt="Screen Shot 2021-07-12 at 10 53 13" src="https://user-images.githubusercontent.com/54184145/125333787-80c71280-e2ff-11eb-8732-294cec5a4c05.png">
<img width="1349" alt="Screen Shot 2021-07-12 at 10 52 56" src="https://user-images.githubusercontent.com/54184145/125333795-83296c80-e2ff-11eb-924d-35ae821e9bdf.png">

