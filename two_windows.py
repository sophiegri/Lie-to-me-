#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.1),
    on April 24, 2019, at 16:31
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'BCI_Exp_v10'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'F:\\Users\\Administrator\\Documents\\PsychopyExperiments\\annika_ma\\training.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1000, 1000], fullscr=True, screen=1,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-0.3,-0.3,-0.3], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
    
win2 = visual.Window(
    size=[1000, 1000], fullscr=True, screen=2,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor2', color=[-0.3,-0.3,-0.3], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
    
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "iViewX_Connect"
iViewX_ConnectClock = core.Clock()
from iViewXAPI import  *            #iViewX library
# ---------------------------------------------
#---- connect to iViewX
# ---------------------------------------------
res = iViewXAPI.iV_Connect(c_char_p('141.54.159.23'), c_int(4444), c_char_p('141.54.159.21'), c_int(5555))

res = iViewXAPI.iV_GetSystemInfo(byref(systemData))
print "iV_GetSystemInfo: " + str(res)
print "Samplerate: " + str(systemData.samplerate)
print "iViewX Verion: " + str(systemData.iV_MajorVersion) + "." + str(systemData.iV_MinorVersion) + "." + str(systemData.iV_Buildnumber)
print "iViewX API Verion: " + str(systemData.API_MajorVersion) + "." + str(systemData.API_MinorVersion) + "." + str(systemData.API_Buildnumber)


'''
# ---------------------------------------------
#---- configure and start calibration
# ---------------------------------------------
#calibrationData = CCalibration(13, 1, 1, 0, 0, 180, 150, 2, 20, b"")

calibrationData = CCalibration(9, 1, 1, 0, 2, 250, 180, 2, 20, b"")
#(method, visualization, display, speed, auto, fg, bg, shape, size, filename)

res = iViewXAPI.iV_SetupCalibration(byref(calibrationData))
print "iV_SetupCalibration " + str(res)
res = iViewXAPI.iV_Calibrate()
print "iV_Calibrate " + str(res)
res = iViewXAPI.iV_Validate()
print "iV_Validate " + str(res)

print "iV_GetAccuracy " + str(res)
print "deviationXLeft " + str(accuracyData.deviationLX) + " deviationYLeft " + str(accuracyData.deviationLY)
print "deviationXRight " + str(accuracyData.deviationRX) + " deviationYRight " + str(accuracyData.deviationRY)
'''

# Initialize components for Routine "bl_instructions"
bl_instructionsClock = core.Clock()
baseline_instructions = visual.TextStim(win=win, name='baseline_instructions',
    text='After the baseline was taken you will have 5 Minutes \nto explore different strategies to increase or decrease your pupil size. \n\n(to start press <space>)',
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=0.0);
    
    # Initialize components for Routine "bl_instructions2"
bl2_instructionsClock = core.Clock()
baseline_instructions2 = visual.TextStim(win=win2, name='baseline_instructions2',
    text='hello',
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=0.0);
    
    
import random
nend=0
clbsloop=0
current_mean = 0




# Initialize components for Routine "baseline"
baselineClock = core.Clock()
zeitpuffer1 = visual.TextStim(win=win, name='zeitpuffer1',
    text=None,
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=0.0);
#baseline_liste=[]
#import numpy

#-----------------------------------
# Begin Experiment
#-----------------------------------
import numpy

bsize_liste = [0]*1900 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
bsize = 0


# Initialize components for Routine "trial"
trialClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text=None,
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=0.0);
from numpy import (log)
maxsize=0
minsize=3000
psizeliste = [0]*19000 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
psize = 0

feedbacktext = ""


# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='default text',
    font='Arial',
    pos=(-10, 0), height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()

text = visual.TextStim(win=win, name='text',
    text="Start activating when the visual feedback appears!\n\n(press 'space')",
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "wait"
waitClock = core.Clock()


# Initialize components for Routine "baseline"
baselineClock = core.Clock()
zeitpuffer1 = visual.TextStim(win=win, name='zeitpuffer1',
    text=None,
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=0.0);
#baseline_liste=[]
#import numpy

#-----------------------------------
# Begin Experiment
#-----------------------------------
import numpy

bsize_liste = [0]*1900 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
bsize = 0


# Initialize components for Routine "training_feedback"
training_feedbackClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text=None,
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=0.0);
from numpy import (log)
maxsize=0
minsize=3000
psizeliste = [0]*19000 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
psize = 0

feedbacktext = ""


# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='default text',
    font='Arial',
    pos=(-10, 0), height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "instructions_noFeedback"
instructions_noFeedbackClock = core.Clock()

text_14 = visual.TextStim(win=win, name='text_14',
    text="Start activating when the color of the cross changes to light gray\n\n(press 'space')",
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "wait"
waitClock = core.Clock()


# Initialize components for Routine "baseline"
baselineClock = core.Clock()
zeitpuffer1 = visual.TextStim(win=win, name='zeitpuffer1',
    text=None,
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=0.0);
#baseline_liste=[]
#import numpy

#-----------------------------------
# Begin Experiment
#-----------------------------------
import numpy

bsize_liste = [0]*1900 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
bsize = 0


# Initialize components for Routine "training_noFeedback"
training_noFeedbackClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text=None,
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=0.0);
from numpy import (log)
maxsize=0
minsize=3000
psizeliste = [0]*19000 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
psize = 0


# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='default text',
    font='Arial',
    pos=(-10, 0), height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "end"
endClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text="The training has finished!\n\n(press 'space')",
    font='Arial',
    pos=[0, 0], height=40, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "iViewX_Connect"-------
t = 0
iViewX_ConnectClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
iViewX_ConnectComponents = []
for thisComponent in iViewX_ConnectComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "iViewX_Connect"-------
while continueRoutine:
    # get current time
    t = iViewX_ConnectClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in iViewX_ConnectComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "iViewX_Connect"-------
for thisComponent in iViewX_ConnectComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "iViewX_Connect" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

####### END HERE

######### START HERE

# ------Prepare to start Routine "bl_instructions"-------
t = 0
bl_instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
bl_instructionsComponents = [baseline_instructions, key_resp_4]
for thisComponent in bl_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "bl_instructions"-------
while continueRoutine:
    # get current time
    t = bl_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *baseline_instructions* updates
    if t >= 0.0 and baseline_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        baseline_instructions.tStart = t
        baseline_instructions.frameNStart = frameN  # exact frame index
        baseline_instructions.setAutoDraw(True)
    
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in bl_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "bl_instructions"-------
for thisComponent in bl_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys=None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "bl_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

