#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.2),
    on November 03, 2022, at 19:38
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
expName = 'delaydiscounting'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\admin\\Documents\\Psychopy Experiments\\tutorial 6\\new design\\delaydiscountingnewdesign_lastrun.py',
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

# --- Initialize components for Routine "trial" ---
bg_polygon = visual.Rect(
    win=win, name='bg_polygon',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
selection_text = visual.TextStim(win=win, name='selection_text',
    text='',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
condition1text = visual.TextStim(win=win, name='condition1text',
    text='',
    font='Open Sans',
    pos=(-0.4, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color=[-0.0039, 1.0000, 0.6627], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
box1_polygon = visual.Rect(
    win=win, name='box1_polygon',
    width=(0.5, 0.1)[0], height=(0.5, 0.1)[1],
    ori=0.0, pos=(-0.4, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7255, -0.8431, -0.5294], fillColor=None,
    opacity=None, depth=-3.0, interpolate=True)
condition2text = visual.TextStim(win=win, name='condition2text',
    text='',
    font='Open Sans',
    pos=(0.4, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color=[-0.0039, 1.0000, 0.6627], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
box2_polygon = visual.Rect(
    win=win, name='box2_polygon',
    width=(0.5, 0.1)[0], height=(0.5, 0.1)[1],
    ori=0.0, pos=(0.4, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7255, -0.8431, -0.5294], fillColor=None,
    opacity=None, depth=-5.0, interpolate=True)
key_resp = keyboard.Keyboard()
time_text = visual.TextStim(win=win, name='time_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "blank" ---
blank_polygon = visual.Rect(
    win=win, name='blank_polygon',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=1.0, depth=0.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('tempconditionfile.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    selection_text.setText('Choose One')
    condition1text.setText(FixedEntry)
    condition2text.setText(VariableEntry)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # Run 'Begin Routine' code from code
    time_text.text = ''
    # keep track of which components have finished
    trialComponents = [bg_polygon, selection_text, condition1text, box1_polygon, condition2text, box2_polygon, key_resp, time_text]
    for thisComponent in trialComponents:
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
    
    # --- Run Routine "trial" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *bg_polygon* updates
        if bg_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bg_polygon.frameNStart = frameN  # exact frame index
            bg_polygon.tStart = t  # local t and not account for scr refresh
            bg_polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bg_polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bg_polygon.started')
            bg_polygon.setAutoDraw(True)
        if bg_polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > bg_polygon.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                bg_polygon.tStop = t  # not accounting for scr refresh
                bg_polygon.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bg_polygon.stopped')
                bg_polygon.setAutoDraw(False)
        
        # *selection_text* updates
        if selection_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            selection_text.frameNStart = frameN  # exact frame index
            selection_text.tStart = t  # local t and not account for scr refresh
            selection_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(selection_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'selection_text.started')
            selection_text.setAutoDraw(True)
        if selection_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > selection_text.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                selection_text.tStop = t  # not accounting for scr refresh
                selection_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'selection_text.stopped')
                selection_text.setAutoDraw(False)
        
        # *condition1text* updates
        if condition1text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            condition1text.frameNStart = frameN  # exact frame index
            condition1text.tStart = t  # local t and not account for scr refresh
            condition1text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(condition1text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'condition1text.started')
            condition1text.setAutoDraw(True)
        if condition1text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > condition1text.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                condition1text.tStop = t  # not accounting for scr refresh
                condition1text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'condition1text.stopped')
                condition1text.setAutoDraw(False)
        
        # *box1_polygon* updates
        if box1_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box1_polygon.frameNStart = frameN  # exact frame index
            box1_polygon.tStart = t  # local t and not account for scr refresh
            box1_polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box1_polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'box1_polygon.started')
            box1_polygon.setAutoDraw(True)
        if box1_polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > box1_polygon.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                box1_polygon.tStop = t  # not accounting for scr refresh
                box1_polygon.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'box1_polygon.stopped')
                box1_polygon.setAutoDraw(False)
        
        # *condition2text* updates
        if condition2text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            condition2text.frameNStart = frameN  # exact frame index
            condition2text.tStart = t  # local t and not account for scr refresh
            condition2text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(condition2text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'condition2text.started')
            condition2text.setAutoDraw(True)
        if condition2text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > condition2text.tStartRefresh + 15.0-frameTolerance:
                # keep track of stop time/frame for later
                condition2text.tStop = t  # not accounting for scr refresh
                condition2text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'condition2text.stopped')
                condition2text.setAutoDraw(False)
        
        # *box2_polygon* updates
        if box2_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box2_polygon.frameNStart = frameN  # exact frame index
            box2_polygon.tStart = t  # local t and not account for scr refresh
            box2_polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box2_polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'box2_polygon.started')
            box2_polygon.setAutoDraw(True)
        if box2_polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > box2_polygon.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                box2_polygon.tStop = t  # not accounting for scr refresh
                box2_polygon.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'box2_polygon.stopped')
                box2_polygon.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.stopped')
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['t','l'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from code
        time_text.text = str(round(15-routineTimer.getTime()))
        
        # *time_text* updates
        if time_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            time_text.frameNStart = frameN  # exact frame index
            time_text.tStart = t  # local t and not account for scr refresh
            time_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(time_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'time_text.started')
            time_text.setAutoDraw(True)
        if time_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > time_text.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                time_text.tStop = t  # not accounting for scr refresh
                time_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'time_text.stopped')
                time_text.setAutoDraw(False)
        if time_text.status == STARTED:  # only update if drawing
            time_text.setText(round(15 - t, ndigits = 1), log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "blank" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [blank_polygon]
    for thisComponent in blankComponents:
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
    
    # --- Run Routine "blank" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_polygon* updates
        if blank_polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_polygon.frameNStart = frameN  # exact frame index
            blank_polygon.tStart = t  # local t and not account for scr refresh
            blank_polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_polygon.started')
            blank_polygon.setAutoDraw(True)
        if blank_polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank_polygon.tStop = t  # not accounting for scr refresh
                blank_polygon.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_polygon.stopped')
                blank_polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank" ---
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


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
