SCALE=32
FPS=24
BAD_APPLE_URL='https://www.youtube.com/watch?v=FtutLA63Cp8'

mkdir frames 1bit-frames
rm -rf frames/* 1bit-frames/*

if test ! -f badapple.mp4; then
	echo "Video not found, downloading..."
	yt-dlp "$BAD_APPLE_URL" -q --progress --merge-output-format webm --output badapple.webm
fi

echo "Converting video to frames..."
ffmpeg -hide_banner -loglevel error -i badapple.webm -vf "fps=${FPS},scale=${SCALE}:${SCALE}" frames/%05d.png

echo "Converting frames to 1 bit colordepth..."
for i in frames/*.png; do
	convert "$i" -depth 1 1bit-frames/"$(basename "$i")"
done