####### END HERE





# ------Prepare to start Routine "baseline"-------
t = 0
baselineClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
bsize_liste = [0]*1900 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz


#-----------------------------------
# Begin Routine
#-----------------------------------

#---------------------
# starting values
state_no = 0

lmarker = -1 

delay_size = 2

#---------------------
# filter preferences
step_limit = 0.19    # 30Hz: 0.19 | 60Hz: 0.09
lower_th = 1
# keep track of which components have finished
baselineComponents = [zeitpuffer1]
for thisComponent in baselineComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "baseline"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = baselineClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *zeitpuffer1* updates
    if t >= 0.0 and zeitpuffer1.status == NOT_STARTED:
        # keep track of start time/frame for later
        zeitpuffer1.tStart = t
        zeitpuffer1.frameNStart = frameN  # exact frame index
        zeitpuffer1.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if zeitpuffer1.status == STARTED and t >= frameRemains:
        zeitpuffer1.setAutoDraw(False)
    res = iViewXAPI.iV_GetSample(byref(sampleData))
    bsize =(sampleData.leftEye.diam) # /32 für highspeed eyetracker, ohne /32 für RED
    
    
    #logging.console.write(str(bsize))
    
    #--------------------
    # state 0: starting
    #--------------------
    if state_no == 0:
     if lmarker < 1:
      lmarker = lmarker + 1
      bsize_liste[lmarker] = bsize
      state_next = 0
     
     else:  
      if bsize > lower_th and bsize_liste[lmarker] > lower_th and bsize_liste[lmarker-1] > lower_th and (abs(bsize-bsize_liste[lmarker]) <= step_limit) and (abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit):
       lmarker = lmarker + 1
       bsize_liste[lmarker] = bsize
       state_next = 1
      else:
       bsize_liste[lmarker-1] = bsize_liste[lmarker]
       bsize_liste[lmarker] = bsize
    
       state_next = 0
    
    
    #----------------------
    # state 1: observation
    #----------------------
    
    if state_no == 1:
     
     # Filter Activation
     #- - - - - - - - - - -
     if bsize <= lower_th:
      on = 1
      jump_marker = lmarker + 1 # marks values to be replaced 
      
            # Identification of last valid_value before the blink
            #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      while on == 1:
       if bsize_liste[lmarker] >= lower_th and bsize_liste[lmarker-1] >= lower_th and bsize_liste[lmarker-2] >= lower_th and abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit and abs(bsize_liste[lmarker-1]-bsize_liste[lmarker-2]) <= step_limit:
        valid_value = bsize_liste[lmarker]
        lmarker = lmarker + 1
        for i in range(lmarker, jump_marker, 1):
         bsize_liste[i] = valid_value
    
        bsize_liste[jump_marker] = valid_value
    
        lmarker = jump_marker
        puffer_size = jump_marker + delay_size
    
        on = 0
        state_next = 2
    
       else:
        lmarker = lmarker-1
        
     else:
      lmarker = lmarker + 1
      bsize_liste[lmarker] = bsize
      
      state_next = 1
    
    
    #-------------------------------------------------------------
    # state 2: identification of next valid_value after the blink
    #-------------------------------------------------------------
    
    if state_no == 2:
     # collecting values following the blink
     #- - - - - - - - - - - - - - - - - - - - - -
     if lmarker < puffer_size:
      lmarker = lmarker + 1
      bsize_liste[lmarker] = bsize
    
      state_next = 2
    
     else:
    # identification of next valid_value after the blink
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - 
      if bsize > lower_th and abs(bsize-bsize_liste[lmarker]) <= step_limit and abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit:               
       lmarker = lmarker + 1
       bsize_liste[lmarker] = bsize
       
       state_next = 1
    
      else:
       lmarker = lmarker + 1
       bsize_liste[lmarker] = bsize
       bsize_liste[lmarker-2] = valid_value
       
       state_next = 2
    
    state_no = state_next
    
    #baseline_liste.append(sampleData.leftEye.diam/32)
    line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
    line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
    line1.draw()
    line2.draw()
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "baseline"-------
for thisComponent in baselineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
#-----------------------------------
# End Routine
#-----------------------------------  

#logging.console.write("test\n")
# computing baseline mean
bsize_liste = filter(None, bsize_liste)
baselinemean = round((sum(bsize_liste)/(len(bsize_liste))),2)
baselinemean = baselinemean


# computing baseline sd
baselinesd = abs(round(numpy.std(bsize_liste),8))

# computing percent-change: sd / mean
prozent_change1= round((baselinesd/baselinemean),2)

# computing aussenringradius - maximum deviation 
aussenringradius = (baselinemean+(baselinemean*prozent_change1))*35

# computing innenringradius - minimum deviation
innenringradius = (baselinemean-(baselinemean*prozent_change1))*35

#--------------------------------------------------------------------------
# savings:

thisExp.addData('Baseline_Liste', bsize_liste)
thisExp.addData('Baseline_Mittelwert', baselinemean)
thisExp.addData('Baseline_Standardabweichung', baselinesd)


# ------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(300.000000)
# update component parameters for each repeat

psizeliste = [0]*190000 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
psize = 0


#---------------------
# starting values
state_no = 0

lmarker = -1 

delay_size = 2

#---------------------
# filter preferences
step_limit = 0.19    # 30Hz: 0.19 | 60Hz: 0.09
lower_th = 1

#---------------------
# plot settings
minsize = 3000
maxsize = 0
plot_marker = 0
mean_length = 3
plot_buffer = 5

abc = 0

#draw
line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
circle2 = visual.Circle(win, edges=96, radius=aussenringradius,lineWidth=1, lineColor=(0 , 0, 0), fillColor=(0 , 0, 0), interpolate=True)
circle3 = visual.Circle(win, edges=96, radius=innenringradius,lineWidth=1, lineColor=(-0.3 , -0.3, -0.3), fillColor=(-0.3 , -0.3, -0.3), interpolate=True)
circle4 = visual.Circle(win, edges=96, radius=baselinemean*35,lineWidth=2, lineColor=(-1 , -1, -1), interpolate=True)
circle5 = visual.Circle(win, edges=96, radius=1000,lineWidth=1, lineColor=(-1 , -1, -1), interpolate=True)
circle6 = visual.Circle(win, edges=96, radius=1000,lineWidth=1, lineColor=(-1 , -1, -1), interpolate=True)

