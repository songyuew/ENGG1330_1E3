import time

bar = [
    " [=     ]",
    " [ =    ]",
    " [  =   ]",
    " [   =  ]",
    " [    = ]",
    " [     =]",
    " [    = ]",
    " [   =  ]",
    " [  =   ]",
    " [ =    ]",
]
i = 0

while True:
    print(bar[i % len(bar)], end="\r")
    time.sleep(.2)
    i += 1
