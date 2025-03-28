Dependencies: 
  - pandas
  - matplotlib
  - sqlite3
  - colorama
  - python3
  - pip

After installing dependencies and cloning this repo, all that is needed is to run the main.py script with ```python3 main.py``` . The database file will automatically be generated. 
Data fields are
  - blood pressure (SYS/DIA)
  - O2 saturation
  - heart rate
  - tempurature
  - fluid intake
  - nausea levels
  - headache levels
  - joint pain
  - emotional state / mood
  - exercise levels
  - and other qualitative data!

This script can be modified to add or remove fields if they dont apply to you or fit your needs.

The program works on Android devices via Termux, though the graphing script does not function correctly. I do not see this as a problem, as the .db file can be transfered to a proper environment and the graphing script can be run from that data.
Simply copy your .db file to the directory on your computer where you cloned this repository, making sure that there are no other .db files in the directory. You can then run main.py or graph.py with ```python3 main.py``` or ```python3 graph.py``` to see your data in a graph. 

I hope this program helps you in your health journey!
