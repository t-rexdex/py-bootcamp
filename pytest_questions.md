what are fixtures?
what does it mean to find the right level of fixtures?
'Fixtures are great for extracting data or objects that you use across multiple tests. However, they aren’t always as good for tests that require slight variations in the data. Littering your test suite with fixtures is no better than littering it with plain data or objects. It might even be worse because of the added layer of indirection.'
monkeypatch is a plugin dealing with replacing values and behaviours
so a fixture is a function that get ran/plugged into functions at runtime?

## having issues with python importing my packages for testing purposes.
# fixes
^^ 
PYTHONPATH=$(pwd) python /Users/RexLAP/PycharmProjects/py_bootcamp/nile_project 
^^
this should allow direct import without needing to add nile_project.whatever


^^
import sys
sys.path.append("/Users/RexLAP/PycharmProjects/py_bootcamp/nile_project")
import local_module
^^
this is supposed to work too but for some reason python is still not seeing this but if i print path it shows the directory that i want to see.


^^
export PYTHONPATH="/Users/RexLAP/PycharmProjects/py_bootcamp/nile_project"
^^ 
appends to python variable within cond env 


NTI = Need To Improve