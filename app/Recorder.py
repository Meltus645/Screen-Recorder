import os, numpy as np, cv2, pyautogui as pg
from datetime import datetime

class Recorder:

    def __init__(self, recdir ='vid'):

        if not os.path.exists(recdir): os.mkdir(recdir)
        filename =f"{recdir}/Rec_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4"
        fourcc =cv2.VideoWriter_fourcc(*'mp4v')
        fps =30.0; resolution =pg.size()
        self.writer =cv2.VideoWriter(filename, fourcc, fps, resolution)
        self.recording =False

    def start(self):

        self.recording =True
        self.record()
    
    def record(self):
        print("[+] Recording...")
        while self.recording:
            try:
                screenshot =pg.screenshot()
                frame =cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
                self.writer.write(frame)
            except KeyboardInterrupt:
                print("[+] Closing Recorder")
                break

            except Exception as e:
                print(f"[-] Error: {e}")
                break
        self.stop()

    def stop(self):

        self.recording =False
        self.writer.release()
        cv2.destroyAllWindows()