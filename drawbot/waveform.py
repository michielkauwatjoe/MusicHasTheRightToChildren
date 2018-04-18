path = '/Users/michiel/Downloads/test.wav'

from scipy.io.wavfile import read

samples = 500000
w = width()
h = height()
maxy = h / 2
dy = h / 4
# read audio samples
input_data = read(path)
#print(input_data)
rawaudio = input_data[1]

l = len(rawaudio)
print('Total number of samples: %d' % l)

if samples < l:
    audio = rawaudio[0:samples+1]
else:
    print('Full length')
    audio= rawaudio[0:]
    samples = l
    


low = audio[:,0]
high = audio[:,1]
lowest = int(min(low))
highest = int(max(high))
diff = highest - lowest
yscale = maxy / diff
meany = h / 2

#print('%s %s' % (lowest,  highest))

stroke(0.8, 0.8, 0)
strokeWidth(1)
interval = 0

di = 50 # Drop samples at higher zoom level.
xscale = w / samples * di

for x in range(0, l):
    if interval > l:
        break
    sample = audio[interval]
    y0 = (int(sample[0]) + abs(lowest)) * yscale + dy

    if y0 > meany:
        y0 = meany
        
    y1 = (int(sample[1]) + abs(lowest)) * yscale + dy
    
    if y1 < meany:
        y1 = meany
        
    #print('%s, %s' % (x, y0))
    #print('%s, %s' % (x, y1))
    newPath()
    moveTo((x * xscale, y0))
    lineTo((x * xscale, y1))
    closePath()
    drawPath()
    interval += di