print("Restarting...")
seconds = 12
for i in tqdm(range(seconds)):
    time.sleep(0.1)
exec(open('ZefroinShell.py').read())
quit()
