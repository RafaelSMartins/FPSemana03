from collections import deque

palavras = input(" ")

queue = deque(palavras.split())

print("", queue)

while queue:
    palavra = queue.popleft()  
    if 'a' in palavra.lower():  
        print(palavra)
