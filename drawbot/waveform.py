from scipy.io.wavfile import read

def drawLine(p0, p1):
    newPath()
    moveTo(p0)
    lineTo(p1)
    closePath()
    drawPath()

path = '/Users/michiel/Downloads/test.wav'
seconds = 10
samplerate = 44100 # kHz, which is samples per second.
# Don't show all samples to reduce drawing.
# TODO: calculate mean.
di = int(samplerate / 1000)
leading = 14
#print(type(di))
#print(di)
maxsamples = seconds * samplerate
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

fill(0.5, 0.6, 0.2)
rect(0, 0, width(), height())
fill(1, 1, 1)
rect(dx, dy, w, maxy)

fill(0, 0.3, 0.1)

offset = 40
text(str(lowest), (dx - offset, dy))
text(str(highest), (dx - offset, maxy + dy))
stroke(1, 0, 0)
strokeWidth(0.5)
drawLine((dx, dy), (w+dx, dy))
drawLine((dx, dy + maxy), (w+dx, dy + maxy))

for x in range(0, maxsamples):
    if interval > maxsamples:
        break
        
    sample = audio[interval]
    y0 = (int(sample[0]) + abs(lowest)) * yscale + dy

    if y0 > meany:
        y0 = meany
        
    y1 = (int(sample[1]) + abs(lowest)) * yscale + dy
    
    if y1 < meany:
        y1 = meany
        
    x0 = (x * xscale) + dx
    p0 = (x0, y0)
    p1 = (x0, y1)
    stroke(0.8, 0.8, 0)
    strokeWidth(1)
    drawLine(p0, p1)
    interval += di

ws = w / seconds
x = 0

for i in range(0, seconds+1):
    stroke(1, 0, 0)
    strokeWidth(0.5)
    drawLine((dx+x, dy), (dx+x, dy+maxy))
    stroke(None)
    text('%ds' % i, (dx+x, dy-leading))
    x += ws