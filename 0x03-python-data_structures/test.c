#include "Python.h"
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	long int x, size = PyList_Size(p);
	PyListObject *mylist = (PyListObject *) p;
	PyObject **myitems = mylist->ob_item;

	printf("[*] Size of the Python List = %li\n", size);	
	printf("[*] Allocated = %li\n", mylist->allocated);
	for (x = 0; x < size; x++)
		printf("Element %li: %s\n", x, myitems[x]->ob_type->tp_name);

}
