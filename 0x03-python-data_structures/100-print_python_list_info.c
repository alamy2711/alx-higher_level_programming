#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: The pointer to PyObject
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t listSize, listAllc, i;
    Py_ssize_t i;
    PyObject *element;

    listSize = PyList_Size(p);
    listAllc = ((PyListObject *)p)->allocated;
    printf("[*] Size of the Python List = %zd\n", listSize);
    printf("[*] Allocated = %zd\n", listAllc);

    for (i = 0; i < listSize; i++)
    {
        printf("Element %zd: ", i);

        element = PyList_GetItem(p, i);
        printf("%s\n", Py_TYPE(element)->tp_name);
    }
}
