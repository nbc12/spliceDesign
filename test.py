import pprint

colors = [
    'blue',
    'orange',
    'green',
    'brown',
    'gray',
    'rgb(200,200,200)',
    'red',
    'rgb(50,50,50)',
    'yellow',
    'violet',
    'pink',
    'aqua'
]

IDCounter = 0
strandCounter = 0


fibers = []
buffers = []
cables = []

for i in range(2):
    for i in range(2):
        for i in range(6):
            fibers.append({'ID': IDCounter, 'strandNumber': strandCounter, 'color': colors[i], 'linkID': 999})
            IDCounter += 1
            strandCounter += 1
        buffers.append(fibers)
        fibers = []
    strandCounter = 0
    cables.append(buffers)
    buffers = []

pp = pprint.PrettyPrinter(indent=4, width = 5, depth = 5, compact=True)
pp.pprint(cables)