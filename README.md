First Download Termux wich is an Open source App for android devices it requires Android 7 or higher

When youre in Termux you need to get a few i will call them to keep it simple programms

pkg install ffmpeg python

pip install pillow

Do this by simply typing them into the 
Terminal

Then you have to get the Badapple.mp4 yourself i will not upload them here for copyright reasons

Then you need to extract the frames by running

ffmpeg -i Badapple.mp4 -r 30 frames/frame_%04d.png

Now if you want Audio you have to extract the mp3 from the Badapple.mp4

Thats done by typing in this command line

ffmpeg -i Badapple.mp4 -q:a 0 -map a Badapple.mp3

Then you have the mp4 split into frames 
and the mp3

Now copy the code from player.py and run.sh 

And if you run the run.sh by typing in

bash run.sh

You will get Badapple in ascii with audio 

If you want to stop it just tap Ctrl+C it stops both codes instantly and thats how you rzn Bad Apple in ASCII in Termux
