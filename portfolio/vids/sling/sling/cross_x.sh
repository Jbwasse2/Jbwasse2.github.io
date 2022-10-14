input=2t7WUuJeko7_80.mp4Old
cross=/home/justin/Downloads/cross.png
check=/home/justin/Downloads/check.png
ffmpeg -i ${input} -vf tpad=stop_mode=clone:stop_duration=2 -y out1.mp4
ffmpeg -i out1.mp4 -i ${check} -filter_complex "[1:v]format=argb,geq=r='r(X,Y)':a='0.9*alpha(X,Y)'[zork]; [0:v][zork]overlay=350:0:enable='between(t,8,10)'" -vcodec libx264 -y out.mp4
rm out1.mp4
