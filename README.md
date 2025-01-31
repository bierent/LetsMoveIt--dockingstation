# LetsMoveIt--dockingstation
The dockingstation is a combination between a elevator and conveyor belt for transporting products up to a height. The task of the dockingstation in this project is to take cases from an AGV and transport them up to the table where an UR-5 is positioned where the UR-5 takes the case from the dockingstation. This dockingstation was custom made by Coomach in 2017 and was automatized in a project at fontys by adding a PLC, multiple sensors and an press on guide. In this project the dockingstation wasn’t further adapted and was only integrated in this project by rewriting the whole software of the PLC. The dockingstation is part of collaboration between an AGV and an UR-5. That's is why in the program in- and outputs of the UR-5 and raspberry are writen. The raspberry is connected to the PLC via I/O's and makes connection with the AGV over WiFi. The UR-5 is connnected via I/O. 

## Getting started
For this project it is assumed you have
+ Windows 7 or higher
+ Lasal class 2
+ Python

## Dockingstation 
First you need to put an ethernet cable between the PLC and your pc. Next you want to change your IP adress range to that from the PLC.
First open the network centrum
![ethernet](https://user-images.githubusercontent.com/52155322/60008621-b0514680-9674-11e9-93cd-c1542019bed6.JPG)
Click on ethernet.

![properties](https://user-images.githubusercontent.com/52155322/60008631-b1827380-9674-11e9-8ca0-ce1922f27aa7.JPG)

Click on properties and on Internet Protocol Version 4 (TCP/IPv4)

![IP-adres](https://user-images.githubusercontent.com/52155322/60008624-b0e9dd00-9674-11e9-8bcd-f725272b71de.JPG)

Change your IP-adres like in the picture above.
Now you will be able to communicate with the PLC from your pc so you can now open Lasal class 2. 

In Lasal click on the online settings

![online](https://user-images.githubusercontent.com/52155322/60008628-b1827380-9674-11e9-8102-e6faac67af99.JPG)

Change here the IP like in the picture or if you have troubles later by finding it click IP-scanner and search for the PLC. Note that the PLC needs about a minute after starting up to configure its own network and it cant be found before that.

![IP docking](https://user-images.githubusercontent.com/52155322/60008623-b0e9dd00-9674-11e9-8baa-ad68be0ee5e1.JPG)

Next click on the online button to go online.

![go online](https://user-images.githubusercontent.com/52155322/60008622-b0514680-9674-11e9-979c-e57c619f20f4.JPG)

Then open the file by clicking on file an on open project.

![open project](https://user-images.githubusercontent.com/52155322/60008629-b1827380-9674-11e9-9a39-3ecdf33607c5.png)

Select the .lcp file.

![program select](https://user-images.githubusercontent.com/52155322/60008630-b1827380-9674-11e9-88a7-cf76d819a801.JPG)

Most of the time the program opens correctly but sometimes you have to open the network seperately. This can be done by clicking on
network on the right side on the screen and click on Network0

![network choose](https://user-images.githubusercontent.com/52155322/60008625-b0e9dd00-9674-11e9-9c2d-1817f6809935.JPG)

If it works correctly you should see the next screen and you have opened the program and you are online.

![network](https://user-images.githubusercontent.com/52155322/60008626-b0e9dd00-9674-11e9-8830-56f20a1c8118.JPG)

To see the program click on the right upper corner of the main block.

![class](https://user-images.githubusercontent.com/52155322/60013725-75084500-967f-11e9-8d13-7c2d02104e07.png)

Then you should be able to see the SFC scheme of the PLC.

![SFC](https://user-images.githubusercontent.com/52155322/60013724-75084500-967f-11e9-89b5-c980edc2c8a2.JPG)

You can then run the code by pressing the next button.

![run](https://user-images.githubusercontent.com/52155322/60014013-45a60800-9680-11e9-82f5-123af188ff12.png)

## AGV integration
For integrating the AGV no change is needed. A raspberry pi is connected to the PLC which can communicate with the AGV over WiFi. The raspberry pi starts automatically when the PLC starts up. For using the raspberry pi a screen is needed to change the IP-adres in the python script on the raspberry. 
The script then starts the dockingstation when the word 'lift' is sent to it. You can test it easily by putting the ip-adress of your laptop in the python script and use the program hercules on windows to send it. Make sure you use the right port in hercules which is by default 8080 in the script. 

## UR-5 integration
For integrating the UR-5 no change is needed. The UR-5 is connected to the PLC via I/O. 

## Total system
By default the UR-5 and AGV are integrated in the program so if you don't have those delete those parts.




