#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints infist
 * @p: PyObj 
 *Return: id 
 */

void print_python_list_info(PyObject *p)
{
    int s, a, x;
    PyObject *it;

    s = Py_SIZE(p);
    a = ((PyListObject *)p)->allocated;
    printf("[*] Size of the Python List = %d\n", s);
    printf("[*] Allocated = %d\n", a);
    for (x = 0; x < s; x++)
    {
	     printf("Element %d: ", x);
        it = PyList_GetItem(p, x);
        printf("%s\n", Py_TYPE(it)->tp_name);
    }
}
