#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bob = (PyBytesObject *) p;
	Py_ssize_t bsize = PyBytes_Size(p), i;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		printf("  size: %ld\n", bsize);
		printf("  trying string: %s", PyBytes_AsString(p));
		for (i = 0; i <= bsize; i++)
			printf("  first %ld bytes: %c\n", i, (bob->ob_sval)[i]);
	}
	else
		printf("  [ERROR] Invalid Bytes Object");

}

void print_python_list(PyObject *p)
{
	PyListObject *lob = (PyListObject *) p;
	Py_ssize_t lsize = PyList_Size(p), i;

	printf("[.] Python list info\n");
	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %ld\n", lsize);
		printf("[*] Allocated = %ld\n", lob->allocated);
		for (i = 0; i < lsize; i++)
		{
			printf("Element %ld: ", i);
			printf("%s\n", (lob->ob_item)[i]->ob_type->tp_name);
			if (PyBytes_Check(lob->ob_item[i]))
				print_python_bytes(p);
		}
	}
	else
		printf("[ERROR] Invalid List Object");
}
