#!/usr/bin/env python
""" Data management script for production
    create DFC MetaData structure put and register files in DFC
    should work for corsika, simtel and EventDisplay output
    derived from cta-prod3-managedata.py and cta-analysis-managedata.py
                    JB September 2018
"""

__RCSID__ = "$Id$"

# generic imports
import os
import glob
import json

# DIRAC imports
import DIRAC
from DIRAC.Core.Utilities.DIRACScript import DIRACScript as Script
Script.parseCommandLine()

# Specific DIRAC imports
from CTADIRAC.Core.Utilities.tool_box import run_number_from_filename
from CTADIRAC.Core.Workflow.Modules.ProdDataManager import ProdDataManager

@Script()
def main():
  """ simple wrapper to put and register all production files

  Keyword arguments:
  args -- a list of arguments in order []
  """
  args = Script.getPositionalArgs()
  metadata = args[0]
  metadata_fields = args[1]
  file_metadata = args[2]
  base_path = args[3]
  output_pattern = args[4]
  package = args[5]
  program_category = args[6]
  catalogs = args[7]
  output_type = args[8]

  # Load catalogs
  catalogs_json = json.loads(catalogs)

  # Create MD structure
  prod_dm = ProdDataManager(catalogs_json)
  result = prod_dm.createMDStructure(metadata, metadata_fields, base_path, program_category)
  if result['OK']:
    path = result['Value']
  else:
    return result

  # Check the content of the output directory
  result = prod_dm._checkemptydir(output_pattern)
  if not result['OK']:
    return result

  # Dump the list of output LFNs
  file = open("output_lfns.txt", 'w')

  # Loop over each file and upload and register
  for localfile in glob.glob(output_pattern):
    file_name = os.path.basename(localfile)
    # Check run number, assign one as file metadata if needed
    fmd_dict = json.loads(file_metadata)
    try:
      run_number = run_number_from_filename(file_name, package)
    except BaseException:
      run_number = -9999
      DIRAC.gLogger.notice('Could not get a correct run number, assigning -9999')
    fmd_dict['runNumber'] = '%08d' % int(run_number)
    # get the output file path
    run_path = prod_dm._getRunPath(fmd_dict)
    lfn = os.path.join(path, output_type, run_path, file_name)
    fmd_json = json.dumps(fmd_dict)
    result = prod_dm.putAndRegister(lfn, localfile, fmd_json, package)
    if not result['OK']:
      return result
    file.write(lfn)
    file.write('\n')
  file.close()

  DIRAC.exit()

####################################################
if __name__ == '__main__':
  main()