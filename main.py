from app import Recorder
import sys

def run(**kwargs):
    
    recorder =Recorder(**kwargs)
    recorder.start()


if __name__ == '__main__': 
    argv =sys.argv
    args ={}
    if len(argv) >1: args['recdir'] =argv[1]
    run(**args)