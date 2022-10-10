#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.2),
    on October 07, 2022, at 12:06
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.2'
expName = 'memoryagain'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\admin\\Documents\\Psychopy Experiments\\Project\\memoryagain_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Welcome" ---
text = visual.TextStim(win=win, name='text',
    text="Welcome to the experiment\nPress 'space' to start",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp_welcome = keyboard.Keyboard()

# --- Initialize components for Routine "Study" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Instructions" ---
instructiontext = visual.TextStim(win=win, name='instructiontext',
    text="Get ready for the test\n\nPress 'y' when you see a familiar word \nOtherwise press 'n' \n\nPress 'space' to start",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intstruction_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Test" ---
text_test = visual.TextStim(win=win, name='text_test',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_test = keyboard.Keyboard()

# --- Initialize components for Routine "feedback" ---
text_feedback = visual.TextStim(win=win, name='text_feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "End" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='Thank you for participating!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
resp_welcome.keys = []
resp_welcome.rt = []
_resp_welcome_allKeys = []
# keep track of which components have finished
WelcomeComponents = [text, resp_welcome]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # *resp_welcome* updates
    waitOnFlip = False
    if resp_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp_welcome.frameNStart = frameN  # exact frame index
        resp_welcome.tStart = t  # local t and not account for scr refresh
        resp_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_welcome, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resp_welcome.started')
        resp_welcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_welcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_welcome.status == STARTED and not waitOnFlip:
        theseKeys = resp_welcome.getKeys(keyList=['space'], waitRelease=False)
        _resp_welcome_allKeys.extend(theseKeys)
        if len(_resp_welcome_allKeys):
            resp_welcome.keys = _resp_welcome_allKeys[-1].name  # just the last key pressed
            resp_welcome.rt = _resp_welcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if resp_welcome.keys in ['', [], None]:  # No response was made
    resp_welcome.keys = None
thisExp.addData('resp_welcome.keys',resp_welcome.keys)
if resp_welcome.keys != None:  # we had a response
    thisExp.addData('resp_welcome.rt', resp_welcome.rt)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
studytrial = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('C:/Users/admin/Documents/Psychopy Experiments/Project/test.xlsx', selection='0:7'),
    seed=None, name='studytrial')
thisExp.addLoop(studytrial)  # add the loop to the experiment
thisStudytrial = studytrial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStudytrial.rgb)
if thisStudytrial != None:
    for paramName in thisStudytrial:
        exec('{} = thisStudytrial[paramName]'.format(paramName))

for thisStudytrial in studytrial:
    currentLoop = studytrial
    # abbreviate parameter names if possible (e.g. rgb = thisStudytrial.rgb)
    if thisStudytrial != None:
        for paramName in thisStudytrial:
            exec('{} = thisStudytrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Study" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    text_4.setText(stim_word)
    # keep track of which components have finished
    StudyComponents = [text_4]
    for thisComponent in StudyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Study" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.stopped')
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StudyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Study" ---
    for thisComponent in StudyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'studytrial'


# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intstruction_resp.keys = []
intstruction_resp.rt = []
_intstruction_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [instructiontext, intstruction_resp]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructiontext* updates
    if instructiontext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructiontext.frameNStart = frameN  # exact frame index
        instructiontext.tStart = t  # local t and not account for scr refresh
        instructiontext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructiontext, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructiontext.started')
        instructiontext.setAutoDraw(True)
    
    # *intstruction_resp* updates
    waitOnFlip = False
    if intstruction_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intstruction_resp.frameNStart = frameN  # exact frame index
        intstruction_resp.tStart = t  # local t and not account for scr refresh
        intstruction_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intstruction_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'intstruction_resp.started')
        intstruction_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intstruction_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intstruction_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intstruction_resp.status == STARTED and not waitOnFlip:
        theseKeys = intstruction_resp.getKeys(keyList=['space'], waitRelease=False)
        _intstruction_resp_allKeys.extend(theseKeys)
        if len(_intstruction_resp_allKeys):
            intstruction_resp.keys = _intstruction_resp_allKeys[-1].name  # just the last key pressed
            intstruction_resp.rt = _intstruction_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if intstruction_resp.keys in ['', [], None]:  # No response was made
    intstruction_resp.keys = None
thisExp.addData('intstruction_resp.keys',intstruction_resp.keys)
if intstruction_resp.keys != None:  # we had a response
    thisExp.addData('intstruction_resp.rt', intstruction_resp.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialtest = data.TrialHandler(nReps=1.0, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('C:/Users/admin/Documents/Psychopy Experiments/Project/test.xlsx'),
    seed=None, name='trialtest')
thisExp.addLoop(trialtest)  # add the loop to the experiment
thisTrialtest = trialtest.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialtest.rgb)
if thisTrialtest != None:
    for paramName in thisTrialtest:
        exec('{} = thisTrialtest[paramName]'.format(paramName))

for thisTrialtest in trialtest:
    currentLoop = trialtest
    # abbreviate parameter names if possible (e.g. rgb = thisTrialtest.rgb)
    if thisTrialtest != None:
        for paramName in thisTrialtest:
            exec('{} = thisTrialtest[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Test" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from testcode
    #check if our old_new status is old or new and assign corr_resp
    if(old_new == 'old'): 
        corr_resp = 'y'
    else:
         corr_resp = 'n'
    thisExp.addData ('corr_resp', corr_resp)
    
    text_test.setText(stim_word)
    key_resp_test.keys = []
    key_resp_test.rt = []
    _key_resp_test_allKeys = []
    # keep track of which components have finished
    TestComponents = [text_test, key_resp_test]
    for thisComponent in TestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Test" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_test* updates
        if text_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_test.frameNStart = frameN  # exact frame index
            text_test.tStart = t  # local t and not account for scr refresh
            text_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_test, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_test.started')
            text_test.setAutoDraw(True)
        
        # *key_resp_test* updates
        waitOnFlip = False
        if key_resp_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_test.frameNStart = frameN  # exact frame index
            key_resp_test.tStart = t  # local t and not account for scr refresh
            key_resp_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_test, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_test.started')
            key_resp_test.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_test.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_test.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_test.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_test.getKeys(keyList=['y','n'], waitRelease=False)
            _key_resp_test_allKeys.extend(theseKeys)
            if len(_key_resp_test_allKeys):
                key_resp_test.keys = _key_resp_test_allKeys[-1].name  # just the last key pressed
                key_resp_test.rt = _key_resp_test_allKeys[-1].rt
                # was this correct?
                if (key_resp_test.keys == str(corr_resp)) or (key_resp_test.keys == corr_resp):
                    key_resp_test.corr = 1
                else:
                    key_resp_test.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Test" ---
    for thisComponent in TestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_test.keys in ['', [], None]:  # No response was made
        key_resp_test.keys = None
        # was no response the correct answer?!
        if str(corr_resp).lower() == 'none':
           key_resp_test.corr = 1;  # correct non-response
        else:
           key_resp_test.corr = 0;  # failed to respond (incorrectly)
    # store data for trialtest (TrialHandler)
    trialtest.addData('key_resp_test.keys',key_resp_test.keys)
    trialtest.addData('key_resp_test.corr', key_resp_test.corr)
    if key_resp_test.keys != None:  # we had a response
        trialtest.addData('key_resp_test.rt', key_resp_test.rt)
    # the Routine "Test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from codefeedback
    item_status = ''
    
    if(old_new == 'old'):
        if(key_resp_test.corr == 1):
           feedback_text = "congratulations\n\n It was old and you knew it!!"
           item_status = 'hit'
        else:
           feedback_text = "Sorry\n\n you got it wrong :("
           item_status = 'miss'
    else:
        if(key_resp_test.corr == 1):
            feedback_text = "congratulations\n\n you didn't get fooled"
            item_status = 'correct rejection'
            
        else:
            feedback_text = "Sorry\n\n  That was a new item"
            item_status = 'false alarm'
            
    thisExp.addData ('item_status', item_status)
    text_feedback.setText(feedback_text)
    # keep track of which components have finished
    feedbackComponents = [text_feedback]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "feedback" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_feedback* updates
        if text_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_feedback.frameNStart = frameN  # exact frame index
            text_feedback.tStart = t  # local t and not account for scr refresh
            text_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_feedback, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_feedback.started')
            text_feedback.setAutoDraw(True)
        if text_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_feedback.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                text_feedback.tStop = t  # not accounting for scr refresh
                text_feedback.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_feedback.stopped')
                text_feedback.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "feedback" ---
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialtest'


# --- Prepare to start Routine "End" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [text_3]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End" ---
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.stopped')
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
