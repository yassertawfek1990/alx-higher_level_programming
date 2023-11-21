#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <floatobject.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Printlists.
 * @p: bject.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t s;
	Py_ssize_t a;
	Py_ssize_t j;
	const char *t;
	PyListObject *l;
	PyVarObject *v;

	l = (PyListObject *)p;
	v = (PyVarObject *)p;
	s = v->ob_size;
	a = l->allocated;
	fflush(stdout);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", a);
	for (j = 0; j < s; j++)
	{
		t = l->ob_item[j]->ob_type->tp_name;
		printf("Element %ld: %s\n", j, t);
		if (strcmp(t, "bytes") == 0)
			print_python_bytes(l->ob_item[j]);
		else if (strcmp(t, "float") == 0)
			print_python_float(l->ob_item[j]);
	}
}

/**
 * print_python_bytes - Printjects.
 * @p: A Pt.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t s;
	Py_ssize_t j;
	PyBytesObject *b;

	b = (PyBytesObject *)p;
	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", b->ob_sval);
	if (((PyVarObject *)p)->ob_size >= 10)
		s = 10;
	else
		s = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %ld bytes: ", s);
	for (j = 0; j < s; j++)
	{
		printf("%02hhx", b->ob_sval[j]);
		if (j == (s - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Printsjects.
 * @p: A Pt.
 */
void print_python_float(PyObject *p)
{
	char *bu;
	PyFloatObject *fl;

	bu = NULL;
	fl = (PyFloatObject *)p;
	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	bu = PyOS_double_to_string(fl->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", bu);
	PyMem_Free(bu);
}
