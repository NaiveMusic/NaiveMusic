理论上fluidsynth一个库就够用了，但是这样的话要实现节拍还得通过noteon之间的sleep实现，太不优雅了，所以还需要一个处理midi格式的库（暂定mido）

fluidsynth用法：
fluidsynth.exe *.sf2 *.mid
    （可以进入mid-demo将任一.mid拖到.bat上来直接播放）
    参数：
    -n  不检测device，不打开port
        目前还用不到，在之后与midi库联合使用时进行实时播放时，应该要用这一功能
    -i  不打开shell
        shell中的用法：（其实就是模拟midi的事件信号）
            noteon channel pitch velocity
                如noteon 0 60 100发出C1
            sleep milliseconds
            noteoff channel pitch
