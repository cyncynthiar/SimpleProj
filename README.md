# SimpleProj
Simple projects for personal use

Issue: I needed a focus timer that would alert me even when i turned off my volume and I didnt want to dowload an app, and online websites would also be silent when my main volume was silened

USE: program is run in the terminal in python depends on these modules: time, os, sys, osascript. Asks user for duration (in seconds) they would like the timer to have, and loops. AND 0 (zero) to exit from user. When alarm goes off the program will ensure the system's sound is on

Options:
  change sound of alarm, in function "count_down" change os.system('afplay /System/Library/Sounds/Sosumi.aiff')
  https://gist.github.com/danielmcclure/56eb86c2d46d481ca65fa5f28b5d2db3

Sources:
  function "count_down" counting and display from
Stack over flow How to make a countdown program in python 
https://stackoverflow.com/questions/68427400/how-to-make-a-countdown-program-in-python
  function "count_down" turn mac audio on
Dev.to Control mac Sound Volume By Python from xkoji
https://dev.to/0xkoji/control-mac-sound-volume-by-python-h4g


Why NO UNITTEST and WHY print statemnets:
in the creation of this simple program i chose not to make a unittest because i wanted to complete something quickly and simply. Also because if this program crashed, it wouldnt cause any issues for the user, me. I could always try another timer program or use a different device. also if the program did not notify me, it wouldnt cause any issues except i would be working on my focused activity longer than expected


future adaptability: 
Can take input from command line, in variable lis_t
