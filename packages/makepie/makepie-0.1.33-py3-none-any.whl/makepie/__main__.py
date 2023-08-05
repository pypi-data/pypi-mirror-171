import importlib, logging, sys
from makepie import makepie_load
from makepie.Config import config

from .Exceptions import MakepieException
from .Decorators import macro, get_macros
from .Utils import env
from .Makepie import main

log = logging.getLogger(__name__)

def makepie():
	# Import make module containing targets
	module = env('MAKEPIE_MAKEMODULE', 'make')
	try:
		make = importlib.import_module(module)
	except ImportError as e:
		log.error(f"Module '{module}' not found")
		sys.exit(1)

	log.debug(f"Loaded user config")
	
	# Load with empty config if not already loaded by user script
	if not config("MAKEPIE_LOADED", False):
		makepie_load()

	# For each element in the make module
	for element in dir(make):
		func = getattr(make, element)
		# If the element is a function and was defined in the make module
		if type(func).__name__ == "function" \
			and func.__module__ == make.__name__:

			log.debug(f"Converting function '{func.__name__}' to macro")
			try:
				make.__dict__[element] = macro(func)
			except MakepieException as e:
				log.warning(f"Ignoring function '{func.__name__}': {e}")

	# Launch makepie
	(macros, default_macro) = get_macros()
	result = main(macros, default_macro, sys.argv)

	if isinstance(result, int):
		sys.exit(result)
	else:
		sys.exit(0)

if __name__ == '__main__':
	makepie()
	