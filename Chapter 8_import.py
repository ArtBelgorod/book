from printing_fun import print_models, show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

import printing_fun

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
printing_fun.print_models(unprinted_designs, completed_models)
printing_fun.show_completed_models(completed_models)

from printing_fun import print_models as p_m
from printing_fun import show_completed_models as s_c_m

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
p_m(unprinted_designs, completed_models)
s_c_m(completed_models)

import printing_fun as p_fun

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
p_fun.print_models(unprinted_designs, completed_models)
p_fun.show_completed_models(completed_models)

from printing_fun import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
