import subprocess
import msvcrt

fs = subprocess.Popen(['fluidsynth.exe', '-n', 'GeneralUser_GS.sf2'], stdin=subprocess.PIPE, bufsize=0)

pitch = [58, 60, 62, 64, 65, 67, 69, 71, 72]
while True:
    a = msvcrt.getch()
    print(int(a))
    a = 'noteon 0 ' + str(pitch[int(a)]) + ' 100'
    fs.stdin.write(bytes(a + '\r\n', encoding='utf8'))
