#!/usr/bin/env python

"""
  Get the files attached to a transformation and optionally update the file status
  Extension of dirac-transformation-get-files with additional options:

  Usage:
    cta-transformation-get-files <transID or ascii file with a list of transID comma separated> <options>

  Options:
  --FileStatus : selection based on the FileStatus
  --TaskStatus : selection based on the TaskStatus
  --setFileStatus : update the FileStatus of the selected files to a new Status
  --dumpLFN : dump the list of selected LFNs in a file
  --dumpFull : dump the list of selected <TransID,LFN> in a file
"""

__RCSID__ = "$Id$"

import os

import DIRAC
from DIRAC import gLogger
from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
from DIRAC.TransformationSystem.Client.TransformationClient import TransformationClient

@Script()
def main():

  Script.registerSwitch('', 'FileStatus=', '    file status')
  Script.registerSwitch('', 'TaskStatus=', '    task status')
  Script.registerSwitch('', 'setFileStatus=', '    new file status')
  Script.registerSwitch('', 'dumpLFN', '    dump the list of selected LFNs in a file')
  Script.registerSwitch('', 'dumpFull', '    dump the list of selected <TransID,LFN> in a file')
  switches, argss = Script.parseCommandLine(ignoreErrors=True)

  transIDList = []
  fileStatus = None
  taskStatus = None
  newFileStatus = None
  dumpLFNFlag = False
  dumpFullFlag = False

  for switch in switches:
    if switch[0] == 'FileStatus':
      fileStatus = switch[1].capitalize()
    elif switch[0] == 'TaskStatus':
      taskStatus = switch[1].capitalize()
    elif switch[0] == 'setFileStatus':
      newFileStatus = switch[1].capitalize()
    elif switch[0] == 'dumpLFN':
      dumpLFNFlag = True
    elif switch[0] == 'dumpFull':
      dumpFullFlag = True

  if len(argss)!=1:
    Script.showHelp()
    DIRAC.exit(-1)

  if os.path.isfile(argss[0]):
    gLogger.notice('\nReading transformation IDs from input file: %s\n' % argss[0])
    lines = open(argss[0], 'rt').readlines()
    transIDList += [transID.strip() for line in lines for transID in line.split(',')]
    gLogger.notice("Found %d transformations" % len(transIDList))
  else:
    transIDList.append(argss[0])

  if fileStatus or taskStatus:
    outputFileName = ("trans%sFiles_%sTasks_%s-%s" % (fileStatus,taskStatus,transIDList[0],transIDList[-1]))

  if (dumpLFNFlag):
    outputLFN = outputFileName + '.lfns'
    f0 = open(outputLFN, 'w')
    
  if (dumpFullFlag):
    outputFull = outputFileName + '.transID_lfns'
    f1 = open(outputFull, 'w')

  tc = TransformationClient()

  for transID in transIDList:

    condDict = {'TransformationID': transID}

    if fileStatus:
      condDict.update({'Status': fileStatus})

    if taskStatus:
      res = tc.getTransformationTasks({'TransformationID': transID, 'ExternalStatus': taskStatus})

      if not res['OK']:
        gLogger.error(res['Message'])
        DIRAC.exit(2)

      if len(res['Value']) == 0:
        gLogger.notice("No tasks selected for transformation %s with status %s" % (transID, taskStatus))

      taskIDs = []
      for task in res['Value']:
        taskIDs.append(task["TaskID"])

      condDict.update({'TaskID': taskIDs})

    res = tc.getTransformationFiles(condDict)

    if not res['OK']:
      gLogger.error(res['Message'])
      DIRAC.exit(2)

    if len(res['Value']) == 0:
      gLogger.notice("No files selected for transformation %s with status %s" % (transID, fileStatus))

    transFiles = []
    for transfile in res['Value']:
      transFiles.append(transfile['LFN'])
      if (dumpLFNFlag):
        f0.write("%s\n" % (transfile['LFN']))
      if (dumpFullFlag):
        f1.write("%s %s\n" % (transID, transfile['LFN']))
      else:
        gLogger.notice(transfile['LFN'])

    if newFileStatus:
      res = tc.setFileStatusForTransformation(transID, newLFNsStatus=newFileStatus, lfns=transFiles)
      if not res['OK']:
        gLogger.error(res['Message'])
        DIRAC.exit(2)
      gLogger.notice(" %d files set to %s status" % (len(transFiles), newFileStatus))

  if (dumpLFNFlag):
    gLogger.notice('%d files dumped in %s' % (len(transFiles), outputLFN))

  if (dumpFullFlag):
    gLogger.notice('%d files dumped in %s' % (len(transFiles), outputFull))

if __name__ == "__main__":
  main()
