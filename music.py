from threading import Thread
from wave import open as waveOpen
from subprocess import Popen, PIPE


class Music(Thread):

    def __init__(self, lokopizza):
        Thread.__init__(self)
        self.lokopizza = lokopizza
        self.scheduled = []
        self.pa = Popen(["pacat", "--latency-msec=1", "--volume=32000", "--client=LokoPizza"], stdin=PIPE, stdout=None, stderr=None)

    def run(self):
        wave = waveOpen("bgm_mouthmoney.wav", "rb")
        self.keeprunning = True
        while(self.keeprunning):
			if not self.scheduled:
				read = wave.readframes(256)
				if not read:
					wave.rewind()
					continue
			else:
				scheduled = self.scheduled[0]
				read = scheduled.readframes(256)
				if not read:
					self.scheduled.remove(scheduled)
					continue
			self.pa.stdin.write(read)
			self.pa.stdin.flush()
	
	def play(self, filename):
		wave = waveOpen(filename, "rb")
		self.scheduled.append(wave)
