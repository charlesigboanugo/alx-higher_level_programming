#include <Python.h>
#include <stdio.h>

/**
* print_python_bytes - print information about a bytes object
* @p: python bytes object
*
* Return: None
*/
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bob = (PyBytesObject *) p;
	Py_ssize_t bsize, i;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		bsize = PyBytes_Size(p);
		printf("  size: %ld\n", bsize);
		printf("  trying string: %s\n", PyBytes_AsString(p));
		printf("  first %ld bytes:", bsize < 10L ? bsize + 1 : 10L);
		for (i = 0; i <= bsize && i < 10L; i++)
			printf(" %.2x", (unsigned char)(bob->ob_sval)[i]);
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");

}

/**
* print_python_list - print information about a list object
* @p: python list object
*
* Return: None
*/
void print_python_list(PyObject *p)
{
	PyListObject *lob = (PyListObject *) p;
	Py_ssize_t lsize, i;

	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
		lsize = PyList_Size(p);
		printf("[*] Size of the Python List = %ld\n", lsize);
		printf("[*] Allocated = %ld\n", lob->allocated);
		for (i = 0; i < lsize; i++)
		{
			printf("Element %ld: ", i);
			printf("%s\n", (lob->ob_item)[i]->ob_type->tp_name);
			if (PyBytes_Check(lob->ob_item[i]))
				print_python_bytes(lob->ob_item[i]);
		}
	}
	else
		printf("[ERROR] Invalid List Object\n");
}
