#
# DrawBot script to visualize the contents of a WAV file.
#

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

# read audio samples
input_data = read(path)
rawaudio = input_data[1]
samples = len(rawaudio)

if seconds > 1:
    # Don't show all samples to reduce drawing.
    di = int(samplerate / 1000)
else:
    di = 1

# Calculate number of audio samples needed.

maxsamples = int(seconds * samplerate)

if maxsamples < samples:
    audio = rawaudio[0:maxsamples]
else:
    # Full length.
    audio= rawaudio[0:]
    maxsamples = samples

print('Total number of samples: %d' % samples)
print('number of samples shown: %d' % maxsamples)


# Display measures.
leading = 14
dx = 50
w = width() - 2 * dx
h = height()
maxy = h / 8 * 3
dyRight = h / 16
dyLeft = h / 2 + h / 16

# FIXME: is this correct?
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
fill(1, 1, 1, 0.5)
rect(dx, dyRight, w, maxy)
rect(dx, dyLeft, w, maxy)


fill(1, 0, 0)

# Y-axis values.
offset = 40
x0 = dx - offset
text(str(lowest), (x0, dyRight))
text(str(highest), (x0, maxy + dyRight))
text('R', (x0, dyRight + maxy / 2))
text(str(lowest), (x0, dyLeft))
text(str(highest), (x0, maxy + dyLeft))
text('L', (x0, dyLeft + maxy / 2))

stroke(1, 0, 0)
strokeWidth(0.5)
drawLine((dx, dyRight), (w+dx, dyRight))
drawLine((dx, dyRight + maxy), (w+dx, dyRight + maxy))
drawLine((dx, dyLeft), (w+dx, dyLeft))
drawLine((dx, dyLeft + maxy), (w+dx, dyLeft + maxy))

# Converts samples to drawable points.

left = []
right = []

for x in range(0, maxsamples):
    if interval >= maxsamples:
        break

    sample = audio[interval]
    yLeft = (int(sample[1]) + abs(lowest)) * yscale + dyLeft
    yRight = (int(sample[0]) + abs(lowest)) * yscale + dyRight
    x0 = (x * xscale) + dx
    pLeft = (x0, yLeft)
    pRight = (x0, yRight)
    left.append(pLeft)
    right.append(pRight)
    interval += di

# Draws points.

strokeWidth(1)
fill(None)
stroke(0, 1, 0)
drawPeaks(left)
drawPeaks(right)

# X-axis values in seconds.

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
    ddy = 5
    ds = int(seconds*10)
    wds = w / ds
    x = 0
    fill(1, 0, 0)
    strokeWidth(0.5)

    for i in range(0, ds+1):
        stroke(None)
        ddx = dx + x
        text('0.%ds' % i, (ddx, dyRight-leading))
        text('0.%ds' % i, (ddx, dyLeft-leading))
        stroke(1, 0, 0)
        drawLine((ddx, dyRight+ddy),  (ddx, dyRight-ddy))
        drawLine((ddx, dyLeft+ddy),  (ddx, dyLeft-ddy))
        x += wds
