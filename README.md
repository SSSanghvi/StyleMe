# StyleMe 
#### By Sahil Sangvi and Jacqueline Zhang

## Introduction
Everyone has those days where they wake up and are either too tired or too distracted to choose a proper outfit - be it a casual errand day, important day at the workplace, or day around town.  
In order to simplify our morning procedures, my partner and I created StyleMe, a Python based desktop application that intelligently suggests outfits for your day,  
in 36 hours as our project for the CalHacks 5.0 hackathon. 
Currently, the project focuses on tailoring outfits to be more comfortable in the weather that the user will experience on a given day. Future expansions are discussed further down. 

## Usage Flow
#### Initial setup: 
User photographs all the pieces of clothing they would like to have the program consider.
All photographs are added to the /assets/images folder.​
#### Upon program startup: 
User inputs the city they will be at tomorrow. Weather data is fetched using the OpenWeatherMap API. 
IBM Watson’s vision recognition service uses a classifier that my partner and I custom-trained with over 1100 images in order to identify the piece of clothing in each image.
Clothes that do not fit the weather are removed from consideration.
The remaining clothes are assembled into outfits.
Outfits are displayed to the user. 

## What's Next?
In the 36 hours of allotted competition time, my partner and I came up with several ambitious ideas that we didn't have time to implement. Some thoughts on where this project could go: 
* A smartphone app, where users can take pictures of their clothes directly through the app. This app could probably automatically get the GPS location of the user every morning and push a notification with outfit choices. 
* Implementation of user accounts and a cloud-based service which could also give shopping recommendations. 
* Natural-language processing bots that pick up on fashion trends by scouring online articles, to keep the program's recommendations trendy. 
