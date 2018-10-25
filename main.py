import svgwrite
from svgwrite import cm, mm   

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


dwg = svgwrite.Drawing(filename='basic_shapes.svg', debug=True)


shapes = dwg.add(dwg.g(id='shapes', fill='black'))
back = dwg.rect((0,0), (1000, 1000))
shapes.add(back)


def drawTree(shape, position, length, amount, spread, weight, existing):
    for i in range(amount):
        if i in existing:
            shape.add(dwg.line(
                position, #start
                (position[0] + length, position[1] + (i * spread) - ((amount - 1) * spread / 2)), #end
                stroke='gray', stroke_width = 2, stroke_dasharray = 8))
        else:
            shape.add(dwg.line(
                position, #start
                (position[0] + length, position[1] + (i * spread) - ((amount - 1) * spread / 2)), #end
                stroke=colors[i], stroke_width = weight))



def drawStrands(shape, position, length, amount, spread, existing, colored):
    for i in range(amount):
        if i in existing:
            shape.add(dwg.line(
                (position[0], position[1] + (spread * i) - (spread * amount / 2) + spread / 2), #start
                (position[0] + length, position[1] + (spread * i) - (spread * amount / 2) + spread / 2), #end
                stroke = 'gray', stroke_width = 2, stroke_dasharray = 8))
        else:
            if colored:
                shape.add(dwg.line(
                    (position[0], position[1] + (spread * i) - (spread * amount / 2) + spread / 2), #start
                    (position[0] + length, position[1] + (spread * i) - (spread * amount / 2) + spread / 2), #end
                    stroke=colors[i],stroke_width=2))
            else:
                shape.add(dwg.line(
                    (position[0], position[1] + (spread * i) - (spread * amount / 2) + spread / 2), #start
                    (position[0] + length, position[1] + (spread * i) - (spread * amount / 2) + spread / 2), #end
                    stroke='white',stroke_width=2))
            
def drawSplices(shape, position, amount, spread, existing):
    for i in range(amount):
        if i not in existing:
            shape.add(dwg.circle((position[0], position[1] + i * spread - (spread * amount / 2) + spread / 2), r = 5, fill='white'))

drawTree(shapes, (200, 100), 100, 12, 10, 2, [0, 1])
drawTree(shapes, (600, 100), -100, 12, 10, 2, [0, 1])
drawStrands(shapes, (300, 100), 100, 12, 10, [0, 1], True)
drawStrands(shapes, (400, 100), 100, 12, 10, [0, 1], True)
drawSplices(shapes, (400, 100), 12, 10, [0, 1])
drawTree(shapes, (100, 150), 100, 2, 100, 5, [])

dwg.save()
