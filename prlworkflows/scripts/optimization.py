#!/usr/bin/env python
from atomate.vasp.workflows.presets.core import wf_structure_optimization
from atomate.vasp.powerups import add_modify_incar
from prlworkflows.utils import mp_structures_from_ids, get_launchpad

################################################################################
#                                CONFIGURATION                                 #                      
################################################################################

# Required configuration
use_api_interface = True  # set to True if you want to use the Materials Project API, False will load the POSCAR in the local dir
mp_structure_id = 'mp-134'  # enter the structure ID. Example: Al is 'mp-134'. See prlworkflows.utils for other options to get Structures.
is_conductor = True  # TODO: needed with custodian?

# Optional configuration
launchpad_file_path = None  # absolute path to LaunchPad. If None, will load from FW_CONFIG_FILE variable
API_KEY = None  # Enter your API key here. If None, your PMG environment variable will be used
custom_incar_settings = None  # dict of your incar settings


################################################################################
#                                     RUN                                      #                      
################################################################################

def main():
    launchpad = get_launchpad(launchpad_file=launchpad_file_path)

    if use_api_interface:
        struct = mp_structures_from_ids([mp_structure_id], API_KEY=API_KEY)[0]
    else:
        from pymatgen import Structure
        struct = Structure.from_file('POSCAR')

    c = {}
    if custom_incar_settings:
        c["USER_INCAR_SETTINGS"] = {"incar_update": custom_incar_settings}
    workflow = wf_structure_optimization(struct)
    workflow = add_modify_incar(workflow)  # get settings from the my_fworker.yaml file
    if is_conductor:
        workflow = add_modify_incar(workflow, modify_incar_params={
            "incar_update": {"SIGMA": 0.2, "ISMEAR": 1}})
    launchpad.add_wf(workflow)

if __name__ == '__main__':
    main()