# win 2
w2_line1 = visual.Line(win2, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
w2_line2 = visual.Line(win2, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
w2_circle2 = visual.Circle(win2, edges=96, radius=aussenringradius,lineWidth=1, lineColor=(0 , 0, 0), fillColor=(0 , 0, 0), interpolate=True)
w2_circle3 = visual.Circle(win2, edges=96, radius=innenringradius,lineWidth=1, lineColor=(-0.3 , -0.3, -0.3), fillColor=(-0.3 , -0.3, -0.3), interpolate=True)
w2_circle4 = visual.Circle(win2, edges=96, radius=baselinemean*35,lineWidth=2, lineColor=(-1 , -1, -1), interpolate=True)
w2_circle5 = visual.Circle(win2, edges=96, radius=1000,lineWidth=1, lineColor=(-1 , -1, -1), interpolate=True)
w2_circle6 = visual.Circle(win2, edges=96, radius=1000,lineWidth=1, lineColor=(-1 , -1, -1), interpolate=True)

w2_circle1 = visual.Circle(win2, edges=96, radius=0,lineWidth=4, lineColor=(0,-1,-1), interpolate=True)

w2_circle2.setAutoDraw(True)
w2_circle3.setAutoDraw(True)
w2_circle1.setAutoDraw(True)
w2_line1.setAutoDraw(True)
w2_line2.setAutoDraw(True)
    
key_resp_9 = event.BuilderKeyResponse()
# keep track of which components have finished
trialComponents = [text_6, key_resp_9]
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    frameRemains = 0.0 + 300- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        text_6.setAutoDraw(False)
    
    #-----------------------------------
    # Each Frame
    #-----------------------------------
    # eye-tracker data
    res = iViewXAPI.iV_GetSample(byref(sampleData))
    psize =(sampleData.leftEye.diam) # /32 für highspeed eyetracker, ohne /32 für RED
    
    
    #--------------------
    # state 0: starting
    #--------------------
    if state_no == 0:
     if lmarker < 1:
      lmarker = lmarker + 1
      psizeliste[lmarker] = psize
      state_next = 0
     
     else:
      if psize > lower_th and psizeliste[lmarker] > lower_th and psizeliste[lmarker-1] > lower_th and (abs(psize-psizeliste[lmarker]) <= step_limit) and (abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit):
       lmarker = lmarker + 1
       psizeliste[lmarker] = psize
       state_next = 1
      else:
       psizeliste[lmarker-1] = psizeliste[lmarker]
       psizeliste[lmarker] = psize
       state_next = 0
    
    
    #----------------------
    # state 1: observation
    #----------------------
    
    if state_no == 1:
     plot_marker = 1 
     # Filter Activation
     #- - - - - - - - - - -
     if psize <= lower_th:
      on = 1
      jump_marker = lmarker + 1 # marks values to be replaced 
      # Identification of last valid_value before the blink
      #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      while on == 1:
       if psizeliste[lmarker] >= lower_th and psizeliste[lmarker-1] >= lower_th and psizeliste[lmarker-2] >= lower_th and abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit and abs(psizeliste[lmarker-1]-psizeliste[lmarker-2]) <= step_limit:
        valid_value = psizeliste[lmarker]
        lmarker = lmarker + 1
        # replacing values
        for i in range(lmarker, jump_marker, 1):
         psizeliste[i] = valid_value
        psizeliste[jump_marker] = valid_value
        lmarker = jump_marker
        puffer_size = jump_marker + delay_size
        on = 0
        state_next = 2
       else:
        lmarker = lmarker-1
     else:
      lmarker = lmarker + 1
      psizeliste[lmarker] = psize
      state_next = 1
    #-------------------------------------------------------------
    # state 2: identification of next valid_value after the blink
    #-------------------------------------------------------------
    if state_no == 2:
     plot_marker = 1
     # collecting values following the blink
     #- - - - - - - - - - - - - - - - - - - - - -
     if lmarker < puffer_size:
      lmarker = lmarker + 1
      psizeliste[lmarker] = psize
      state_next = 2
    
     else:
     # identification of next valid_value after the blink
     #- - - - - - - - - - - - - - - - - - - - - - - - - - - - 
      if psize > lower_th and abs(psize-psizeliste[lmarker]) <= step_limit and abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit:               
       lmarker = lmarker + 1
       psizeliste[lmarker] = psize
       state_next = 1
      else:
       lmarker = lmarker + 1
       psizeliste[lmarker] = psize
       psizeliste[lmarker-2] = valid_value
       state_next = 2
    
    #- - - - - - - - - - - - - - - - - - - - - - - - - - -
    # smooth & plot data:
    #- - - - - - - - - - - - - - - - - - - - - - - - - - -
    if state_no == 0 or state_no == 1 or state_no == 2:
     if plot_marker == 1:
            # BASELINE RINGE (schwarz): MW +/-SD
            #- - - - - - - - - - - - - - - - - - - -
            #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -     
            # FEEDBACK RINGE (rot | grau): Pupillengröße u. Extrema
            #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      if lmarker >= mean_length + plot_buffer:
       current_mean = 0
       for p in range(1, mean_length+1, 1):
        current_mean = psizeliste[lmarker-p-plot_buffer] + current_mean
       current_mean = (current_mean/mean_length)*35
    
      if current_mean > maxsize and current_mean > aussenringradius:
       maxsize = current_mean
       circle5 = visual.Circle(win, edges=96, radius=maxsize,lineWidth=1, lineColor=(0.2 , 0.2, 0.2), interpolate=True)
      elif current_mean < minsize and current_mean < innenringradius and current_mean != 0:
       minsize = current_mean
       circle6 = visual.Circle(win, edges=96, radius=minsize,lineWidth=1, lineColor=(0.2 , 0.2, 0.2), interpolate=True)
    
    #red circle
    circle1 = visual.Circle(win, edges=96, radius=current_mean,lineWidth=4, lineColor=(0,-1,-1), interpolate=True)
    # w2_circle1 = visual.Circle(win2, edges=96, radius=current_mean,lineWidth=4, lineColor=(0,-1,-1), interpolate=True)
    
    w2_circle1.radius = current_mean
    
    abc = abc+0.03
    
    circle2.draw()
    circle3.draw()
    circle1.draw()
    line1.draw()
    line2.draw()
    
    # window 2
    # w2_circle2.draw()
    # w2_circle3.draw()
    # w2_circle1.draw()
    # w2_line1.draw()
    # w2_line2.draw()
    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
    state_no = state_next
    
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    frameRemains = 0.0 + 300- win.monitorFramePeriod * 0.75  # most of one frame period left
    if key_resp_9.status == STARTED and t >= frameRemains:
        key_resp_9.status = STOPPED
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_9.keys = theseKeys[-1]  # just the last key pressed
            key_resp_9.rt = key_resp_9.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        win2.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
psizeliste = filter(None, psizeliste)

psizemean = round((sum(psizeliste)/(len(psizeliste))),2)

thisExp.addData('Pupil_Liste', psizeliste)
thisExp.addData('Pupil_Mean', psizemean)
thisExp.addData('feedback', 'visual')


feedbacktext = "Your baseline was: " + str(baselinemean)+ "\n" + "Your average pupildilation was: " + str(psizemean)+ "\n" 

# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys=None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()

# ------Prepare to start Routine "feedback"-------
t = 0
feedbackClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()
text_12.setText(feedbacktext)
# keep track of which components have finished
feedbackComponents = [key_resp_6, text_12]
for thisComponent in feedbackComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "feedback"-------
while continueRoutine:
    # get current time
    t = feedbackClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_12* updates
    if t >= 0.0 and text_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_12.tStart = t
        text_12.frameNStart = frameN  # exact frame index
        text_12.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback"-------
for thisComponent in feedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys=None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "feedback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
instructionsComponents = [text, key_resp_2]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
feedbackLoop = data.TrialHandler(nReps=10, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='feedbackLoop')
thisExp.addLoop(feedbackLoop)  # add the loop to the experiment
thisFeedbackLoop = feedbackLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFeedbackLoop.rgb)
if thisFeedbackLoop != None:
    for paramName in thisFeedbackLoop:
        exec('{} = thisFeedbackLoop[paramName]'.format(paramName))

for thisFeedbackLoop in feedbackLoop:
    currentLoop = feedbackLoop
    # abbreviate parameter names if possible (e.g. rgb = thisFeedbackLoop.rgb)
    if thisFeedbackLoop != None:
        for paramName in thisFeedbackLoop:
            exec('{} = thisFeedbackLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "wait"-------
    t = 0
    waitClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    
    key_resp_10 = event.BuilderKeyResponse()
    # keep track of which components have finished
    waitComponents = [key_resp_10]
    for thisComponent in waitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "wait"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = waitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #baseline_liste.append(sampleData.leftEye.diam/32)
        line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
        line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
        line1.draw()
        line2.draw()
        
        
        # *key_resp_10* updates
        if t >= 0.0 and key_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_10.tStart = t
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_10.status == STARTED and t >= frameRemains:
            key_resp_10.status = STOPPED
        if key_resp_10.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_10.keys = theseKeys[-1]  # just the last key pressed
                key_resp_10.rt = key_resp_10.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wait"-------
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys=None
    feedbackLoop.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        feedbackLoop.addData('key_resp_10.rt', key_resp_10.rt)
    
    # ------Prepare to start Routine "baseline"-------
    t = 0
    baselineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    bsize_liste = [0]*1900 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
    
    
    #-----------------------------------
    # Begin Routine
    #-----------------------------------
    
    #---------------------
    # starting values
    state_no = 0
    
    lmarker = -1 
    
    delay_size = 2
    
    #---------------------
    # filter preferences
    step_limit = 0.19    # 30Hz: 0.19 | 60Hz: 0.09
    lower_th = 1
    # keep track of which components have finished
    baselineComponents = [zeitpuffer1]
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "baseline"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = baselineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *zeitpuffer1* updates
        if t >= 0.0 and zeitpuffer1.status == NOT_STARTED:
            # keep track of start time/frame for later
            zeitpuffer1.tStart = t
            zeitpuffer1.frameNStart = frameN  # exact frame index
            zeitpuffer1.setAutoDraw(True)
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if zeitpuffer1.status == STARTED and t >= frameRemains:
            zeitpuffer1.setAutoDraw(False)
        res = iViewXAPI.iV_GetSample(byref(sampleData))
        bsize =(sampleData.leftEye.diam) # /32 für highspeed eyetracker, ohne /32 für RED
        
        
        #logging.console.write(str(bsize))
        
        #--------------------
        # state 0: starting
        #--------------------
        if state_no == 0:
         if lmarker < 1:
          lmarker = lmarker + 1
          bsize_liste[lmarker] = bsize
          state_next = 0
         
         else:  
          if bsize > lower_th and bsize_liste[lmarker] > lower_th and bsize_liste[lmarker-1] > lower_th and (abs(bsize-bsize_liste[lmarker]) <= step_limit) and (abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit):
           lmarker = lmarker + 1
           bsize_liste[lmarker] = bsize
           state_next = 1
          else:
           bsize_liste[lmarker-1] = bsize_liste[lmarker]
           bsize_liste[lmarker] = bsize
        
           state_next = 0
        
        
        #----------------------
        # state 1: observation
        #----------------------
        
        if state_no == 1:
         
         # Filter Activation
         #- - - - - - - - - - -
         if bsize <= lower_th:
          on = 1
          jump_marker = lmarker + 1 # marks values to be replaced 
          
                # Identification of last valid_value before the blink
                #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
          while on == 1:
           if bsize_liste[lmarker] >= lower_th and bsize_liste[lmarker-1] >= lower_th and bsize_liste[lmarker-2] >= lower_th and abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit and abs(bsize_liste[lmarker-1]-bsize_liste[lmarker-2]) <= step_limit:
            valid_value = bsize_liste[lmarker]
            lmarker = lmarker + 1
            for i in range(lmarker, jump_marker, 1):
             bsize_liste[i] = valid_value
        
            bsize_liste[jump_marker] = valid_value
        
            lmarker = jump_marker
            puffer_size = jump_marker + delay_size
        
            on = 0
            state_next = 2
        
           else:
            lmarker = lmarker-1
            
         else:
          lmarker = lmarker + 1
          bsize_liste[lmarker] = bsize
          
          state_next = 1
        
        
        #-------------------------------------------------------------
        # state 2: identification of next valid_value after the blink
        #-------------------------------------------------------------
        
        if state_no == 2:
         # collecting values following the blink
         #- - - - - - - - - - - - - - - - - - - - - -
         if lmarker < puffer_size:
          lmarker = lmarker + 1
          bsize_liste[lmarker] = bsize
        
          state_next = 2
        
         else:
        # identification of next valid_value after the blink
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - 
          if bsize > lower_th and abs(bsize-bsize_liste[lmarker]) <= step_limit and abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit:               
           lmarker = lmarker + 1
           bsize_liste[lmarker] = bsize
           
           state_next = 1
        
          else:
           lmarker = lmarker + 1
           bsize_liste[lmarker] = bsize
           bsize_liste[lmarker-2] = valid_value
           
           state_next = 2
        
        state_no = state_next
        
        #baseline_liste.append(sampleData.leftEye.diam/32)
        line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
        line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
        line1.draw()
        line2.draw()
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "baseline"-------
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #-----------------------------------
    # End Routine
    #-----------------------------------  
    
    #logging.console.write("test\n")
    # computing baseline mean
    bsize_liste = filter(None, bsize_liste)
    baselinemean = round((sum(bsize_liste)/(len(bsize_liste))),2)
    baselinemean = baselinemean
    
    
    # computing baseline sd
    baselinesd = abs(round(numpy.std(bsize_liste),8))
    
    # computing percent-change: sd / mean
    prozent_change1= round((baselinesd/baselinemean),2)
    
    # computing aussenringradius - maximum deviation 
    aussenringradius = (baselinemean+(baselinemean*prozent_change1))*35
    
    # computing innenringradius - minimum deviation
    innenringradius = (baselinemean-(baselinemean*prozent_change1))*35
    
    #--------------------------------------------------------------------------
    # savings:
    
    thisExp.addData('Baseline_Liste', bsize_liste)
    thisExp.addData('Baseline_Mittelwert', baselinemean)
    thisExp.addData('Baseline_Standardabweichung', baselinesd)
    
    
    # ------Prepare to start Routine "training_feedback"-------
    t = 0
    training_feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    
    psizeliste = [0]*190000 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
    psize = 0
    
    
    #---------------------
    # starting values
    state_no = 0
    
    lmarker = -1 
    
    delay_size = 2
    
    #---------------------
    # filter preferences
    step_limit = 0.19    # 30Hz: 0.19 | 60Hz: 0.09
    lower_th = 1
    
    #---------------------
    # plot settings
    minsize = 3000
    maxsize = 0
    plot_marker = 0
    mean_length = 3
    plot_buffer = 5
    
    abc = 0
    
    #draw
    line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
    line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
    circle2 = visual.Circle(win, edges=96, radius=aussenringradius,lineWidth=1, lineColor=(0 , 0, 0), fillColor=(0 , 0, 0), interpolate=True)
    circle3 = visual.Circle(win, edges=96, radius=innenringradius,lineWidth=1, lineColor=(-0.3 , -0.3, -0.3), fillColor=(-0.3 , -0.3, -0.3), interpolate=True)
    circle4 = visual.Circle(win, edges=96, radius=baselinemean*35,lineWidth=2, lineColor=(-1 , -1, -1), interpolate=True)
    circle5 = visual.Circle(win, edges=96, radius=1000,lineWidth=1, lineColor=(-1 , -1, -1), interpolate=True)
    circle6 = visual.Circle(win, edges=96, radius=1000,lineWidth=1, lineColor=(-1 , -1, -1), interpolate=True)
    
    
    w2_line1 = visual.Line(win2, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
    w2_line2 = visual.Line(win2, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
    w2_circle2 = visual.Circle(win2, edges=96, radius=aussenringradius,lineWidth=1, lineColor=(0 , 0, 0), fillColor=(0 , 0, 0), interpolate=True)
    w2_circle3 = visual.Circle(win2, edges=96, radius=innenringradius,lineWidth=1, lineColor=(-0.3 , -0.3, -0.3), fillColor=(-0.3 , -0.3, -0.3), interpolate=True)
    w2_circle4 = visual.Circle(win2, edges=96, radius=baselinemean*35,lineWidth=2, lineColor=(-1 , -1, -1), interpolate=True)
    w2_circle5 = visual.Circle(win2, edges=96, radius=1000,lineWidth=1, lineColor=(-1 , -1, -1), interpolate=True)
    w2_circle6 = visual.Circle(win2, edges=96, radius=1000,lineWidth=1, lineColor=(-1 , -1, -1), interpolate=True)
    
    
    key_resp_11 = event.BuilderKeyResponse()
    # keep track of which components have finished
    training_feedbackComponents = [text_13, key_resp_11]
    for thisComponent in training_feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "training_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = training_feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_13* updates
        if t >= 0.0 and text_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_13.tStart = t
            text_13.frameNStart = frameN  # exact frame index
            text_13.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_13.status == STARTED and t >= frameRemains:
            text_13.setAutoDraw(False)
        
        #-----------------------------------
        # Each Frame
        #-----------------------------------
        # eye-tracker data
        res = iViewXAPI.iV_GetSample(byref(sampleData))
        psize =(sampleData.leftEye.diam) # /32 für highspeed eyetracker, ohne /32 für RED
        
        
        #--------------------
        # state 0: starting
        #--------------------
        if state_no == 0:
         if lmarker < 1:
          lmarker = lmarker + 1
          psizeliste[lmarker] = psize
          state_next = 0
         
         else:
          if psize > lower_th and psizeliste[lmarker] > lower_th and psizeliste[lmarker-1] > lower_th and (abs(psize-psizeliste[lmarker]) <= step_limit) and (abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit):
           lmarker = lmarker + 1
           psizeliste[lmarker] = psize
           state_next = 1
          else:
           psizeliste[lmarker-1] = psizeliste[lmarker]
           psizeliste[lmarker] = psize
           state_next = 0
        
        
        #----------------------
        # state 1: observation
        #----------------------
        
        if state_no == 1:
         plot_marker = 1 
         # Filter Activation
         #- - - - - - - - - - -
         if psize <= lower_th:
          on = 1
          jump_marker = lmarker + 1 # marks values to be replaced 
          # Identification of last valid_value before the blink
          #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
          while on == 1:
           if psizeliste[lmarker] >= lower_th and psizeliste[lmarker-1] >= lower_th and psizeliste[lmarker-2] >= lower_th and abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit and abs(psizeliste[lmarker-1]-psizeliste[lmarker-2]) <= step_limit:
            valid_value = psizeliste[lmarker]
            lmarker = lmarker + 1
            # replacing values
            for i in range(lmarker, jump_marker, 1):
             psizeliste[i] = valid_value
            psizeliste[jump_marker] = valid_value
            lmarker = jump_marker
            puffer_size = jump_marker + delay_size
            on = 0
            state_next = 2
           else:
            lmarker = lmarker-1
         else:
          lmarker = lmarker + 1
          psizeliste[lmarker] = psize
          state_next = 1
        #-------------------------------------------------------------
        # state 2: identification of next valid_value after the blink
        #-------------------------------------------------------------
        if state_no == 2:
         plot_marker = 1
         # collecting values following the blink
         #- - - - - - - - - - - - - - - - - - - - - -
         if lmarker < puffer_size:
          lmarker = lmarker + 1
          psizeliste[lmarker] = psize
          state_next = 2
        
         else:
         # identification of next valid_value after the blink
         #- - - - - - - - - - - - - - - - - - - - - - - - - - - - 
          if psize > lower_th and abs(psize-psizeliste[lmarker]) <= step_limit and abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit:               
           lmarker = lmarker + 1
           psizeliste[lmarker] = psize
           state_next = 1
          else:
           lmarker = lmarker + 1
           psizeliste[lmarker] = psize
           psizeliste[lmarker-2] = valid_value
           state_next = 2
        
        #- - - - - - - - - - - - - - - - - - - - - - - - - - -
        # smooth & plot data:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - -
        if state_no == 0 or state_no == 1 or state_no == 2:
         if plot_marker == 1:
                # BASELINE RINGE (schwarz): MW +/-SD
                #- - - - - - - - - - - - - - - - - - - -
                #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -     
                # FEEDBACK RINGE (rot | grau): Pupillengröße u. Extrema
                #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
          if lmarker >= mean_length + plot_buffer:
           current_mean = 0
           for p in range(1, mean_length+1, 1):
            current_mean = psizeliste[lmarker-p-plot_buffer] + current_mean
           current_mean = (current_mean/mean_length)*35
        
          if current_mean > maxsize and current_mean > aussenringradius:
           maxsize = current_mean
           circle5 = visual.Circle(win, edges=96, radius=maxsize,lineWidth=1, lineColor=(0.2 , 0.2, 0.2), interpolate=True)
          elif current_mean < minsize and current_mean < innenringradius and current_mean != 0:
           minsize = current_mean
           circle6 = visual.Circle(win, edges=96, radius=minsize,lineWidth=1, lineColor=(0.2 , 0.2, 0.2), interpolate=True)
        
        #red circle
        circle1 = visual.Circle(win, edges=96, radius=current_mean,lineWidth=4, lineColor=(0,-1,-1), interpolate=True)
        w2_circle1 = visual.Circle(win2, edges=96, radius=current_mean,lineWidth=4, lineColor=(0,-1,-1), interpolate=True)
        
        abc = abc+0.03
        
        circle2.draw()
        circle3.draw()
        #circle4.draw()
        circle1.draw()
        line1.draw()
        line2.draw()
        
        
        w2_circle2.draw()
        w2_circle3.draw()
        #circle4.draw()
        w2_circle1.draw()
        w2_line1.draw()
        w2_line2.draw()
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        
        state_no = state_next
        
        
        # *key_resp_11* updates
        if t >= 0.0 and key_resp_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_11.tStart = t
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_11.status == STARTED and t >= frameRemains:
            key_resp_11.status = STOPPED
        if key_resp_11.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_11.keys = theseKeys[-1]  # just the last key pressed
                key_resp_11.rt = key_resp_11.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in training_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "training_feedback"-------
    for thisComponent in training_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psizeliste = filter(None, psizeliste)
    
    psizemean = round((sum(psizeliste)/(len(psizeliste))),2)
    
    thisExp.addData('Pupil_Liste', psizeliste)
    thisExp.addData('Pupil_Mean', psizemean)
    
    
    feedbacktext = "Your baseline was: " + str(baselinemean)+ "\n" + "Your average pupildilation was: " + str(psizemean)+ "\n" 
    
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys=None
    feedbackLoop.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        feedbackLoop.addData('key_resp_11.rt', key_resp_11.rt)
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6 = event.BuilderKeyResponse()
    text_12.setText(feedbacktext)
    # keep track of which components have finished
    feedbackComponents = [key_resp_6, text_12]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6.keys = theseKeys[-1]  # just the last key pressed
                key_resp_6.rt = key_resp_6.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_12* updates
        if t >= 0.0 and text_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_12.tStart = t
            text_12.frameNStart = frameN  # exact frame index
            text_12.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys=None
    feedbackLoop.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        feedbackLoop.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10 repeats of 'feedbackLoop'

# get names of stimulus parameters
if feedbackLoop.trialList in ([], [None], None):
    params = []
else:
    params = feedbackLoop.trialList[0].keys()
# save data for this loop
feedbackLoop.saveAsText(filename + 'feedbackLoop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "instructions_noFeedback"-------
t = 0
instructions_noFeedbackClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

key_resp_12 = event.BuilderKeyResponse()
# keep track of which components have finished
instructions_noFeedbackComponents = [text_14, key_resp_12]
for thisComponent in instructions_noFeedbackComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions_noFeedback"-------
while continueRoutine:
    # get current time
    t = instructions_noFeedbackClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *text_14* updates
    if t >= 0.0 and text_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_14.tStart = t
        text_14.frameNStart = frameN  # exact frame index
        text_14.setAutoDraw(True)
    
    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_noFeedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_noFeedback"-------
for thisComponent in instructions_noFeedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "instructions_noFeedback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
noFeedbackLoop = data.TrialHandler(nReps=10, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='noFeedbackLoop')
thisExp.addLoop(noFeedbackLoop)  # add the loop to the experiment
thisNoFeedbackLoop = noFeedbackLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNoFeedbackLoop.rgb)
if thisNoFeedbackLoop != None:
    for paramName in thisNoFeedbackLoop:
        exec('{} = thisNoFeedbackLoop[paramName]'.format(paramName))

for thisNoFeedbackLoop in noFeedbackLoop:
    currentLoop = noFeedbackLoop
    # abbreviate parameter names if possible (e.g. rgb = thisNoFeedbackLoop.rgb)
    if thisNoFeedbackLoop != None:
        for paramName in thisNoFeedbackLoop:
            exec('{} = thisNoFeedbackLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "wait"-------
    t = 0
    waitClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    
    key_resp_10 = event.BuilderKeyResponse()
    # keep track of which components have finished
    waitComponents = [key_resp_10]
    for thisComponent in waitComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "wait"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = waitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #baseline_liste.append(sampleData.leftEye.diam/32)
        line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
        line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
        line1.draw()
        line2.draw()
        
        
        # *key_resp_10* updates
        if t >= 0.0 and key_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_10.tStart = t
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_10.status == STARTED and t >= frameRemains:
            key_resp_10.status = STOPPED
        if key_resp_10.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_10.keys = theseKeys[-1]  # just the last key pressed
                key_resp_10.rt = key_resp_10.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wait"-------
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys=None
    noFeedbackLoop.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        noFeedbackLoop.addData('key_resp_10.rt', key_resp_10.rt)
    
    # ------Prepare to start Routine "baseline"-------
    t = 0
    baselineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    bsize_liste = [0]*1900 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
    
    
    #-----------------------------------
    # Begin Routine
    #-----------------------------------
    
    #---------------------
    # starting values
    state_no = 0
    
    lmarker = -1 
    
    delay_size = 2
    
    #---------------------
    # filter preferences
    step_limit = 0.19    # 30Hz: 0.19 | 60Hz: 0.09
    lower_th = 1
    # keep track of which components have finished
    baselineComponents = [zeitpuffer1]
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "baseline"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = baselineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *zeitpuffer1* updates
        if t >= 0.0 and zeitpuffer1.status == NOT_STARTED:
            # keep track of start time/frame for later
            zeitpuffer1.tStart = t
            zeitpuffer1.frameNStart = frameN  # exact frame index
            zeitpuffer1.setAutoDraw(True)
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if zeitpuffer1.status == STARTED and t >= frameRemains:
            zeitpuffer1.setAutoDraw(False)
        res = iViewXAPI.iV_GetSample(byref(sampleData))
        bsize =(sampleData.leftEye.diam) # /32 für highspeed eyetracker, ohne /32 für RED
        
        
        #logging.console.write(str(bsize))
        
        #--------------------
        # state 0: starting
        #--------------------
        if state_no == 0:
         if lmarker < 1:
          lmarker = lmarker + 1
          bsize_liste[lmarker] = bsize
          state_next = 0
         
         else:  
          if bsize > lower_th and bsize_liste[lmarker] > lower_th and bsize_liste[lmarker-1] > lower_th and (abs(bsize-bsize_liste[lmarker]) <= step_limit) and (abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit):
           lmarker = lmarker + 1
           bsize_liste[lmarker] = bsize
           state_next = 1
          else:
           bsize_liste[lmarker-1] = bsize_liste[lmarker]
           bsize_liste[lmarker] = bsize
        
           state_next = 0
        
        
        #----------------------
        # state 1: observation
        #----------------------
        
        if state_no == 1:
         
         # Filter Activation
         #- - - - - - - - - - -
         if bsize <= lower_th:
          on = 1
          jump_marker = lmarker + 1 # marks values to be replaced 
          
                # Identification of last valid_value before the blink
                #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
          while on == 1:
           if bsize_liste[lmarker] >= lower_th and bsize_liste[lmarker-1] >= lower_th and bsize_liste[lmarker-2] >= lower_th and abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit and abs(bsize_liste[lmarker-1]-bsize_liste[lmarker-2]) <= step_limit:
            valid_value = bsize_liste[lmarker]
            lmarker = lmarker + 1
            for i in range(lmarker, jump_marker, 1):
             bsize_liste[i] = valid_value
        
            bsize_liste[jump_marker] = valid_value
        
            lmarker = jump_marker
            puffer_size = jump_marker + delay_size
        
            on = 0
            state_next = 2
        
           else:
            lmarker = lmarker-1
            
         else:
          lmarker = lmarker + 1
          bsize_liste[lmarker] = bsize
          
          state_next = 1
        
        
        #-------------------------------------------------------------
        # state 2: identification of next valid_value after the blink
        #-------------------------------------------------------------
        
        if state_no == 2:
         # collecting values following the blink
         #- - - - - - - - - - - - - - - - - - - - - -
         if lmarker < puffer_size:
          lmarker = lmarker + 1
          bsize_liste[lmarker] = bsize
        
          state_next = 2
        
         else:
        # identification of next valid_value after the blink
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - 
          if bsize > lower_th and abs(bsize-bsize_liste[lmarker]) <= step_limit and abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit:               
           lmarker = lmarker + 1
           bsize_liste[lmarker] = bsize
           
           state_next = 1
        
          else:
           lmarker = lmarker + 1
           bsize_liste[lmarker] = bsize
           bsize_liste[lmarker-2] = valid_value
           
           state_next = 2
        
        state_no = state_next
        
        #baseline_liste.append(sampleData.leftEye.diam/32)
        line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
        line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
        line1.draw()
        line2.draw()
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "baseline"-------
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #-----------------------------------
    # End Routine
    #-----------------------------------  
    
    #logging.console.write("test\n")
    # computing baseline mean
    bsize_liste = filter(None, bsize_liste)
    baselinemean = round((sum(bsize_liste)/(len(bsize_liste))),2)
    baselinemean = baselinemean
    
    
    # computing baseline sd
    baselinesd = abs(round(numpy.std(bsize_liste),8))
    
    # computing percent-change: sd / mean
    prozent_change1= round((baselinesd/baselinemean),2)
    
    # computing aussenringradius - maximum deviation 
    aussenringradius = (baselinemean+(baselinemean*prozent_change1))*35
    
    # computing innenringradius - minimum deviation
    innenringradius = (baselinemean-(baselinemean*prozent_change1))*35
    
    #--------------------------------------------------------------------------
    # savings:
    
    thisExp.addData('Baseline_Liste', bsize_liste)
    thisExp.addData('Baseline_Mittelwert', baselinemean)
    thisExp.addData('Baseline_Standardabweichung', baselinesd)
    
    
    # ------Prepare to start Routine "training_noFeedback"-------
    t = 0
    training_noFeedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    
    psizeliste = [0]*190000 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
    psize = 0
    
    
    #---------------------
    # starting values
    state_no = 0
    
    lmarker = -1 
    
    delay_size = 2
    
    #---------------------
    # filter preferences
    step_limit = 0.19    # 30Hz: 0.19 | 60Hz: 0.09
    lower_th = 1
    
    #---------------------
    # plot settings
    minsize = 3000
    maxsize = 0
    plot_marker = 0
    mean_length = 3
    plot_buffer = 5
    
    abc = 0
    
    #draw
    line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
    line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
    circle2 = visual.Circle(win, edges=96, radius=aussenringradius,lineWidth=1, lineColor=(0 , 0, 0), fillColor=(0 , 0, 0), interpolate=True)
    circle3 = visual.Circle(win, edges=96, radius=innenringradius,lineWidth=1, lineColor=(-0.3 , -0.3, -0.3), fillColor=(-0.3 , -0.3, -0.3), interpolate=True)
    circle4 = visual.Circle(win, edges=96, radius=baselinemean*35,lineWidth=2, lineColor=(-1 , -1, -1), interpolate=True)
    circle5 = visual.Circle(win, edges=96, radius=1000,lineWidth=1, lineColor=(-1 , -1, -1), interpolate=True)
    circle6 = visual.Circle(win, edges=96, radius=1000,lineWidth=1, lineColor=(-1 , -1, -1), interpolate=True)
    
    # keep track of which components have finished
    training_noFeedbackComponents = [text_11]
    for thisComponent in training_noFeedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "training_noFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = training_noFeedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_11* updates
        if t >= 0.0 and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_11.status == STARTED and t >= frameRemains:
            text_11.setAutoDraw(False)
        
        #-----------------------------------
        # Each Frame
        #-----------------------------------
        # eye-tracker data
        res = iViewXAPI.iV_GetSample(byref(sampleData))
        psize =(sampleData.leftEye.diam) # /32 für highspeed eyetracker, ohne /32 für RED
        
        
        #--------------------
        # state 0: starting
        #--------------------
        if state_no == 0:
         if lmarker < 1:
          lmarker = lmarker + 1
          psizeliste[lmarker] = psize
          state_next = 0
         
         else:
          if psize > lower_th and psizeliste[lmarker] > lower_th and psizeliste[lmarker-1] > lower_th and (abs(psize-psizeliste[lmarker]) <= step_limit) and (abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit):
           lmarker = lmarker + 1
           psizeliste[lmarker] = psize
           state_next = 1
          else:
           psizeliste[lmarker-1] = psizeliste[lmarker]
           psizeliste[lmarker] = psize
           state_next = 0
        
        
        #----------------------
        # state 1: observation
        #----------------------
        
        if state_no == 1:
         plot_marker = 1 
         # Filter Activation
         #- - - - - - - - - - -
         if psize <= lower_th:
          on = 1
          jump_marker = lmarker + 1 # marks values to be replaced 
          # Identification of last valid_value before the blink
          #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
          while on == 1:
           if psizeliste[lmarker] >= lower_th and psizeliste[lmarker-1] >= lower_th and psizeliste[lmarker-2] >= lower_th and abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit and abs(psizeliste[lmarker-1]-psizeliste[lmarker-2]) <= step_limit:
            valid_value = psizeliste[lmarker]
            lmarker = lmarker + 1
            # replacing values
            for i in range(lmarker, jump_marker, 1):
             psizeliste[i] = valid_value
            psizeliste[jump_marker] = valid_value
            lmarker = jump_marker
            puffer_size = jump_marker + delay_size
            on = 0
            state_next = 2
           else:
            lmarker = lmarker-1
         else:
          lmarker = lmarker + 1
          psizeliste[lmarker] = psize
          state_next = 1
        #-------------------------------------------------------------
        # state 2: identification of next valid_value after the blink
        #-------------------------------------------------------------
        if state_no == 2:
         plot_marker = 1
         # collecting values following the blink
         #- - - - - - - - - - - - - - - - - - - - - -
         if lmarker < puffer_size:
          lmarker = lmarker + 1
          psizeliste[lmarker] = psize
          state_next = 2
        
         else:
         # identification of next valid_value after the blink
         #- - - - - - - - - - - - - - - - - - - - - - - - - - - - 
          if psize > lower_th and abs(psize-psizeliste[lmarker]) <= step_limit and abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit:               
           lmarker = lmarker + 1
           psizeliste[lmarker] = psize
           state_next = 1
          else:
           lmarker = lmarker + 1
           psizeliste[lmarker] = psize
           psizeliste[lmarker-2] = valid_value
           state_next = 2
        
        #- - - - - - - - - - - - - - - - - - - - - - - - - - -
        # smooth & plot data:
        #- - - - - - - - - - - - - - - - - - - - - - - - - - -
        if state_no == 0 or state_no == 1 or state_no == 2:
         if plot_marker == 1:
                # BASELINE RINGE (schwarz): MW +/-SD
                #- - - - - - - - - - - - - - - - - - - -
                #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -     
                # FEEDBACK RINGE (rot | grau): Pupillengröße u. Extrema
                #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
          if lmarker >= mean_length + plot_buffer:
           current_mean = 0
           for p in range(1, mean_length+1, 1):
            current_mean = psizeliste[lmarker-p-plot_buffer] + current_mean
           current_mean = (current_mean/mean_length)*35
        
          if current_mean > maxsize and current_mean > aussenringradius:
           maxsize = current_mean
           circle5 = visual.Circle(win, edges=96, radius=maxsize,lineWidth=1, lineColor=(0.2 , 0.2, 0.2), interpolate=True)
          elif current_mean < minsize and current_mean < innenringradius and current_mean != 0:
           minsize = current_mean
           circle6 = visual.Circle(win, edges=96, radius=minsize,lineWidth=1, lineColor=(0.2 , 0.2, 0.2), interpolate=True)
        
        #red circle
        #circle1 = visual.Circle(win, edges=96, radius=current_mean,lineWidth=4, lineColor=(0,-1,-1), interpolate=True)
        
        #abc = abc+0.03
        
        #circle2.draw()
        #circle3.draw()
        #circle4.draw()
        #circle1.draw()
        #line1.draw()
        #line2.draw()
        
        line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-0, -0, -0))
        line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-0, -0, -0))
        line1.draw()
        line2.draw()
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        
        state_no = state_next
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in training_noFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "training_noFeedback"-------
    for thisComponent in training_noFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    psizeliste = filter(None, psizeliste)
    
    psizemean = round((sum(psizeliste)/(len(psizeliste))),2)
    
    thisExp.addData('Pupil_Liste', psizeliste)
    thisExp.addData('Pupil_Mean', psizemean)
    
    
    feedbacktext = "Your baseline was: " + str(baselinemean)+ "\n" + "Your average pupildilation was: " + str(psizemean)+ "\n" 
    
    
    # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6 = event.BuilderKeyResponse()
    text_12.setText(feedbacktext)
    # keep track of which components have finished
    feedbackComponents = [key_resp_6, text_12]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6.keys = theseKeys[-1]  # just the last key pressed
                key_resp_6.rt = key_resp_6.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *text_12* updates
        if t >= 0.0 and text_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_12.tStart = t
            text_12.frameNStart = frameN  # exact frame index
            text_12.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys=None
    noFeedbackLoop.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        noFeedbackLoop.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10 repeats of 'noFeedbackLoop'

# get names of stimulus parameters
if noFeedbackLoop.trialList in ([], [None], None):
    params = []
else:
    params = noFeedbackLoop.trialList[0].keys()
# save data for this loop
noFeedbackLoop.saveAsText(filename + 'noFeedbackLoop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
endComponents = [text_end, key_resp_3]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if t >= 0.0 and text_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_end.tStart = t
        text_end.frameNStart = frameN  # exact frame index
        text_end.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



res = iViewXAPI.iV_Disconnect()
res = iViewXAPI.iV_Disconnect()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
win2.close()
core.quit()
