#include <Python.h>
void print_python_list_info(PyObject *p)
{
	long int size = size;
	int i;
	PyObject *item = (PyList_GetItem *)p;

size = PyList_Size(p);
printf("[*] Size of Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}
