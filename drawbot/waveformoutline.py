from scipy.io.wavfile import read

def drawLine(p0, p1):
    newPath()
    moveTo(p0)
    lineTo(p1)
    closePath()
    drawPath()

def drawPeaks(coords):
    newPath()
    p0 = coords[0]
    moveTo(p0)
    for p1 in coords[1:]:
        lineTo(p1)
    #closePath()
    drawPath()

# Tweak these.

path = '/Users/michiel/Downloads/test.wav'
seconds = 0.5
samplerate = 44100 # kHz or samples per second.

if seconds > 1:
    # Don't show all samples to reduce drawing.
    di = int(samplerate / 1000)
else:
    di = 1

#
leading = 14
maxsamples = int(seconds * samplerate)
dx = 50
w = width() - 2 * dx
h = height()
maxy = h / 2
dy = h / 4
# read audio samples
input_data = read(path)
rawaudio = input_data[1]
samples = len(rawaudio)
print('Total number of samples: %d' % samples)

if maxsamples < samples:
    audio = rawaudio[0:maxsamples]
else:
    print('Full length')
    audio= rawaudio[0:]
    maxsamples = samples

low = audio[:,0]
high = audio[:,1]
lowest = int(min(low))
highest = int(max(high))
diff = highest - lowest
yscale = maxy / diff
meany = h / 2
interval = 0
xscale = w / maxsamples * di

fill(0.9, 0.9, 0.8)
rect(0, 0, width(), height())
fill(1, 1, 1)
rect(dx, dy, w, maxy)


fill(1, 0, 0)

offset = 40
text(str(lowest), (dx - offset, dy))
text(str(highest), (dx - offset, maxy + dy))
stroke(1, 0, 0)
strokeWidth(0.5)
drawLine((dx, dy), (w+dx, dy))
drawLine((dx, dy + maxy), (w+dx, dy + maxy))

left = []
right = []

for x in range(0, maxsamples):
    if interval >= maxsamples:
        break
        
    sample = audio[interval]
    y0 = (int(sample[0]) + abs(lowest)) * yscale + dy        
    y1 = (int(sample[1]) + abs(lowest)) * yscale + dy        
    x0 = (x * xscale) + dx
    p0 = (x0, y0)
    p1 = (x0, y1)
    left.append(p0)
    right.append(p1)
    interval += di

strokeWidth(1)
fill(None)
stroke(0, 1, 0)
drawPeaks(right)
#stroke(0, 1, 0)
#drawPeaks(left)


# Show seconds.

if seconds > 1:
    ws = w / seconds
    x = 0
    fill(1, 0, 0)
    strokeWidth(0.5)
    stroke(None)
    for i in range(0, seconds+1):
        text('%ds' % i, (dx+x, dy-leading))
        x += ws
else:
    ds = int(seconds*10)
    wds = w / ds
    x = 0
    fill(1, 0, 0)
    strokeWidth(0.5)
    stroke(None)
    
    for i in range(0, ds+1):
        text('0.%ds' % i, (dx+x, dy-leading))
        x += wds