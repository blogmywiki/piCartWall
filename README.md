# piCartWall
A radio / theatre cartwall to play jingles or sound FX instantly on touch screen

# What it does
Cartwalls are used in radio studios to play in jingles at the touch of a button. This is designed to do the same on a bog-standard Raspberry Pi connected to a touch screen. It does not require ANY other software or libraries to be installed, all you need is a Raspberry Pi with Raspbian installed, some WAV files in your Pi's defualt Music folder - and a touch screen for full effect. It could be used in student, hospital or community radio or for playing sound effects in a play.

# How to set it up
Place some WAV files in /home/pi/Music/ on your Raspberry Pi, up to 14. Any other files, including MP3s, will be ignored. Run picartwall.py and it will assign a button to the first 14 WAV files it finds in alphanumeric order. The layout is optimised for a 800x480 pixel display like the Pimoroni HyperPixel. If you want to use a bigger display you could rejig the code.

# How to use it
Press a button. Noise comes out. It uses the default audio output which you can select in the normal way. You could use a USB DAC for better sound quality.
There are buttons. One shows the Raspberry Pi's IP address, which could be useful if you're trying to manage it remotely by SSH or VNC.
Another button shuts the whole system down pretty immediately - you'd probably want to disable this in a broadcast environment!
The next button just closes the app so you can get to the normal PIXEL desktop.
There is a spare button that I haven't found a use for yet. Perhaps I should add some volume control buttons. I did think about GTS (pips) or 1kHz tone but these would require additional audio files.

# To do
- The clock is a cut-and-shunt job from another project and it stops when audio plays. It should be integrated / threaded somehow.
- Better indication of when audio is playing e.g. button goes red. This has defeated me thus far.
- Some indication of duration / play progress / out-time. All a bit hard.
- Meaningful wordy button labels... from file name? User-configurbale?
