import os

for i in range(11,20):
    command = "wget https://web.stanford.edu/class/cs168/l/l" + str(i) + ".pdf"
    os.system(command)
