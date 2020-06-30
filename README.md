# ArenaModyBot
Bot for arenamody.pl browser game. It lets you automate certain things like:
  * **gathering emeralds**
  * **fighting**
  
DISCLAIMER: This project is made for learning purposes like practicing Python Selenium, Page Object Pattern, clean code, writing documentation, etc. I do not support any kind of cheating
# How to use
Clone or download project. Then fill UserConfig.py with your preferred configuration. There you can also write down login and password.
Then go to run.py and run one of the methods.

NOTE: To fight, you have to first use **find_enemies()** method
# Files
![enter image description here](https://i.imgur.com/d7FCkpw.png)
# Overview of methods
   * **gather_emeralds()** - Bot will gather emeralds until stopped
   
  * **find_enemies()** - Bot will check ranking for characters that you can win and fulfill level criteria.  Then it will add them to **enemies**. Every checked character is added to **checked_enemies** to avoid future checking and save time

  * **gather_emerald_and_fight()** - Bot will gather emeralds and between every gathering it will attack enemies from **enemies** till there is less energy than specified in **UserConfig.py**
 
  * **fight()** - If there is any emerald activity - bot will turn off. Otherwise bot will fight **enemies** till 0 energy.
  
  * **recheck_checked_enemies()** - Recheck every character from checked_enemies if they meet requirements and add them to **enemies** if so.
 Should be used at the beginning of certain events, after leveling up and every few weeks.
  
  * **recheck_enemies()** - It checks characters from **enemies** and delete ones that does not meet criteria anymore. Should be use after certain events, after leveling up and every few weeks.
  # Description of fighting
  Note: To use fighting, you have to use **fight_enemies()** method first.
  
  enemies.csv file after using **find_enemies()**:![enemies.csv file after using **find_enemies**](https://i.imgur.com/vsmb7RX.png)
  
  Values are gonna get updated after every attack.
 1. Bot will choose enemies only between those where next_attack_time is lesser than time since epoch in seconds.
 2. Bot will choose enemies according to expected worth of the enemy which is calculated by: (sum_prizes/am_attacks + last_attack_prize)/2. If there were no attacks expected worth is as specified in UserConfig.py
 3. If there is am_attacks in {1,2,3}, additional value specified in UserConfig.py will be added to expected worth
 4. If enemy is attacked or couldn't be attacked for some reason next_attack time is changed according to values specified in UserConfig.py