# WakeUp Pc

<img src="https://github.com/bbbirkan/Wake_Up_My_Pc/blob/master/WakeUpPc.png" alt="WakeUpPc" width="500" >

![](images/WakeUpPc.png)

Requirements
* Ethernet connection.
* A peer to peer network between two or more computers.
* The computer must be in either sleep or hibernation mode for this to work.
* Windows Configuration
* Bios Configuration
* IP Address - Mac Address

Windows Configuration
1. Press keyboard Win + X - Select Device Manager
2. Expand Network adapters  - select Ethernet adapter - right-click select Properties
3. Power Management - Click All boxes
4. Advanced -Scroll down in the Property box  - select Wake on Magic Packet - ok.

IP Address - Mac Address
1. Press keyboard Win + R  -  type cmd  press Enter - type ipconfig /all press Enter
2. Save this physical address + IP address in the ‘Wake up PC’ program.

Bios setting 
Find the internet your mainboard WOL setting, Example;
1. Press F2 during boot to enter BIOS Setup.
2. Go to the Power menu.
3. Set Wake-on-LAN to Power On or enable
4. Press F10 to save and exit the BIOS Setup.

Recommendation
1. Press Windows key + X then Power Options
2. Click Choose what the power buttons - change settings
3. Set up all button sleep - Save 

Follow - YouTube channel www.youtube.com/bbbirkan
